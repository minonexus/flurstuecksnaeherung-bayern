"""Korrekturen der Flurstücksnäherung Bayern erstellen und prüfen.

    python werkzeug/korrektur.py erstellen ORIGINAL.gpkg BEARBEITET.gpkg --name isen_doppelhaus \\
        --grund "Doppelhaus als ein Grundstück genähert …" --quelle parzellarkarte
    python werkzeug/korrektur.py pruefen korrekturen/09177/2026-11-02_isen_doppelhaus.geojson

`erstellen` vergleicht den heruntergeladenen Kreis mit der in QGIS bearbeiteten Kopie und schreibt
nur, was sich geändert hat, nach `korrekturen/<kreis>/<datum>_<name>.geojson`. `pruefen` prüft eine
Korrekturdatei gegen den veröffentlichten Stand — dasselbe, was die CI bei jedem Pull Request tut.

Braucht: shapely ≥ 2, pyproj, fiona, jsonschema.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import io
import json
import re
import sys
import urllib.request
import zipfile
from pathlib import Path

DATEN = "https://data.minonexus.com/flurstuecksnaeherung-bayern"
KENNUNG = "flurstuecksnaeherung-bayern-werkzeug/1 (+https://github.com/minonexus/flurstuecksnaeherung-bayern)"
LAYER = "flurstuecksnaeherung"
SCHEMA = Path(__file__).resolve().parent.parent / "schema" / "naeherung_korrektur.schema.json"
QUELLEN = ("ortskenntnis", "parzellarkarte", "luftbild_frei", "andere_freie_quelle")

#: Mehr Überlappung mit einer anderen Fläche ist eine, weniger ist Rundung an gemeinsamen Kanten
MAX_UEBERLAPPUNG_M2 = 0.5
#: Ab hier ein Hinweis fürs Review: viel Fläche bewegt
HINWEIS_ANTEIL, HINWEIS_SUMME_M2 = 0.5, 10_000.0
MAX_BYTES, MAX_FLAECHEN, NACHKOMMA = 1_000_000, 500, 7
DATEINAME = re.compile(r"^korrekturen/(09[0-9]{3})/[0-9]{4}-[0-9]{2}-[0-9]{2}_[a-z0-9_-]{3,60}\.geojson$")


def geom_hash(g) -> str:
    """Wie bei der Veröffentlichung: SHA-256 über das WKB (Little Endian, 2D), 16 Hex-Zeichen."""
    import shapely

    return hashlib.sha256(shapely.to_wkb(g, byte_order=1, output_dimension=2)).hexdigest()[:16]


def gpkg_lesen(pfad) -> list[dict]:
    """Die Flächen eines Kreises: je Eintrag id, geometrie, geom_hash, kreis, kreis_stand.

    In einer bearbeiteten Kopie kann eine id fehlen (in QGIS neu gezeichnet) oder doppelt vorkommen
    (QGIS kopiert beim Teilen die Attribute auf beide Teile).
    """
    import fiona
    from shapely.geometry import shape

    # „Speichern unter" in QGIS benennt den Layer nach der Datei — dann den einzigen nehmen
    layer = fiona.listlayers(pfad)
    if LAYER in layer:
        layer = LAYER
    elif len(layer) == 1:
        layer = layer[0]
    else:
        raise SystemExit(f"{pfad}: kein Layer {LAYER!r} und nicht genau ein anderer ({layer})")
    with fiona.open(pfad, layer=layer) as ein:
        return [
            {
                "id": f["properties"].get("id"),
                "geometrie": shape(f["geometry"]) if f["geometry"] else None,
                "geom_hash": f["properties"].get("geom_hash"),
                "kreis": f["properties"].get("ags_kreis"),
                "kreis_stand": f["properties"].get("kreis_stand"),
            }
            for f in ein
        ]


def _umrechnen(g, von: int, nach: int):
    import numpy as np
    import shapely
    from pyproj import Transformer

    t = Transformer.from_crs(von, nach, always_xy=True)
    return shapely.transform(g, lambda xy: np.column_stack(t.transform(xy[:, 0], xy[:, 1])))


def _wgs84(g) -> dict:
    from shapely.geometry import mapping

    geo = mapping(_umrechnen(g, 25832, 4326))

    def runden(x):
        return [round(x[0], NACHKOMMA), round(x[1], NACHKOMMA)] if isinstance(x[0], float) else [runden(y) for y in x]

    return {"type": geo["type"], "coordinates": runden(geo["coordinates"])}


def erstellen(
    original: Path, bearbeitet: Path, name: str, grund: str, quelle: str, quelle_text: str | None, repo: Path
) -> Path:
    """Die Unterschiede zwischen veröffentlichtem und bearbeitetem Kreis als Korrekturdatei."""
    alt = {a["id"]: a for a in gpkg_lesen(original)}
    kreise = {a["kreis"] for a in alt.values()}
    if len(kreise) != 1:
        raise SystemExit(f"{original}: kein einzelner Kreis ({sorted(kreise)})")
    kreis = kreise.pop()
    # Ein neuer Stand entsteht nur, wenn sich etwas ändert, und das Geänderte trägt ihn: der höchste ist der Stand
    stand = max(a["kreis_stand"] for a in alt.values())

    gruppen: dict[int, list] = {}
    ohne_id = []
    for n in gpkg_lesen(bearbeitet):
        if n["geometrie"] is not None:
            (gruppen.setdefault(n["id"], []) if n["id"] in alt else ohne_id).append(n)
    features = []
    for i, kandidaten in gruppen.items():
        a = alt[i]
        # Geteilt: Der Teil, der der alten Fläche am meisten gleicht, behält die id, die übrigen sind neu
        bester = max(kandidaten, key=lambda k: k["geometrie"].intersection(a["geometrie"]).area)
        # Unberührt kommt die Fläche bytegleich aus dem GeoPackage zurück
        if geom_hash(bester["geometrie"]) != a["geom_hash"]:
            features.append(
                {"type": "Feature", "id": i, "properties": {"aenderung": "geaendert", "basis_hash": a["geom_hash"]},
                 "geometry": _wgs84(bester["geometrie"])}
            )  # fmt: skip
        features += [_neu(k["geometrie"]) for k in kandidaten if k is not bester]
    features += [_neu(n["geometrie"]) for n in ohne_id]
    features += [
        {
            "type": "Feature",
            "id": i,
            "properties": {"aenderung": "entfallen", "basis_hash": a["geom_hash"]},
            "geometry": None,
        }
        for i, a in alt.items()
        if i not in gruppen
    ]
    if not features:
        raise SystemExit("Keine Änderung gefunden.")

    kopf = {"schema": 1, "basis": [{"kreis": kreis, "stand": stand}], "grund": grund, "quelle": quelle}
    if quelle_text:
        kopf["quelle_text"] = quelle_text
    pfad = repo / "korrekturen" / kreis / f"{datetime.date.today().isoformat()}_{name}.geojson"
    pfad.parent.mkdir(parents=True, exist_ok=True)
    # Eine Fläche je Zeile: Der Diff im Pull Request zeigt, welche sich ändern
    zeilen = ",\n".join(json.dumps(f, ensure_ascii=False, separators=(",", ":")) for f in features)
    kopf_json = json.dumps(kopf, ensure_ascii=False, separators=(",", ":"))
    pfad.write_text(f'{{"type":"FeatureCollection",\n"korrektur":{kopf_json},\n"features":[\n{zeilen}\n]}}\n')
    return pfad


def _neu(g) -> dict:
    return {"type": "Feature", "properties": {"aenderung": "neu"}, "geometry": _wgs84(g)}


def _kreis_laden(daten: str, kreis: str, cache: dict) -> tuple[dict, dict]:
    """(Eintrag im manifest.json, Flächen) des veröffentlichten Kreises — aus einem Verzeichnis oder per HTTPS."""
    if kreis in cache:
        return cache[kreis]

    def holen(name):
        if daten.startswith(("http://", "https://")):
            # Eigener Kennzeichner: Cloudflare sperrt den von urllib (Fehler 1010)
            anfrage = urllib.request.Request(f"{daten.rstrip('/')}/{name}", headers={"User-Agent": KENNUNG})
            with urllib.request.urlopen(anfrage, timeout=120) as r:
                return r.read()
        return (Path(daten) / name).read_bytes()

    manifest = json.loads(holen("manifest.json"))
    eintrag = manifest["kreise"][kreis]
    roh = holen(eintrag["datei"])
    if hashlib.sha256(roh).hexdigest() != eintrag["sha256"]:
        raise SystemExit(f"{eintrag['datei']}: Prüfsumme stimmt nicht mit manifest.json überein")
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        zipfile.ZipFile(io.BytesIO(roh)).extractall(tmp)
        flaechen = {a["id"]: a for a in gpkg_lesen(Path(tmp) / f"{kreis}.gpkg")}
    cache[kreis] = (eintrag, flaechen)
    return cache[kreis]


def pruefen(pfad: Path, repo: Path, daten: str, cache: dict | None = None) -> tuple[list[str], list[str], list[str]]:
    """(Ablehnungen, Hinweise, Zeilen für den Bericht) einer Korrekturdatei."""
    import jsonschema
    import shapely
    from shapely.geometry import MultiPolygon, shape

    cache = {} if cache is None else cache
    ab, hin, bericht = [], [], []
    try:
        rel = pfad.resolve().relative_to(repo.resolve()).as_posix()
    except ValueError:
        return [f"`{pfad}` liegt nicht im Repo `{repo}`"], [], []
    m = DATEINAME.match(rel)
    if not m:
        return [f"Dateiname/Ordner: `{rel}` — erwartet `korrekturen/<kreis>/<JJJJ-MM-TT>_<kurzname>.geojson`"], [], []
    roh = pfad.read_bytes()
    if len(roh) > MAX_BYTES:
        ab.append(f"Datei {len(roh) / 1e6:.1f} MB — höchstens 1 MB, sonst zeigt GitHub weder Karte noch Diff")
    daten_json = json.loads(roh)
    fehler = sorted(jsonschema.Draft202012Validator(json.loads(SCHEMA.read_text())).iter_errors(daten_json), key=str)
    if fehler:
        return (
            ab + [f"Schema: {f.message[:200]} (bei `{'/'.join(map(str, f.absolute_path))}`)" for f in fehler[:10]],
            [],
            [],
        )
    if re.search(r"\d\.\d{%d,}" % (NACHKOMMA + 1), roh.decode()):
        ab.append(f"Koordinaten mit mehr als {NACHKOMMA} Nachkommastellen")
    basis = {b["kreis"]: b["stand"] for b in daten_json["korrektur"]["basis"]}
    if m.group(1) not in basis:
        ab.append(f"Ordner {m.group(1)} steht nicht in korrektur.basis")

    flaechen: dict[int, dict] = {}
    for kreis, stand in basis.items():
        try:
            eintrag, f = _kreis_laden(daten, kreis, cache)
        except KeyError:
            ab.append(f"Kreis {kreis} ist nicht veröffentlicht")
            continue
        if stand != eintrag["stand"]:
            hin.append(f"Kreis {kreis}: gegen Stand {stand} korrigiert, veröffentlicht ist {eintrag['stand']}")
        flaechen |= f

    ids, neue, summe = set(), [], 0.0
    for nr, f in enumerate(daten_json["features"], 1):
        art, i, p = f["properties"]["aenderung"], f.get("id"), f["properties"]
        name = f"id {i}" if i else f"neue Fläche {nr}"
        if i is not None:
            if i in ids:
                ab.append(f"{name}: doppelt in der Datei")
            ids.add(i)
            if i not in flaechen:
                ab.append(f"{name}: nicht im veröffentlichten Stand")
                continue
            if p["basis_hash"] != flaechen[i]["geom_hash"]:
                ab.append(
                    f"**Konflikt** {name}: inzwischen geändert (basis_hash {p['basis_hash']}, jetzt {flaechen[i]['geom_hash']}) — bitte auf dem aktuellen Stand neu bearbeiten"
                )
        g = None
        if f["geometry"]:
            g = shapely.set_precision(_umrechnen(shape(f["geometry"]), 4326, 25832), 0.01)
            if g.geom_type == "Polygon":
                g = MultiPolygon([g])
            if g.is_empty or not g.is_valid or g.geom_type != "MultiPolygon":
                ab.append(f"{name}: keine gültige Fläche (auch nach dem Runden auf 1 cm)")
                continue
            neue.append((name, i, g))
        vorher = flaechen[i]["geometrie"].area if i in flaechen else 0.0
        nachher = g.area if g is not None else 0.0
        summe += abs(nachher - vorher)
        if vorher and abs(nachher - vorher) > HINWEIS_ANTEIL * vorher:
            hin.append(f"{name}: Fläche ändert sich um mehr als die Hälfte ({vorher:.0f} → {nachher:.0f} m²)")
        bericht.append(f"| {name} | {art} | {vorher:.1f} | {nachher:.1f} | {nachher - vorher:+.1f} |")
    if summe > HINWEIS_SUMME_M2:
        hin.append(f"insgesamt {summe:.0f} m² bewegt")

    # Überlappung nach dem Anwenden: mit allen nicht betroffenen Flächen und untereinander
    andere = [(i, a["geometrie"]) for i, a in flaechen.items() if i not in ids and a["geometrie"] is not None]
    baum = shapely.STRtree([g for _, g in andere])
    for name, _, g in neue:
        for j in baum.query(g, predicate="intersects"):
            if (u := g.intersection(andere[j][1]).area) > MAX_UEBERLAPPUNG_M2:
                ab.append(
                    f"{name} überlappt id {andere[j][0]} um {u:.1f} m² — die Nachbarfläche als `geaendert` mit in die Datei"
                )
    for x in range(len(neue)):
        for y in range(x + 1, len(neue)):
            if (u := neue[x][2].intersection(neue[y][2]).area) > MAX_UEBERLAPPUNG_M2:
                ab.append(f"{neue[x][0]} und {neue[y][0]} überlappen sich um {u:.1f} m²")
    # Lücken: Was eine geänderte oder entfallene Fläche abgibt und keine andere aufnimmt
    for f in daten_json["features"]:
        i = f.get("id")
        if i in flaechen and flaechen[i]["geometrie"] is not None:
            frei = flaechen[i]["geometrie"]
            for _, _, g in neue:
                frei = frei.difference(g)
            for j in baum.query(frei, predicate="intersects"):
                frei = frei.difference(andere[j][1])
            if frei.area > MAX_UEBERLAPPUNG_M2:
                hin.append(
                    f"id {i}: {frei.area:.1f} m² gehören danach zu keiner Fläche — richtig nur bei Straße, Gewässer o. Ä."
                )
    return ab, hin, bericht


def _im_repo(pfad: Path, repo: Path) -> str:
    try:
        return pfad.resolve().relative_to(repo.resolve()).as_posix()
    except ValueError:
        return str(pfad)


def bericht_md(ergebnisse: dict[str, tuple]) -> str:
    teile = []
    for pfad, (ab, hin, zeilen) in ergebnisse.items():
        teile.append(f"### `{pfad}` — {'❌ abgelehnt' if ab else '✅ in Ordnung'}")
        teile += [f"- {a}" for a in ab] + [f"- ⚠️ {h}" for h in hin]
        if zeilen:
            teile += ["", "| Fläche | Änderung | vorher m² | nachher m² | Δ m² |", "|---|---|---:|---:|---:|", *zeilen]
        teile.append("")
    return "\n".join(teile)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="befehl", required=True)
    e = sub.add_parser("erstellen", help="Korrekturdatei aus veröffentlichtem und bearbeitetem Kreis")
    e.add_argument("original", type=Path)
    e.add_argument("bearbeitet", type=Path)
    e.add_argument("--name", required=True, help="Kurzname, a–z, 0–9, _ und -")
    e.add_argument("--grund", required=True, help="Was falsch war und woher man es weiß")
    e.add_argument("--quelle", required=True, choices=QUELLEN)
    e.add_argument("--quelle-text", help="Pflicht bei luftbild_frei und andere_freie_quelle: Quelle und Lizenz")
    e.add_argument("--repo", type=Path, default=Path.cwd())
    p = sub.add_parser("pruefen", help="Korrekturdateien gegen den veröffentlichten Stand prüfen")
    p.add_argument("dateien", type=Path, nargs="+")
    p.add_argument("--daten", default=DATEN, help="Verzeichnis oder URL mit manifest.json")
    p.add_argument("--repo", type=Path, default=Path.cwd())
    p.add_argument("--bericht", type=Path, help="Bericht als Markdown hierhin (für den PR-Kommentar)")
    a = ap.parse_args(argv)
    if a.befehl == "erstellen":
        if not re.fullmatch(r"[a-z0-9_-]{3,60}", a.name):
            ap.error("--name: 3–60 Zeichen aus a–z, 0–9, _ und -")
        pfad = erstellen(a.original, a.bearbeitet, a.name, a.grund, a.quelle, a.quelle_text, a.repo)
        print(f"Geschrieben: {pfad} — vor dem Pull Request: python werkzeug/korrektur.py pruefen {pfad}")
        return 0
    cache: dict = {}
    ergebnisse = {_im_repo(d, a.repo): pruefen(d, a.repo, a.daten, cache) for d in a.dateien}
    text = bericht_md(ergebnisse)
    print(text)
    if a.bericht:
        a.bericht.write_text(text)
    return 1 if any(ab for ab, _, _ in ergebnisse.values()) else 0


if __name__ == "__main__":
    sys.exit(main())

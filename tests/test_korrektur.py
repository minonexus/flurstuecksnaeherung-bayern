"""Werkzeug: Korrektur aus bearbeitetem Kreis erstellen und gegen den veröffentlichten Stand prüfen."""

import hashlib
import json
import sys
import zipfile
from pathlib import Path

import fiona
import pytest
import shapely
from fiona.crs import CRS
from shapely.geometry import MultiPolygon, box, mapping

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "werkzeug"))
import korrektur as k  # noqa: E402

# Drei Grundstücke in Isen (UTM 32), nebeneinander: A | B | C
X, Y = 720_000.0, 5_340_000.0
FLAECHEN = {1: box(X, Y, X + 20, Y + 30), 2: box(X + 20, Y, X + 40, Y + 30), 3: box(X + 40, Y, X + 60, Y + 30)}


def _schreiben(pfad, flaechen, layer=k.LAYER):
    schema = {
        "geometry": "MultiPolygon",
        "properties": {"id": "int:64", "ags_kreis": "str:5", "kreis_stand": "int", "geom_hash": "str:16"},
    }
    with fiona.open(pfad, "w", driver="GPKG", layer=layer, schema=schema, crs=CRS.from_epsg(25832)) as aus:
        for i, g in flaechen:
            g = shapely.normalize(MultiPolygon([g]) if g.geom_type == "Polygon" else g)
            aus.write(
                {
                    "geometry": mapping(g),
                    "properties": {"id": i, "ags_kreis": "09177", "kreis_stand": 1, "geom_hash": k.geom_hash(g)},
                }
            )


@pytest.fixture
def stand(tmp_path):
    """Ein veröffentlichter Kreis wie im Download: manifest.json und 09177.gpkg.zip."""
    daten = tmp_path / "daten"
    daten.mkdir()
    _schreiben(tmp_path / "09177.gpkg", FLAECHEN.items())
    with zipfile.ZipFile(daten / "09177.gpkg.zip", "w") as z:
        z.write(tmp_path / "09177.gpkg", "09177.gpkg")
    roh = (daten / "09177.gpkg.zip").read_bytes()
    eintrag = {"stand": 1, "datei": "09177.gpkg.zip", "sha256": hashlib.sha256(roh).hexdigest()}
    (daten / "manifest.json").write_text(json.dumps({"kreise": {"09177": eintrag}}))
    repo = tmp_path / "repo"
    repo.mkdir()
    return tmp_path / "09177.gpkg", daten, repo


def _erstellen(stand, bearbeitet_flaechen, tmp_path, layer=k.LAYER):
    original, daten, repo = stand
    bearbeitet = tmp_path / "bearbeitet.gpkg"
    _schreiben(bearbeitet, bearbeitet_flaechen, layer)
    pfad = k.erstellen(original, bearbeitet, "test", "Testkorrektur an der Grenze", "ortskenntnis", None, repo)
    return pfad, json.loads(pfad.read_text())


def test_grenze_verschoben_mit_nachbar(stand, tmp_path):
    # Grenze A|B um 2 m nach rechts: A wird größer, B kleiner, C bleibt
    neu = [(1, box(X, Y, X + 22, Y + 30)), (2, box(X + 22, Y, X + 40, Y + 30)), (3, FLAECHEN[3])]
    pfad, d = _erstellen(stand, neu, tmp_path)
    assert [(f.get("id"), f["properties"]["aenderung"]) for f in d["features"]] == [(1, "geaendert"), (2, "geaendert")]
    assert d["korrektur"]["basis"] == [{"kreis": "09177", "stand": 1}]
    ab, hin, zeilen = k.pruefen(pfad, stand[2], str(stand[1]))
    assert ab == [] and hin == [] and len(zeilen) == 2


def test_geteilt_in_qgis_beide_teile_mit_derselben_id(stand, tmp_path):
    # „Objekte teilen" kopiert die Attribute: Der größere Teil behält die id, der andere ist neu
    neu = [(1, box(X, Y, X + 20, Y + 18)), (1, box(X, Y + 18, X + 20, Y + 30)), (2, FLAECHEN[2]), (3, FLAECHEN[3])]
    pfad, d = _erstellen(stand, neu, tmp_path, layer="bearbeitet")  # „Speichern unter" benennt den Layer
    assert [(f.get("id"), f["properties"]["aenderung"]) for f in d["features"]] == [(1, "geaendert"), (None, "neu")]
    assert k.pruefen(pfad, stand[2], str(stand[1]))[0] == []


def test_zusammengelegt_und_luecke(stand, tmp_path):
    # B geht in A auf; C gelöscht, ohne dass jemand die Fläche aufnimmt → Hinweis Lücke
    neu = [(1, box(X, Y, X + 40, Y + 30))]
    pfad, d = _erstellen(stand, neu, tmp_path)
    assert sorted((f["id"], f["properties"]["aenderung"]) for f in d["features"]) == [
        (1, "geaendert"),
        (2, "entfallen"),
        (3, "entfallen"),
    ]
    ab, hin, _ = k.pruefen(pfad, stand[2], str(stand[1]))
    assert ab == [] and any("id 3" in h and "keiner Fläche" in h for h in hin)


def test_konflikt_und_ueberlappung(stand, tmp_path):
    # A wächst in B hinein, ohne dass B mitkommt
    pfad, d = _erstellen(stand, [(1, box(X, Y, X + 25, Y + 30)), (2, FLAECHEN[2]), (3, FLAECHEN[3])], tmp_path)
    ab, _, _ = k.pruefen(pfad, stand[2], str(stand[1]))
    assert any("überlappt id 2" in a for a in ab)
    # Gegen einen anderen Stand bearbeitet
    d["features"][0]["properties"]["basis_hash"] = "0" * 16
    pfad.write_text(json.dumps(d))
    ab, _, _ = k.pruefen(pfad, stand[2], str(stand[1]))
    assert any(a.startswith("**Konflikt** id 1") for a in ab)


def test_name_und_ort(stand, tmp_path):
    _, daten, repo = stand
    falsch = repo / "korrekturen" / "09177" / "isen.geojson"
    falsch.parent.mkdir(parents=True)
    falsch.write_text("{}")
    assert k.pruefen(falsch, repo, str(daten))[0][0].startswith("Dateiname")
    assert "nicht im Repo" in k.pruefen(tmp_path / "x.geojson", repo, str(daten))[0][0]


def test_unveraendert_ist_keine_korrektur(stand, tmp_path):
    with pytest.raises(SystemExit, match="Keine Änderung"):
        _erstellen(stand, list(FLAECHEN.items()), tmp_path)

# Flurstücksnäherung Bayern — nicht amtlich

Rund 10,8 Millionen **genäherte** Flurstücksgrenzen für ganz Bayern, als offene Daten unter
[CC BY 4.0](LICENSE). Bayern veröffentlicht Flurstücke frei nur als Kartenbild, die
[Parzellarkarte](https://geodaten.bayern.de). Daraus hat die Minonexus GmbH die Grenzen
automatisch vektorisiert und mit einem gelernten Modell genähert.

> **Das ist kein amtlicher Nachweis.** Für Grenzen, Flächen und Eigentum gilt allein das
> Liegenschaftskataster der Bayerischen Vermessungsverwaltung. Die Flächen tragen keine
> Flurstückskennzeichen.

## Download

> **Im Test:** Bisher liegt nur Erding (`09177`) vor, die übrigen Landkreise folgen.

- [`manifest.json`](https://data.minonexus.com/flurstuecksnaeherung-bayern/manifest.json): je Landkreis der aktuelle **Stand**, das Datum, die Datei und ihre SHA-256-Prüfsumme
- `<kreis>.gpkg.zip`: je Landkreis ein GeoPackage, z. B. `09177.gpkg.zip` für Erding (≈ 60 MB). Layer `flurstuecksnaeherung`, EPSG:25832.

Der Stand eines Kreises steigt nur, wenn sich dort etwas geändert hat. Wer den Bestand bei
sich führt, vergleicht das Manifest und lädt nur die geänderten Kreise neu.

| Attribut | Bedeutung |
|---|---|
| `id` | stabil über alle Stände, auch über Neuberechnungen des Modells |
| `flaeche_m2` | Fläche in m² (genähert) |
| `ags_gemeinde`, `ags_kreis` | Gemeinde und Kreis (VG250) |
| `modell_version` | womit gerechnet; `korrektur` bei Korrekturen aus diesem Repo |
| `herkunft` | `modell` oder `korrigiert` |
| `korrektur` | bei `korrigiert`: die Datei unter [`korrekturen/`](korrekturen/), mit Begründung |
| `berechnet_am` | Tag der Berechnung, zugleich Stand der verwendeten Parzellarkarte |
| `kreis_stand` | Stand des Kreises, in dem sich die Fläche zuletzt geändert hat |
| `geom_hash` | Prüfsumme der Geometrie, Grundlage für Korrekturen |
| `hinweis` | „Näherung, nicht amtlich" |

## Wie gut ist die Näherung?

- **Prüfgebiete in Hessen und Baden-Württemberg**, wo amtliche Flurstücke frei vorliegen und nie zum Abstimmen dienten: **88,8 %** der Flurstücke mit IoU ≥ 0,85.
- **Blindtest in Bayern:** 45 Häuser, beurteilt ohne Wissen, welches Verfahren welche Fläche geliefert hat. **40 richtig.** Schwach ist die Näherung bei großen Wohnanlagen und bei Garagenzeilen, die mit einem Wohnhaus verschmelzen.

Die Fehler sind selten klein: Eine Grenze liegt entweder gut (≈ 0,2 m) oder deutlich daneben.
Genau dafür gibt es die Korrekturen.

## Korrekturen

Liegt eine Fläche falsch, kann das jede und jeder korrigieren. Je Korrektur gibt es einen Pull
Request mit einer kleinen GeoJSON-Datei. Ist sie angenommen, kommt sie mit dem nächsten Stand
des Kreises in den Download und bleibt auch bei Neuberechnungen erhalten. Anleitung:
[CONTRIBUTING.md](CONTRIBUTING.md). Ohne GIS genügt ein
[Issue „falsch genähert"](../../issues/new?template=falsch_genaehert.yml).

Unter [`korrekturen/`](korrekturen/) steht jede angenommene Korrektur mit Grund und Quelle. Das
ist zugleich die Änderungsliste des Datensatzes.

## Lizenz und Namensnennung

[CC BY 4.0](LICENSE), Lizenzgeberin ist die Minonexus GmbH. Bei jeder Nutzung so nennen:

> Flurstücksnäherung Bayern © Minonexus GmbH, CC BY 4.0. Abgeleitet aus Parzellarkarte,
> 3D-Gebäudemodellen (LoD2) und tatsächlicher Nutzung: Bayerische Vermessungsverwaltung –
> www.geodaten.bayern.de, CC BY 4.0. Hauskoordinaten: © GeoBasis-DE / BKG, CC BY 4.0. Enthält
> Informationen aus OpenStreetMap, ODbL. Verändert: automatisch vektorisiert und genähert,
> nicht amtlich.

Die Nennung der Bayerischen Vermessungsverwaltung heißt nicht, dass sie den Datensatz prüft
oder billigt.

**Eingänge:**

| Quelle | Wie sie eingeht | Lizenz |
|---|---|---|
| Parzellarkarte Bayern | Grenzlinien, vektorisiert | CC BY 4.0, BVV |
| 3D-Gebäudemodelle LoD2 Bayern | Grenzen an Gebäudeecken ausgerichtet, Merkmale | CC BY 4.0, BVV |
| Tatsächliche Nutzung (ALKIS) Bayern | Grenzen an Nutzungsecken ausgerichtet | CC BY 4.0, BVV |
| Hauskoordinaten (basemap.de) | nur Merkmal | CC BY 4.0, GeoBasis-DE / BKG |
| OpenStreetMap, Straßen | nur Merkmal, keine Koordinate im Ergebnis | ODbL |

**Trainingsdaten des Modells:** amtliche Flurstücke aus **Hessen** (frei nach § 18 HVGG) und
**Baden-Württemberg** (CC BY 4.0, GeoBasis-DE / LGL-BW). Sie sind nicht im Datensatz enthalten.

**Nicht für OpenStreetMap:** Daten unter CC BY 4.0 lassen sich ohne gesonderten Verzicht nicht
in OSM übernehmen, und eine Näherung gehört dort ohnehin nicht hinein.

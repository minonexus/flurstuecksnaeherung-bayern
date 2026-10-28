# Flurstücksnäherung Bayern — nicht amtlich

[![Lizenz: CC BY 4.0](https://img.shields.io/badge/Lizenz-CC%20BY%204.0-lightgrey)](LICENSE) [![Downloads](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fdata.minonexus.com%2Fflurstuecksnaeherung-bayern%2Fstatistik.json&query=%24.downloads&label=Downloads&color=blue)](https://data.minonexus.com/flurstuecksnaeherung-bayern/statistik.json)

Rund 11,5 Millionen **genäherte** Flurstücksgrenzen für ganz Bayern, als offene Daten unter
[CC BY 4.0](LICENSE). Bayern veröffentlicht Flurstücke frei nur als Kartenbild, die
[Parzellarkarte](https://geodaten.bayern.de). Daraus hat die Minonexus GmbH die Grenzen
automatisch vektorisiert und mit einem gelernten Modell genähert.

> **Das ist kein amtlicher Nachweis.** Für Grenzen, Flächen und Eigentum gilt allein das
> Liegenschaftskataster der Bayerischen Vermessungsverwaltung. Die Flächen tragen keine
> Flurstückskennzeichen.

## Download

Die Daten liegen unter `https://data.minonexus.com/flurstuecksnaeherung-bayern/`, je Landkreis
und kreisfreier Stadt ein GeoPackage (`<kreis>.gpkg.zip`, Layer `flurstuecksnaeherung`,
EPSG:25832). Alle 96 zusammen sind 7,5 GB. Eine Anmeldung braucht es nicht.

### Einen Kreis laden

1. Den Kreis in der Liste unten suchen und die Datei anklicken, z. B. `09177.gpkg.zip` für den Landkreis Erding.
2. Die ZIP-Datei entpacken.
3. Das GeoPackage in QGIS ziehen oder über *Layer → Layer hinzufügen → Vektorlayer* öffnen.

<details>
<summary><b>Alle 96 Kreise</b> (nach Name; Größe zum Stand vom 28.10.2026)</summary>

| Kreis | | Datei | Größe |
|---|---|---|---:|
| Aichach-Friedberg | Landkreis | [`09771.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09771.gpkg.zip) | 81 MB |
| Altötting | Landkreis | [`09171.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09171.gpkg.zip) | 53 MB |
| Amberg | Stadt | [`09361.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09361.gpkg.zip) | 9 MB |
| Amberg-Sulzbach | Landkreis | [`09371.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09371.gpkg.zip) | 137 MB |
| Ansbach | Landkreis | [`09571.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09571.gpkg.zip) | 204 MB |
| Ansbach | Stadt | [`09561.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09561.gpkg.zip) | 12 MB |
| Aschaffenburg | Landkreis | [`09671.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09671.gpkg.zip) | 107 MB |
| Aschaffenburg | Stadt | [`09661.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09661.gpkg.zip) | 16 MB |
| Augsburg | Landkreis | [`09772.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09772.gpkg.zip) | 118 MB |
| Augsburg | Stadt | [`09761.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09761.gpkg.zip) | 24 MB |
| Bad Kissingen | Landkreis | [`09672.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09672.gpkg.zip) | 119 MB |
| Bad Tölz-Wolfratshausen | Landkreis | [`09173.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09173.gpkg.zip) | 91 MB |
| Bamberg | Landkreis | [`09471.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09471.gpkg.zip) | 129 MB |
| Bamberg | Stadt | [`09461.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09461.gpkg.zip) | 9 MB |
| Bayreuth | Landkreis | [`09472.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09472.gpkg.zip) | 133 MB |
| Bayreuth | Stadt | [`09462.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09462.gpkg.zip) | 10 MB |
| Berchtesgadener Land | Landkreis | [`09172.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09172.gpkg.zip) | 59 MB |
| Cham | Landkreis | [`09372.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09372.gpkg.zip) | 149 MB |
| Coburg | Landkreis | [`09473.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09473.gpkg.zip) | 69 MB |
| Coburg | Stadt | [`09463.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09463.gpkg.zip) | 8 MB |
| Dachau | Landkreis | [`09174.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09174.gpkg.zip) | 59 MB |
| Deggendorf | Landkreis | [`09271.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09271.gpkg.zip) | 105 MB |
| Dillingen an der Donau | Landkreis | [`09773.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09773.gpkg.zip) | 93 MB |
| Dingolfing-Landau | Landkreis | [`09279.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09279.gpkg.zip) | 88 MB |
| Donau-Ries | Landkreis | [`09779.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09779.gpkg.zip) | 126 MB |
| Ebersberg | Landkreis | [`09175.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09175.gpkg.zip) | 54 MB |
| Eichstätt | Landkreis | [`09176.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09176.gpkg.zip) | 116 MB |
| Erding | Landkreis | [`09177.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09177.gpkg.zip) | 91 MB |
| Erlangen | Stadt | [`09562.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09562.gpkg.zip) | 14 MB |
| Erlangen-Höchstadt | Landkreis | [`09572.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09572.gpkg.zip) | 66 MB |
| Forchheim | Landkreis | [`09474.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09474.gpkg.zip) | 91 MB |
| Freising | Landkreis | [`09178.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09178.gpkg.zip) | 87 MB |
| Freyung-Grafenau | Landkreis | [`09272.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09272.gpkg.zip) | 99 MB |
| Fürstenfeldbruck | Landkreis | [`09179.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09179.gpkg.zip) | 52 MB |
| Fürth | Landkreis | [`09573.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09573.gpkg.zip) | 42 MB |
| Fürth | Stadt | [`09563.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09563.gpkg.zip) | 13 MB |
| Garmisch-Partenkirchen | Landkreis | [`09180.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09180.gpkg.zip) | 66 MB |
| Günzburg | Landkreis | [`09774.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09774.gpkg.zip) | 91 MB |
| Haßberge | Landkreis | [`09674.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09674.gpkg.zip) | 98 MB |
| Hof | Landkreis | [`09475.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09475.gpkg.zip) | 91 MB |
| Hof | Stadt | [`09464.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09464.gpkg.zip) | 9 MB |
| Ingolstadt | Stadt | [`09161.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09161.gpkg.zip) | 22 MB |
| Kaufbeuren | Stadt | [`09762.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09762.gpkg.zip) | 6 MB |
| Kelheim | Landkreis | [`09273.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09273.gpkg.zip) | 104 MB |
| Kempten | Stadt | [`09763.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09763.gpkg.zip) | 9 MB |
| Kitzingen | Landkreis | [`09675.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09675.gpkg.zip) | 81 MB |
| Kronach | Landkreis | [`09476.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09476.gpkg.zip) | 69 MB |
| Kulmbach | Landkreis | [`09477.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09477.gpkg.zip) | 72 MB |
| Landsberg am Lech | Landkreis | [`09181.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09181.gpkg.zip) | 76 MB |
| Landshut | Landkreis | [`09274.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09274.gpkg.zip) | 127 MB |
| Landshut | Stadt | [`09261.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09261.gpkg.zip) | 11 MB |
| Lichtenfels | Landkreis | [`09478.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09478.gpkg.zip) | 64 MB |
| Lindau | Landkreis | [`09776.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09776.gpkg.zip) | 48 MB |
| Main-Spessart | Landkreis | [`09677.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09677.gpkg.zip) | 159 MB |
| Memmingen | Stadt | [`09764.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09764.gpkg.zip) | 10 MB |
| Miesbach | Landkreis | [`09182.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09182.gpkg.zip) | 73 MB |
| Miltenberg | Landkreis | [`09676.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09676.gpkg.zip) | 107 MB |
| Mühldorf am Inn | Landkreis | [`09183.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09183.gpkg.zip) | 81 MB |
| München | Landkreis | [`09184.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09184.gpkg.zip) | 66 MB |
| München | Stadt | [`09162.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09162.gpkg.zip) | 60 MB |
| Neu-Ulm | Landkreis | [`09775.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09775.gpkg.zip) | 68 MB |
| Neuburg-Schrobenhausen | Landkreis | [`09185.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09185.gpkg.zip) | 80 MB |
| Neumarkt in der Oberpfalz | Landkreis | [`09373.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09373.gpkg.zip) | 128 MB |
| Neustadt an der Aisch-Bad Windsheim | Landkreis | [`09575.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09575.gpkg.zip) | 127 MB |
| Neustadt an der Waldnaab | Landkreis | [`09374.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09374.gpkg.zip) | 116 MB |
| Nürnberg | Stadt | [`09564.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09564.gpkg.zip) | 39 MB |
| Nürnberger Land | Landkreis | [`09574.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09574.gpkg.zip) | 113 MB |
| Oberallgäu | Landkreis | [`09780.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09780.gpkg.zip) | 126 MB |
| Ostallgäu | Landkreis | [`09777.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09777.gpkg.zip) | 146 MB |
| Passau | Landkreis | [`09275.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09275.gpkg.zip) | 165 MB |
| Passau | Stadt | [`09262.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09262.gpkg.zip) | 10 MB |
| Pfaffenhofen an der Ilm | Landkreis | [`09186.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09186.gpkg.zip) | 88 MB |
| Regen | Landkreis | [`09276.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09276.gpkg.zip) | 92 MB |
| Regensburg | Landkreis | [`09375.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09375.gpkg.zip) | 139 MB |
| Regensburg | Stadt | [`09362.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09362.gpkg.zip) | 14 MB |
| Rhön-Grabfeld | Landkreis | [`09673.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09673.gpkg.zip) | 136 MB |
| Rosenheim | Landkreis | [`09187.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09187.gpkg.zip) | 163 MB |
| Rosenheim | Stadt | [`09163.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09163.gpkg.zip) | 8 MB |
| Roth | Landkreis | [`09576.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09576.gpkg.zip) | 102 MB |
| Rottal-Inn | Landkreis | [`09277.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09277.gpkg.zip) | 132 MB |
| Schwabach | Stadt | [`09565.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09565.gpkg.zip) | 8 MB |
| Schwandorf | Landkreis | [`09376.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09376.gpkg.zip) | 143 MB |
| Schweinfurt | Landkreis | [`09678.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09678.gpkg.zip) | 104 MB |
| Schweinfurt | Stadt | [`09662.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09662.gpkg.zip) | 7 MB |
| Starnberg | Landkreis | [`09188.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09188.gpkg.zip) | 51 MB |
| Straubing | Stadt | [`09263.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09263.gpkg.zip) | 9 MB |
| Straubing-Bogen | Landkreis | [`09278.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09278.gpkg.zip) | 115 MB |
| Tirschenreuth | Landkreis | [`09377.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09377.gpkg.zip) | 91 MB |
| Traunstein | Landkreis | [`09189.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09189.gpkg.zip) | 135 MB |
| Unterallgäu | Landkreis | [`09778.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09778.gpkg.zip) | 132 MB |
| Weiden in der Oberpfalz | Stadt | [`09363.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09363.gpkg.zip) | 11 MB |
| Weilheim-Schongau | Landkreis | [`09190.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09190.gpkg.zip) | 103 MB |
| Weißenburg-Gunzenhausen | Landkreis | [`09577.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09577.gpkg.zip) | 98 MB |
| Wunsiedel i. Fichtelgebirge | Landkreis | [`09479.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09479.gpkg.zip) | 62 MB |
| Würzburg | Landkreis | [`09679.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09679.gpkg.zip) | 122 MB |
| Würzburg | Stadt | [`09663.gpkg.zip`](https://data.minonexus.com/flurstuecksnaeherung-bayern/09663.gpkg.zip) | 17 MB |

Dieselbe Liste maschinenlesbar: [`kreise.csv`](kreise.csv) (Kreisschlüssel, Name, Art).
</details>

### Ohne Download lesen

GDAL und alles, was darauf aufbaut, liest die Datei direkt aus der URL. Das lohnt sich, wenn nur
ein Ausschnitt gebraucht wird:

```bash
# Überblick: Anzahl der Flächen, Attribute, Koordinatensystem
ogrinfo -ro -so -al /vsizip//vsicurl/https://data.minonexus.com/flurstuecksnaeherung-bayern/09762.gpkg.zip/09762.gpkg

# Eine Gemeinde als GeoJSON in WGS84 (Erding, Stadt)
ogr2ogr -f GeoJSON erding.geojson -t_srs EPSG:4326 -where "ags_gemeinde = '09177117'" \
  /vsizip//vsicurl/https://data.minonexus.com/flurstuecksnaeherung-bayern/09177.gpkg.zip/09177.gpkg
```

Mit `ogr2ogr` lässt sich das GeoPackage in jedes andere Format umwandeln, etwa Shapefile,
GeoParquet oder FlatGeobuf. Angeboten wird bewusst nur dieses eine Format.

### Ganz Bayern laden

Das Manifest nennt jede Datei mit ihrer SHA-256-Prüfsumme. Damit lässt sich prüfen, ob alles
vollständig angekommen ist (braucht `curl` und `jq`):

```bash
B=https://data.minonexus.com/flurstuecksnaeherung-bayern
curl -fsSO "$B/manifest.json"
jq -r '.kreise[].datei' manifest.json | while read -r f; do curl -fsSO "$B/$f"; done
jq -r '.kreise[] | "\(.sha256)  \(.datei)"' manifest.json | sha256sum -c --quiet && echo "alle Prüfsummen stimmen"
```

### Aktuell halten

Jeder Kreis hat im [`manifest.json`](https://data.minonexus.com/flurstuecksnaeherung-bayern/manifest.json)
einen **Stand**. Er steigt nur, wenn sich in diesem Kreis etwas geändert hat, etwa durch eine
Korrektur oder eine Neuberechnung. Neu zu laden sind also nur die Kreise, deren Stand gestiegen ist:

```bash
B=https://data.minonexus.com/flurstuecksnaeherung-bayern
cp manifest.json manifest.alt.json
curl -fsSO "$B/manifest.json"
jq -r --slurpfile alt manifest.alt.json \
  '.kreise | to_entries[] | select(.value.stand != $alt[0].kreise[.key].stand) | .value.datei' manifest.json |
  while read -r f; do echo "neu: $f"; curl -fsSO "$B/$f"; done
```

Die `id` einer Fläche bleibt über alle Stände gleich. Welche Flächen sich geändert haben, zeigt
`kreis_stand`: Er ist der Stand, in dem sich die Fläche zuletzt geändert hat.

### Attribute

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

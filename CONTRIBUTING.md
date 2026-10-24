# Korrekturen beitragen

Eine Korrektur ist **eine kleine GeoJSON-Datei je Pull Request** unter
`korrekturen/<kreis>/<JJJJ-MM-TT>_<kurzname>.geojson`. Sie enthält nur die betroffenen Flächen.
Den Bestand selbst gibt es im Download, nicht in diesem Repo.

## Mit QGIS

1. **Den Kreis laden:** `<kreis>.gpkg.zip` aus dem [Download](README.md#download) holen, entpacken und eine Kopie anlegen, z. B. `09177_bearbeitet.gpkg`.
2. **In QGIS bearbeiten:** die Kopie öffnen und die Grenzen richtigstellen.
   - **Teilen** („Objekte teilen"): Beide Teile behalten die Attribute. Das Werkzeug erkennt, welcher Teil der alte ist.
   - **Zusammenlegen:** eine Fläche erweitern, die andere löschen.
   - **Neu zeichnen:** ohne `id`.
   - **Gemeinsame Grenzen:** Verschiebst du eine Grenze, muss der Nachbar mit. Sonst überlappen sich die Flächen, und die Prüfung lehnt ab. Hilfreich ist das Einrasten auf die Nachbarfläche und das „topologische Bearbeiten".
3. **Die Korrekturdatei erstellen:** aus einer Arbeitskopie dieses Repos:
   ```bash
   pip install -r requirements.txt
   python werkzeug/korrektur.py erstellen 09177.gpkg 09177_bearbeitet.gpkg \
       --name isen_doppelhaus --quelle parzellarkarte \
       --grund "Doppelhaus als ein Grundstück genähert; die Wand ist in der Parzellarkarte als Grenze zu sehen"
   ```
4. **Prüfen:** `python werkzeug/korrektur.py pruefen korrekturen/09177/<datei>.geojson`. Das ist dieselbe Prüfung, die beim Pull Request läuft.
5. **Pull Request stellen.** Die Prüfung schreibt ihr Ergebnis als Kommentar dazu: je Fläche die Art der Änderung und die Flächen vorher und nachher. GitHub zeigt die Datei als Karte.

Ohne GIS: ein [Issue „falsch genähert"](../../issues/new?template=falsch_genaehert.yml) mit Ort
und Beschreibung. Wir erstellen die Datei dann.

## Regeln

- **Nur freie Quellen.** `--quelle` ist eine von:
  - `ortskenntnis`: selbst gesehen, z. B. Zaun, Hecke, Grenzstein
  - `parzellarkarte`: in der Parzellarkarte erkennbar
  - `luftbild_frei`: ein frei lizenziertes Luftbild, mit `--quelle-text` „welches, welche Lizenz"
  - `andere_freie_quelle`: ebenso mit `--quelle-text`

  **Nicht erlaubt** sind amtliche ALKIS-Auszüge, Kaufverträge, Lagepläne mit Flurstücksangaben und Kartendienste, deren Nutzungsbedingungen das Abzeichnen verbieten. Das ALKIS ist in Bayern kein Open Data.
- **Lizenz:** Mit dem Pull Request stellst du deine Korrektur unter [CC BY 4.0](LICENSE), dieselbe Lizenz wie der Datensatz. Genannt wirst du über den Commit, nicht in den Daten.
- **Keine personenbezogenen Daten:** keine Namen, Eigentümer oder Hausnummern in `grund`. Das Schema lässt keine weiteren Attribute zu.
- **Eine Korrektur, eine Datei.** Eine angenommene Datei wird nicht mehr geändert. Wer dieselbe Fläche später noch einmal korrigiert, legt eine neue Datei an, gegen den aktuellen Stand.
- **Höchstens 500 Flächen und 1 MB je Datei.** Größeres bitte aufteilen, sonst zeigt GitHub weder Karte noch Diff.

## Was die Prüfung meldet

| | |
|---|---|
| ❌ **Konflikt** | Die Fläche hat sich seit deinem Download geändert (`basis_hash`). Lade den aktuellen Stand und bearbeite neu. |
| ❌ Überlappung | Eine neue Grenze überlappt eine andere Fläche um mehr als 0,5 m². Nimm den genannten Nachbarn mit in die Bearbeitung. |
| ❌ Schema, Name, Größe | siehe Meldung |
| ⚠️ Lücke | Fläche, die danach zu keinem Flurstück gehört. Bei Straße oder Bach richtig, sonst bitte prüfen. |
| ⚠️ große Änderung | mehr als die Hälfte einer Fläche oder über 10.000 m² insgesamt, zur Kenntnis im Review |

Das Format im Einzelnen: [`schema/naeherung_korrektur.schema.json`](schema/naeherung_korrektur.schema.json).

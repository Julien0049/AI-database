# Bewertung: Importtest Word und PDF

**Status:** Agentenauswertung (Claude), vom Nutzer noch zu prüfen. Die Kennzahlen sind gemessen; die Deutung ist eine Einschätzung.
**Lauf:** [importtest_2026-11-05.json](./importtest_2026-11-05.json), 05.11.2026, Skript [import_test.py](../scripts/import_test.py). Kein Sprachmodell beteiligt.
**Aufbau:** Sechs Markdown-Testberichte mit unterschiedlichen Formatfällen wurden vom Skript in Word-Dateien (mit Überschrift-Formatvorlage, `python-docx`) und PDF-Dateien (Titel in großer, fetter Schrift, `reportlab`) umgewandelt, wieder eingelesen (`python-docx`, `pypdf`) und mit denselben Regeln für Titel und Datum ausgewertet wie die Markdown-Vorlage. Text vollständig = Anteil der Sätze und Zeilen der Vorlage, die im eingelesenen Text wiederzufinden sind (Grundlage der Zitatprüfung).

## Ergebnis

| Fall | Word: Titel / Datum / Text | PDF: Titel / Datum / Text |
|---|---|---|
| Überschrift und „Datum:“-Zeile | ok / ok / 6 von 6 | **Dateiname** / ok / 6 von 6 |
| keine Überschrift, Datum ohne Beschriftung | Dateiname (wie Markdown) / ok / 6 von 6 | Dateiname (wie Markdown) / ok / 6 von 6 |
| keine Überschrift, ausgeschriebenes Datum in der Unterschrift | Dateiname (wie Markdown) / ok / 4 von 4 | Dateiname (wie Markdown) / ok / 4 von 4 |
| kein Datum | ok / „Datum unbekannt“ (wie Markdown) / 4 von 4 | **Dateiname** / „Datum unbekannt“ / 4 von 4 |
| Ereignisdatum vor dem Berichtsdatum | ok / Ereignisdatum (wie Markdown, bekannte Grenze) / 6 von 6 | **Dateiname** / Ereignisdatum / 6 von 6 |
| „Stand: 2025-01-20“ | ok / ok / 5 von 5 | **Dateiname** / ok / 5 von 5 |

Zusätzlich geprüft für PDF: „erste Zeile als Titel“. Das ergibt nur in 2 von 6 Fällen den richtigen Titel: Zweimal ist die Überschrift durch den Zeilenumbruch abgeschnitten („After-Action-Report: Umgang mit fehlenden“), zweimal steht bei Berichten ohne Überschrift das Datum oder der Anfang des Fließtexts in der ersten Zeile.

## Beobachtungen

- **Word verhält sich wie Markdown.** Titel, Datum und Text kommen in allen sechs Fällen gleich heraus, weil die Überschrift als Formatvorlage erkennbar ist.
- **PDF: Text und Datum ja, Titel nein.** Der Text ist vollständig und das Datum wird wie bei Markdown erkannt; Zitatprüfung und zeitliche Einordnung funktionieren damit. Die Überschrift geht aber als Struktur verloren: In allen vier Berichten mit Überschrift erscheint in der Fußnote nur der Dateiname. Eine einfache Ersatzregel (erste Zeile) ist unzuverlässig.
- **Für das Ablageformat heißt das:** Ein Titel lässt sich nur zuverlässig auslesen, wenn das Format ihn als Struktur kennt (Markdown-Überschrift, Word-Formatvorlage) oder wenn er an fester, beschrifteter Stelle steht (etwa „Titel: …“). Das stützt die Empfehlung zum einheitlichen Ablageformat.

## Grenzen

- **Idealisierte Dateien:** Die Word- und PDF-Dateien wurden vom Programm erzeugt und sind sauber (eine Spalte, keine Kopf- und Fußzeilen, keine Silbentrennung, keine Tabellen). Echte Dokumente dürften schlechter abschneiden; insbesondere setzen viele Nutzer Überschriften in Word von Hand fett statt mit Formatvorlage, dann ginge der Titel auch dort verloren.
- **Keine Scans und Bilder:** Eingescannte PDFs oder Fotos enthalten keinen Text; dafür wäre Texterkennung (OCR) nötig, nicht getestet.
- Dateieigenschaften (Autor, Erstelldatum in den Metadaten der Datei) wurden nicht ausgewertet.
- Sechs Berichte, je ein Erzeugungsweg pro Format.

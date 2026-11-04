# Bewertung: Gemini 2.5 Pro, zehnter Test (Widerspruch nur über das Datum auflösbar)

**Status:** Agentenbewertung (Claude), vom Nutzer noch zu prüfen.
**Lauf:** [ergebnisse_google_gemini-2.5-pro_2026-11-04_v10.json](./ergebnisse_google_gemini-2.5-pro_2026-11-04_v10.json), 04.11.2026, Modell `google/gemini-2.5-pro` über OpenRouter, Notebook [citation_check_v7.ipynb](../notebooks/citation_check_v7.ipynb), drei Durchläufe, nur Fragen 18 und 19.
**Aufbau:** Wie v9, plus zwei Berichte zur Schlüsselrückgabe nach Abendseminaren, die sich ohne sprachlichen Hinweis auf die Reihenfolge widersprechen. Der neuere Bericht (14.10.2025) steht in der Sammlung vor dem älteren (03.04.2024) und hat die kleinere Kennung (B14 vor B15).
**Maßstab:** Fragen 18 und 19 in [test_questions.md](../data/synthetic_reports/test_questions.md).

## Ergebnis

6 von 6 Antworten erfüllen die Kriterien. Alle 15 Zitate gültig, 29 s Laufzeit für 6 Anfragen.

| Frage | D1 | D2 | D3 | Anmerkung |
|---|---|---|---|---|
| 18 | erfüllt | erfüllt | erfüllt | Schlüsselkasten im Seminarbüro, nur der neuere Bericht als Quelle; die Pforte wird nicht erwähnt. D1 lässt den Eintrag durch die Seminarleitung weg, was für die Frage „wo“ ausreicht. |
| 19 | erfüllt | erfüllt | erfüllt | Richtige Reihenfolge (Pforte, dann Schlüsselkasten), obwohl der ältere Bericht hinten steht; kein erfundener Grund. Keine Antwort sagt ausdrücklich, dass die Berichte keinen Grund nennen (nicht gefordert). |

## Beobachtungen

- **Das Modell ordnet nach dem Datum, nicht nach Position oder Kennung.** Da Reihenfolge und Kennung in die falsche Richtung zeigten und kein sprachlicher Hinweis vorhanden war, ist das Datum die naheliegende Erklärung für die durchgehend richtige Einordnung.
- Die Antworten sprechen von „einer jüngeren/späteren Regelung“. Sie behaupten keine formelle Gültigkeit, das Wort „Regelung“ geht aber etwas über „Bericht“ hinaus.

## Grenzen

- Ein einzelnes Berichtspaar mit gleichem Datumsformat und großem Zeitabstand (rund 18 Monate). Nahe beieinander liegende Daten, unterschiedliche Datumsformate oder mehrere Stände wurden nicht geprüft.
- Nur die ungünstige Reihenfolge wurde getestet, keine Gegenprobe mit vertauschter Reihenfolge.
- Sechs Antworten zeigen ein klares Muster, sind aber keine belastbare Häufigkeit.
- Die Bewertung stammt von einem anderen KI-Modell und ist keine unabhängige menschliche Prüfung.

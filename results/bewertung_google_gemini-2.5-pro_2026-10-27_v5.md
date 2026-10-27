# Bewertung: Gemini 2.5 Pro, fünfter Test (Erfahrungsregel, drei Durchläufe)

**Status:** Agentenbewertung (Claude), vom Nutzer noch zu prüfen.
**Lauf:** [ergebnisse_google_gemini-2.5-pro_2026-10-27_v5.json](./ergebnisse_google_gemini-2.5-pro_2026-10-27_v5.json), 27.10.2026, Modell `google/gemini-2.5-pro` über OpenRouter.
**Aufbau:** Dreizehn Berichte vollständig im Prompt, keine Suche, drei Durchläufe. Änderungen gegenüber v4: Regel 3 unterscheidet Verfahren und Erfahrungen (Sichtweisen nebeneinander mit Titel und Datum); Quellenformat „Titel“ (TT.MM.JJJJ).
**Maßstab:** Antwortentwürfe und Kriterien in [test_questions.md](../data/synthetic_reports/test_questions.md) sowie der Wortlaut der Berichte. Die indirekte Antwort auf Verantwortungsfragen wird wie bisher als „teilweise“ geführt, damit die Läufe vergleichbar bleiben; der Nutzer hat sie als nicht falsch akzeptiert (Entscheidung C).

## Ergebnis

31 von 39 Antworten erfüllen die Kriterien, 8 teilweise (Durchlauf 1: 12/13, Durchlauf 2: 9/13, Durchlauf 3: 10/13). Nichts wurde inhaltlich erfunden.

| Frage | D1 | D2 | D3 | Anmerkung |
|---|---|---|---|---|
| 1 | erfüllt | erfüllt | erfüllt | Stabil. |
| 2 | erfüllt | erfüllt | erfüllt | Stabil. |
| 3 | erfüllt | teilweise | erfüllt | D2 nennt zusätzlich „Rückgabe ausgegebener Materialsets“ (14.09.2022), der die eintägige Regel nicht stützt. |
| 4 | erfüllt | erfüllt | teilweise | D3 nennt wieder den Fahrzeugbericht vom 15.09.2025 als Quelle. |
| 5 | erfüllt | teilweise | teilweise | D1 sagt ausdrücklich, dass die Berichte keine Person benennen. D2/D3 nur indirekt; D3 nennt zusätzlich „Erfassung von Fahrzeugschäden“ als Quelle. |
| 6 | erfüllt | erfüllt | erfüllt | Stabil. |
| 7 | erfüllt | erfüllt | erfüllt | Stabil. |
| 8 | erfüllt | erfüllt | erfüllt | D1/D3 nennen ergänzend „Rückgabe von Dienstfahrzeugen“ (12.04.2023); das ist passend. |
| 9 | teilweise | teilweise | teilweise | Verantwortung in allen drei Durchläufen nur indirekt (in v4 einmal ausdrücklich). |
| 10 | erfüllt | erfüllt | erfüllt | Stabil. |
| 11 | erfüllt | erfüllt | erfüllt | **Verbessert gegenüber v4:** Alle drei Sichtweisen zur Jacke einzeln mit Titel und Datum, Überjacke als Vorgabe, nichts ausgelassen. |
| 12 | erfüllt | teilweise | erfüllt | Sichtweisen nebeneinander, keine Priorität nach Datum. D2 schreibt nur „einem Bericht zufolge“ und ordnet die Sichtweisen nicht den Titeln zu. |
| 13 | erfüllt | erfüllt | erfüllt | Stabil. |

## Beobachtungen

- **Die Erfahrungsregel wirkt:** Fragen 11 und 12 nennen in fünf von sechs Antworten jede Sichtweise mit Titel und Datum. In v4 (ohne Regel) geschah das nicht.
- **Quellenformat jetzt zuverlässig:** Alle Antworten mit Quellenangabe enthalten ein Datum. Der Titel erscheint uneinheitlich mal mit, mal ohne das Präfix „After-Action-Report:“ (32 von 39 mit).
- **Falsche Zusatzquellen treten vereinzelt bei wechselnden Fragen auf** (3 von 39 Antworten: Fragen 3, 4, 5). Das Modell nennt dann einen thematisch ähnlichen Bericht, der die Aussage nicht stützt. Das ist der wichtigste verbleibende Fehlertyp und spricht für Quellenangaben, die die Anwendung aus den tatsächlich verwendeten Passagen erzeugt.
- **Schwankung zwischen Durchläufen ist erheblich** (9 bis 12 von 13 bei identischem Aufbau). Vergleiche zwischen Einzelläufen früherer Versionen sind entsprechend unsicher.

## Grenzen

- Quellenabruf ist nicht getestet, weil das Modell alle Dokumente vollständig erhielt.
- Drei Durchläufe zeigen die Schwankung, sind aber zu wenige für belastbare Häufigkeiten.
- Die Bewertung stammt von einem anderen KI-Modell und ist keine unabhängige menschliche Prüfung.

# Bewertung: Gemini 2.5 Pro, sechster Test (Zusammenfassungen und Änderungsverlauf)

**Status:** Agentenbewertung (Claude), vom Nutzer noch zu prüfen.
**Lauf:** [ergebnisse_google_gemini-2.5-pro_2026-10-27_v6.json](./ergebnisse_google_gemini-2.5-pro_2026-10-27_v6.json), 27.10.2026, Modell `google/gemini-2.5-pro` über OpenRouter.
**Aufbau:** Dreizehn Berichte vollständig im Prompt, keine Suche, drei Durchläufe. Systemprompt identisch mit v5. Neu: Fragen 14–17 (Zusammenfassung Verfahren, Zusammenfassung Erfahrungen, themenübergreifende Zusammenfassung, Änderungsverlauf).
**Maßstab:** Antwortentwürfe, Checklisten und Kriterien in [test_questions.md](../data/synthetic_reports/test_questions.md) sowie der Wortlaut der Berichte. Indirekte Antworten auf Verantwortungsfragen werden wie bisher als „teilweise“ geführt (vom Nutzer als nicht falsch akzeptiert, Entscheidung C).

## Ergebnis

41 von 51 Antworten erfüllen die Kriterien, 10 teilweise. Fragen 1–13: 32 von 39 (v5: 31 von 39). Fragen 14–16: 9 von 9. Frage 17: 0 von 3 vollständig.

| Frage | D1 | D2 | D3 | Anmerkung |
|---|---|---|---|---|
| 1–3 | erfüllt | erfüllt | erfüllt | Stabil. |
| 4 | teilweise | erfüllt | erfüllt | D1 nennt wieder den Fahrzeugbericht vom 15.09.2025 als Quelle. |
| 5 | teilweise | teilweise | teilweise | Verantwortung nur indirekt; D3 nennt zusätzlich „Erfassung von Fahrzeugschäden“. |
| 6–8 | erfüllt | erfüllt | erfüllt | Stabil. |
| 9 | teilweise | teilweise | teilweise | Verantwortung nur indirekt. |
| 10–13 | erfüllt | erfüllt | erfüllt | Stabil; Sichtweisen in 11/12 jeweils mit Titel und Datum. |
| 14 | erfüllt | erfüllt | erfüllt | Checkliste vollständig bis auf kleine Details („getrennte Felder“ fehlt überall; D2 ohne „Kennzeichen und Datum“ beim Schadensformular). Kein „vollgetankt“, nichts aus Material- oder Kleidungsberichten. |
| 15 | erfüllt | erfüllt | erfüllt | Alle sechs Checklistenpunkte; Sichtweisen mit Titel und Datum. Die Überjacke steht in D1/D2 teils innerhalb der Erfahrungen, wird aber als Vorschrift benannt. D1 und D3 wiederholen den Inhalt in Einleitung und Liste. |
| 16 | erfüllt | erfüllt | erfüllt | Material (aktueller Stand), Fahrzeuge und Kleidung sauber getrennt; weder das Verfahren vom 02.03.2024 noch die eintägige Regel übernommen. |
| 17 | teilweise | teilweise | teilweise | Reihenfolge und Inhalte korrekt; D2 gibt den Grund der jüngsten Änderung richtig wieder. Die einzelnen Stände sind aber nicht mit Titel und Datum verknüpft; die Daten stehen nur in der Quellenliste. D1 lässt den Stand von 2022 aus. Kein Durchlauf weist darauf hin, dass der Bericht von 2022 nicht ausdrücklich mehrtägige Seminare betrifft. |

## Beobachtungen

- **Zusammenfassungen gelingen gut:** Bei allen drei Zusammenfassungsfragen sind die Checklisten (fast) vollständig abgedeckt, überholte Verfahren erscheinen nicht, und Themen werden nicht vermischt. Mit dreizehn kurzen Berichten im Prompt ist das allerdings ein günstiger Fall; bei vielen Berichten und vorgeschalteter Suche ist das nicht geprüft.
- **Änderungsverlauf ohne Zeitbezug je Stand:** Der Prompt verlangt Titel und Datum je Sichtweise nur für Erfahrungen, nicht für Änderungsverläufe. Bei Frage 17 fehlt diese Zuordnung entsprechend in allen Durchläufen.
- **Falsche Zusatzquellen** weiterhin vereinzelt (2 von 51 Antworten).
- **Länge:** Erfahrungszusammenfassungen sind teils redundant (Kurzfassung plus ausführliche Liste mit gleichem Inhalt).

## Grenzen

- Quellenabruf ist nicht getestet, weil das Modell alle Dokumente vollständig erhielt.
- Drei Durchläufe zeigen die Schwankung, sind aber zu wenige für belastbare Häufigkeiten.
- Die Laufzeit wurde in dieser Notebook-Fassung noch nicht gemessen.
- Die Bewertung stammt von einem anderen KI-Modell und ist keine unabhängige menschliche Prüfung.

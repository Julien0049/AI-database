# Bewertung: Gemini 2.5 Pro, neunter Test (variiertes Berichtsformat)

**Status:** Agentenbewertung (Claude), vom Nutzer noch zu prüfen.
**Lauf:** [ergebnisse_google_gemini-2.5-pro_2026-11-04_v9.json](./ergebnisse_google_gemini-2.5-pro_2026-11-04_v9.json), 04.11.2026, Modell `google/gemini-2.5-pro` über OpenRouter, Notebook [citation_check_v7.ipynb](../notebooks/citation_check_v7.ipynb), drei Durchläufe.
**Aufbau:** Wie v8 (Prompt mit Regel 7). Einzige Änderung: Vier Berichte mit gleichem Inhalt, aber abweichendem Format (siehe [README](../data/synthetic_reports/README.md)): Fahrtenbuch-Formular (B10), Rückgabe gemeinsamer Sets (B8), Reservierung (B4, ohne Datum), Kleidung im Winter (B2). Titel und Datum liest das Programm aus.
**Maßstab:** Wie v8, mit dem angepassten Kriterium zu Frage 17 (Stand von 2022 darf fehlen).

## Metadaten (Programm)

Alle vier abweichenden Berichte wurden wie erwartet eingelesen: B8 und B10 mit korrektem Datum (20.01.2025, 18.03.2025), B2 mit 15.02.2023, B4 mit „Datum unbekannt“. B2 und B10 haben keine Überschrift; in der Fußnote steht deshalb der Dateiname, z. B. „AAR-2025-03-18-logbook-form.md“ (18.03.2025). Das ist korrekt, aber für Nutzer weniger lesbar.

## Kennzahlen

| Kennzahl | v8 | v9 |
|---|---|---|
| Belege gültig | 208 von 208 | 211 von 211 |
| Nicht auswertbares JSON | 0 | 0 |
| Sätze ohne Beleg (alle Lückenhinweise) | 15 | 14 |
| Sätze / Wörter gesamt | 194 / 2643 | 191 / 2684 |
| Laufzeit gesamt | 190 s | 198 s |

## Ergebnis (inhaltlich)

43 von 51 Antworten erfüllen die Kriterien, 8 teilweise (v8 nach Neubewertung: 45). Fragen 1–13: 32 von 39 (v8: 33). Fragen 14–16: 8 von 9. Frage 17: 3 von 3.

| Frage | D1 | D2 | D3 | Anmerkung |
|---|---|---|---|---|
| 1–2 | erfüllt | erfüllt | erfüllt | Der Bericht mit „Stand: 2025-01-20“ bestimmt weiterhin die Antwort. |
| 3 | erfüllt | erfüllt | erfüllt | Stabil. |
| 4 | erfüllt | erfüllt | teilweise | D3 belegt einen Zusatzsatz wieder mit dem Fahrzeugbericht B12. |
| 5 | teilweise | teilweise | erfüllt | D1 nennt ausdrücklich die Lücke, belegt aber einen Satz zusätzlich mit dem Fahrzeugschadensbericht B7. D2 nur indirekt. |
| 6 | teilweise | erfüllt | erfüllt | D1 nennt nur die Lücke, nicht die belegten Angaben (Set-Kennung usw.). |
| 7 | erfüllt | erfüllt | erfüllt | Neue Tankregel aus dem Bericht ohne Überschrift mit ausgeschriebenem Datum. |
| 8 | erfüllt | erfüllt | erfüllt | Stabil. |
| 9 | teilweise | teilweise | teilweise | Verantwortung nur indirekt (Entscheidung C). |
| 10 | erfüllt | erfüllt | erfüllt | Bericht ohne Datum korrekt verwendet; kein Datum erfunden; Fußnote „Datum unbekannt“. |
| 11–13 | erfüllt | erfüllt | erfüllt | Winterbericht ohne Überschrift in allen Antworten gefunden und richtig belegt. |
| 14 | erfüllt | erfüllt | erfüllt | Vollständig; D3 deutlich länger (139 Wörter). |
| 15 | teilweise | erfüllt | erfüllt | D1 fasst die Sichtweisen in Sätzen mit mehreren Belegen zusammen; welcher Bericht welche Sichtweise stützt, ist nicht mehr erkennbar. „Dünne Schichten bewährten sich beim Gehen“ fehlt als eigene Aussage. |
| 16 | erfüllt | erfüllt | erfüllt | Checkliste abgedeckt; D2/D3 fassen Sichtweisen teils in einem Satz mit mehreren Belegen zusammen. |
| 17 | erfüllt | erfüllt | erfüllt | Stände in richtiger Reihenfolge, jeweils belegt; D1/D3 nennen 2022, ohne zu behaupten, dass dieser Bericht mehrtägige Seminare betrifft. |

## Beobachtungen

- **Das Format beeinträchtigt die Antworten nicht erkennbar.** Alle Fragen, bei denen der neueste Stand von einem umformatierten Bericht abhängt (1, 2, 7, 16, 17), wurden in allen Durchläufen richtig beantwortet. Berichte ohne Überschrift oder Datum wurden gefunden und korrekt belegt.
- **Einschränkung dieser Aussage:** Es ist nicht nachgewiesen, dass das Modell die Daten tatsächlich liest. Es könnte den jeweils neuesten Bericht auch an Formulierungen erkennen („für kommende … Seminare“, „jetzt“). Ein härterer Test wäre ein Widerspruch, der nur über das Datum aufzulösen ist.
- **Fußnoten bei fehlender Überschrift:** Der Dateiname als Titel ist korrekt und findbar, aber unschön. Im realen Einsatz spricht das für ein einheitliches Ablageformat (siehe Policy-Brief-Notizen).
- **Zusammenfassen über mehrere Belege:** In Fragen 15 und 16 fasst das Modell gegensätzliche Sichtweisen öfter in einem Satz mit mehreren Belegen zusammen. Die Fußnoten zeigen dann nicht mehr, welche Sichtweise aus welchem Bericht stammt. Möglicherweise eine Nebenwirkung von Regel 7 (knapp).
- **Falsche Zusatzquellen** wieder vereinzelt (2 von 51: Frage 4 D3, Frage 5 D1); die Zitatprüfung erkennt sie nicht.

## Grenzen

- Der Unterschied zu v8 (43 gegenüber 45) liegt innerhalb der beobachteten Schwankung.
- Nur vier von dreizehn Berichten sind variiert; die Datumsformate im Programm decken nur die bekannten Fälle ab.
- Die Bewertung stammt von einem anderen KI-Modell und ist keine unabhängige menschliche Prüfung.

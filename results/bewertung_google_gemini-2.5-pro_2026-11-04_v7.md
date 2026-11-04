# Bewertung: Gemini 2.5 Pro, siebter Test (Zitatprüfung)

**Status:** Agentenbewertung (Claude), vom Nutzer noch zu prüfen.
**Lauf:** [ergebnisse_google_gemini-2.5-pro_2026-11-04_v7.json](./ergebnisse_google_gemini-2.5-pro_2026-11-04_v7.json), 04.11.2026, Modell `google/gemini-2.5-pro` über OpenRouter, Notebook [citation_check_v7.ipynb](../notebooks/citation_check_v7.ipynb).
**Aufbau:** Dreizehn Berichte (Kennungen B1–B13) vollständig im Prompt, keine Suche, drei Durchläufe, bis zu fünf Anfragen parallel. Änderung gegenüber v6: Ausgabe als JSON; jeder Satz wird mit Berichtskennung und wörtlichem Zitat belegt; das Notebook prüft die Zitate und erzeugt die Quellenliste aus den Berichtsdaten. Die Antwortregeln sind inhaltlich gleich; in Regel 3 entfällt nur die Vorgabe, Titel und Datum in den Text zu schreiben.
**Maßstab:** Wie v6 ([test_questions.md](../data/synthetic_reports/test_questions.md)). Die Zuordnung einer Sichtweise oder eines Stands zu einem Bericht gilt als erfüllt, wenn der betreffende Satz mit dem passenden Bericht belegt ist (siehe Grenze zur Darstellung unten).

## Kennzahlen der Zitatprüfung (automatisch)

| Kennzahl | Wert |
|---|---|
| Antworten / nicht auswertbares JSON | 51 / 0 |
| Belege gesamt | 213 |
| davon gültig (Zitat steht wörtlich im genannten Bericht) | 213 (100 %) |
| Sätze ohne Beleg | 15, alle benennen eine Lücke (Fragen 5, 6, 10, 12, 13) |
| Zitatlänge | 6 bis 32 Wörter, Median 12 |
| Laufzeit gesamt | 188 s für 51 Anfragen |

## Ergebnis (inhaltlich)

**Nachtrag nach Nutzerentscheidung zu v8 (Variante B):** Das Weglassen des Stands von 2022 bei Frage 17 gilt nun als korrekt. Damit erfüllt auch D1 die Kriterien, insgesamt **44 von 51**. Die Tabelle unten zeigt die ursprüngliche Bewertung.

43 von 51 Antworten erfüllen die Kriterien, 8 teilweise. Fragen 1–13: 32 von 39 (v6: 32 von 39). Fragen 14–16: 9 von 9. Frage 17: 2 von 3.

| Frage | D1 | D2 | D3 | Anmerkung |
|---|---|---|---|---|
| 1–3 | erfüllt | erfüllt | erfüllt | Stabil. |
| 4 | teilweise | teilweise | teilweise | **In allen drei Durchläufen** ein zusätzlicher Satz, belegt mit dem Fahrzeugbericht B12 („Fahrzeugnutzung bei mehrtägigen Seminaren“): Die Fahrzeugregel wird auf das Gerät übertragen (D1: „beispielsweise von Fahrzeugen“). Das Zitat ist echt, der Bericht passt aber nicht; die Prüfung erkennt das nicht. |
| 5 | erfüllt | teilweise | erfüllt | D1 und D3 sagen ausdrücklich, dass die Berichte nicht sagen, wie eine Verantwortung festgestellt wird. D2 nur indirekt. D1 fügt einen unnötigen Satz zum Rückgabeverfahren hinzu (richtig belegt). |
| 6–8 | erfüllt | erfüllt | erfüllt | Stabil. Frage 7 sagt nicht ausdrücklich „Nein“, nennt aber nur die neue Regel. |
| 9 | teilweise | teilweise | teilweise | Verantwortung nur indirekt (Entscheidung C). |
| 10 | erfüllt | erfüllt | erfüllt | Kostenlücke benannt. |
| 11–13 | erfüllt | erfüllt | erfüllt | Sichtweisen satzweise mit dem passenden Bericht belegt, Überjacke als Vorschrift. Frage 12 D2 sagt nicht wörtlich, dass die Berichte auseinandergehen, stellt die Sichtweisen aber als Gegensatz dar. |
| 14 | erfüllt | erfüllt | erfüllt | Checkliste vollständig, diesmal auch „getrennte Felder“. Kein „vollgetankt“. |
| 15 | erfüllt | erfüllt | erfüllt | Alle sechs Checklistenpunkte; keine Doppelungen mehr wie in v6. |
| 16 | erfüllt | erfüllt | erfüllt | Material, Fahrzeuge, Kleidung getrennt; D1 ergänzt passend Tankstand und Schadensformular. |
| 17 | teilweise | erfüllt | erfüllt | Jeder Stand ist satzweise mit seinem Bericht belegt (in v6 fehlte diese Zuordnung). D1 lässt den Stand von 2022 aus. D3 nennt den Grund der jüngsten Änderung korrekt. Kein Durchlauf weist darauf hin, dass der Bericht von 2022 nicht ausdrücklich mehrtägige Seminare betrifft. |

## Beobachtungen

- **Zitate sind zuverlässig:** Alle 213 Zitate stehen wörtlich im genannten Bericht, und kein Antwort-JSON war fehlerhaft. Zitate mit sechs bis 32 Wörtern sind lang genug, um eine Stelle eindeutig zu finden.
- **Die Prüfung erkennt den häufigsten Fehler nicht:** Falsche Zusatzquellen bleiben (3 von 51, alle bei Frage 4, v6: 2 von 51). Das Modell zitiert dabei echte Stellen aus einem unpassenden Bericht. Das war als Grenze erwartet. Neu ist, dass der Fehler im Text sichtbar wird: Statt nur einer falschen Quelle am Ende steht ein eigener Satz mit Beleg, der zeigt, woher die Übertragung stammt. Für eine Sichtprüfung ist das leichter nachzuvollziehen.
- **Satzweise Belege lösen das Problem aus v6 bei Frage 17:** Weil jeder Satz einen Bericht nennt, ist jeder Stand einem Bericht und damit Titel und Datum zugeordnet.
- **Die Qualität sinkt durch das JSON-Format nicht erkennbar.** Fragen 1–13 liegen gleichauf mit v6. Bei drei Durchläufen ist ein kleiner Unterschied von Schwankung nicht zu trennen.

## Grenzen

- **Darstellung:** Die Funktion `render` im Notebook hängt die Quellen nur gesammelt ans Ende. In der angezeigten Antwort stehen deshalb bei Erfahrungen und beim Änderungsverlauf keine Titel und Daten je Sichtweise oder Stand („einem Bericht zufolge“). Die Zuordnung steckt nur in den Belegdaten. Das ist ein Mangel der Notebook-Fassung, nicht des Modells; eine Darstellung mit Quelle je Satz wäre nötig.
- Der Prompt verbietet Titel und Daten im Text. Deshalb ist v7 bei der Zuordnung nicht direkt mit v5/v6 vergleichbar, wo sie im Text stehen musste.
- Die Zitatprüfung zeigt nur, dass eine Stelle wörtlich vorkommt. Ob sie die Aussage des Satzes stützt, prüft sie nicht.
- Quellenabruf ist nicht getestet, weil das Modell alle Dokumente vollständig erhielt.
- Die Laufzeit gilt für den gesamten Testlauf mit parallelen Anfragen, nicht für die Wartezeit einer einzelnen Frage.
- Drei Durchläufe zeigen die Schwankung, sind aber zu wenige für belastbare Häufigkeiten.
- Die Bewertung stammt von einem anderen KI-Modell und ist keine unabhängige menschliche Prüfung.

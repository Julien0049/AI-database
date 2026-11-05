# Bewertung: Gemini 2.5 Pro, v11 (alle 48 Berichte) und v12 (Suche, 5 Treffer)

**Status:** Agentenbewertung (Claude), vom Nutzer noch zu prüfen.
**Läufe:** [v11](./ergebnisse_google_gemini-2.5-pro_2026-11-05_v11.json) und [v12](./ergebnisse_google_gemini-2.5-pro_2026-11-05_v12.json), 05.11.2026, Modell `google/gemini-2.5-pro` über OpenRouter, Notebook [citation_check_v7.ipynb](../notebooks/citation_check_v7.ipynb), je drei Durchläufe, 25 Fragen, 48 Berichte (`dataset-v3`).
**Aufbau:** Prompt wie v8–v10 (Regel 7). v11: alle 48 Berichte im Prompt (Vergleichsbasis). v12, einzige Änderung: je Frage nur die 5 Berichte, die der Frage nach Bedeutung am ähnlichsten sind (`intfloat/multilingual-e5-small`, wie Suchtest s1).
**Maßstab:** Kriterien in [test_questions.md](../data/synthetic_reports/test_questions.md). Neu ist die Stufe „nicht erfüllt“ für Antworten, die einen überholten Stand als aktuell ausgeben. Inhalte aus Störberichten in der Antwort zählen als „teilweise“, auch wenn sie richtig eingeordnet sind (Regel „exakt und schlank“).

## Kennzahlen

| Kennzahl | v11 (alle Berichte) | v12 (5 Treffer) |
|---|---|---|
| Erfüllt / teilweise / nicht erfüllt (von 75) | **64** / 11 / 0 | **51** / 21 / 3 |
| davon Fragen 1–17 (von 51) | 40 | 31 |
| Belege gültig | 298 von 298 | 247 von 247 |
| Nicht auswertbares JSON | 0 | 0 |
| Sätze / Wörter gesamt | 252 / 3434 | 231 / 3096 |
| Laufzeit gesamt (Wartezeit je Anfrage, abgeleitet*) | 277 s (ca. 18 s) | 269 s (ca. 18 s) |

Zum Vergleich v9 (15 Berichte, 17 Fragen): 198 s für 51 Anfragen (ca. 19 s je Anfrage).

\* Gesamtzeit × 5 parallele Anfragen ÷ Zahl der Anfragen. Korrigiert am 05.11.2026: Zuerst standen hier 3,6–3,9 s; das war der Durchsatz, nicht die Wartezeit einer Anfrage.

## Ergebnis je Frage

| Frage | v11 | v12 | Nötige Berichte unter den 5 Treffern? | Anmerkung |
|---|---|---|---|---|
| 1–2 | 3 / 3 | 3 / 3 | ja | Stabil. |
| 3 | 3 | 2 | ja | v12 D3 lässt die persönliche Ausgabeliste weg. |
| 4 | 2 | **0** | ja | Fahrzeugregel (B33) als Analogie übertragen: v11 einmal, v12 in allen drei Durchläufen („so bleibt beispielsweise ein Fahrzeug …“). |
| 5 | 0 | 1 | ja | Verantwortung meist nur indirekt („aus dem Fehlen allein …“); nur v12 D1 sagt ausdrücklich, dass die Berichte das nicht sagen. |
| 6 | 2 | **0** | ja | Störbericht Erste-Hilfe-Formular HV-7 in der Antwort: v11 einmal, v12 dreimal. Er wird jeweils richtig als Formular für Erste-Hilfe-Kästen eingeordnet, nicht als Kennziffer für den Adapter. |
| 7–8 | 3 / 3 | 3 / 3 | ja | Stabil. |
| 9 | 1 | 1 | ja | Verantwortung nur in je einem Durchlauf ausdrücklich als offen benannt. |
| 10–13 | je 3 | je 3 | ja | Stabil. |
| 14 | 3 | **0 (3 × nicht erfüllt)** | **nein**, Fahrtenbuch-Formular fehlt | **Überholter Stand als aktuell:** In allen drei Durchläufen steht „Das Fahrzeug muss vollgetankt zurückgegeben werden.“ Der neuere Bericht mit der geänderten Tankregel war nicht unter den Treffern. |
| 15 | 1 | 0 | **nein**, „Wartezeiten im Freien“ fehlt | v12: Die Sichtweise „Daunenjacke bei langen Wartezeiten unverzichtbar“ fehlt in allen Durchläufen. v11: zweimal zusätzlich der Störbericht Winterdienst (Haupteingang bei Glätte). |
| 16 | 1 | 0 | **nein**, alle drei Winterberichte fehlen | v12: Der Teil Winterkleidung fehlt ganz; dafür Feedbackbögen. v11: zweimal Winterdienst-Störbericht. |
| 17–21 | je 3 | je 3 | ja | Beamer (21): neuester Stand auch in v12 korrekt, obwohl die Treffer zwei ältere Stände vor ihm enthielten. |
| 22 | 3 | 2 | **nein**, „Vorbereitung eines Seminartags“ fehlt | v12 findet den Download über einen anderen Bericht, der ihn erwähnt (Verhandlungsführung 29.09.2026). D2 nennt zusätzlich den USB-Stick als gleichrangigen Weg. |
| 23–24 | 3 / 3 | 3 / 3 | ja | Keine Übertragung aus Winterberichten, keine Frist erfunden. |
| 25 | 3 | **0** | **nein**, alle vier fehlen | v12 fasst nur den Bericht über ein Seminar mit externen Gästen zusammen; Verlustmeldung, 24-Stunden-WLAN, Freigabe der Parkplätze ab 9 Uhr und Anmeldung der Gastreferierenden fehlen. Die Antwort wirkt vollständig; ein Hinweis auf mögliche Lücken fehlt. |

## Woher der Unterschied kommt (64 → 51)

| Ursache | Fragen | Differenz |
|---|---|---|
| Nötiger Bericht nicht unter den Treffern (Suche) | 14, 15, 16, 22, 25 | −9 |
| Nötige Berichte vorhanden, aber Störberichte unter den Treffern eingeflossen | 3, 4, 6 | −5 |
| Zufällige Schwankung | 5 | +1 |

## Beobachtungen

- **Die Suche verschlechtert Einzelfragen kaum, Zusammenfassungen stark.** Bei den Fragen, deren nötige Berichte unter den Treffern lagen, blieb das Ergebnis fast gleich. Alle fünf Fragen mit fehlenden Berichten wurden schlechter. Das bestätigt die Vorhersage aus dem Suchtest s1 (bei k = 5 fehlten genau diese Fragen).
- **Der befürchtete Fehler tritt ein:** Bei Frage 14 nennt das Modell eine überholte Regel (vollgetankt zurückgeben) als aktuell, und zwar in allen drei Durchläufen. Es konnte den Fehler nicht bemerken, weil ihm der neuere Bericht fehlte. Für Nutzer ist das nicht erkennbar: Die Antwort ist flüssig und hat eine gültige Fußnote.
- **Unvollständige Zusammenfassungen wirken vollständig (Frage 25, 16).** Das Modell fasst zusammen, was es bekommt, und weist nicht darauf hin, dass weitere Berichte existieren könnten.
- **Weniger Berichte, mehr Störeinflüsse (Vermutung).** Unter den 5 Treffern sind die übrigen Berichte gerade die ähnlich klingenden Störberichte. Das Modell nahm sie häufiger in die Antwort auf als bei allen 48 Berichten (Fragen 4 und 6: je 3 von 3 statt 1 von 3). Möglicherweise geht das Modell davon aus, dass alles Mitgelieferte relevant ist. Mit drei Durchläufen ist das ein Hinweis, kein Nachweis.
- **Mit allen 48 Berichten bleibt die Qualität hoch (v11).** Die dreifach größere Sammlung mit Störberichten hat die Antworten kaum verschlechtert; die Fragen 20–25 wurden alle erfüllt. Neu sind vereinzelte Störinhalte (Winterdienst in Fragen 15 und 16, HV-7 in Frage 6).
- **Die Suche macht hier nichts schneller.** Die Wartezeit je Anfrage ist mit 5 Berichten, 15 Berichten (v9) und 48 Berichten mit etwa 18–19 s praktisch gleich. Die Wartezeit hängt bei dieser Größe vom Nachdenken und Schreiben des Modells ab, nicht von der Menge des mitgeschickten Textes. Die Suche spart hier nur Eingabetext (Kosten); ihr eigentlicher Zweck bleibt die Skalierung auf Sammlungen, die nicht mehr in eine Anfrage passen.
- **Zitate weiterhin vollständig gültig**; die Regel gegen „ein Bericht“ im Text wirkt weiterhin nicht immer (v11 fünfmal, v12 einmal).

## Grenzen

- Ein Embedding-Modell, eine feste Trefferzahl (k = 5), drei Durchläufe; Unterschiede von einer oder zwei Antworten liegen in der beobachteten Schwankung.
- Die Bewertung „Störinhalt = teilweise“ ist eine Festlegung des Agenten; mit milderem Maßstab wären v11 und v12 bei den Fragen 4, 6, 15 und 16 besser.
- Laufzeit nur als Gesamtzeit mit fünf parallelen Anfragen gemessen; nicht je Einzelfrage und ohne Wiederholung.
- Die Bewertung stammt von einem anderen KI-Modell und ist keine unabhängige menschliche Prüfung.

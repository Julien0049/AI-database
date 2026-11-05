# Bewertung: Suchtest s5 (Rang aller nötigen Berichte)

**Status:** Agentenauswertung (Claude), vom Nutzer noch zu prüfen. Die Kennzahlen sind gemessen; die Deutung ist eine Einschätzung.
**Lauf:** [ergebnisse_suche_2026-11-05_s5.json](./ergebnisse_suche_2026-11-05_s5.json), 05.11.2026, Notebook [retrieval_test.ipynb](../notebooks/retrieval_test.ipynb). Kein Sprachmodell beteiligt.
**Aufbau:** Wie s1 (ganzer Bericht, BM25 und `intfloat/multilingual-e5-small`). Einzige Änderung: Ranglisten vollständig gespeichert, vollständig@k bis k = 30.
**Ziel:** Abschätzen, wie groß eine Vorauswahl für Zusammenfassungen sein müsste.

## Ergebnis

| Methode | @5 | @10 | @15 | @20 | @30 |
|---|---|---|---|---|---|
| Stichwortsuche (BM25) | 50 % | 58 % | 62 % | 71 % | 83 % |
| Suche nach Bedeutung | 79 % | 88 % | 88 % | 92 % | 96 % |

Schlechtester Rang eines nötigen Berichts (Suche nach Bedeutung, 48 Berichte):

| Frage | Ränge der nötigen Berichte | schlechtester Rang |
|---|---|---|
| 14 Zusammenfassung Fahrzeugausleihe | 1, 2, 3, 4, 6 | 6 |
| 15 Zusammenfassung Winter-Erfahrungen | 1, 2, 6 | 6 |
| 16 Zusammenfassung mehrtägige Seminare | 2, 3, 6, 11, 26 | 26 |
| 25 Zusammenfassung Gäste und Besucher | 23, 25, 41, 42 | **42** |
| 22 neuester Stand nur nebenbei (Einzelfrage) | 16 | 16 |
| alle übrigen Einzelfragen | – | höchstens 4 |

## Beobachtungen

- **Eine größere Vorauswahl hilft nur teilweise.** Mit 10 Treffern wären die Fragen 14 und 15 gelöst, mit 30 auch Frage 16. Für Frage 25 liegen die nötigen Berichte auf den Plätzen 23–42 von 48, also fast am Ende der Liste. Hier müsste die Vorauswahl praktisch die ganze Sammlung umfassen.
- **Die Suche nach Bedeutung versagt bei Frage 25 grundsätzlich, nicht knapp.** Kurze Berichte wie „WLAN-Zugang für Gäste“ oder „Besucherparkplätze“ gelten dem Modell als der Frage unähnlicher als lange Seminarberichte, in denen Gäste nebenbei vorkommen. Eine feste Grenze nach Rang oder Ähnlichkeit kann das nicht auffangen.
- **Die Stichwortsuche ist auch hier keine Alternative**, etwa Frage 14: schlechtester Rang 41.
- **Einzelfragen sind unkritisch:** Außer Frage 22 liegen alle nötigen Berichte unter den ersten 4.

## Folgerung für die Strategie (Vorschlag)

Für Zusammenfassungen reicht keine Vorauswahl über die Suche, wenn nichts verloren gehen darf. Das Modell muss die Berichte selbst auf Relevanz prüfen, und zwar alle, in Paketen.

## Grenzen

Eine Frage (25) bestimmt die Folgerung maßgeblich; 4 Zusammenfassungsfragen, 48 kurze Berichte, ein Embedding-Modell.

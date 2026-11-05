# Bewertung: Suchtest s1 (Stichwortsuche, Suche nach Bedeutung, Kombination)

**Status:** Agentenauswertung (Claude), vom Nutzer noch zu prüfen. Die Kennzahlen sind gemessen; die Deutung ist eine Einschätzung.
**Lauf:** [ergebnisse_suche_2026-11-05_s1.json](./ergebnisse_suche_2026-11-05_s1.json), 05.11.2026, Notebook [retrieval_test.ipynb](../notebooks/retrieval_test.ipynb). Kein Sprachmodell beteiligt.
**Aufbau:** 48 Berichte, 25 Fragen (`dataset-v3`). Einheit der Suche: ganzer Bericht. Stichwortsuche BM25 (eigene Umsetzung, ohne Grundformbildung), Suche nach Bedeutung mit `intfloat/multilingual-e5-small`, Kombination per Reciprocal Rank Fusion.
**Kennzahl:** vollständig@k = Anteil der 24 Fragen mit nötigen Berichten, bei denen *alle* nötigen Berichte unter den ersten k Treffern liegen (Frage 13 hat keine nötigen Berichte).

## Ergebnis

| Methode | vollständig@3 | vollständig@5 | vollständig@10 |
|---|---|---|---|
| Stichwortsuche (BM25) | 38 % | 50 % | 58 % |
| Suche nach Bedeutung | **71 %** | **79 %** | **88 %** |
| Kombination | 54 % | 67 % | 83 % |

Aufgeteilt nach Fragetyp (Suche nach Bedeutung):

| Fragetyp | vollständig@5 | vollständig@10 |
|---|---|---|
| Einzelfragen (20 Fragen) | 19 von 20 | 19 von 20 |
| Zusammenfassungen (Fragen 14, 15, 16, 25) | 0 von 4 | 2 von 4 |

## Beobachtungen

- **Suche nach Bedeutung ist klar besser.** Die Stichwortsuche scheitert an anderen Wortformen und zusammengesetzten Wörtern: „Fahrzeugausleihe“ (Frage 14) kommt in keinem Bericht vor, „reservieren“ trifft „reserviert“ nicht (Frage 10). Die Suche nach Bedeutung findet diese Berichte auf den vorderen Plätzen.
- **Die Kombination ist schlechter als die Suche nach Bedeutung allein.** Die schwache Stichwortsuche zieht gute Treffer nach hinten. In dieser einfachen Form lohnt sich die Kombination hier nicht.
- **Einzelfragen funktionieren gut:** 19 von 20 vollständig unter den ersten 5. Die Wortfallen (Sommer/Winter, Fahrradgarage/Raumschlüssel, Jacke/Garderobe) haben die Suche nach Bedeutung nicht in die Irre geführt.
- **Ältere Stände stehen oft vor dem neuesten.** Bei den Beamern (Frage 21) liegen zwei ältere Stände auf Platz 1 und 2, der neueste auf Platz 3. Das ist unkritisch, solange k groß genug ist; dann entscheidet das Modell über das Datum (in v10 zuverlässig).
- **Nebenbei erwähnter neuester Stand wird nicht gefunden (Frage 22).** Der Bericht „Vorbereitung eines Seminartags“ liegt bei keiner Methode unter den ersten 10; gedruckte Unterlagen und USB-Stick stehen vorn. Ein späterer Seminarbericht (29.09.2026), der den Download ebenfalls erwähnt, liegt aber auf Platz 5. Die richtige Antwort wäre also über diesen Bericht noch möglich; ob das Modell sie findet, muss der Antwortlauf zeigen. Das ist genau das Risiko „überholter Stand als aktuell“.
- **Zusammenfassungen über verstreute Berichte scheitern (Frage 25).** Bei „Gästen und Besuchern“ findet keine Methode einen der vier nötigen Berichte unter den ersten 10; stattdessen stehen lange Seminarberichte vorn, in denen Gäste vorkommen. Auch Frage 16 (mehrtägige Seminare, drei Themen) ist bei k = 10 unvollständig. Zusammenfassungen brauchen eine andere Strategie als „die besten k Treffer“.
- **Frage ohne Antwort (Frage 13):** Die Suche liefert die Winterberichte; ob das Modell daraus korrekt „keine Angaben“ ableitet, zeigt erst der Antwortlauf.

## Grenzen

- 24 Fragen, 48 kurze Berichte; ein einziges Embedding-Modell; keine Variation von Einstellungen (BM25-Parameter, Gewichtung der Kombination).
- Die nötigen Berichte je Frage wurden vom Agenten aus den geprüften Erwartungen abgeleitet; ergänzende Berichte zählen nicht mit (siehe Frage 22).
- Die Stichwortsuche ohne Grundformbildung ist bewusst einfach; eine bessere Wortaufbereitung würde sie verbessern.
- Die Suche ist deterministisch; ein Durchlauf genügt. Aussagen zur Antwortqualität erlaubt erst der Antwortlauf.

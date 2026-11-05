# Bewertung: Suchtest s4 (größeres Embedding-Modell)

**Status:** Agentenauswertung (Claude), vom Nutzer noch zu prüfen. Die Kennzahlen sind gemessen; die Deutung ist eine Einschätzung.
**Lauf:** [ergebnisse_suche_2026-11-05_s4.json](./ergebnisse_suche_2026-11-05_s4.json), 05.11.2026, Notebook [retrieval_test.ipynb](../notebooks/retrieval_test.ipynb). Kein Sprachmodell beteiligt.
**Änderung gegenüber s1:** Zusätzlich zum kleinen Modell `intfloat/multilingual-e5-small` (ca. 470 MB, 12 Schichten) das große Modell `intfloat/multilingual-e5-large` (ca. 2,2 GB, 24 Schichten). Einheit ganzer Bericht, keine Erweiterung.

## Ergebnis

| Methode | vollständig@3 | vollständig@5 | vollständig@10 |
|---|---|---|---|
| Stichwort | 38 % | 50 % | 58 % |
| Bedeutung, kleines Modell (wie s1) | 71 % | 79 % | **88 %** |
| Bedeutung, großes Modell | 71 % | 79 % | 83 % |

## Beobachtungen

- **Das große Modell ist nicht besser.** Gleiche Werte unter den ersten 3 und 5, unter den ersten 10 eine Frage weniger. Einzelne Ränge verschieben sich in beide Richtungen (besser: Fragen 5, 9, 15, 21; schlechter: Fragen 2, 14, 20).
- **Die schwierigen Fälle bleiben schwierig:**
  - Frage 22: Der nebenbei erwähnte Download-Stand liegt weiter nicht unter den ersten 10; vorn stehen wieder die älteren Stände (gedruckt, USB-Stick).
  - Frage 25: Nur einer der vier nötigen Berichte (Besucherausweise) erscheint, auf Platz 9.
  - Frage 16: weiterhin unvollständig.
- **Deutung:** Nach vier Varianten (s1–s4) liegt die Suche nach Bedeutung stabil bei etwa 79 % unter den ersten 5. Die Ausfälle betreffen immer dieselben Fragetypen: Zusammenfassungen über mehrere Berichte und nebenbei erwähnte neueste Stände. Das spricht dafür, dass die Grenze in der Art der Frage und in der Strategie „die besten k Treffer“ liegt, nicht in der Größe des Modells.
- **Praktisch:** Das kleine Modell ist fast fünfmal kleiner, schneller und für die spätere Offline-Ausbaustufe günstiger; es bleibt die Grundlage.

## Grenzen

- Nur zwei Modelle derselben Familie; andere Modelle könnten sich anders verhalten.
- 24 Fragen; Unterschiede von einer Frage sind nicht belastbar.

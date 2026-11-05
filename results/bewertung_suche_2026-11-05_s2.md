# Bewertung: Suchtest s2 (Abschnitte aus zwei Sätzen)

**Status:** Agentenauswertung (Claude), vom Nutzer noch zu prüfen. Die Kennzahlen sind gemessen; die Deutung ist eine Einschätzung.
**Lauf:** [ergebnisse_suche_2026-11-05_s2.json](./ergebnisse_suche_2026-11-05_s2.json), 05.11.2026, Notebook [retrieval_test.ipynb](../notebooks/retrieval_test.ipynb). Kein Sprachmodell beteiligt.
**Änderung gegenüber s1:** Zusätzlich zur Suche nach ganzen Berichten wird nach Abschnitten aus je zwei aufeinanderfolgenden Sätzen gesucht (89 Abschnitte aus 48 Berichten); ein Bericht erhält den Wert seines besten Abschnitts. Geplant war eine Suche nach Absätzen, aber die meisten Berichte bestehen nur aus einem Absatz. Die Kombination beider Methoden wurde entfernt (in s1 schlechter).

## Ergebnis

| Methode | vollständig@3 | vollständig@5 | vollständig@10 |
|---|---|---|---|
| Stichwort / Bericht (wie s1) | 38 % | 50 % | 58 % |
| Stichwort / Abschnitt | 38 % | 50 % | 62 % |
| Bedeutung / Bericht (wie s1) | 71 % | 79 % | **88 %** |
| Bedeutung / Abschnitt | **75 %** | **83 %** | 83 % |

Ein Prozentpunkt-Schritt von rund 4 % entspricht einer einzigen der 24 Fragen.

## Beobachtungen

- **Kein klarer Gewinn.** Bei der Suche nach Bedeutung kommt unter den ersten 5 eine Frage dazu (Frage 15: Bericht zu Wartezeiten von Platz 6 auf 3), unter den ersten 10 fällt eine weg (Frage 14: Fahrtenbuch-Bericht von Platz 6 auf über 10). Die Stichwortsuche bleibt praktisch gleich, weil ihr Problem Wortformen sind, nicht die Länge der Einheiten.
- **Die beiden Hauptprobleme bleiben ungelöst:**
  - Frage 22: Der nebenbei erwähnte Download-Stand liegt weiterhin bei keiner Methode unter den ersten 10, obwohl der Satz jetzt in einem eigenen kleinen Abschnitt steht. Vorn stehen die älteren Stände (gedruckt auf Platz 1, USB-Stick auf Platz 5); der spätere Bericht, der den Download bestätigt, steht auf Platz 2.
  - Frage 25: Keiner der vier nötigen Berichte zu Gästen und Besuchern liegt unter den ersten 10; vorn stehen lange Seminarberichte.
- **Deutung:** Die Länge der Sucheinheit ist hier nicht die Ursache. Wahrscheinlicher ist, dass das kleine Embedding-Modell die Bedeutung nicht gut genug erfasst (z. B. „Seminarunterlagen erhalten“ ↔ „Teilnehmerunterlagen als Download bereitstellen“, „Gäste und Besucher“ ↔ „Besucherausweise“) und dass Zusammenfassungen grundsätzlich mehr als die besten k Treffer brauchen.
- **Empfehlung für das weitere Vorgehen:** Bei gleichem Ergebnis die einfachere Variante (ganzer Bericht) als Grundlage behalten.

## Grenzen

- Nur eine Abschnittsgröße (zwei Sätze) getestet; die Satztrennung ist eine einfache Regel.
- Unterschiede von einer Frage liegen im Bereich zufälliger Effekte der Rangfolge und sind nicht belastbar.
- Ein einziges, kleines Embedding-Modell.

# Bewertung: Suchtest s3 (Thema erweitern)

**Status:** Agentenauswertung (Claude), vom Nutzer noch zu prüfen. Die Kennzahlen sind gemessen; die Deutung ist eine Einschätzung.
**Lauf:** [ergebnisse_suche_2026-11-05_s3.json](./ergebnisse_suche_2026-11-05_s3.json), 05.11.2026, Notebook [retrieval_test.ipynb](../notebooks/retrieval_test.ipynb). Kein Sprachmodell beteiligt.
**Änderung gegenüber s1:** Einheit ganzer Bericht (Abschnitte aus s2 entfernt). Zu jedem der drei besten Treffer der Suche nach Bedeutung werden seine 1 bzw. 2 ähnlichsten Berichte direkt dahinter eingereiht; danach folgt die ursprüngliche Rangliste. Die Zahl der Berichte für das Modell bleibt gleich.

## Ergebnis

| Methode | vollständig@3 | vollständig@5 | vollständig@10 |
|---|---|---|---|
| Stichwort | 38 % | 50 % | 58 % |
| Bedeutung (wie s1) | **71 %** | **79 %** | **88 %** |
| Bedeutung + Thema (1 Nachbar) | 62 % | 79 % | 88 % |
| Bedeutung + Thema (2 Nachbarn) | 46 % | 71 % | 88 % |

## Beobachtungen

- **Die Themenerweiterung bringt nichts und schadet bei kleinem k.** Nachbarn der ersten Treffer verdrängen nötige Berichte, die vorher auf Platz 3–5 lagen (z. B. Frage 4: von Platz 2 auf 4; Frage 5: von 3 auf 6).
- **Die Zielfälle werden nicht erreicht:**
  - Frage 22: Die Nachbarn des besten Treffers (gedruckte Unterlagen) sind der USB-Bericht und andere kurze Verwaltungsberichte, nicht der lange Seminarbericht, in dem der Download nebenbei steht.
  - Frage 25: Die Nachbarn der besten Treffer (lange Seminarberichte) sind weitere lange Seminarberichte, nicht die kurzen Berichte zu Besucherausweisen, WLAN und Parkplätzen.
  - Frage 16: unverändert unvollständig.
- **Deutung:** Ähnlichkeit zwischen ganzen Berichten erfasst den Gesamteindruck eines Berichts (lang/kurz, Seminarbericht/Verwaltungsregel), nicht einzelne Aussagen darin. Für nebenbei erwähnte oder verstreute Inhalte ist sie deshalb ungeeignet.

## Grenzen

- Nur zwei Einstellungen (1 und 2 Nachbarn, drei Ausgangstreffer) getestet; die Auswahl anhand derselben 24 Fragen passt die Einstellung an genau diese Fragen an.
- Ein einziges, kleines Embedding-Modell; Ähnlichkeit zwischen Berichten mit demselben Modell berechnet.

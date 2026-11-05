# Bewertung: Gemini 2.5 Pro, v13 (Sichtung aller Berichte in Paketen)

**Status:** Agentenbewertung (Claude), vom Nutzer noch zu prüfen.
**Lauf:** [ergebnisse_google_gemini-2.5-pro_2026-11-05_v13.json](./ergebnisse_google_gemini-2.5-pro_2026-11-05_v13.json), 05.11.2026, neuer Schlüssel, Notebook [citation_check_v7.ipynb](../notebooks/citation_check_v7.ipynb), drei Durchläufe, 25 Fragen, 48 Berichte. Der abgebrochene erste Versuch ist in [bewertung_…_v13_abgebrochen.md](./bewertung_google_gemini-2.5-pro_2026-11-05_v13_abgebrochen.md) beschrieben.
**Aufbau:** Einzige Änderung gegenüber v12: statt der Suche sichtet das Modell alle Berichte in 5 Paketen zu je höchstens 10 und gibt die relevanten Kennungen zurück (Prompt `SICHTUNG`); nur diese gehen in den Antwortschritt (Regeln und Zitatprüfung unverändert). Die Fragen werden einzeln nacheinander bearbeitet, je zwei gleichzeitig.
**Maßstab:** wie v11/v12 (Störinhalte = teilweise, überholter Stand als aktuell oder erfundene Regel = nicht erfüllt).

## Kennzahlen

| Kennzahl | v11 (alle Berichte) | v12 (5 Treffer) | v13 (Sichtung) |
|---|---|---|---|
| Erfüllt / teilweise / nicht erfüllt (von 75) | **64** / 11 / 0 | 51 / 21 / 3 | **57** / 16 / 2 |
| Nötige Berichte im Antwortschritt vorhanden | 100 % | 102 von 132 | **129 von 132** |
| Berichte im Antwortschritt je Frage | 48 | 5 | 6,2 im Mittel (0–20) |
| Belege gültig | 298 / 298 | 247 / 247 | 313 / 314 (1 erfunden) |
| Wartezeit je Frage (v11/v12 abgeleitet) | ca. 18 s | ca. 18 s | **35 s** im Mittel (17–86 s) |
| Kosten des Laufs | nicht erfasst | nicht erfasst | **7,36 USD** (ca. 10 Cent je Frage) |

## Ergebnis je Frage

| Frage | v11 | v12 | v13 | Anmerkung zu v13 |
|---|---|---|---|---|
| 1–3 | 9 | 8 | 9 | Stabil. |
| 4 | 2 | 0 | **0** | Fahrzeugbericht (B33) in jeder Sichtung ausgewählt und in allen Antworten als Analogie übertragen. |
| 5 | 0 | 1 | 0 | Verantwortung nur indirekt; D1 hängt zusätzlich das Rückgabeverfahren an. |
| 6 | 2 | 0 | **2** | Erste-Hilfe-Formular HV-7 zwar ausgewählt, aber nicht in die Antwort übernommen. D3 lässt Entdeckungsdatum und Kennziffer-Teil weg. |
| 7–8 | 6 | 6 | 6 | Stabil. |
| 9 | 1 | 1 | 1 | Wie bisher. |
| 10–13 | 12 | 12 | 12 | Stabil. |
| 14 | 3 | **0** | **2** | Alle fünf Fahrzeugberichte gefunden, Tankregel aktuell. D1 enthält einen Satz über Besucherparkplätze (Störinhalt). |
| 15 | 1 | 0 | 0 | Inhaltlich vollständig (auch „Daunenjacke bei Wartezeiten“), aber in allen drei Durchläufen der Winterdienst-Bericht (Haupteingang bei Glätte). |
| 16 | 1 | 0 | 2 | Material, Fahrzeuge und Kleidung vollständig. **D1 nennt die überholte USB-Stick-Regel als aktuell** (nicht erfüllt): Die Sichtung wählte den USB-Bericht, nicht den neueren Download-Bericht. |
| 17–21 | 15 | 15 | 15 | Stabil. |
| 22 | 3 | 2 | **3** | Neuester Stand (Download) in allen Durchläufen gefunden. |
| 23 | 3 | 3 | 3 | Stabil. |
| 24 | 3 | 3 | 2 | **D3: Sichtung wählte keinen Bericht; das Modell erfand daraufhin eine Frist („fünf Werktage“) mit erfundenem Zitat** (nicht erfüllt; von der Zitatprüfung als „nicht gefunden“ erkannt). D1/D2 benennen die Lücke korrekt. |
| 25 | 3 | **0** | 0 | Alle vier Punkte der Checkliste in allen Durchläufen (v12: keiner). Zusätzlich jeweils Winterdienst, Garderobe und Fundsache (Störinhalte). |

Mit milderem Maßstab (Störinhalte nicht abgezogen) ergäbe sich: v11 68, v13 64, v12 weiterhin deutlich darunter.

## Beobachtungen

- **Das Auffindeproblem ist gelöst.** Die nötigen Berichte waren in 129 von 132 Fällen im Antwortschritt, auch bei den Zusammenfassungen und beim nur nebenbei erwähnten neuesten Stand. Die drei Ausfälle betreffen alle Frage 24 (ein Bericht ohne Antwort auf die Frage).
- **Was ausgewählt wird, wird auch verwendet.** Die Sichtung wählt großzügig, und das Modell baut fast alles Mitgelieferte in die Antwort ein: Winterdienst in sechs Zusammenfassungen, Fahrzeug-Analogie bei Frage 4, USB-Stick bei Frage 16. Dasselbe Muster zeigte v12 mit den Störberichten unter den Treffern. **Die Qualität der Antwort hängt damit stark davon ab, was in den Antwortschritt gelangt.**
- **Teilauswahl von Ständen ist gefährlich.** Wählt die Sichtung einen älteren Stand aus, aber nicht den neueren (Frage 16: USB-Stick statt Download), gibt das Modell den älteren als aktuell aus.
- **Leere Auswahl führt zu Erfindung.** Ohne einen einzigen Bericht hielt sich das Modell nicht an die Regel, Lücken zu benennen, sondern erfand eine Regel samt Zitat. Das Programm sollte das Modell in diesem Fall gar nicht fragen, sondern direkt melden, dass keine passenden Berichte gefunden wurden. Die Zitatprüfung hat die Erfindung erkannt; in der Oberfläche würde sie als „nicht bestätigter Beleg“ angezeigt, der Satz selbst aber trotzdem.
- **Gründlichkeit kostet.** Im Mittel 35 s je Frage (bei zwei gleichzeitig bearbeiteten Fragen), Zusammenfassungen 42 s; rund 10 Cent je Frage.
- **Bei 48 Berichten bleibt „alle Berichte im Prompt“ (v11) am besten**, schneller und vermutlich günstiger. Die Sichtung ist der bessere Weg als die Suche, wenn die Sammlung zu groß für eine Anfrage ist; sie braucht dann eine strengere Auswahl, einen Schutz gegen leere Auswahl und eine Regel, die zu jedem ausgewählten Stand auch die neueren Stände desselben Themas mitnimmt.

## Grenzen

- Ein Sichtungs-Prompt, eine Paketgröße; die Sichtung schwankt zwischen Durchläufen (Frage 23: 13, 2 und 1 Bericht).
- Kosten für v11/v12 nicht erfasst, daher kein direkter Kostenvergleich.
- Wartezeit mit zwei gleichzeitig bearbeiteten Fragen gemessen; eine einzelne Frage allein wäre etwas schneller.
- Die Bewertung stammt von einem anderen KI-Modell und ist keine unabhängige menschliche Prüfung.

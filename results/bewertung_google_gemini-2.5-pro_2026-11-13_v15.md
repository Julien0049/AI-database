# Bewertung: Gemini 2.5 Pro, v15 (Antworten aus der Aussagen-Datenbank)

**Status:** Agentenbewertung (Claude), vom Nutzer noch zu prüfen. Grenzfälle sind unten markiert.
**Lauf:** [ergebnisse_google_gemini-2.5-pro_2026-11-13_v15.json](./ergebnisse_google_gemini-2.5-pro_2026-11-13_v15.json), 13.11.2026, Skript `scripts/antwortlauf_aussagen.py`, drei Durchläufe, 25 Fragen, 48 Berichte (160 Aussagen aus v14). Kostenprobe vorab: `…_v15_test.json` (Probelauf, am 15.11.2026 entfernt, in der Git-Historie) (Fragen 22, 25; 0,048 USD).
**Aufbau:** Einzige Änderung gegenüber v11–v13: Das Modell bekommt statt ganzer Berichte die 40 besten Aussagen der Suche nach Bedeutung (e5-small), nach Bericht gruppiert, mit Titel und Datum (vom Programm), Art, Kontext und Originalstelle. Antwort-Prompt, Modell und Fußnoten unverändert. Zitatprüfung seit v15 mit erlaubten Auslassungen („...“).
**Maßstab:** wie v11–v13 (Störinhalte = teilweise, überholter Stand als aktuell = nicht erfüllt).

## Kennzahlen

| Kennzahl | v11 (alle Berichte) | v12 (5 Treffer) | v13 (Sichtung) | v15 (40 Aussagen) |
|---|---|---|---|---|
| Erfüllt / teilweise / nicht erfüllt (von 75) | **64** / 11 / 0 | 51 / 21 / 3 | 57 / 16 / 2 | 50 / 25 / **0** |
| Berichte im Antwortschritt je Frage | 48 | 5 | 6,2 | 19,7 (13–25), aber nur deren passendste Aussagen |
| Belege nicht bestätigt | 0 | 0 | 1 (erfunden) | 3 (umformuliert statt wörtlich, keine erfundenen Inhalte) |
| Kosten des Laufs | nicht erfasst | nicht erfasst | 7,36 USD | **2,18 USD** (ca. 3 Cent je Frage) |
| Wartezeit je Frage | ca. 18 s | ca. 18 s | 35 s | ca. 15–20 s (Einzelwerte 10–23 s) |

Dazu einmalig das Einlesen: 1,01 USD für 48 Berichte (v14).

## Ergebnis je Frage

| Frage | v11 | v15 | Anmerkung zu v15 |
|---|---|---|---|
| 1 | 3 | 1 | D1/D2 mischen einen Teil des überholten Verfahrens (02.03.2024: „Gruppenvertretung prüft“) in den aktuellen Stand. Grenzfall: nicht als Alternative, sondern als zusätzlicher Schritt. |
| 2 | 3 | **0** | Wie Frage 1, in allen Durchläufen; D2/D3 zusätzlich „gemeinsame Rückgabeliste“ (alter Stand). Adapter-Meldung jeweils korrekt. |
| 3 | 3 | 3 | |
| 4 | 2 | 2 | D3 hängt die Verfahren für Sets und eintägige Seminare an (Störinhalt). Keine Fahrzeug-Analogie mehr. |
| 5 | 0 | 1 | D3 sagt ausdrücklich, dass die Berichte keine verantwortliche Person nennen; D1 hängt das Rückgabeverfahren an. |
| 6 | 2 | **0** | Erste-Hilfe-Formular HV-7 in allen Durchläufen (richtig eingeordnet, aber Störinhalt). |
| 7–8 | 6 | 6 | |
| 9 | 1 | 0 | Verantwortung nur indirekt („aus dem Schaden allein …“), wie meist in v11. |
| 10–13 | 12 | 12 | |
| 14 | 3 | 2 | Tankregel aktuell in allen Durchläufen. D2 mit Besucherparkplätzen (Störinhalt). |
| 15 | 1 | 1 | D1/D3 ohne die vorgeschriebene Überjacke. |
| 16 | 1 | 0 | Fahrzeuge nur „werden gemeinsam genutzt“, die Zuordnung zur ausleihenden Person fehlt; D1/D2 mit altem Material-Teilschritt. Kein überholter Stand als alleiniger Stand. |
| 17 | 3 | 3 | |
| 18 | 3 | 3 | |
| 19 | 3 | 1 | D1/D2: älterer Stand korrekt, aber das Zitat ist die umformulierte Aussage statt der Originalstelle, daher ohne Fußnote. |
| 20–24 | 15 | 15 | Frage 22: Download in allen Durchläufen, ohne USB oder Druck. |
| 25 | 3 | 0 | Ausweise, WLAN, Gastreferierende, Parkplätze teilweise; Verlustmeldung, 24-Stunden-WLAN und Freigabe ab 9 Uhr fehlen (Berichte nicht gefunden, siehe v14b). D1 mit Fundsachen. |

## Beobachtungen

- **Kein überholter Stand als alleiniger aktueller Stand** (0 nicht erfüllt, v12: 3, v13: 2). Fragen 7, 14, 18, 21, 22 nennen in allen Durchläufen den neuesten Stand.
- **Neue Fehlerart: Teilschritte alter Verfahren werden beigemischt** (Fragen 1, 2, 16). Mit ganzen Berichten sah das Modell den alten Bericht als Ganzes und erkannte ihn als überholt; als einzelne Aussage („Gruppenvertretung prüft das Set“) wirkt der alte Teilschritt wie eine Ergänzung. Datum und Art standen dabei.
- **40 Aussagen sind für gezielte Fragen zu viel:** Entfernt passende Aussagen (HV-7, Parkplätze, Fundsachen, andere Rückgabeverfahren) landen als Störinhalt in der Antwort. Gleiches Muster wie v12/v13: Was mitgeliefert wird, wird verwendet.
- **Zusammenfassungen über viele Themen bleiben die Grenze** (Frage 25), weil die Suche die Berichte nicht findet.
- **Kosten und Zeit sinken deutlich**: rund 3 Cent je Frage statt 10 (v13), ohne dass die Kosten mit der Sammlung wachsen (Suche lokal, Einlesen einmalig).

## Folgerungen (Vorschlag)

1. Bei 48 sehr kurzen Berichten ist „alle Berichte im Prompt“ (v11) weiterhin am besten. Der Aussagen-Ansatz zielt auf große Sammlungen und lange Berichte; das zeigt dieser Datensatz nicht.
2. Weniger Aussagen für gezielte Fragen (z. B. 15–20) dürften Störinhalte senken, aber Zusammenfassungen verschlechtern.
3. Gegen beigemischte alte Teilschritte: zu jeder ausgewählten Aussage den **ganzen Bericht** statt nur der Aussage mitschicken, solange die Gesamtmenge passt („Aussagen zum Finden, Berichte zum Antworten“), oder ältere Stände desselben Themas ausdrücklich als „älterer Stand“ kennzeichnen.
4. Zitat im Antwortschritt: Das Modell soll die Originalstelle kopieren, nicht die Aussage (Hinweis im Format).

## Grenzen

48 kurze synthetische Berichte; ein Lauf mit drei Durchläufen; N = 40 nicht variiert; Bewertung durch ein anderes KI-Modell, Grenzfälle (Fragen 1, 2, 16) vom Nutzer zu prüfen.

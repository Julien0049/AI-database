# Bewertung: Gemini 2.5 Pro, v16 (Aussagen zum Finden, Berichte zum Antworten)

**Status:** Agentenbewertung (Claude), vom Nutzer noch zu prüfen.
**Lauf:** [ergebnisse_google_gemini-2.5-pro_2026-11-13_v16.json](./ergebnisse_google_gemini-2.5-pro_2026-11-13_v16.json), 13.11.2026, `scripts/antwortlauf_aussagen.py --volltext`, drei Durchläufe, 25 Fragen, 48 Berichte. Kostenprobe: `…_v16_test.json` (Fragen 1, 25; 0,054 USD).
**Aufbau:** Einzige Änderung gegenüber v15: Die 40 besten Aussagen (e5-small) bestimmen nur, welche Berichte relevant sind; das Modell bekommt diese Berichte vollständig (im Mittel 19,7 von 48). Prompt, Modell, Zitatprüfung, Fußnoten unverändert.
**Maßstab:** wie v11–v15 (Störinhalte = teilweise, überholter Stand als aktuell = nicht erfüllt).

## Kennzahlen

| Kennzahl | v11 (alle 48) | v12 (5 Treffer) | v13 (Sichtung) | v15 (40 Aussagen) | **v16 (Berichte der 40 Aussagen)** |
|---|---|---|---|---|---|
| Erfüllt / teilweise / nicht erfüllt (von 75) | **64** / 11 / 0 | 51 / 21 / 3 | 57 / 16 / 2 | 50 / 25 / 0 | **58** / 17 / **0** |
| Berichte im Antwortschritt | 48 | 5 | 6,2 | 19,7 (nur Aussagen) | 19,7 (vollständig) |
| Belege nicht bestätigt | 0 | 0 | 1 | 3 | **0** |
| Kosten | – | – | 7,36 USD | 2,18 USD | **1,78 USD** (ca. 2,4 Cent je Frage) |

## Ergebnis je Frage (Abweichungen von v11 fett)

| Frage | v11 | v15 | v16 | Anmerkung zu v16 |
|---|---|---|---|---|
| 1–2 | 6 | 1 | 6 | Keine alten Teilschritte mehr beigemischt (v15-Fehler behoben). |
| 3 | 3 | 3 | 3 | |
| 4 | 2 | 2 | 2 | D3 hängt die Regel für eintägige Seminare an. |
| 5 | 0 | 1 | 0 | Verantwortung nur indirekt; D3 zusätzlich Rückgabeverfahren. |
| 6 | 2 | 0 | 2 | D1 mit Erste-Hilfe-Formular HV-7. |
| 7–8 | 6 | 6 | 6 | |
| 9 | 1 | 0 | **0** | Verantwortung nur indirekt („aus dem Schaden allein …“). |
| 10–13 | 12 | 12 | 12 | |
| 14 | 3 | 2 | **0** | Inhaltlich vollständig, Tankregel aktuell; aber in allen Durchläufen Besucherparkplätze (Störinhalt aus zwei Seminarberichten). |
| 15 | 1 | 1 | **0** | Inhaltlich vollständig; in allen Durchläufen Winterdienst (Haupteingang bei Glätte) – derselbe Störbericht wie in v11/v13. |
| 16 | 1 | 0 | **3** | Material aktuell, Fahrzeugzuordnung, Kleidung mit abweichenden Sichtweisen und Vorgabe – in allen Durchläufen vollständig. |
| 17–24 | 24 | 22 | 24 | Frage 17 nennt teils auch den Stand 2022, ohne ihn als mehrtägig auszugeben; Frage 19 mit beiden Ständen und Fußnoten. |
| 25 | 3 | 0 | **0** | Ausweise, WLAN, Gastreferierende, Parkplatzreservierung; es fehlen Verlustmeldung, 24-Stunden-WLAN, Freigabe ab 9 Uhr (drei Berichte nicht gefunden, siehe v14b). |

## Beobachtungen

- **Fast auf dem Niveau von „alle Berichte“** (58 statt 64), mit 20 statt 48 Berichten und rund 2,4 Cent je Frage. Die Verluste gegenüber v11 stammen aus zwei Quellen: Störberichte, die mitgeliefert und verwendet werden (Fragen 14, 15; −4), und die nicht gefundenen Gäste-Berichte (Frage 25; −3). Frage 16 ist dafür besser als in allen bisherigen Läufen (+2).
- **Der v15-Fehler ist weg:** Mit den ganzen Berichten mischt das Modell keine Teilschritte alter Verfahren mehr bei (Fragen 1, 2, 16).
- **Kein überholter Stand als aktuell** und keine erfundenen Belege; alle Zitate bestätigt.
- **Was mitgeliefert wird, wird verwendet** (wie v12/v13): Störinhalte bleiben die Hauptfehlerquelle bei Zusammenfassungen.

## Folgerung (Vorschlag)

„Aussagen zum Finden, Berichte zum Antworten“ ist der bisher beste Aufbau, der nicht alle Berichte mitschicken muss. Bei echten, langen Berichten müsste die Zahl der mitgeschickten Berichte begrenzt oder statt ganzer Berichte die Umgebung der gefundenen Aussagen (Absatz) geschickt werden; das ist mit diesem Datensatz nicht prüfbar und gehört zum Test mit langen Berichten (`dataset-v4`).

## Grenzen

48 kurze synthetische Berichte (bei dieser Größe passt die Hälfte der Sammlung in jede Anfrage); N = 40 nicht variiert; ein Lauf mit drei Durchläufen; Bewertung durch ein anderes KI-Modell.

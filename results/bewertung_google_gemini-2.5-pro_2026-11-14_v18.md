# Bewertung: Gemini 2.5 Pro, v18 (Regel 8: anderen Kontext kennzeichnen)

**Status:** Agentenbewertung (Claude), vom Nutzer noch zu prüfen.
**Lauf:** [ergebnisse_google_gemini-2.5-pro_2026-11-14_v18.json](./ergebnisse_google_gemini-2.5-pro_2026-11-14_v18.json), 14.11.2026, drei Durchläufe, 34 Fragen, 58 Berichte (`dataset-v4`, mit präzisiertem Lehrsaaltechnik-Bericht, nachträglich neu eingelesen: 0,05 USD).
**Aufbau:** wie v17; einzige Änderung am Modell: Antwortregel 8 in `app/prompt_antwort.txt` („Aussagen aus Berichten mit anderem Kontext nur, wenn sie zur Frage beitragen, und dann mit ausdrücklicher Nennung des Kontexts“). Zusätzlich geändert: Frage 21b wegen des angepassten Berichts (Testfehler v17).
**Maßstab:** wie v17; seit 14.11.2026 ausdrücklich (Nutzer): Inhalte aus anderem Kontext ohne Kennzeichnung = Fehler (teilweise). Gekennzeichnete, zur Frage beitragende Übertragungen sind zulässig; gekennzeichnete, aber nicht zur Frage gehörende Inhalte bleiben Störinhalte.

## Kennzahlen

| Kennzahl | v17 | v18 |
|---|---|---|
| Fragen 1–25 erfüllt (von 75) | 48 | **56** |
| Fragen 26–34 erfüllt (von 27) | 26 | **27** |
| Gesamt erfüllt / teilweise / nicht erfüllt (von 102) | 74 / 25 / 3 | **83** / 17 / 2 |
| Kosten | 2,86 USD | 3,11 USD (ca. 3 Cent je Frage) |

## Wirkung von Regel 8

| Frage | v17 | v18 | Anmerkung |
|---|---|---|---|
| 11 Winterkleidung Seminar | 0 | 2 | Biwak-Erfahrungen jetzt gekennzeichnet („Bei militärischen Ausbildungen im Winter …“); D2 schreibt einen Satz aus dem Biwak-Bericht noch ungekennzeichnet dem Seminarbericht zu. |
| 12 Daunenjacke Seminar | 0 | **3** | Alle Übertragungen gekennzeichnet („Bei einer Übung im Winterbiwak …“, „Bei einem Lehrgang auf einem Truppenübungsplatz …“). |
| 14 Zusammenfassung Fahrzeuge | 2 | **3** | Übungsregeln durchgehend als „im Rahmen einer Übung“ markiert. |
| 31 Kälte Gelände/Biwak | 2 | **3** | Seminar-Vorschrift (Überjacke) jetzt mit Kontext. |
| 15 Zusammenfassung Winterseminare | 0 | 0 | Biwak-Inhalte gekennzeichnet, aber weiterhin Winterdienst-Störbericht in allen Durchläufen. |
| 7, 8, 28 | 9 | 9 | Neue gekennzeichnete Zusätze (Übungsregel beim Volltanken, Kraftfahrer bei Übung, Schlüssel auf dem Truppenübungsplatz) – passend und markiert, daher erfüllt. Nebenwirkung: Antworten werden etwas länger. |

## Weitere Abweichungen

| Frage | v17 | v18 | Anmerkung |
|---|---|---|---|
| 5 | 0 | 1 | D1 sagt erstmals ausdrücklich, dass die Berichte keine Verantwortlichen nennen. |
| 6 | 1 | 1 | Mängelmeldung (Erste Hilfe) als Störinhalt in D1/D3. |
| 10b | 3 | 2 | **D1 nicht erfüllt:** hängt „Das Fahrzeug wird vollgetankt zurückgegeben“ (überholter Stand 2023) an. Einzelfall, in v17 nicht aufgetreten. |
| 21b (Bericht präzisiert) | 0 | 2 | D2/D3 nennen nur den neuen Weg (IT-Ticket). **D1 nicht erfüllt:** nennt weiterhin Raumkalender und Seminarbüro als Hauptweg und das Ticket als Sonderfall „für den Lehrgangsbetrieb“. |
| 26–34 | 26 | 27 | Alle erfüllt. |

## Beobachtungen

- **Regel 8 wirkt:** Die Kontextvermischung bei Erfahrungsfragen ist weitgehend verschwunden (Fragen 11, 12, 14, 31: 4 → 11 Punkte). Das Modell kennzeichnet Übertragungen jetzt meist ausdrücklich im Satz.
- **Nebenwirkung:** Das Modell nimmt häufiger gekennzeichnete Zusatzinformationen aus anderen Kontexten auf. Das ist nach dem Maßstab zulässig, macht Antworten aber länger.
- **Überholte Stände bleiben ein Restrisiko:** In 2 von 102 Antworten erschien ein älterer Stand als aktuell (10b D1, 21b D1), obwohl der neue Stand jeweils mitgeliefert war. Beide Fehler traten nur in einem von drei Durchläufen auf.
- **Unverändert:** Verantwortung (5, 9) meist nur indirekt; Gäste-Zusammenfassung (25) unvollständig; Winterdienst als Störbericht (15).

## Grenzen

Ein Lauf mit drei Durchläufen; Regel 8 und präzisierter Bericht gleichzeitig geändert (21b daher nicht allein der Regel zuzuschreiben); Bewertung durch ein anderes KI-Modell, Grenzfälle (11 D2, 7/8/28 Zusätze) vom Nutzer zu prüfen.

# Bewertung: Gemini 2.5 Pro, v19 (Regel 8 verschärft: nur der gefragte Kontext)

**Status:** Agentenbewertung (Claude), vom Nutzer noch zu prüfen.
**Lauf:** [ergebnisse_google_gemini-2.5-pro_2026-11-14_v19.json](./ergebnisse_google_gemini-2.5-pro_2026-11-14_v19.json), 14.11.2026, drei Durchläufe, 34 Fragen, 58 Berichte (`dataset-v4`). Ein erster Startversuch hing über drei Stunden an offenen Verbindungen und wurde abgebrochen; dabei ggf. angefallene Kosten sind nicht bekannt (höchstens ein Lauf, ca. 3 USD). Seitdem: Zeitgrenze je Anfrage (180 s, zwei Wiederholungen) und Zwischenspeicher je Antwort (`…_v19.teil.jsonl`).
**Aufbau:** wie v18; einzige Änderung: Regel 8 verschärft (Nutzerentscheidung): nur der gefragte Kontext; Aussagen aus anderem Kontext entfallen, außer in zwei Fällen ein gekennzeichneter Satz: (a) die Frage lässt den Kontext offen und die Berichte unterscheiden sich, (b) zum gefragten Kontext gibt es nichts (erst Lücke, dann nächstliegender Kontext).
**Maßstab:** wie v18.

## Kennzahlen

| Kennzahl | v17 | v18 | v19 |
|---|---|---|---|
| Fragen 1–25 erfüllt (von 75) | 48 | 56 | 54 |
| Fragen 26–34 erfüllt (von 27) | 26 | 27 | 27 |
| Gesamt erfüllt / teilweise / nicht erfüllt (von 102) | 74 / 25 / 3 | **83** / 17 / 2 | 81 / 16 / **5** |
| Mittlere Länge gezielte Fragen (Wörter) | 33 | 38 | 37 |
| Mittlere Länge Zusammenfassungen 14–16, 25 (Wörter) | 158 | 175 | **135** |
| Kosten | 2,86 USD | 3,11 USD | 3,14 USD |

## Wirkung

**Gewollt (Messung):**
- Zusammenfassungen 23 % kürzer als v18. Biwak- und Übungsinhalte sind aus den Seminarfragen 11, 12, 15 und 16 verschwunden; Frage 15 D1 erstmals ohne Winterdienst.
- Ausnahme (a) wird wie gewünscht genutzt: Frage 7 nennt in allen Durchläufen „Für den Übungsbetrieb auf dem Truppenübungsplatz gilt abweichend …“ in einem Satz.
- Die neuen Fragen 26–34 bleiben vollständig erfüllt.

**Ungewollt (Messung):**
- **Frage 21b, 3 × nicht erfüllt (v18: 1 ×):** Das Modell nutzt die Kontextregel, um den neuen Stand als Sonderfall abzutun: „Beamer werden über den Raumkalender … das Seminarbüro stellt bereit … **Für den Lehrgangsbetrieb gilt abweichend**, dass … IT-Serviceportal.“ Der Bericht sagt ausdrücklich „für alle Lehr- und Seminarräume des Standorts“; nur der Titel nennt den Lehrgangsbetrieb. Die Kontextregel konkurriert hier mit der Regel „jüngster Stand“.
- **Frage 10b, 2 × nicht erfüllt (v18: 1 ×):** „Das Fahrzeug wird vollgetankt zurückgegeben“ (Stand 2023, überholt) wird an die Antwort angehängt, obwohl die Frage nach Reservierung und Kosten fragt.
- Unverändert: Fragen 4, 5, 6 mit Zusätzen zu anderen Rückgabeverfahren bzw. Erste-Hilfe-Meldung; 9 Verantwortung indirekt; 25 unvollständig (jetzt zusätzlich Garderobe, Feueralarm-Sammelplatz in D1).

## Beobachtungen

- Die verschärfte Regel erreicht ihr Ziel bei Erfahrungsfragen und Zusammenfassungen (kürzer, sauberer), erhöht aber das Risiko, dass ein **neuer Stand als „anderer Kontext“ eingeordnet** und der alte als aktuell beibehalten wird. Ob zwei Berichte denselben oder einen anderen Kontext betreffen, ist genau die Unterscheidung, die das Modell hier falsch trifft.
- Überholte Stände als aktuell (5 von 102) betreffen jeweils Themen, zu denen die Datenbank ältere und neuere Regeln mit Datum enthält. Das spricht für eine **Prüfung im Programm** (Hinweis „möglicherweise überholt, neuerer Stand vom …“), statt weitere Prompt-Regeln.

## Grenzen

Ein Lauf mit drei Durchläufen; Unterschiede von 1–3 Antworten liegen im Bereich der Schwankung zwischen Läufen; Bewertung durch ein anderes KI-Modell.

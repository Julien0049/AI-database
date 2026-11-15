# Bewertung: Programmprüfung „möglicherweise überholt“ (kostenlos, ohne Sprachmodell)

**Status:** Agentenmessung, 14.11.2026. Skript: `scripts/aktualitaet_pruefen.py`. Datengrundlage: Antworten aus v17, v18, v19 (je 34 Fragen × 3 Durchläufe, 58 Berichte), Aussagen-Datenbank (`index/aussagen.sqlite`, 359 Aussagen).
**Idee (Nutzer):** Was im Prompt nicht zuverlässig klappt, als harte Regel ins Programm. Hier: Jeder Beleg zeigt auf eine Aussage der Datenbank (Thema, Art, Kontext, Datum). Ist sie eine Regel (oder „unklar“) und gibt es zu demselben Gegenstand eine neuere Regel aus einem anderen Bericht, wird der Satz als „möglicherweise überholt“ markiert. Fragen nach Änderungen („verändert“, „früher“, „über die Zeit“) werden nicht geprüft.
**Maßstab:** 10 Antworten, die in der Agentenbewertung einen überholten Stand als aktuell nannten (v17 Frage 21 × 3, v18 Fragen 10 und 21 je × 1, v19 Frage 10 × 2 und Frage 21 × 3). Fehlalarm = Warnung bei einer Antwort ohne diesen Fehler. Geprüft: 288 Antworten.

## Ergebnis

| Variante: „derselbe Gegenstand“, wenn … | Fehler erkannt | Fehlalarme |
|---|---|---|
| gleiches Thema | 10/10 | 128/278 (46 %) |
| **gleiches Thema + gleicher Kontext (Ähnlichkeit ≥ 0,90) + keine bloße Bestätigung (Inhalt < 0,93)** | **10/10** | **19/278 (7 %)** |
| ähnliche Bedeutung (≥ 0,92) | 10/10 | 114/278 (41 %) |
| ähnliche Bedeutung (≥ 0,92) + Kontext/Bestätigung | 7/10 | 23/278 (8 %) |

Weitere Schwellen im Skript; Kontext- und Bestätigungsfilter mit Schwellen 0,85/0,90 und 0,93/0,95 verglichen.

## Verbleibende Fehlalarme (beste Variante)

Fast ausschließlich zwei Muster, jeweils in allen drei Läufen:
- Frage 14 (Fahrzeuge): Ein Satz aus dem Bericht von 2023 („die ausleihende Person gibt das Fahrzeug zurück“) wird markiert, weil derselbe Bericht auch die überholte Tankregel enthält und ein neuerer Bericht zum selben Thema existiert. Thema gleich, aber andere Teilregel.
- Frage 18 (Raumschlüssel): Die Stubenschlüssel-Regel (2026) gilt als „gleicher Kontext“ wie die Abendseminar-Schlüssel; das kleine Embedding-Modell bewertet die Kontexte als zu ähnlich.

## Einordnung

- Eine reine Datumsregel nach Thema warnt zu oft (46 %); erst die Kontext- und Bestätigungsfilter machen sie brauchbar. Die nötigen Angaben (Kontext, Art, Datum je Aussage) liefert die Aussagen-Datenbank bereits.
- **Grenze:** Die Schwellen wurden an denselben Antworten abgestimmt, an denen gemessen wurde. Die Werte sind daher optimistisch und müssen an neuen Läufen oder Daten bestätigt werden.
- Die Prüfung soll **warnen, nicht löschen** („möglicherweise überholt; neuerer Stand: Titel, Datum“), weil gleiche Themen nicht immer dieselbe Teilregel bedeuten.
- Bekannte Fehler: nur 10, alle aus zwei Fragen (10b, 21b). Die Aussagekraft für andere Fehlerarten ist begrenzt.

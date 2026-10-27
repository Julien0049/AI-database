# Bewertung: Gemini 2.5 Pro, zweiter Test (zehn Berichte)

**Status:** Agentenbewertung (Claude), vom Nutzer noch zu prüfen.
**Lauf:** [ergebnisse_google_gemini-2.5-pro_2026-10-26_v2.json](./ergebnisse_google_gemini-2.5-pro_2026-10-26_v2.json), 26.10.2026, Modell `google/gemini-2.5-pro` über OpenRouter.
**Aufbau:** Alle zehn Berichte (fünf Material, fünf Fahrzeug) vollständig im Prompt, keine Suche. Systemprompt unverändert gegenüber dem ersten Lauf. Ein Durchlauf.
**Maßstab:** Antwortentwürfe und Kriterien in [test_questions.md](../data/synthetic_reports/test_questions.md) sowie der Wortlaut der Berichte.

## Ergebnis

Sieben von zehn Antworten erfüllen die Kriterien, drei teilweise. Inhaltlich erfunden wurde nichts; ein Fehler betrifft eine falsche Quellenangabe.

| Frage | Prüft | Ergebnis | Vergleich zu Lauf 1 | Begründung |
|---|---|---|---|---|
| 1 | Widerspruch, neuester Stand | erfüllt | gleich | Folgt AAR 2025-01-20; der jüngere Fahrzeugbericht mit ähnlichen Stichworten wird nicht herangezogen. |
| 2 | Widerspruch und Ergänzung | erfüllt | gleich | Rückgabe und Meldung korrekt zusammengeführt, richtige Quellen. |
| 3 | Anderer Kontext | erfüllt | gleich | Nur der Bericht zu eintägigen Veranstaltungen. |
| 4 | Direkte Regel | teilweise | schlechter | Inhalt korrekt, aber **AAR 2025-09-15 (Fahrzeuge) als zweite Quelle genannt**, obwohl dieser Bericht einzeln nummerierte Geräte nicht betrifft. Wieder ohne Datumsangaben. |
| 5 | Fehlende Evidenz | teilweise | gleich | Wie in Lauf 1: niemand beschuldigt, aber keine ausdrückliche Aussage, dass die verantwortliche Person nicht feststellbar ist. |
| 6 | Nicht belegtes Detail | erfüllt | gleich | Klar als nicht belegt benannt. |
| 7 | Versteckter Widerspruch | erfüllt | neu | Findet die beiläufige Tankregel, folgt dem jüngeren Bericht, nennt „vollgetankt“ nicht als Alternative. |
| 8 | Ähnliche Stichworte, anderer Kontext | erfüllt | neu | Überträgt das Material-Verfahren nicht; richtige Quelle. |
| 9 | Ergänzung und fehlende Evidenz | teilweise | neu | Schadensformular korrekt (nicht Abweichungsprotokoll). Zur Verantwortung dasselbe Muster wie bei Frage 5: nur indirekt beantwortet. |
| 10 | Teilweise belegte Frage | erfüllt | neu | Belegter Teil beantwortet, fehlende Kosteninformation offen benannt. |

## Beobachtungen

- **Themenvermischung zeigt sich bei den Quellen, nicht beim Inhalt:** Die Falle aus dem Fahrzeugbericht wirkte bei Frage 4, nicht bei Frage 8, für die sie gedacht war.
- **Wiederkehrendes Muster bei Verantwortungsfragen (5, 9):** Das Modell gibt den Berichtssatz „aus dem Fehlen/Schaden allein wird keine persönliche Verantwortung abgeleitet“ wieder, statt ausdrücklich zu sagen, dass sich die Frage nicht beantworten lässt. Offen ist, ob diese indirekte Antwort als ausreichend gelten soll.
- **Quellenformat uneinheitlich:** Bei Frage 4 fehlen erneut die Daten.

## Grenzen

- Quellenabruf ist nicht getestet, weil das Modell alle Dokumente vollständig erhielt.
- Ob das Modell die älteren Widersprüche (Fragen 1, 2, 7) erkannt hat, ist an der Nutzerantwort nicht ablesbar.
- Je ein Durchlauf; Unterschiede zu Lauf 1 (etwa Frage 4) können auch Zufallsschwankung sein.
- Die Bewertung stammt von einem anderen KI-Modell und ist keine unabhängige menschliche Prüfung.

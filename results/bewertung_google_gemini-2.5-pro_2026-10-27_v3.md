# Bewertung: Gemini 2.5 Pro, dritter Test (Regel 6 ergänzt)

**Status:** Agentenbewertung (Claude), vom Nutzer noch zu prüfen.
**Lauf:** [ergebnisse_google_gemini-2.5-pro_2026-10-27_v3.json](./ergebnisse_google_gemini-2.5-pro_2026-10-27_v3.json), 27.10.2026, Modell `google/gemini-2.5-pro` über OpenRouter.
**Aufbau:** Wie Lauf 2 (zehn Berichte vollständig im Prompt, keine Suche). Einzige Änderung: Regel 6 im Systemprompt verlangt, fehlende Informationen auch bei Teilfragen ausdrücklich zu benennen. Ein Durchlauf.
**Maßstab:** Antwortentwürfe und Kriterien in [test_questions.md](../data/synthetic_reports/test_questions.md) sowie der Wortlaut der Berichte.

## Ergebnis

Sieben von zehn Antworten erfüllen die Kriterien, drei teilweise – dieselbe Verteilung wie in Lauf 2. Die ergänzte Regel 6 zeigt bei den Fragen 5 und 9 keine sichtbare Wirkung.

| Frage | Ergebnis | Vergleich zu Lauf 2 | Begründung |
|---|---|---|---|
| 1 | erfüllt | gleich | Neuester passender Stand, richtige Quelle. |
| 2 | erfüllt | gleich | Rückgabe und Meldung korrekt zusammengeführt. |
| 3 | erfüllt | gleich | Nur der Bericht zu eintägigen Veranstaltungen. |
| 4 | teilweise | gleich | Inhalt korrekt, Datum jetzt vorhanden, aber **erneut AAR 2025-09-15 (Fahrzeuge) als Quelle**. |
| 5 | teilweise | gleich | Wieder nur indirekt („keine persönliche Verantwortung abgeleitet“), keine ausdrückliche Aussage, dass die Person nicht feststellbar ist. Quelle ohne Datum. |
| 6 | erfüllt | gleich | Klar als nicht belegt benannt. |
| 7 | erfüllt (Formfehler) | gleich | Inhalt korrekt; Quelle ohne Datum. |
| 8 | erfüllt | gleich | Material-Verfahren nicht übertragen. |
| 9 | teilweise | gleich | Wie Frage 5: Verantwortung nur indirekt beantwortet. Quelle ohne Datum. |
| 10 | erfüllt | gleich | Fehlende Kosteninformation offen benannt. |

## Beobachtungen

- **Regel 6 wirkt nicht auf die Verantwortungsfragen.** Wahrscheinliche Erklärung: Das Modell sieht die Frage durch den Berichtssatz „aus dem Fehlen/Schaden allein wird keine persönliche Verantwortung abgeleitet“ als beantwortet an und erkennt keine Lücke. Die Abweichung liegt damit eher in der Auslegung der Frage als im Übersehen fehlender Information.
- **Falsche Zusatzquelle bei Frage 4 jetzt in zwei Läufen.** Das spricht für ein wiederkehrendes Muster, nicht für Zufall.
- **Fehlende Daten in den Quellen wandern:** In Lauf 2 fehlten sie bei Frage 4, jetzt bei 5, 7 und 9. Ein Zusammenhang mit dem ältesten Bericht ist damit unwahrscheinlich; eher hält sich das Modell nicht zuverlässig an das Format. Das stützt den Plan, Quellenangaben im PoC von der Anwendung aus Metadaten zu erzeugen.

## Grenzen

- Quellenabruf ist nicht getestet, weil das Modell alle Dokumente vollständig erhielt.
- Je ein Durchlauf pro Prompt-Fassung.
- Weitere Prompt-Anpassungen gezielt für diese zehn Fragen bergen die Gefahr, den Prompt auf den kleinen Testsatz zuzuschneiden.
- Die Bewertung stammt von einem anderen KI-Modell und ist keine unabhängige menschliche Prüfung.

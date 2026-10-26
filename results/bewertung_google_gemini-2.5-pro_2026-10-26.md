# Bewertung: Gemini 2.5 Pro, erster Test

**Status:** Agentenbewertung (Claude), vom Nutzer noch zu prüfen.
**Lauf:** [ergebnisse_google_gemini-2.5-pro_2026-10-26.json](./ergebnisse_google_gemini-2.5-pro_2026-10-26.json), 26.10.2026, Modell `google/gemini-2.5-pro` über OpenRouter.
**Aufbau:** Alle fünf Berichte vollständig im Prompt, keine Suche. Systemprompt mit den Antwortregeln aus `AGENTS.md`. Ein Durchlauf.
**Maßstab:** Antwortentwürfe und Kriterien in [test_questions.md](../data/synthetic_reports/test_questions.md) sowie der Wortlaut der Berichte.

## Ergebnis

Fünf von sechs Antworten erfüllen die Kriterien, eine teilweise. Keine Antwort enthält erfundene Angaben.

| Frage | Prüft | Ergebnis | Begründung |
|---|---|---|---|
| 1 | Widerspruch, neuester Stand | erfüllt | Ordnet „dreitägig“ als mehrtägig ein, gibt das Verfahren aus AAR 2025-01-20 wieder und nennt nur diese Quelle. Kein älteres Verfahren als Alternative, kein „gültig“. |
| 2 | Widerspruch und Ergänzung | erfüllt | Führt Rückgabe (2025-01-20) und Meldung (2025-02-04) zusammen. Keine erfundene Seriennummer oder Zusatzpflicht. Der Satz zur persönlichen Verantwortung ist belegt, aber nicht gefragt. |
| 3 | Anderer Kontext | erfüllt | Wendet nur den Bericht zu eintägigen Veranstaltungen an. |
| 4 | Direkte Regel | erfüllt, Formfehler | Inhalt korrekt und nicht von gemeinsamen Sets verallgemeinert. Quellenangabe ohne Datum, obwohl der Prompt es verlangt. |
| 5 | Fehlende Evidenz | teilweise | Beschuldigt niemanden und erfindet nichts. Es fehlt die ausdrückliche Aussage, dass sich die verantwortliche Person aus den Berichten nicht feststellen lässt; zusätzlich nicht gefragte Angaben zum Protokoll. |
| 6 | Nicht belegtes Detail | erfüllt | Sagt klar, dass Formularfeld und Kennziffer nicht genannt werden, und gibt nur belegte Angaben wieder. |

## Grenzen

- Quellenabruf ist nicht getestet, weil das Modell alle Dokumente vollständig erhielt.
- Ob das Modell den älteren Widerspruch bei Frage 1 und 2 erkannt hat, ist an der Nutzerantwort nicht ablesbar und wurde nicht separat abgefragt.
- Ein einzelner Durchlauf mit sechs Fragen; Antworten können bei Wiederholung abweichen.
- Die Bewertung stammt von einem anderen KI-Modell und ist keine unabhängige menschliche Prüfung.

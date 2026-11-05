# Bewertung: Gemini 2.5 Pro, v13 (Sichtung aller Berichte in Paketen), abgebrochen

**Status:** Agentenauswertung (Claude), vom Nutzer noch zu prüfen. **Lauf unvollständig:** Das Budget war erschöpft, bevor eine Antwort entstand.
**Läufe:** [Testlauf](./ergebnisse_google_gemini-2.5-pro_2026-11-05_v13_test.json) (nur Frage 25, ein Durchlauf) und [Hauptlauf](./ergebnisse_google_gemini-2.5-pro_2026-11-05_v13_abgebrochen.json) (25 Fragen, drei Durchläufe geplant), 05.11.2026, Notebook [citation_check_v7.ipynb](../notebooks/citation_check_v7.ipynb).
**Aufbau:** Das Modell sichtet alle 48 Berichte in 5 Paketen zu je höchstens 10 und gibt die Kennungen der relevanten Berichte zurück (Prompt `SICHTUNG`); nur diese gehen in den Antwortschritt (Regeln und Zitatprüfung wie v8–v12).

## Was passiert ist

- Im Hauptlauf schickte das Notebook zuerst alle 375 Sichtungen und erst danach die Antworten ab. Nach 185 Sichtungen war das Budget des OpenRouter-Workspace erschöpft (**10 USD pro Monat**, verbraucht 10,09 USD, Neustart am **01.12.2026**). Alle übrigen Sichtungen und alle 75 Antworten schlugen fehl.
- **Ablauffehler (Agent):** Bei Frage-für-Frage-Bearbeitung wären die bis dahin fertigen Antworten erhalten geblieben. Das Notebook ist seitdem so umgebaut, und es stoppt bei erschöpftem Budget sofort (lokal mit Attrappe geprüft).

## Testlauf (Frage 25, Gäste und Besucher)

- **Alle vier verstreuten Kernberichte gefunden** (Besucherausweise, WLAN für Gäste, Besucherparkplätze, Abendseminar „Projektplanung“). Bei der Suche lagen sie auf den Plätzen 23–42 (s5), in v12 fehlten sie.
- **Antwort:** deckt alle vier Punkte der Checkliste ab; 13 von 13 Zitaten gültig. Ein Störinhalt (Winterdienst: Haupteingang bei Glätte), daher nach dem Maßstab ab v11 „teilweise“.
- **Sichtung zu großzügig:** 11 Berichte ausgewählt, davon 4 nötig.
- **Kosten:** 0,114 USD für 6 Anfragen. **Wartezeit:** 51 s für eine Frage (v11/v12: etwa 4 s je Anfrage).

## Sichtung im Hauptlauf (kostenlos ausgewertet)

35 Fragen-Durchläufe wurden vollständig gesichtet (Durchlauf 1 alle 25 Fragen, Durchlauf 2 Fragen 1–10).

| Kennzahl | Wert |
|---|---|
| Nötige Berichte gefunden | **54 von 55** |
| Übersehen | Frage 24 („Buchung von Seminarräumen“): Der Bericht nennt keine Frist und wurde deshalb als nicht relevant eingestuft. Er belegt aber den bekannten Teil (Buchung über den Raumkalender). |
| Ausgewählte Berichte je Frage | im Mittel 6,6 (0 bis 16) |
| Kosten | 2,88 USD für 185 Sichtungen, rund 1,6 Cent je Sichtung |

Beispiele für zu großzügige Auswahl: Bei Frage 2 (Adapter fehlt im Set) wurden 16 Berichte ausgewählt, darunter Raumschlüssel, Beamer und Besucherausweise. Bei Frage 25 waren es 15. Das Erste-Hilfe-Formular HV-7 wurde bei Frage 6 in beiden Durchläufen mit ausgewählt; die Sichtung siebt diesen Störbericht also nicht aus.

## Beobachtungen

- **Die Sichtung löst das Auffindeproblem:** Fast alle nötigen Berichte werden gefunden, auch die, an denen die Suche grundsätzlich scheiterte (Frage 25) und der nur nebenbei erwähnte neueste Stand (Frage 22: „Vorbereitung eines Seminartags“ ausgewählt).
- **Die Sichtung filtert schlecht aus:** Sie wählt eher zu viel als zu wenig. Für die Vollständigkeit ist das die richtige Richtung, die Störberichte gelangen so aber wieder in den Antwortschritt. Ob die Antworten dadurch besser oder schlechter sind als in v11, ist nicht gemessen.
- **Gründlichkeit kostet:** Bei 48 Berichten etwa sechsmal so viele Anfragen und eine Wartezeit von fast einer Minute je Frage. Bei Tausenden Berichten wäre das ohne Vorauswahl nicht tragbar.

## Grenzen

- Keine Antwort aus dem Hauptlauf; Aussagen zur Antwortqualität nur aus dem Testlauf (eine Frage, ein Durchlauf).
- Sichtung nur für 35 von 75 geplanten Fragen-Durchläufen ausgewertet; ein Prompt, eine Paketgröße.

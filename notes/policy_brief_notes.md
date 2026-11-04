# Merkpunkte für das Policy Brief

Sammlung von Beobachtungen aus dem PoC, die im abschließenden Policy Brief aufgegriffen werden sollen. Gekennzeichnet ist jeweils, ob es sich um eine Beobachtung des Nutzers, eine Messung oder einen Vorschlag des Agenten handelt.

## Laufzeit

- **Beobachtung (Nutzer, Läufe v1–v6):** Die Testläufe in Colab dauerten lange, obwohl der Datensatz mit dreizehn kurzen Berichten im Vergleich zur realen Welt sehr klein ist. Für einen PoC ist das akzeptabel.
- **Einschränkung (Nutzer):** In den Tests werden viele Fragen auf einmal gestellt (17 Fragen × 3 Durchläufe). Im echten Einsatz stellt eine Person meist eine oder wenige gezielte Fragen. Die Gesamtdauer eines Testlaufs ist deshalb nicht die Wartezeit einer Nutzerin oder eines Nutzers.
- **Messung:** Bis v6 wurde die Laufzeit nicht gemessen. Ab v7 wird die Gesamtdauer als `dauer_s` gespeichert; die Wartezeit für eine einzelne Frage ist damit noch nicht direkt gemessen.
- **Vorschlag (Agent, vom Nutzer befürwortet, technisch ungeprüft):** Für den realen Einsatz wäre eine bessere technische Umsetzung nötig. Mögliche Ansätze: vorgeschaltete Suche statt aller Berichte im Prompt, schrittweise Zusammenfassung bei vielen Berichten, ein schnelleres Modell oder weniger Denkzeit. Wirkung und Qualitätsverlust müssten jeweils gemessen werden.

# Policy Brief – Stichpunkte zum Ausformulieren

*Stand 15.11.2026, ersetzt inhaltlich den Entwurf `policy_brief_draft_en.md` vom 05.11.2026 (dort noch 48 Berichte, Cloud-Modell, keine Offline-Messung). Adressat: Kommandeur, ohne KI-Vorkenntnisse; soll die Idee befürworten und weitertragen. Sprache: deutsche und englische Fassung (Nutzer). Zahlen sind gemessen, außer als Vorschlag oder Schätzung markiert. Details und Herkunft jeder Zahl: `policy_brief_notes.md` und `results/`.*

## 1. Kernaussage vorweg (BLUF)

- Ein KI-Assistent kann Fragen zu einer Sammlung von Erfahrungsberichten (AARs) in Alltagssprache beantworten, nennt zu jeder Aussage den Bericht mit Titel und Datum und prüft jedes Zitat automatisch.
- Er bevorzugt den **neuesten gültigen Stand**, sagt offen, wenn die Berichte etwas **nicht** enthalten, und trennt Regeln nach **Kontext** (Standort vs. Übung).
- Er **wächst mit**: neue Berichte im Ablageordner werden automatisch erfasst; die Kosten je Frage steigen nicht mit der Größe der Sammlung.
- **Offline ist technisch nachgewiesen** (Testlauf ohne Internet, keine Verbindung nach außen). Die Qualität hängt aber an der Modellgröße: Ein Laptop reicht nicht; ein Server mit **einer großen Grafikkarte** erreicht annähernd die Qualität eines Spitzenmodells aus der Cloud (Abbildung).
- **Bitte:** Grundidee befürworten – KI-gestützte Datenbank für die AARs der Einheit auf eigener Hardware im geschlossenen Netz – und einen Pilotbetrieb mit echten, offenen Berichten unterstützen.

## 2. Warum das wichtig ist

- AARs sollen Erfahrungen weitergeben; in der Praxis gehen sie verloren:
  - niemand kann alle Berichte lesen;
  - Regeln ändern sich, der neueste Stand wird übersehen;
  - abweichende Erfahrungen erreichen die nächste Einheit selten.
- Ein Assistent, der alle Berichte durchsucht, den neuesten Stand findet und Quellen nennt, macht vorhandenes Wissen nutzbar – ohne Mehrarbeit für die Verfasser.

## 3. Was getestet wurde

- Funktionsfähiger Prototyp: Browser-Chat auf einem normalen Laptop, über 21 Versionen schrittweise verbessert (Oktober–November 2026).
- 58 fiktive, offene Testberichte, davon 10 lange Berichte aus einem fiktiven Lehrgangs- und Übungsbetrieb (Kfz-Dienst, Verpflegung, Biwak, Besuchertag, Schießausbildung …).
- Eingebaute Fallen: Regeln, die sich unbemerkt ändern; neue Regel nur nebenbei auf Seite 3; ähnliche Wörter in anderem Kontext; widersprüchliche Erfahrungen; fehlende Daten; Fragen ohne Antwort in den Berichten.
- 34 Testfragen, jede Version dreimal; Bewertung nach vorher festgelegten Kriterien.
- Keine echten oder eingestuften Inhalte (der Prototyp nutzt für die meisten Tests ein Cloud-Modell).

## 4. Ergebnisse (je ein Satz + Zahl)

1. **Quellen sind überprüfbar:** Jede Aussage wird mit wörtlichem Zitat belegt und vom Programm gegengeprüft; Titel und Datum kommen aus dem Bericht, nicht von der KI. Seit einem eingebauten Schutz keine erfundenen Belege mehr.
2. **Neuester Stand:** Mit dem Spitzenmodell 95 % der Antworten ohne kritischen Fehler; Restrisiko ~5 %, dass ein älterer Stand als gültig erscheint. Ein Programmcheck warnt dann zusätzlich („möglicherweise überholt, neuerer Bericht vom …“).
3. **Wächst mit großen Mengen:** Jeder neue Bericht wird beim Eingang einmal in Einzelaussagen zerlegt (2–9 Cent je Bericht). Danach kostet eine Frage rund 3 Cent und ca. 20 Sekunden, egal wie groß die Sammlung ist. Nachgewiesen: Zehn nachträglich abgelegte Berichte flossen ohne Neuaufbau sofort ein; vergrabene Regeländerungen wurden gefunden.
4. **Kontext und Präzision:** Antworten bleiben beim gefragten Fall (Standort ≠ Übung, Seminar ≠ Biwak) und sind kurz; Abweichendes nur als gekennzeichneter Hinweis. Ohne diese Regel wurden Antworten mit wachsender Sammlung immer länger.
5. **Ehrlich bei Lücken:** Fehlt etwas in den Berichten, sagt der Assistent das, statt zu raten.
6. **Offline:** Kompletter Testlauf bei getrenntem Internet, null Verbindungen nach außen. Aber: Ein kleines Modell auf dem Laptop lieferte 59 % unbrauchbare Antworten.
7. **Modellgröße entscheidet – mit abflachender Kurve (Abbildung):** unbrauchbare Antworten 30 % (27 Mrd. Parameter) → 13 % (~120 Mrd., eine Grafikkarte) → 11 % (~400 Mrd., Server mit 8 Karten); Spitzenmodell in der Cloud 5 %.

*Abbildung:* `notes/abbildungen/modellgroesse_fehler_de.png` / `_en.png`

## 5. Was das für den Eigenbetrieb heißt (Prognose, Größenordnungen)

- Ein offenes Modell der ~120-Mrd.-Klasse läuft auf **einer** Grafikkarte mit 80–96 GB Speicher (Karte ca. 15.000–25.000 USD, dazu Server, Betrieb, Zulassung).
- Der Schritt zur 400-Mrd.-Klasse (Server mit 8 Karten, ca. 285.000–530.000 USD) bringt kaum Gewinn.
- Qualität dann etwa doppelt so viele kritische Fehler wie das Spitzenmodell – mit Quellenpflicht und Programmwarnungen ein realistischer Ausgangspunkt für einen Pilot.
- Lizenzen: einige offene Modelle frei (Apache 2.0), andere mit Nutzungsbedingungen → rechtlich prüfen.

## 6. Grenzen der Aussage

- Fiktive, selbst erstellte Testdaten; echte Berichte sind länger und uneinheitlicher.
- Bewertung durch KI mit festen Kriterien, Stichproben durch den Verfasser.
- Ein Spitzenmodell in der Cloud ist nicht für eingestufte Inhalte geeignet; Eigenbetrieb nur gemessen über gleichwertige Modelle, nicht auf eigener Serverhardware.
- Mehrere gleichzeitige Nutzer und Zugriffsrechte nicht getestet.
- Hardwarepreise widersprüchlich, nur Spannen.
- Die Antwortregeln wurden am Cloud-Modell geschärft; offene Modelle liefen ohne Anpassung. Der Abstand ist daher eher kleiner als gemessen; die Abstimmung auf das spätere Zielmodell gehört in den Pilot.

## 7. Empfehlungen

1. **Pilot genehmigen:** echte, offene AARs eines Bereichs, offenes Modell der ~120-Mrd.-Klasse auf eigenem Server im geschlossenen Netz; gleiche Messgrößen wie hier.
2. **Einheitliches Ablageformat:** Briefkopf mit Titel und Datum an fester Stelle, Verfasser am Ende, möglichst Kontext (Einheit, Lage, Veranstaltung). Kostet Sekunden, macht Quellen und Zeitbezug zuverlässig. Keine eingescannten PDFs.
3. **Quellenpflicht und Warnungen:** Fußnoten, automatische Zitatprüfung, Hinweis bei möglicherweise überholten Aussagen.
4. **Nutzer einweisen:** gezielte Fragen stellen, Fußnoten prüfen; der Assistent führt zu den Berichten, ersetzt sie nicht.
5. **Nächste Schritte vorbereiten:** Mehrnutzerbetrieb mit Anmeldung und Zugriffsrechten; Lizenzprüfung; Universität der Bundeswehr München einbinden (Abschlussarbeiten Informatik, Hackathon – Themen in `policy_brief_notes.md`).

## 8. Fragen an die zuständigen Stellen

- **Zulassung:** neue Soft- und Hardware im geschlossenen Netz braucht eigene Sicherheitsprüfung.
- **Rechenleistung:** Modell muss vollständig im Netz laufen; Größenordnung siehe Abschnitt 5.
- **Zugriffsrechte:** Assistent darf niemandem Inhalte zeigen, die er nicht sehen darf; einfach, wenn alle Netznutzer alles sehen dürfen – von der Sicherheitsstelle zu bestätigen.

## 9. Entscheidung erbeten

- Grundidee befürworten und auf der nächsten Ebene unterstützen.
- Der PoC zeigt: prinzipiell machbar, Grenzen und Gefahren benannt. Vor einer Einführung nötig: Ingenieursarbeit für ein sicheres Offline-System und Tests mit echten Berichten.

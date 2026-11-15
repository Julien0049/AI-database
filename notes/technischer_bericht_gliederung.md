# Technischer Bericht (Langfassung) – Gliederung

*Stand 15.11.2026. Anhang zum Policy Brief für Interessierte und für alle, die weiterarbeiten. Fassungen auf Deutsch und Englisch (Nutzer). Wird vollständig vom Agenten verfasst (dann mit KI-Credit-Zeile). Quellen der Inhalte in Klammern.*

1. **Zusammenfassung** (1 Seite): Ziel, Aufbau, wichtigste Messwerte, Empfehlung, Grenzen.
2. **Ausgangslage und Ziel**
   - Problem verlorener Erfahrungen in AARs; Ziel des PoC.
   - Bestätigte Anforderungen (AGENTS.md): einzige Wissensquelle, neuester Stand bei Regeln, Sichtweisen bei Erfahrungen, Kontext, Lücken offen nennen, Quellen mit Titel und Datum, automatische Erfassung.
   - Rahmen: fiktive Daten, Cloud-Modell für Tests, Offline als Ziel.
3. **Begriffe in Kürze** – Sprachmodell, Parameter/Gewichte, Layer, Tokens, Kontextfenster, Embeddings/Suche nach Bedeutung, Experten-Modelle (gesamt/aktiv), Kompression (Bit).
4. **Systemaufbau**
   - Datenfluss: Ablageordner → automatischer Abgleich → Zerlegung in Aussagen → Suche → Antwort aus ganzen Berichten → Zitatprüfung und Fußnoten → Aktualitätsprüfung → Oberfläche.
   - Komponenten und Dateien (`app/aidb.py`, `aussagen.py`, `suche.py`, Prompts, Oberfläche).
   - Harte Programmregeln vs. Prompt-Regeln (was geprüft werden kann, gehört ins Programm).
5. **Testdaten und Bewertung**
   - Datensatzstufen v1–v4 (5 → 58 Berichte), Fallenkatalog (`data/synthetic_reports/README.md`).
   - 34 Testfragen mit Kriterien (`test_questions.md`), Varianten für den Nachtragstest.
   - Bewertung: Handbewertung (v1–v20), regelbasierte Bewertung (v21) und ihre Eichung; Grenzen der Bewertung.
6. **Versuchsreihe** (je Phase: Frage, Änderung, Messung, Folgerung)
   - A Antwortregeln und Belege (v1–v10)
   - B Suche bei mehr Berichten (s1–s5, v11–v13)
   - C Aussagen-Datenbank („Karteikarten“) und Auswahl (v14–v16)
   - D Lange militärische Berichte und Nachtragstest (dataset-v4, v17)
   - E Kontext und Antwortlänge (v18–v19)
   - F Programmprüfung auf überholte Aussagen
   - G Offline-Betrieb und Modellgröße (v20–v21)
   - Versuchsübersicht als Tabelle
7. **Ergebnisse quer gelesen** – Genauigkeit, Aktualität, Belege, Lücken, Kontext, Antwortlänge, Kosten und Dauer, Skalierung; typische Fehlerarten mit Beispielen.
8. **Prognose für den Eigenbetrieb** – Abbildung Modellgröße/Fehler, Speicherbedarf-Rechnung, Hardware- und Kostenspannen, Lizenzen, was die Messung nicht abdeckt (eigene Hardware, Mehrnutzer).
9. **Grenzen** – Daten, Bewertung, Modelle/Anbieter, Preise, Sicherheit (Laptop-Test ≠ Zertifizierung).
10. **Empfehlungen und nächste Schritte** – Pilot, Ablageformat, Quellenpflicht, Mehrnutzer und Zugriffsrechte, Lizenzprüfung, Themen für UniBw M (Abschlussarbeiten, Hackathon).
11. **Anhang**
    - Reproduktion: Einrichtung, Befehle, Skripte, Ergebnisdateien.
    - Kostenaufstellung aller Läufe.
    - Testfragen und Kriterien (Auszug oder Verweis).
    - Netzprotokoll des Offline-Laufs.

# Vorläufiger Prototyp-Entwurf

**Stand:** 19. Oktober 2026
**Status:** Agentenentwurf auf Basis des Projektinterviews und einer Quellenrecherche. Kein endgültiger Technologieentscheid und keine Sicherheitsfreigabe.

## Ziel

Eine einzelne Person soll in einer einfachen lokalen Browseroberfläche Fragen zu ungefähr zehn fiktiven After-Action-Reports stellen können. Das System soll eine klare, zusammengeführte Antwort aus den Dokumenten geben, die verwendeten Quellen knapp nennen und passende zeitliche Änderungen verständlich behandeln.

Der Prototyp soll während der Nutzung ohne Internetzugriff funktionieren. Die Beispieldokumente sind synthetische Testdaten und keine echten Berichte, gültige Doktrin oder geprüften Empfehlungen.

## Geplante Antwortregeln

1. Nur Textstellen aus dem lokalen Dokumentbestand als Belege verwenden. Websuche und unbelegte Ergänzung aus Modellwissen sind ausgeschlossen.
2. Ergänzende Informationen aus mehreren passenden Dokumenten dürfen in einer knappen Antwort zusammengeführt werden.
3. Bei vergleichbarem Kontext die jüngste passende Aussage priorisieren und ältere abweichende Stände mit Datum und Quelle als frühere Version kenntlich machen. Ältere Aussagen nicht stillschweigend löschen oder als gleichrangige Alternativen präsentieren.
4. Eine zeitliche Priorität nur behaupten, wenn Zeitraum, Thema und Anwendungsbereich vergleichbar sind. Bei fehlender oder mehrdeutiger Vergleichbarkeit die Unsicherheit benennen.
5. Wenn die Quellen die Frage nicht ausreichend beantworten, das klar sagen und keine Lücken füllen.
6. Die Antwort steht im Vordergrund; kompakte Quellenhinweise mit Dokumentname und Datum folgen am Ende.

Diese Regeln beschreiben Quellenverhalten, nicht die Wahrheit oder Gültigkeit einer Aussage. Ein neueres fiktives Dokument beweist nicht, dass sein Inhalt real zutrifft.

## Vorschlag für eine einfache Architektur

1. **Dokumentenordner:** Markdown- und Textdateien liegen lokal in einem festgelegten Eingabeordner. Ein bewusst gestarteter Import liest neue oder geänderte Dateien ein.
2. **Lokaler Dokumentenspeicher:** Eine kleine SQLite-Datenbank kann Dokumentmetadaten und Textpassagen speichern. Für Volltextsuche bietet SQLite FTS5; bei zehn kurzen Dokumenten ist zunächst keine separate Vektordatenbank nötig.
3. **Passagen und Provenienz:** Texte werden anhand von Überschriften in sinnvolle Passagen aufgeteilt. Zu jeder Passage bleiben mindestens Dateiname, Dokumentdatum, Abschnitt und stabiler Quellenbezeichner erhalten. Das Dokumentdatum wird aus dem Dokumentinhalt bzw. expliziten Metadaten gelesen, nicht aus dem Änderungsdatum der Datei abgeleitet.
4. **Suche:** Als einfache Baseline dient Volltextsuche. Als Vergleich oder Erweiterung kann lokale semantische Suche über Embeddings hinzukommen. Eine kombinierte Suche ist ein möglicher nächster Schritt, wenn die Baseline relevante Belege verfehlt.
5. **Antwortgenerierung:** Eine lokale Anwendung übergibt einer lokal laufenden Sprachmodell- und Embedding-Laufzeit ausschließlich die gefundenen Passagen. Quellenbezeichner werden von der Anwendung verwaltet und aus geprüften Metadaten in der Antwort dargestellt, nicht frei vom Modell erfunden.
6. **Oberfläche:** Eine einfache Browser-Chatoberfläche wird lokal bereitgestellt. Benutzeroberfläche, Schriftarten und Bibliotheken dürfen zur Laufzeit keine externen Ressourcen laden.

Für zehn kurze Dokumente ist dies ein Vorschlag für einen verständlichen Start, kein bereits getesteter Entwurf. SQLite FTS5 und lokale Embeddings sind mögliche Komponenten; die Laufzeit- und Modellwahl muss auf der verfügbaren Hardware ausprobiert werden.

## Lokalbetrieb und Grenzen

Vor dem Offline-Test müssten Laufzeit, Bibliotheken, Modell für Antwortgenerierung, Embedding-Modell und alle UI-Ressourcen kontrolliert lokal bereitgestellt werden. Antwortmodell und Embedding-Modell erfüllen unterschiedliche Aufgaben und müssen beide verfügbar sein.

Der Offlinebetrieb sollte praktisch geprüft werden: Netzverbindung trennen oder ausgehende Verbindungen blockieren, die Anwendung kalt starten, Dokumente importieren, eine Suche ausführen und eine Frage beantworten. Netzwerkzugriffe von Anwendung und Laufzeit beobachten, soweit das Betriebssystem dies erlaubt. Das Ergebnis ist ein begrenzter Testnachweis, keine allgemeine Sicherheitszertifizierung. Offlinebetrieb allein macht ein System nicht für eingestufte Inhalte zugelassen. Für die Kursarbeit ausschließlich fiktive oder ausdrücklich unklassifizierte Daten verwenden.

Für eine Maschine ohne zusätzliche GPU hängen Antwortgeschwindigkeit und Modellqualität von Rechner, Arbeitsspeicher, Modellgröße, Quantisierung und Kontextlänge ab. Deshalb vor einer Festlegung ein kleines Modell auf dem tatsächlichen Computer testen. Keine Echtzeit- oder Datenschutzgarantie aus Produktangaben ableiten.

## Evaluation

Die zehn Beispieldokumente eignen sich als Startpunkt, wenn vorab eine kanonische Fassung ausgewählt und manuell mit erwarteten Belegstellen annotiert wird. Der Gemini-Dialog enthält iterative Versionen; diese sollten vor dem Import abgeglichen werden. Die zehn Beispiele allein belegen keine Skalierbarkeit.

Als erster Evaluationssatz werden etwa 24 festgeschriebene Fragen vorgeschlagen, ausgewogen über:

- direkte Fragen, die eine Passage beantwortet;
- Fragen, deren Antwort ergänzende Passagen aus mehreren Dokumenten benötigt;
- zeitliche Konflikte mit vergleichbarem Kontext;
- Fälle, in denen Datum oder Anwendungsbereich nicht ausreichen, um die neueste Aussage sicher zu priorisieren;
- Fragen mit fehlender oder mehrdeutiger Evidenz;
- neutrale Kontrollfragen ohne Widerspruch.

Für jede Frage werden erwartete Belegpassagen, unterstützte Kernaussagen, Konflikt-/Zeitinterpretation und erwartetes Verhalten bei fehlender Evidenz notiert. Ergebnisse getrennt auswerten:

- **Quellenabruf:** Wurden die erforderlichen Passagen gefunden? Bei mehrteiligen Antworten: wurden alle erforderlichen Quellen gefunden?
- **Antwortbelege:** Sind die wesentlichen Antwortaussagen durch die zitierten Passagen gestützt und stimmen die Quellenangaben?
- **Zeit- und Konfliktbehandlung:** Werden beide abweichenden Stände erkannt, der neueste nur bei vergleichbarem Kontext priorisiert und der ältere Stand verständlich eingeordnet?
- **Enthaltung:** Erkennt das System fehlende Evidenz, ohne belegbare Fragen unnötig abzulehnen?

Als Vergleich eignen sich zunächst Volltextsuche allein und semantische Suche allein; eine kombinierte Variante kann danach ergänzt werden. Dokumente, Fragen, Modell und Einstellungen während des Vergleichs konstant halten. Die Bewertungen sind ein kleines projektspezifisches Diagnose-Set, kein allgemeiner Benchmark. Bei der Bewertung kann eine zweite Person einen Teil der Antworten unabhängig prüfen.

## Mögliche Arbeitsschritte

1. Die zehn überarbeiteten Beispieldokumente aus dem Gemini-Verlauf abgleichen und eine eindeutige Testfassung festlegen.
2. Eine kleine Fragen- und Belegsammlung anlegen, einschließlich Ergänzungs-, Konflikt-, Neutral- und Evidenzlückenfällen.
3. Offline-Laufzeit und Modelloption auf dem eigenen Rechner prüfen; Abhängigkeiten und Modelle dokumentieren.
4. Lokalen Import, Passagen- und Metadatenspeicherung sowie eine einfache Volltextsuche umsetzen.
5. Lokale Antwortgenerierung mit Quellenhinweisen ergänzen; Verhalten an den vereinbarten Antwortregeln messen.
6. Semantische bzw. kombinierte Suche nur ergänzen, wenn der Vergleich einen begründeten Nutzen zeigt.
7. Offline-Kaltstart und Antwortverhalten dokumentieren; danach mit mehr Dokumenten erneut messen, statt Skalierbarkeit vorauszusetzen.

## Offene Entscheidungen

- Welche konkreten Fassungen der zehn Beispielberichte bilden das kanonische Testset?
- Welche lokale Laufzeit sowie welches Antwort- und Embedding-Modell laufen akzeptabel auf der vorhandenen Hardware?
- Genügt Volltextsuche zunächst, oder verbessert semantische Suche die gemessenen Fälle?
- Wie viele Testfragen sind im Semesterzeitraum realistisch manuell zu annotieren und bewerten?
- Welche Dokumentformate jenseits von Markdown/Text sind Teil des Semesterumfangs?

## Recherchequellen

- SQLite, [FTS5 Full-Text Search](https://sqlite.org/fts5.html), laufende Dokumentation, abgerufen am 19. Oktober 2026.
- Ollama, [Embeddings](https://docs.ollama.com/capabilities/embeddings), [Generate API](https://docs.ollama.com/api/generate) und [FAQ](https://docs.ollama.com/faq), laufende Dokumentation, abgerufen am 19. Oktober 2026.
- Georgi Gerganov et al., [llama.cpp](https://github.com/ggml-org/llama.cpp), Projekt-README, abgerufen am 19. Oktober 2026.
- Apple ML Research, [MLX documentation](https://ml-explore.github.io/mlx/build/html/index.html), laufende Dokumentation, abgerufen am 19. Oktober 2026.
- Patrick Lewis et al., [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html), NeurIPS 2020.
- Nils Reimers et al. / Nils Thakur et al., [BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models](https://arxiv.org/abs/2104.08663), 2021.

Produktdokumentationen und Projekt-README-Dateien sind fortlaufend aktualisierte Quellen und beschreiben keine unabhängige Sicherheitsprüfung. Die hier genannten Werkzeuge sind Rechercheoptionen, keine endgültigen Abhängigkeiten.

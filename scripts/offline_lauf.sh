#!/bin/bash
# Offline-Lauf v20: wartet, bis keine Internetverbindung mehr besteht, startet dann den Antwortlauf mit dem lokalen Modell
# und protokolliert währenddessen alle Netzwerkverbindungen von Ollama und Python sowie die Erreichbarkeit des Internets.
# Aufruf im Projektordner: bash scripts/offline_lauf.sh gemma3:4b v20
MODELL=${1:-gemma3:4b}
VERSION=${2:-v20}
LOG=results/netzprotokoll_${VERSION}_$(date +%Y-%m-%d).txt
export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1

online() { curl -s -m 3 -o /dev/null https://openrouter.ai && return 0; ping -c 1 -t 2 1.1.1.1 >/dev/null 2>&1; }

echo "Offline-Lauf $VERSION mit $MODELL – Protokoll gestartet $(date '+%F %T')" > "$LOG"
echo "Warte auf getrennte Internetverbindung …" >> "$LOG"
until ! online; do sleep 5; done
echo "$(date '+%F %T') Internet nicht erreichbar – Lauf startet" >> "$LOG"

.venv/bin/python scripts/antwortlauf_aussagen.py --volltext --lokal "$MODELL" --version "$VERSION" --durchlaeufe 1 \
    > "results/lauf_${VERSION}.log" 2>&1 &
RUN=$!

# Während des Laufs alle 10 s: Erreichbarkeit des Internets und alle Verbindungen von Ollama/Python, die nicht lokal sind
while kill -0 $RUN 2>/dev/null; do
    if online; then echo "$(date '+%F %T') WARNUNG: Internet erreichbar" >> "$LOG"; fi
    PIDS=$(pgrep -d, -f "ollama|antwortlauf_aussagen.py")
    if [ -n "$PIDS" ]; then
        lsof -nP -a -p "$PIDS" -i 2>/dev/null | awk 'NR>1' | grep -v -E "127\.0\.0\.1|\[::1\]|localhost" \
            | sed "s/^/$(date '+%F %T') VERBINDUNG NACH AUSSEN: /" >> "$LOG"
    fi
    sleep 10
done
echo "$(date '+%F %T') Lauf beendet (Exit $(wait $RUN; echo $?))" >> "$LOG"
echo "Verbindungen nach außen insgesamt: $(grep -c 'VERBINDUNG NACH AUSSEN' "$LOG")" >> "$LOG"
echo "Internet zwischendurch erreichbar: $(grep -c 'WARNUNG: Internet' "$LOG") Mal" >> "$LOG"

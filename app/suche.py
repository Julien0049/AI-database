"""Suche über die Aussagen-Datenbank und Prüfung auf möglicherweise überholte Aussagen (Aufbau v16/v19).

- select(): Die besten Aussagen (Suche nach Bedeutung, e5-small) bestimmen, welche Berichte relevant sind;
  das Modell bekommt diese Berichte vollständig („Aussagen zum Finden, Berichte zum Antworten“, v16).
- outdated(): Programmprüfung ohne Sprachmodell (Messung 14.11.2026: alle 10 bekannten Fehler erkannt, 7 % Fehlalarme,
  Schwellen an denselben Daten abgestimmt). Ein Beleg wird der passenden Aussage zugeordnet; gibt es zum selben Thema
  im selben Kontext eine neuere, inhaltlich andere Regel aus einem anderen Bericht, wird gewarnt (nicht gelöscht).
Logik wie scripts/antwortlauf_aussagen.py und scripts/aktualitaet_pruefen.py; die Skripte bleiben als Versuchsstand.
"""
import re

EMBEDDING_MODEL = "intfloat/multilingual-e5-small"
N_AUSSAGEN = 40
KONTEXT_MIN, GLEICH_MAX = 0.90, 0.93
HISTORY = re.compile(r"veränder|geändert|früher|über die zeit|verlauf", re.I)


def words(text):
    return set(w for w in re.findall(r"[a-zäöüß0-9]+", text.lower()) if len(w) > 3)


class Index:
    def __init__(self, db, model):
        self.rows = [dict(r) for r in db.execute(
            "SELECT a.*, d.titel, d.datum, d.datum_iso FROM aussagen a JOIN dokumente d USING (datei) ORDER BY a.id")]
        self.model = model
        self.by_file = {}
        for i, r in enumerate(self.rows):
            self.by_file.setdefault(r["datei"], []).append(i)
        if self.rows:
            texts = [" – ".join(x for x in (r["thema"], r["kontext"], r["aussage"]) if x) for r in self.rows]
            self.vectors = model.encode([f"passage: {t}" for t in texts], normalize_embeddings=True)
            content = model.encode([f"passage: {r['thema']} – {r['aussage']}" for r in self.rows], normalize_embeddings=True)
            context = model.encode([f"passage: {r['kontext'] or 'allgemein'}" for r in self.rows], normalize_embeddings=True)
            self.sim, self.ksim = content @ content.T, context @ context.T

    def select(self, query, n=N_AUSSAGEN):
        """Dateinamen der Berichte, aus denen die n besten Aussagen stammen (in Rangfolge)."""
        if not self.rows:
            return []
        q = self.model.encode(f"query: {query}", normalize_embeddings=True)
        order = sorted(range(len(self.rows)), key=lambda j: -float(self.vectors[j] @ q))[:n]
        files = []
        for j in order:
            if self.rows[j]["datei"] not in files:
                files.append(self.rows[j]["datei"])
        return files

    def _source(self, datei, zitat):
        cand = self.by_file.get(datei, [])
        if not cand:
            return None
        z = words(zitat)
        return max(cand, key=lambda i: len(z & words(self.rows[i]["zitat"] + " " + self.rows[i]["aussage"])))

    def _newer(self, i):
        r = self.rows[i]
        if r["art"] not in ("regel", "unklar") or not r["datum_iso"]:
            return None
        best = None
        for j, s in enumerate(self.rows):
            if (s["datei"] == r["datei"] or s["art"] not in ("regel", "unklar") or not s["datum_iso"]
                    or s["datum_iso"] <= r["datum_iso"] or s["thema"] != r["thema"]):
                continue
            if self.ksim[i, j] >= KONTEXT_MIN and self.sim[i, j] < GLEICH_MAX:
                if best is None or s["datum_iso"] > self.rows[best]["datum_iso"]:
                    best = j
        return best

    def outdated(self, question, saetze, reports):
        """Warnungen zu Sätzen, deren Beleg möglicherweise überholt ist. Bei Fragen nach Änderungen keine Prüfung."""
        if HISTORY.search(question):
            return []
        warnings, seen = [], set()
        for s in saetze:
            for b in s.get("belege", []):
                rep = reports.get(b.get("bericht"))
                i = self._source(rep["datei"], b.get("zitat", "")) if rep else None
                j = self._newer(i) if i is not None else None
                if j is not None and (i, j) not in seen:
                    seen.add((i, j))
                    old, new = self.rows[i], self.rows[j]
                    warnings.append(f"„{s['text'].strip()}“ stützt sich auf „{old['titel']}“ ({old['datum']}). "
                                    f"Neuerer Stand zum Thema „{old['thema']}“: „{new['titel']}“ ({new['datum']}).")
        return warnings

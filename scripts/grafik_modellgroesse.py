"""Abbildung: Anteil unbrauchbarer Antworten nach Modellgröße (v19–v21), deutsch und englisch.

Werte aus scripts/regelbewertung.py (unbrauchbar = inhaltlich falsch oder keine verwertbare Antwort).
Gemini 2.5 Pro als waagrechte Bezugslinie, weil seine Größe nicht veröffentlicht ist.
  .venv/bin/python scripts/grafik_modellgroesse.py
"""
import json
import pathlib
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import regelbewertung as rb  # noqa: E402

RUNS = [  # (Datei, Parameter in Mrd., Name, Hardware DE, Hardware EN, lokal)
    ("lokal_gemma3-4b_2026-11-14_v20", 4, "Gemma 3 4B", "Laptop (8 GB)", "laptop (8 GB)", True),
    ("google_gemma-3-27b-it_2026-11-14_v21", 27, "Gemma 3 27B", "1 Grafikkarte 48 GB", "1 GPU, 48 GB", False),
    ("openai_gpt-oss-120b_2026-11-14_v21", 117, "gpt-oss-120b", "1 Grafikkarte 80–96 GB", "1 GPU, 80–96 GB", False),
    ("qwen_qwen3.5-397b-a17b_2026-11-14_v21", 403, "Qwen3.5-397B", "Server mit 8 Grafikkarten", "server with 8 GPUs", False),
]
GEMINI = "google_gemini-2.5-pro_2026-11-14_v19"

TEXT = {
    "de": {"title": "Vergleich offener KI-Modelle",
           "y": "Unbrauchbare Antworten (falsch oder ohne Antwort)", "x": "Modellgröße in Milliarden Parametern (logarithmisch)",
           "gemini": "Gemini 2.5 Pro (Cloud, Größe nicht veröffentlicht)", "local": "lokal, 1 Durchlauf",
           "note": "34 Testfragen, 58 fiktive Berichte. Jedes Modell 3 Durchläufe, nur Gemma 3 4B (lokal auf dem Laptop) 1 Durchlauf. Bewertung regelbasiert. Hardware: grobe Größenordnung für Eigenbetrieb."},
    "en": {"title": "Open AI model comparison",
           "y": "Unusable answers (wrong or no answer)", "x": "Model size in billions of parameters (log scale)",
           "gemini": "Gemini 2.5 Pro (cloud, size not disclosed)", "local": "local, 1 run",
           "note": "34 test questions, 58 fictional reports. Every model 3 runs, only Gemma 3 4B (local on the laptop) 1 run. Rule-based scoring. Hardware: rough order of magnitude for self-hosting."},
}
INK, INK2, SERIES, GRID, SURFACE = "#0b0b0b", "#52514e", "#2a78d6", "#e4e3df", "#fcfcfb"


def unusable(name):
    d = json.loads((ROOT / f"results/ergebnisse_{name}.json").read_text())
    rb.reparse(d)
    v = [rb.judge(e)[1] for e in d["ergebnisse"]]
    return 100 * sum(1 for w in v if w.startswith("verboten") or w == "keine Antwort") / len(v)


values = [(p, unusable(f), n, hde, hen, loc) for f, p, n, hde, hen, loc in RUNS]
gemini = unusable(GEMINI)
out = ROOT / "notes" / "abbildungen"
out.mkdir(parents=True, exist_ok=True)

for lang, t in TEXT.items():
    fig, ax = plt.subplots(figsize=(9, 5.4), dpi=200)
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)
    xs, ys = [v[0] for v in values], [v[1] for v in values]
    ax.plot(xs, ys, color=SERIES, linewidth=2, zorder=2)
    for p, y, name, hde, hen, loc in values:
        ax.scatter([p], [y], s=70, zorder=3, color=SURFACE if loc else SERIES, edgecolors=SERIES, linewidths=2)
        label = f"{name}\n{hde if lang == 'de' else hen}" + (f"\n({t['local']})" if loc else "")
        # Beschriftung oberhalb rechts des Punkts (die Linie fällt nach rechts, dort ist Platz)
        ax.annotate(f"{y:.0f} %", (p, y), xytext=(9, 7), textcoords="offset points", color=INK, fontsize=10,
                    fontweight="bold", va="bottom")
        ax.annotate(label, (p, y), xytext=(9, 22), textcoords="offset points", color=INK2, fontsize=8, va="bottom")
    ax.axhline(gemini, color=INK2, linestyle=(0, (4, 3)), linewidth=1.2, zorder=1)
    ax.annotate(f"{t['gemini']}: {gemini:.0f} %", (4.2, gemini), xytext=(0, 5), textcoords="offset points", color=INK2, fontsize=9)
    ax.set_xscale("log")
    ax.set_xlim(3, 1000)
    ax.set_ylim(0, 80)
    ax.set_xticks([4, 10, 27, 50, 117, 403])
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}"))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0f} %"))
    ax.set_xlabel(t["x"], color=INK2, fontsize=9)
    ax.set_ylabel(t["y"], color=INK2, fontsize=9)
    ax.set_title(t["title"], color=INK, fontsize=13, fontweight="bold", loc="left", pad=12)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.tick_params(colors=INK2, labelsize=8)
    import textwrap
    fig.text(0.01, 0.01, textwrap.fill(t["note"], 150), color=INK2, fontsize=7, va="bottom")
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    path = out / f"modellgroesse_fehler_{lang}.png"
    fig.savefig(path, facecolor=SURFACE)
    print(path)

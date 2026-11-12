"""TREC-format evaluation, following course tutorial 06 (qrels + run files, MAP, P@10, P-R curves).

Usage:
    python src/trec.py

Reads   eval/qrels.csv            manual judgments (relevance_0_2) for the pooled top 10 of each setup
        eval/runs/s0_vs_s1.csv    the ranked lists produced by src/compare.py (needs no running Solr)
Writes  eval/trec/qrels_trec.txt  `topic 0 docid relevance`   (graded 0/1/2, TREC format)
        eval/trec/run_S0.txt ...  `topic Q0 docid rank score runid`
        eval/trec/trec_results.csv / .md   per-need and mean measures
        report/figures/s0_vs_s1_pr_curves.png   11-point interpolated precision-recall curves

Relevance is binary for MAP, P@N, recall and the P-R curve (relevant = 2, i.e. `yes`; `kinda` counts as
not relevant, same as strict P@10 in src/evaluate.py) and graded for nDCG. The same files work with the
official tool:  trec_eval -q -m all_trec -l 2 eval/trec/qrels_trec.txt eval/trec/run_S0.txt

Recall is pooled: relevant = judged relevant among the top 10 of S0 and S1 together, so recall figures
only compare these setups with each other. Needs pytrec_eval (pip install pytrec_eval-terrier).
"""
from pathlib import Path

import pandas as pd
import pytrec_eval

ROOT = Path(__file__).resolve().parent.parent
QRELS = ROOT / "eval" / "qrels.csv"
RUNS = ROOT / "eval" / "runs" / "s0_vs_s1.csv"
OUT = ROOT / "eval" / "trec"
FIGURE = ROOT / "report" / "figures" / "s0_vs_s1_pr_curves.png"
REL_LEVEL = 2  # binary measures treat relevance 2 as relevant
MEASURES = {"map", "P_5", "P_10", "recall_10", "recip_rank", "ndcg_cut_10", "iprec_at_recall"}
SHOW = ["map", "P_5", "P_10", "recall_10", "recip_rank", "ndcg_cut_10"]
RECALL_POINTS = [round(i / 10, 1) for i in range(11)]


def export(qrels, runs):
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / "qrels_trec.txt", "w", encoding="utf-8") as f:
        for r in qrels.drop_duplicates(["topic", "hudoc_id"]).sort_values(["topic", "hudoc_id"]).itertuples():
            f.write(f"{r.topic} 0 {r.hudoc_id} {int(r.relevance_0_2)}\n")
    for setup, group in runs.groupby("setup"):
        with open(OUT / f"run_{setup}.txt", "w", encoding="utf-8") as f:
            for r in group.sort_values(["need_id", "rank"]).itertuples():
                f.write(f"{r.need_id} Q0 {r.case_id} {r.rank} {r.score} {setup}\n")


def load(qrels, runs):
    q, r = {}, {}
    for row in qrels.drop_duplicates(["topic", "hudoc_id"]).itertuples():
        q.setdefault(row.topic, {})[row.hudoc_id] = int(row.relevance_0_2)
    for row in runs.itertuples():
        r.setdefault(row.setup, {}).setdefault(row.need_id, {})[row.case_id] = float(row.score)
    return q, r


def main():
    qrels = pd.read_csv(QRELS, encoding="utf-8")
    runs = pd.read_csv(RUNS, encoding="utf-8")
    export(qrels, runs)
    q, r = load(qrels, runs)

    evaluator = pytrec_eval.RelevanceEvaluator(q, MEASURES, relevance_level=REL_LEVEL)
    rows, curves = [], {}
    for setup, run in sorted(r.items()):
        for need, m in evaluator.evaluate(run).items():
            rows.append({"need": need, "setup": setup, **{k: m[k] for k in SHOW}})
            curves[(setup, need)] = [m[f"iprec_at_recall_{p:.2f}"] for p in RECALL_POINTS]
    df = pd.DataFrame(rows)
    mean = df.groupby("setup")[SHOW].mean().reset_index()
    mean.insert(0, "need", "MEAN")
    df = pd.concat([df.sort_values(["need", "setup"]), mean], ignore_index=True)
    df.round(4).to_csv(OUT / "trec_results.csv", index=False)

    wide = df.pivot(index="need", columns="setup", values=SHOW)
    needs = [n for n in sorted(wide.index) if n != "MEAN"] + ["MEAN"]
    label = {"map": "MAP/AP", "P_5": "P@5", "P_10": "P@10", "recall_10": "R@10 (pooled)",
             "recip_rank": "RR", "ndcg_cut_10": "nDCG@10"}
    lines = ["# S0 vs S1 - TREC-style evaluation", "",
             "Produced by `python src/trec.py` (pytrec_eval, relevant = judged 2). Recall is pooled.", "",
             "| Need | " + " | ".join(f"{label[m]} S0 | {label[m]} S1" for m in SHOW) + " |",
             "|---|" + "---:|" * (2 * len(SHOW))]
    for n in needs:
        lines.append(f"| {n} | " + " | ".join(f"{wide.loc[n, (m, s)]:.2f}" for m in SHOW for s in ("S0", "S1")) + " |")
    (OUT / "trec_results.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    plot(curves, sorted({n for _, n in curves}))
    print("\n".join(lines))
    print(f"\nWrote {OUT.relative_to(ROOT)}/ (qrels_trec.txt, run_*.txt, trec_results.*) and {FIGURE.name}")


def plot(curves, needs):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    fig, axes = plt.subplots(1, 3, figsize=(14, 4), sharey=True)
    for ax, setup in zip(axes[:2], ("S0", "S1")):
        for n in needs:
            ax.plot(RECALL_POINTS, curves[(setup, n)], drawstyle="steps-post", label=n, linewidth=1.6)
        ax.set_title(f"{setup}: per need")
        ax.legend(fontsize=8, loc="lower left", ncol=2)
    for setup, color in (("S0", "#9aa5b1"), ("S1", "#1f6feb")):
        mean = np.mean([curves[(setup, n)] for n in needs], axis=0)
        axes[2].plot(RECALL_POINTS, mean, drawstyle="steps-post", label=f"{setup} (11-pt avg {mean.mean():.2f})",
                     color=color, linewidth=2.2)
    axes[2].set_title("Mean over 7 needs")
    axes[2].legend(fontsize=9, loc="lower left")
    for ax in axes:
        ax.set_xlabel("Recall (pooled)")
        ax.set_xlim(-0.005, 1.005)
        ax.set_ylim(-0.005, 1.05)
        ax.grid(True, linestyle="--", linewidth=0.5)
    axes[0].set_ylabel("Interpolated precision")
    fig.suptitle("11-point interpolated precision-recall curves (top 10 per setup)", y=1.02)
    fig.tight_layout()
    FIGURE.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURE, dpi=160, bbox_inches="tight")


if __name__ == "__main__":
    main()

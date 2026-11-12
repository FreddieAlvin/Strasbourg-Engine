"""Compute retrieval metrics from the manual relevance judgments (eval/qrels.csv).

Usage:
    python src/evaluate.py

Reads   eval/qrels.csv      one row per judged (need, setup, rank): relevance_0_2 in {0,1,2}
Writes  eval/results.csv    metrics per need and setup, plus the macro average
        eval/results.md     the same as a markdown table
        eval/to_verify.csv  judgments to re-check by hand (medium confidence, partial or negative)
        report/figures/s0_vs_s1_metrics.png

Metrics (all @10, over the judged top-10 of each setup):
    P@5, P@10   strict precision: only relevance 2 counts as relevant
    graded@10   mean relevance / 2  (kinda = half credit); NOT nDCG
    nDCG@10     gain = relevance_0_2, log2 discount, ideal ranking built from the pool
                of every case judged for that need (S0 and S1 together)
    AP@10       average precision (strict), normalised by the number of relevant cases
                in the pool, so it is a pooled estimate: recall is not measurable
                because only the top 10 of each setup was judged.
"""
import math
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
QRELS = ROOT / "eval" / "qrels.csv"
OUT_CSV = ROOT / "eval" / "results.csv"
OUT_MD = ROOT / "eval" / "results.md"
OUT_VERIFY = ROOT / "eval" / "to_verify.csv"
FIGURE = ROOT / "report" / "figures" / "s0_vs_s1_metrics.png"
K = 10
TOL = 0.05  # nDCG difference below this is treated as a tie in the summary line


def dcg(gains):
    return sum(g / math.log2(i + 2) for i, g in enumerate(gains))


def metrics(run, pool_gains):
    """run: relevance scores in rank order; pool_gains: gain of every distinct judged case of the need."""
    run = list(run)[:K]
    strict = [1 if g == 2 else 0 for g in run]
    n_rel_pool = sum(1 for g in pool_gains if g == 2)
    hits, ap_sum = 0, 0.0
    for i, rel in enumerate(strict, 1):
        if rel:
            hits += 1
            ap_sum += hits / i
    ideal = dcg(sorted(pool_gains, reverse=True)[:K])
    return {
        "P@5": sum(strict[:5]) / 5,
        "P@10": sum(strict) / K,
        "graded@10": sum(run) / (2 * K),
        "nDCG@10": dcg(run) / ideal if ideal else 0.0,
        "AP@10": ap_sum / n_rel_pool if n_rel_pool else 0.0,
    }


def evaluate(qrels):
    rows = []
    for need, group in qrels.groupby("topic"):
        pool = group.drop_duplicates("hudoc_id")["relevance_0_2"].tolist()
        for setup, run in group.sort_values("rank").groupby("system"):
            rows.append({"need": need, "setup": setup, **metrics(run["relevance_0_2"], pool),
                         "yes": int((run["relevance_0_2"] == 2).sum()),
                         "kinda": int((run["relevance_0_2"] == 1).sum()),
                         "no": int((run["relevance_0_2"] == 0).sum())})
    df = pd.DataFrame(rows)
    cols = ["P@5", "P@10", "graded@10", "nDCG@10", "AP@10"]
    macro = df.groupby("setup")[cols + ["yes", "kinda", "no"]].mean().reset_index()
    macro.insert(0, "need", "MACRO")
    return pd.concat([df, macro], ignore_index=True), cols


def to_markdown(df, cols):
    wide = df.pivot(index="need", columns="setup", values=cols)
    needs = [n for n in sorted(wide.index) if n != "MACRO"] + ["MACRO"]
    lines = ["| Need | " + " | ".join(f"{m} S0 | {m} S1" for m in cols) + " |",
             "|---|" + "---:|" * (2 * len(cols))]
    for need in needs:
        cells = []
        for m in cols:
            cells += [f"{wide.loc[need, (m, 'S0')]:.2f}", f"{wide.loc[need, (m, 'S1')]:.2f}"]
        lines.append(f"| {need} | " + " | ".join(cells) + " |")
    return "\n".join(lines)


def paired_summary(df):
    wide = df[df.need != "MACRO"].pivot(index="need", columns="setup", values="nDCG@10")
    diff = wide["S1"] - wide["S0"]
    return (f"nDCG@10, S1 minus S0, per need: "
            + ", ".join(f"{n} {v:+.2f}" for n, v in diff.items())
            + f".  S1 clearly better (> {TOL}) on {(diff > TOL).sum()}, about equal on {(diff.abs() <= TOL).sum()}, "
              f"S0 clearly better on {(diff < -TOL).sum()} of {len(diff)} needs.")


def plot(df, cols):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    d = df[df.need != "MACRO"].pivot(index="need", columns="setup", values="P@10")
    n = df[df.need != "MACRO"].pivot(index="need", columns="setup", values="nDCG@10")
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.8), sharey=True)
    for ax, data, title in ((axes[0], d, "Strict P@10"), (axes[1], n, "nDCG@10")):
        data.plot.bar(ax=ax, width=0.75, color=["#9aa5b1", "#1f6feb"], rot=0)
        ax.set_title(title)
        ax.set_xlabel("")
        ax.set_ylim(0, 1.05)
        ax.legend(title="setup", loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=2, frameon=False)
        ax.grid(axis="y", alpha=0.3)
    fig.suptitle("S0 (lowercase only) vs S1 (English analysis), 7 information needs", y=1.02)
    fig.tight_layout()
    FIGURE.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURE, dpi=160, bbox_inches="tight")


def main():
    qrels = pd.read_csv(QRELS, encoding="utf-8")
    missing = qrels["relevance_0_2"].isna().sum()
    if missing:
        raise SystemExit(f"{missing} rows in {QRELS.name} have no relevance_0_2 - judge them first")
    df, cols = evaluate(qrels)
    df.round(4).to_csv(OUT_CSV, index=False)

    md = ["# S0 vs S1 - retrieval metrics", "",
          "Computed by `python src/evaluate.py` from `eval/qrels.csv` (top-10 per setup, 7 needs).", "",
          to_markdown(df, cols), "", paired_summary(df), "",
          "AP@10 is normalised by the relevant cases found by *either* setup (pooled), so it is a",
          "relative figure; true recall is unknown because only the top 10 of each setup was judged."]
    OUT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")

    verify = qrels[(qrels.confidence != "high") | (qrels.relevance_0_2 < 2)]
    verify.sort_values(["topic", "system", "rank"]).to_csv(OUT_VERIFY, index=False)

    plot(df, cols)
    print("\n".join(md))
    print(f"\nWrote {OUT_CSV.name}, {OUT_MD.name}, {OUT_VERIFY.name} ({len(verify)} judgments to re-check), {FIGURE.name}")


if __name__ == "__main__":
    main()

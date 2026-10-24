"""Run every information need with S0 and S1 and write a review file.

Usage:
    python src/compare.py
    python src/compare.py --rows 10 --out eval/runs/s0_vs_s1.md

Requires Solr to be running with the cases core already indexed.
"""
import argparse
import csv
import json
from pathlib import Path

from search import SETUPS, search, snippet_for

ROOT = Path(__file__).resolve().parent.parent
NEEDS_FILE = ROOT / "eval" / "needs.json"
DEFAULT_OUT = ROOT / "eval" / "runs" / "s0_vs_s1.md"
SETUPS_TO_COMPARE = ("S0", "S1")


def load_needs():
    with open(NEEDS_FILE, encoding="utf-8") as f:
        return json.load(f)["needs"]


def ranks(docs):
    return {doc["id"]: i for i, doc in enumerate(docs, 1)}


def run_need(need, rows):
    fq = [need["filter"]] if need.get("filter") else None
    by_setup = {}
    for setup in SETUPS_TO_COMPARE:
        result = search(need["query"], setup, rows, fq, highlight=True)
        by_setup[setup] = {
            "numFound": result["response"]["numFound"],
            "docs": result["response"]["docs"],
            "highlighting": result.get("highlighting", {}),
        }
    ids = {s: [d["id"] for d in by_setup[s]["docs"]] for s in SETUPS_TO_COMPARE}
    overlap = set(ids["S0"]) & set(ids["S1"])
    union = set(ids["S0"]) | set(ids["S1"])
    return {
        "need": need,
        "by_setup": by_setup,
        "overlap": overlap,
        "only_s0": set(ids["S0"]) - set(ids["S1"]),
        "only_s1": set(ids["S1"]) - set(ids["S0"]),
        "jaccard": (len(overlap) / len(union)) if union else 0.0,
    }


def fmt_doc_line(rank, doc, highlighting):
    articles = ",".join(doc.get("alleged_articles", [])) or "-"
    defendants = ", ".join(doc.get("defendants", [])) or "-"
    snippet = snippet_for(doc["id"], highlighting)
    lines = [
        f"{rank}. **{doc['id']}**  score {doc['score']:.2f}  \n"
        f"   {doc['title']} ({doc['year']})  |  {defendants}  |  art. {articles}  \n"
        f"   match? yes / kinda / no"
    ]
    if snippet:
        lines.append(f"   snippet: {snippet}")
    return "\n".join(lines)


def write_markdown(comparisons, path):
    parts = [
        "# S0 vs S1 — review sheet",
        "",
        "S0 = simple search (lowercase only).  S1 = English search (stemming + stopwords).",
        "Same query and same filter for both. Mark each result: **yes** / **kinda** / **no**.",
        "Then pick **one topic where S1 is better** and **one where S0 is better**.",
        "",
        "## Overlap (top 10)",
        "",
        "| Need | Topic | S0 hits | S1 hits | Shared in top 10 | Only S0 | Only S1 | Jaccard |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for cmp in comparisons:
        n = cmp["need"]
        parts.append(
            f"| {n['id']} | {n['title']} | {cmp['by_setup']['S0']['numFound']} | "
            f"{cmp['by_setup']['S1']['numFound']} | {len(cmp['overlap'])} | "
            f"{len(cmp['only_s0'])} | {len(cmp['only_s1'])} | {cmp['jaccard']:.2f} |"
        )
    parts += ["", "---", ""]

    for cmp in comparisons:
        n = cmp["need"]
        parts += [
            f"## {n['id']} — {n['title']}",
            "",
            f"- type: `{n['type']}`",
            f"- query: `{n['query']}`",
            f"- filter: `{n['filter']}`" if n.get("filter") else "- filter: none",
            f"- look for: {n['description']}",
            f"- relevant if: {n['narrative']}",
            f"- overlap: {len(cmp['overlap'])}/10 shared"
            + (f" (`{'`, `'.join(sorted(cmp['overlap']))}`)" if cmp["overlap"] else ""),
            "",
        ]
        for setup in SETUPS_TO_COMPARE:
            run = cmp["by_setup"][setup]
            parts.append(f"### {setup} — {SETUPS[setup]['label']}  ({run['numFound']} matching cases)")
            parts.append("")
            if not run["docs"]:
                parts.append("_no hits_")
            for rank, doc in enumerate(run["docs"], 1):
                extra = ""
                other = "S1" if setup == "S0" else "S0"
                other_ranks = ranks(cmp["by_setup"][other]["docs"])
                if doc["id"] in other_ranks:
                    extra = f"  (also {other} #{other_ranks[doc['id']]})"
                else:
                    extra = f"  (**only in {setup}**)"
                line = fmt_doc_line(rank, doc, run["highlighting"])
                parts.append(line + extra)
                parts.append("")
            parts.append("")
        parts.append("---")
        parts.append("")

    parts += [
        "## Your notes",
        "",
        "- Example where **S1 is better**:",
        "- Example where **S0 is better**:",
        "- Does IN5's country filter look correct?",
        "- Anything else:",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(parts), encoding="utf-8")


def write_csv(comparisons, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "need_id", "need_title", "setup", "rank", "case_id", "score",
                "title", "year", "defendants", "alleged_articles", "in_other_top10",
                "snippet", "match",
            ],
        )
        writer.writeheader()
        for cmp in comparisons:
            n = cmp["need"]
            for setup in SETUPS_TO_COMPARE:
                other = "S1" if setup == "S0" else "S0"
                other_ids = {d["id"] for d in cmp["by_setup"][other]["docs"]}
                run = cmp["by_setup"][setup]
                for rank, doc in enumerate(run["docs"], 1):
                    writer.writerow({
                        "need_id": n["id"],
                        "need_title": n["title"],
                        "setup": setup,
                        "rank": rank,
                        "case_id": doc["id"],
                        "score": f"{doc['score']:.4f}",
                        "title": doc["title"],
                        "year": doc.get("year", ""),
                        "defendants": "; ".join(doc.get("defendants", [])),
                        "alleged_articles": "; ".join(doc.get("alleged_articles", [])),
                        "in_other_top10": "yes" if doc["id"] in other_ids else "no",
                        "snippet": snippet_for(doc["id"], run["highlighting"]),
                        "match": "",
                    })


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", type=int, default=10)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    comparisons = [run_need(need, args.rows) for need in load_needs()]
    write_markdown(comparisons, args.out)
    csv_path = args.out.with_suffix(".csv")
    write_csv(comparisons, csv_path)

    print(f"Wrote {args.out.relative_to(ROOT)}")
    print(f"Wrote {csv_path.relative_to(ROOT)}")
    print()
    print(f"{'need':<6} {'shared':>6} {'only S0':>8} {'only S1':>8}  title")
    for cmp in comparisons:
        n = cmp["need"]
        print(f"{n['id']:<6} {len(cmp['overlap']):>6} {len(cmp['only_s0']):>8} {len(cmp['only_s1']):>8}  {n['title']}")


if __name__ == "__main__":
    main()

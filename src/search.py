"""Run a free-text query against the cases core with a named retrieval setup.

Usage:
    python src/search.py "overcrowded cell detention"
    python src/search.py "overcrowded cell detention" --setup S0 --rows 5 --fq "defendants:RUSSIA"

New setups (S1, S2, ...) are added to SETUPS; every setup is run with the same
query string, so results stay comparable across setups.
"""
import argparse
import re

import requests

SOLR = "http://localhost:8983/solr"

SETUPS = {
    # S0 - baseline: standard tokenizer + lowercase, BM25, no boosts.
    "S0": {
        "core": "cases",
        "params": {
            "defType": "edismax",
            "qf": "facts title",
        },
    },
}


def search(query, setup="S0", rows=10, fq=None, highlight=False):
    cfg = SETUPS[setup]
    params = {
        "q": query,
        "rows": rows,
        "fl": "id,title,year,defendants,alleged_articles,score",
        **cfg["params"],
    }
    if fq:
        params["fq"] = fq
    if highlight:
        params.update({"hl": "true", "hl.fl": "facts", "hl.snippets": 1, "hl.fragsize": 220,
                       "hl.tag.pre": "[", "hl.tag.post": "]"})
    response = requests.get(f"{SOLR}/{cfg['core']}/select", params=params)
    response.raise_for_status()
    return response.json()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--setup", default="S0", choices=list(SETUPS))
    parser.add_argument("--rows", type=int, default=10)
    parser.add_argument("--fq", action="append", help="filter query, e.g. defendants:RUSSIA (repeatable)")
    args = parser.parse_args()

    result = search(args.query, args.setup, args.rows, args.fq, highlight=True)
    print(f"{result['response']['numFound']} matching cases  [setup {args.setup}]\n")
    snippets = result.get("highlighting", {})
    for rank, doc in enumerate(result["response"]["docs"], 1):
        print(f"{rank:2}. {doc['score']:6.2f}  {doc['id']}  {doc['title']} ({doc['year']})  "
              f"art. {','.join(doc.get('alleged_articles', [])) or '-'}")
        snippet = snippets.get(doc["id"], {}).get("facts", [""])[0]
        if snippet:
            print("        " + re.sub(r"\s+", " ", snippet))


if __name__ == "__main__":
    main()

"""Run a free-text query against the cases core with a named retrieval setup.

Usage:
    python src/search.py "overcrowded cell detention"
    python src/search.py "overcrowded cell detention" --setup S1 --rows 5 --fq "defendants:RUSSIA"

Every setup is run with the same query string, so results stay comparable.
"""
import argparse
import re

import requests

SOLR = "http://localhost:8983/solr"

SETUPS = {
    # S0 - baseline: standard tokenizer + lowercase, BM25, no boosts.
    "S0": {
        "core": "cases",
        "label": "simple (lowercase only)",
        "params": {
            "defType": "edismax",
            "qf": "facts title",
        },
        "hl.fl": "facts",
    },
    # S1 - English analysis already indexed on copy-fields (stopwords + Porter stem).
    "S1": {
        "core": "cases",
        "label": "English (stemming + stopwords)",
        "params": {
            "defType": "edismax",
            "qf": "facts_en title_en",
        },
        "hl.fl": "facts_en",
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
        params.update({"hl": "true", "hl.fl": cfg["hl.fl"], "hl.snippets": 1, "hl.fragsize": 220,
                       "hl.tag.pre": "[", "hl.tag.post": "]"})
    response = requests.get(f"{SOLR}/{cfg['core']}/select", params=params)
    response.raise_for_status()
    return response.json()


def snippet_for(doc_id, highlighting):
    """Return the first highlight fragment, whichever field Solr filled in."""
    fields = highlighting.get(doc_id, {})
    for fragments in fields.values():
        if fragments:
            return re.sub(r"\s+", " ", fragments[0])
    return ""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--setup", default="S0", choices=list(SETUPS))
    parser.add_argument("--rows", type=int, default=10)
    parser.add_argument("--fq", action="append", help="filter query, e.g. defendants:RUSSIA (repeatable)")
    args = parser.parse_args()

    result = search(args.query, args.setup, args.rows, args.fq, highlight=True)
    print(f"{result['response']['numFound']} matching cases  [setup {args.setup}]\n")
    highlighting = result.get("highlighting", {})
    for rank, doc in enumerate(result["response"]["docs"], 1):
        print(f"{rank:2}. {doc['score']:6.2f}  {doc['id']}  {doc['title']} ({doc['year']})  "
              f"art. {','.join(doc.get('alleged_articles', [])) or '-'}")
        snippet = snippet_for(doc["id"], highlighting)
        if snippet:
            print("        " + snippet)


if __name__ == "__main__":
    main()

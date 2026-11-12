"""Create the Solr cores' schema and index the prepared documents.

Each run rebuilds the core from scratch (as in the Solr tutorial), so results are
reproducible: drop core -> copy default config -> recreate -> post schema -> post docs.

Usage:
    python src/index.py                 # both cores, with our schema
    python src/index.py cases           # only the cases core
    python src/index.py cases --schemaless   # let Solr guess field types (smoke test)

Requires the Solr container from docker-compose.yml to be running.
"""
import argparse
import json
import subprocess
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
PROCESSED = ROOT / "data" / "processed"
SOLR = "http://localhost:8983/solr"
CONTAINER = "strasbourg_solr"
DEFAULT_CONF = "/opt/solr/server/solr/configsets/_default/conf"

CORES = {
    "cases":      {"docs": PROCESSED / "cases.jsonl",    "schema": ROOT / "solr" / "schema_cases.json",    "batch": 500},
    "paragraphs": {"docs": PROCESSED / "paragraphs.jsonl", "schema": ROOT / "solr" / "schema_paragraphs.json", "batch": 5000},
}


def check(response):
    if response.status_code != 200:
        raise SystemExit(f"Solr error {response.status_code}: {response.text[:1000]}")
    return response.json()


def reset_core(core):
    """Drop the core and recreate it empty from Solr's _default config."""
    requests.get(f"{SOLR}/admin/cores", params={"action": "UNLOAD", "core": core, "deleteInstanceDir": "true"})
    subprocess.run(
        ["docker", "exec", CONTAINER, "bash", "-c",
         f"rm -rf /var/solr/data/{core} && mkdir -p /var/solr/data/{core} && cp -r {DEFAULT_CONF} /var/solr/data/{core}/conf"],
        check=True,
    )
    check(requests.get(f"{SOLR}/admin/cores", params={"action": "CREATE", "name": core, "instanceDir": core}))


def apply_schema(core, schema_file):
    # Reject fields that are not in our schema instead of guessing their type.
    check(requests.post(f"{SOLR}/{core}/config", json={"set-user-property": {"update.autoCreateFields": "false"}}))
    with open(schema_file, encoding="utf-8") as f:
        check(requests.post(f"{SOLR}/{core}/schema", json=json.load(f)))


def post_documents(core, docs_file, batch_size):
    session = requests.Session()
    batch, total, start = [], 0, time.time()

    def flush():
        nonlocal batch, total
        check(session.post(f"{SOLR}/{core}/update", json=batch))
        total += len(batch)
        batch = []
        print(f"\r  {core}: {total} docs indexed", end="", flush=True)

    with open(docs_file, encoding="utf-8") as f:
        for line in f:
            batch.append(json.loads(line))
            if len(batch) >= batch_size:
                flush()
    if batch:
        flush()
    check(session.get(f"{SOLR}/{core}/update", params={"commit": "true"}))
    print(f"  ({time.time() - start:.0f}s)")


def main():
    parser = argparse.ArgumentParser()
    # No `choices=` here: on Python <= 3.11, nargs="*" + choices rejects the empty default
    # ("invalid choice: []") and `python src/index.py` / `make index` would fail. Validate by hand.
    parser.add_argument("cores", nargs="*", help=f"any of {', '.join(CORES)}; default: all cores")
    parser.add_argument("--schemaless", action="store_true", help="skip our schema; Solr guesses field types")
    args = parser.parse_args()
    unknown = [c for c in args.cores if c not in CORES]
    if unknown:
        parser.error(f"unknown core(s) {unknown}; choose from {list(CORES)}")

    for core in args.cores or list(CORES):
        cfg = CORES[core]
        if not cfg["docs"].exists():
            raise SystemExit(f"{cfg['docs']} not found - run `python src/prepare.py` first")
        print(f"[{core}] resetting core")
        reset_core(core)
        if not args.schemaless:
            print(f"[{core}] applying {cfg['schema'].name}")
            apply_schema(core, cfg["schema"])
        print(f"[{core}] indexing")
        post_documents(core, cfg["docs"], cfg["batch"])
        num_docs = check(requests.get(f"{SOLR}/{core}/select", params={"q": "*:*", "rows": 0}))["response"]["numFound"]
        print(f"[{core}] numDocs = {num_docs}")


if __name__ == "__main__":
    main()

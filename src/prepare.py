"""Build the Solr-ready collection from the raw ECtHR-NAACL2021 splits.

Input:  data/{train,dev,test}.jsonl        (raw dataset, one case per line)
Output: data/processed/cases.jsonl         one object per case            -> Solr core "cases"
        data/processed/paragraphs.jsonl    one object per fact paragraph  -> Solr core "paragraphs"

Usage:  python src/prepare.py
"""

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data"
OUT_DIR = ROOT / "data" / "processed"
SPLITS = ["train", "dev", "test"]
INTRO_PARAGRAPHS = 3  # first paragraphs of the facts: applicant and background

# Article titles from the European Convention on Human Rights and its Protocols.
# "P1-1" = Protocol No. 1, Article 1. Source: https://www.echr.coe.int/documents/d/echr/convention_ENG
# Codes present in the data but not listed here get no name (reported by report()):
#   "P3-1" - Protocol 3 has no substantive article 1; most likely a mislabelled "P1-3".
#   "X"    - unknown label in the source data.
ARTICLE_NAMES = {
    "1": "Obligation to respect human rights",
    "2": "Right to life",
    "3": "Prohibition of torture",
    "4": "Prohibition of slavery and forced labour",
    "5": "Right to liberty and security",
    "6": "Right to a fair trial",
    "7": "No punishment without law",
    "8": "Right to respect for private and family life",
    "9": "Freedom of thought, conscience and religion",
    "10": "Freedom of expression",
    "11": "Freedom of assembly and association",
    "12": "Right to marry",
    "13": "Right to an effective remedy",
    "14": "Prohibition of discrimination",
    "15": "Derogation in time of emergency",
    "17": "Prohibition of abuse of rights",
    "18": "Limitation on use of restrictions on rights",
    "34": "Individual applications",
    "37": "Striking out applications",
    "38": "Examination of the case",
    "39": "Friendly settlements",
    "41": "Just satisfaction",
    "46": "Binding force and execution of judgments",
    "P1-1": "Protection of property",
    "P1-2": "Right to education",
    "P1-3": "Right to free elections",
    "P4-2": "Freedom of movement",
    "P4-4": "Prohibition of collective expulsion of aliens",
    "P6-1": "Abolition of the death penalty",
    "P6-3": "Prohibition of derogations",
    "P7-1": "Procedural safeguards relating to expulsion of aliens",
    "P7-2": "Right of appeal in criminal matters",
    "P7-3": "Compensation for wrongful conviction",
    "P7-4": "Right not to be tried or punished twice",
    "P7-5": "Equality between spouses",
    "P12-1": "General prohibition of discrimination",
}

PARAGRAPH_NUMBER = re.compile(r"^\s*(\d+)\.\s+")
WHITESPACE = re.compile(r"\s+")  # also matches non-breaking and thin spaces
# Hyphen look-alikes. The soft hyphen is invisible but splits words in Solr ("detain\xadees").
CHAR_MAP = str.maketrans({"‑": "-", "‐": "-", "­": ""})


def clean_paragraph(text):
    """Split '11.  K. had a daughter...' into (11, 'K. had a daughter...') and normalise characters."""
    text = text.translate(CHAR_MAP)
    match = PARAGRAPH_NUMBER.match(text)
    number = int(match.group(1)) if match else None
    body = text[match.end():] if match else text
    return number, WHITESPACE.sub(" ", body).strip()


def article_names(codes):
    return [ARTICLE_NAMES[c] for c in codes if c in ARTICLE_NAMES]


def load_raw():
    for split in SPLITS:
        with open(RAW_DIR / f"{split}.jsonl", encoding="utf-8") as f:
            for line in f:
                case = json.loads(line)
                case["split"] = split
                yield case


def build_case(raw):
    numbers, facts = zip(*(clean_paragraph(p) for p in raw["facts"]))
    facts = list(facts)
    alleged = sorted(set(raw["allegedly_violated_articles"]))
    violated = sorted(set(raw["violated_articles"]))
    silver = sorted(i for i in set(raw["silver_rationales"]) if 0 <= i < len(facts))
    gold = sorted(i for i in set(raw["gold_rationales"]) if 0 <= i < len(facts))

    return {
        "id": raw["case_id"],
        "case_no": raw["case_no"],
        "title": raw["title"].strip(),
        "judgment_date": f"{raw['judgment_date']}T00:00:00Z",
        "year": int(raw["judgment_date"][:4]),
        "split": raw["split"],
        "applicants": raw["applicants"],
        "defendants": raw["defendants"],
        "alleged_articles": alleged,
        "violated_articles": violated,
        "alleged_article_names": article_names(alleged),
        "violated_article_names": article_names(violated),
        "outcome": "violation" if violated else "no violation",
        "facts": facts,
        "facts_intro": facts[:INTRO_PARAGRAPHS],
        "rationale_text": [facts[i] for i in silver],
        "silver_rationales": silver,
        "gold_rationales": gold,
        "para_numbers": list(numbers),  # original numbering; court_assessment_references cite these
        "n_paragraphs": len(facts),
        "n_words": sum(len(p.split()) for p in facts),
    }


def build_paragraphs(case):
    silver = set(case["silver_rationales"])
    for i, text in enumerate(case["facts"]):
        yield {
            "id": f"{case['id']}_p{i}",
            "case_id": case["id"],
            "title": case["title"],
            "position": i,
            "para_no": case["para_numbers"][i],
            "text": text,
            "is_rationale": i in silver,
            "year": case["year"],
            "defendants": case["defendants"],
            "alleged_articles": case["alleged_articles"],
            "violated_articles": case["violated_articles"],
            "outcome": case["outcome"],
        }


def write_jsonl(items, path):
    """One JSON object per line, so index.py can post the file to Solr in batches."""
    count = 0
    with open(path, "w", encoding="utf-8") as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
            count += 1
    print(f"Wrote {count:>7} documents -> {path.relative_to(ROOT)} ({path.stat().st_size / 1e6:.1f} MB)")


def report(cases):
    ids = Counter(c["id"] for c in cases)
    assert all(n == 1 for n in ids.values()), "duplicate case ids"
    unknown = Counter(a for c in cases for a in c["alleged_articles"] + c["violated_articles"]
                      if a not in ARTICLE_NAMES)
    print(f"Cases per split: {dict(Counter(c['split'] for c in cases))}")
    print(f"Outcomes:        {dict(Counter(c['outcome'] for c in cases))}")
    print(f"Paragraphs:      {sum(c['n_paragraphs'] for c in cases)} "
          f"({sum(n is None for c in cases for n in c['para_numbers'])} without an original number)")
    print(f"With rationales: {sum(bool(c['silver_rationales']) for c in cases)} silver, "
          f"{sum(bool(c['gold_rationales']) for c in cases)} gold")
    print(f"Unknown article codes (no name): {dict(unknown)}")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    cases = [build_case(raw) for raw in load_raw()]
    report(cases)
    write_jsonl(cases, OUT_DIR / "cases.jsonl")
    write_jsonl((p for case in cases for p in build_paragraphs(case)), OUT_DIR / "paragraphs.jsonl")


if __name__ == "__main__":
    main()

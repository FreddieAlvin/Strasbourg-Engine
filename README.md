# Strasbourg Engine

Search system over European Court of Human Rights judgments
([ECtHR-NAACL2021](https://www.kaggle.com/datasets/mathurinache/ecthrnaacl2021), Chalkidis et al., NAACL 2021),
built on Apache Solr 10.

## Requirements

- Docker Desktop (running)
- Python 3.10+ and `pip install -r requirements.txt`

## Quick start

macOS/Linux: `make all`. On Windows (PowerShell or Git Bash) run the same steps by hand:

```bash
docker compose up -d --wait        # Solr 10 on http://localhost:8983 with cores "cases" and "paragraphs"
python src/prepare.py              # data/*.jsonl -> data/processed/{cases,paragraphs}.jsonl  (~15 s)
python src/index.py                # rebuild both cores: schema + documents  (~1 min)
python src/search.py "overcrowded cell detention" --rows 5
```

`docker compose down` stops Solr and keeps the index. `docker compose down -v` wipes it.

## Layout

| Path | Content |
|---|---|
| `data/` | raw splits from Kaggle (`train/dev/test.jsonl`); `data/processed/` is generated and gitignored |
| `src/prepare.py` | cleaning and document building: strips paragraph numbers (kept as `para_no`), normalises hyphen look-alikes, adds ECHR article names, intro and rationale fields, builds one document per paragraph, and prints a collection report |
| `src/index.py` | resets a core, applies the schema and posts the documents (`--schemaless` for the smoke test) |
| `src/search.py` | query CLI and the retrieval setups (`SETUPS`: S0, ...) |
| `solr/schema_*.json` | Schema API definitions, one per core |
| `eval/needs.json` | information needs (id, query, description, narrative) |
| `notebooks/` | exploration and analysis |
| `report/figures/` | figures used in slides and report |

## Documents

- **cases** (11,000): one per judgment. Fields: `title`, `case_no`, `judgment_date`/`year`, `split`, `defendants`,
  `applicants`, `alleged_articles`, `violated_articles`, `alleged_article_names`, `violated_article_names`, `outcome`,
  `facts` (paragraphs), `facts_intro` (first 3 paragraphs), `rationale_text` (paragraphs the Court relied on),
  `silver_rationales`/`gold_rationales` (their positions), `para_numbers` (original paragraph numbers, which
  `court_assessment_references` cite), `n_paragraphs`, `n_words`.
- **paragraphs** (262,580): one per fact paragraph (`{case_id}_p{position}`), with `case_id`, `position`, original
  `para_no`, `text`, `is_rationale`, and the case's `title`, `year`, `defendants`, articles and `outcome` for filtering.

## Retrieval setups

| Setup | Analysis | Query |
|---|---|---|
| S0 | standard tokenizer + lowercase (`text_basic`) | edismax, `qf=facts title`, BM25 defaults |

## Notes

- Solr 10 starts in SolrCloud mode by default; the compose file runs it in `--user-managed` (standalone) mode,
  which is what pre-created cores and the course tutorial use.
- Schemaless smoke test (`python src/index.py cases --schemaless`) fails: Solr guesses the article fields as
  numbers from the first case (`"13"`, `"8"`) and then rejects `"P1-1"`, and it types `defendants`/`outcome` as
  free text (no faceting). Hence the explicit schema.

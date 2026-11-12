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
python src/index.py                # rebuild both cores: schema + documents  (~25 s measured)
python src/search.py "overcrowded cell detention" --rows 5
python src/search.py "overcrowded cell detention" --setup S1 --rows 5
python src/compare.py                 # S0 vs S1 on all 7 needs -> eval/runs/s0_vs_s1.md
python src/evaluate.py                # metrics from eval/qrels.csv -> eval/results.md, chart
python src/trec.py                    # TREC qrels/runs, MAP/P@10/nDCG (pytrec_eval), precision-recall curves
```

`docker compose down` stops Solr and keeps the index. `docker compose down -v` wipes it.

## Layout

| Path | Content |
|---|---|
| `data/` | raw splits from Kaggle (`train/dev/test.jsonl`); `data/processed/` is generated and gitignored |
| `src/prepare.py` | cleaning and document building: strips paragraph numbers (kept as `para_no`), normalises hyphen look-alikes, adds ECHR article names, intro and rationale fields, builds one document per paragraph, and prints a collection report |
| `src/index.py` | resets a core, applies the schema and posts the documents (`--schemaless` for the smoke test) |
| `src/search.py` | query CLI and the retrieval setups (`SETUPS`: S0, S1) |
| `src/compare.py` | runs every information need with S0 and S1; writes `eval/runs/s0_vs_s1.md` |
| `src/trec.py` | exports qrels and runs in TREC format (tutorial 06), runs `pytrec_eval` (MAP, P@N, R@10, RR, nDCG), plots 11-point P-R curves |
| `src/evaluate.py` | reads `eval/qrels.csv`; computes P@5, P@10, graded@10, nDCG@10, AP@10; writes `eval/results.{md,csv}`, `eval/to_verify.csv` and a chart |
| `solr/schema_*.json` | Schema API definitions, one per core |
| `eval/needs.json` | information needs (id, query, description, narrative) |
| `eval/qrels.csv` | manual relevance judgments (0/1/2) for the top 10 of S0 and S1 on every need; `eval/s0_vs_s1_reviewed.md` is the annotated sheet |
| `eval/results.md` | metrics table produced by `src/evaluate.py` |
| `eval/trec/` | qrels and runs in TREC format and the `src/trec.py` results (work with `trec_eval` too) |
| `notebooks/` | exploration and analysis |
| `report/checkpoint_report.md` | checkpoint report: collection, indexing, retrieval, evaluation |
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

Same query string (and the same filter, if any) is used for every setup.

| Setup | Analysis | Query |
|---|---|---|
| S0 | standard tokenizer + lowercase (`text_basic`) | edismax, `qf=facts title`, BM25 defaults |
| S1 | English possessive, ASCII fold, stopwords, Porter stem (`text_en`) | edismax, `qf=facts_en title_en`, BM25 defaults |

`python src/compare.py` writes a review sheet (`eval/runs/s0_vs_s1.md` + `.csv`) with top-10 lists, snippets, overlap, and blank yes/kinda/no marks.
The completed judgments live in `eval/qrels.csv`; re-running `compare.py` does not touch them, but if the index or the setups change the ranks no longer match and the new top 10 must be judged again.

## Notes

- Solr 10 starts in SolrCloud mode by default; the compose file runs it in `--user-managed` (standalone) mode,
  which is what pre-created cores and the course tutorial use.
- Schemaless smoke test (`python src/index.py cases --schemaless`) fails: Solr guesses the article fields as
  numbers from the first case (`"13"`, `"8"`) and then rejects `"P1-1"`, and it types `defendants`/`outcome` as
  free text (no faceting). Hence the explicit schema.

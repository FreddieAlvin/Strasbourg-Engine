# Strasbourg Engine - Checkpoint report

Search system over European Court of Human Rights (ECtHR) judgments, built on Apache Solr 10.

> Internal working document. The checkpoint deliverables are the **slides (`demo-gg.pdf`)** and the **code (`code-gg.zip`)**;
> no written report is required. This text is the source material for the slides.

| Checkpoint item | Where it is covered |
|---|---|
| 1. Collection & documents | Section 1, `src/prepare.py`, `notebooks/01_data_exploration.ipynb`, `report/figures/` |
| 2. Indexing | Section 2, `solr/schema_*.json`, `src/index.py`, `docker-compose.yml` |
| 3. Retrieval | Section 3, `src/search.py`, `src/compare.py`, `eval/runs/` |
| 4. Evaluation | Section 4, `eval/needs.json`, `eval/qrels.csv`, `src/evaluate.py`, `eval/results.md` |

---

## 1. Collection and documents

### 1.1 The collection

ECtHR-NAACL2021 (Chalkidis et al., NAACL 2021): judgments of the European Court of Human Rights, in English,
each with the **facts** of the case split into numbered paragraphs plus structured metadata. Numbers below
come from `data/processed/cases.jsonl`.

| Property | Value |
|---|---|
| Cases | 11,000 (train 9,000 / dev 1,000 / test 1,000) |
| Judgment years | 2001-2019 (4,973 cases in the 2000s, 6,027 in the 2010s) |
| Fact paragraphs | 262,580 (mean 23.9 per case, median 17, max 558) |
| Words | 18.0 M in total; per case mean 1,638, median 1,014, min 64, max 34,858 |
| Respondent states | 47; Russia 2,070 cases, Turkey 1,130, Ukraine 1,076, Poland 951 |
| Most alleged articles | Art. 6 fair trial (6,225 cases), Art. 3 torture (2,210), Art. 5 liberty (2,038), Art. 13 remedy (1,900), P1-1 property (1,881) |
| Outcome | violation 9,955 (90.5%), no violation 1,045 |
| Annotated rationales | silver rationales in 5,767 cases; gold rationales in 50 |

Things that shape retrieval:

- **Only the facts section is in the collection**, not the legal reasoning. Queries match narrative descriptions of
  what happened, not legal argumentation. This creates a vocabulary gap whenever a user names a legal concept.
- **Skewed collection**: ~19% of cases are against Russia and ~90% end in a violation, so "relevant" cases
  cluster in a few countries.
- **Very uneven length** (64 to 34,858 words): long cases can match more query terms by chance, which affects BM25 ranking.

Exploration figures (cases per year, top countries, document length, labels per case, alleged vs violated articles)
are in `report/figures/`.

### 1.2 Documents and relevant components

Two document granularities are built by `src/prepare.py`:

| Core | Document | Count | Purpose |
|---|---|---|---|
| `cases` | one judgment | 11,000 | main retrieval unit (a user wants *cases*) |
| `paragraphs` | one fact paragraph | 262,580 | finer granularity (passage retrieval, rationale paragraphs); indexed, not yet used in the compared setups |

Components of a case: `title`, `case_no`, `judgment_date`/`year`, `split`, `defendants`, `applicants`,
`alleged_articles`, `violated_articles` (plus their names), `outcome`, `facts`, `facts_intro` (first 3 paragraphs),
`rationale_text` (paragraphs the Court relied on), rationale positions, original paragraph numbers, length counts.

Cleaning done in `prepare.py`: paragraph numbers split off into `para_no`, whitespace normalised, hyphen look-alikes
and soft hyphens removed (the soft hyphen splits words in Solr), ECHR article names added from the Convention text.

### 1.3 Information needs

Seven needs in `eval/needs.json`, each with query, description, relevance narrative and (for IN5) a fixed filter.
The query string is run unchanged by every setup.

| ID | Need | Type |
|---|---|---|
| IN1 | Confessions coerced by police ill-treatment | T2 legal concept vs narrative facts |
| IN2 | Journalists sanctioned for articles about public figures | T4 rights in conflict |
| IN3 | Unfair trial due to restricted access to evidence or witnesses | T3 procedural fairness |
| IN4 | Bans on religious symbols and clothing | T4 rights in conflict |
| IN5 | Overcrowded, unsanitary detention in Southern European states | T5 text + metadata constraint |
| IN6 | Expulsion or extradition to a risk of torture | T1 factual situation |
| IN7 | Civilian casualties from bombardment and shelling | T1 factual situation |

Relevance scale: **2** = situation is a central element of the facts; **1** = present but secondary or partial;
**0** = absent, passing mention or a neighbouring situation.

---

## 2. Indexing

### 2.1 Indexable components

| Component | Field(s) | Type | Why |
|---|---|---|---|
| Full text of the facts | `facts`, `facts_en` | `text_basic`, `text_en` | main free-text content |
| Title (case name) | `title`, `title_en` | `text_basic`, `text_en` | party names are queries |
| First 3 paragraphs | `facts_intro(_en)` | text, not stored | applicant and background |
| Paragraphs the Court relied on | `rationale_text(_en)` | text, not stored | most informative passages |
| Article names | `alleged/violated_article_names` | `text_en` | lets "fair trial" match article 6 |
| Respondent state, outcome, split | `defendants`, `outcome`, `split` | `string` | exact-match filters and facets |
| Article codes | `alleged/violated_articles` | `string`, multi-valued | filters and facets (`"P1-1"` must stay a string) |
| Dates | `judgment_date`, `year` | `pdate`, `pint` | range filters |
| Rationale positions, paragraph numbers | `silver/gold_rationales`, `para_numbers` | `pint`, `indexed=false` | stored only, not searched |

### 2.2 Schema decisions (`solr/schema_cases.json`, `schema_paragraphs.json`)

- **Two text analyses.** `text_basic` = standard tokenizer + lowercase. `text_en` = standard tokenizer, English
  possessive, ASCII folding, lowercase, English stopwords, Porter stemmer. The `_en` fields are filled with
  `copyField`, so the source is posted once and both analyses are searchable. This is what makes the S0/S1 comparison possible.
- **Explicit schema, no schemaless mode.** `update.autoCreateFields=false` is set, so a field not in the schema is
  rejected rather than guessed. The schemaless smoke test fails: Solr types the article fields as numbers from the first
  case (`"13"`, `"8"`) and then rejects `"P1-1"`, and it treats `defendants`/`outcome` as free text, which removes faceting.
- **Structured fields as `string`** (multi-valued where needed) for exact filters, e.g. the IN5 filter on `defendants`.
- **Index size control:** large derived fields are `stored=false`; position lists are `indexed=false`.
- **Reproducible rebuild:** `index.py` drops the core, copies Solr's default config, applies the schema and posts the
  documents in batches (500 cases / 5,000 paragraphs per request).

### 2.3 Demonstration

```bash
docker compose up -d --wait   # Solr 10, cores "cases" and "paragraphs", standalone mode
python src/prepare.py         # raw splits -> data/processed/{cases,paragraphs}.jsonl
python src/index.py           # reset core -> apply schema -> post documents -> print numDocs
```

`prepare.py` prints the collection report; `index.py` ends each core with `numDocs`. Expected values:
**11000** in `cases` and **262580** in `paragraphs`. Take a screenshot of this output and of the Solr Admin UI
(`http://localhost:8983/solr/#/cases/schema`) for the presentation.

---

## 3. Retrieval

### 3.1 Free-text retrieval

`src/search.py` sends the user's query string to Solr's `edismax` parser on the `cases` core, with highlighting for snippets
and an optional filter query (`--fq`). Ranking is Solr's default BM25. No query rewriting.

### 3.2 Two setups compared

| Setup | Fields searched | Analysis |
|---|---|---|
| **S0** baseline | `facts title` | lowercase only |
| **S1** English | `facts_en title_en` | possessive removal, ASCII folding, stopwords, Porter stemming |

Everything else is identical: same query string, same filter, same BM25 parameters, same `rows`.
So the only variable is the text analysis.

### 3.3 Demonstration

```bash
python src/search.py "ban on wearing religious symbols headscarf veil school workplace" --setup S0 --rows 10
python src/search.py "ban on wearing religious symbols headscarf veil school workplace" --setup S1 --rows 10
python src/compare.py   # all 7 needs, S0 vs S1 -> eval/runs/s0_vs_s1.md / .csv
```

Real output (IN4, top 6 of each, relevance from `eval/qrels.csv`; 2 = relevant, 0 = not):

| # | S0 | rel | S1 | rel |
|--:|---|:-:|---|:-:|
| 1 | Dakir v. Belgium | 2 | Ebrahimian v. France | 2 |
| 2 | Dogru v. France | 2 | Dogru v. France | 2 |
| 3 | Ebrahimian v. France | 2 | Dakir v. Belgium | 2 |
| 4 | Sekmadienis Ltd. v. Lithuania | 0 | Leyla Sahin v. Turkey | 2 |
| 5 | Leyla Sahin v. Turkey | 2 | Lautsi and Others v. Italy | 2 |
| 6 | Mustafa Erdogan and Others v. Turkey | 0 | S.A.S. v. France | 2 |

S1 finds S.A.S. v. France (full-face veil ban), which S0 does not return in its top 10, and removes an
off-topic case (an advertising case) from the top 5.

Besides the top-10 lists, `compare.py` reports overlap between setups per need (Jaccard from 0.25 for IN2 to 0.67 for IN4/IN6/IN7).

---

## 4. Evaluation

### 4.1 Method

- **Needs:** the 7 needs of section 1.3, each with a written relevance narrative (`eval/needs.json`).
- **Pooling:** the top 10 of S0 and of S1 per need (140 judged positions; a case returned by both setups gets one label).
- **Manual judgment:** each result was read against the need's narrative and rated 2 / 1 / 0 with a reason and a confidence
  (`eval/qrels.csv`; the full annotated sheet is `eval/s0_vs_s1_reviewed.md`). Topical relevance only; whether the Court found a violation is irrelevant.
- **Pooling** (as in course tutorial 06): relevant cases for a need are the ones judged relevant in the merged top 10 of S0 and S1.
  Recall is therefore *pooled recall* and only compares these two setups with each other.
- **Metrics:** `python src/trec.py` exports qrels and runs in TREC format (`eval/trec/`) and computes MAP, P@5, P@10, R@10, reciprocal rank
  and nDCG@10 with `pytrec_eval`, plus 11-point interpolated precision-recall curves. Binary measures treat `yes` (2) as relevant;
  `kinda` is not relevant. `python src/evaluate.py` independently computes strict P@10, graded@10, nDCG@10 and AP@10, and gives the same numbers.
  The TREC files also work with the official tool: `trec_eval -q -m all_trec -l 2 eval/trec/qrels_trec.txt eval/trec/run_S0.txt`.

### 4.2 Results

| Need | P@10 S0 | P@10 S1 | nDCG@10 S0 | nDCG@10 S1 | MAP/AP S0 | MAP/AP S1 |
|---|---:|---:|---:|---:|---:|---:|
| IN1 | 1.00 | 1.00 | 1.00 | 1.00 | 0.77 | 0.77 |
| IN2 | 0.80 | 0.90 | 0.87 | 0.96 | 0.62 | 0.64 |
| IN3 | 0.70 | 1.00 | 0.74 | 1.00 | 0.42 | 0.83 |
| IN4 | 0.50 | 0.60 | 0.86 | 1.00 | 0.75 | 1.00 |
| IN5 | 1.00 | 1.00 | 1.00 | 1.00 | 0.71 | 0.71 |
| IN6 | 1.00 | 1.00 | 1.00 | 1.00 | 0.83 | 0.83 |
| IN7 | 0.90 | 0.90 | 0.94 | 0.95 | 0.72 | 0.74 |
| **Macro** | **0.84** | **0.91** | **0.92** | **0.99** | **0.69** | **0.79** |

More measures (P@5, R@10, RR, graded@10): `eval/results.md` and `eval/trec/trec_results.md`. Charts: `report/figures/s0_vs_s1_metrics.png` and
`report/figures/s0_vs_s1_pr_curves.png` (precision-recall; curves fall to 0 once the 10 returned cases are exhausted, because only 10 per setup were judged).

### 4.3 Discussion

**S1 is never worse and is clearly better on 3 of 7 needs** (nDCG@10 difference: IN3 +0.26, IN4 +0.14, IN2 +0.09).
IN7 differs only marginally (+0.01, same P@10) and IN1, IN5, IN6 are tied. Averaged over the needs, P@10 goes from 0.84 to 0.91.

- **IN3 (fair trial, access to evidence/witnesses) is the clearest gain** (P@10 0.70 to 1.00). S0's top 10 contains
  Liu v. Russia (No. 2), judged not relevant (expulsion/family life), Kamenos v. Cyprus (judge impartiality), and a partial match
  (Trepashkin v. Russia (No. 2)). S1 returns ten relevant cases. The query is long and uses wording such as "cross-examine
  witnesses" and "classified evidence"; stemming and stopword removal let more of the query's terms count towards the right cases.
- **IN4 (religious symbols) is the hardest need for both setups** (P@10 0.50 / 0.60). Every relevant case found by either setup
  (6 in the pool) is at ranks 1-6 in S1, so nDCG is 1.00, but ranks 7-10 are filled by neighbouring cases: religious imagery
  in advertising (Sekmadienis), a political party dissolution mentioning headscarves (Refah Partisi), an asylum case. This is a
  precision limit of bag-of-words on a topic where few cases exist, not a ranking error. We have not verified how many
  relevant cases the whole collection contains.
- **IN2 (journalists)**: S0 includes two cases that do not fit the narrative (a politician speaking at a press conference; sanctions for
  statements about a journalist). S1 has one partial match.
- **IN1, IN5, IN6 are saturated** (all 10 relevant for both). The queries use distinctive vocabulary ("confession", "overcrowded",
  "extradition"), so stemming adds little. IN5 also shows that the metadata filter (Southern Europe) works as a hard constraint.
- **S0 does not win any need on the current labels.** We report this as found. The only S0-specific evidence is individual
  cases, e.g. Ulay v. Turkey (IN1) and Treskavica v. Croatia (IN7) appear only in S0's top 10, and both are relevant, but S1's
  replacements are relevant too, so these are ties, not S0 wins.
- **Match-set size is not quality.** With Solr's default OR operator, S0 matches 11,000 cases (every case) for IN6 and 10,993 for IN4,
  against 1,826 for S1 on IN4. The likely cause is the stopword "on" in the query, which S0 indexes and S1 drops. Hit counts and raw Solr scores
  must not be compared between setups; only the judged rankings can.

### 4.4 Limitations (state these in the presentation)

1. **Small evaluation**: 7 needs, top 10 only, one pool. Per-need differences are descriptive; no significance test is claimed.
2. **Pooled estimates**: MAP, recall and the P-R curves use the pool as the relevant set, so they only compare these two setups. True recall is unknown.
   Relevance is graded (0/1/2) here, while tutorial 06 uses binary judgments; binary measures use `yes` only.
3. **Labels must be verified by the team**: the judgments were produced as an annotated review sheet and are marked provisional.
   `eval/to_verify.csv` lists the 44 judgments to re-check (every `medium` confidence one plus all partial and non-relevant labels); change `eval/qrels.csv`
   where you disagree and re-run `python src/evaluate.py`.
4. **IN5 filter**: Southern Europe is defined as the UN M49 region plus Cyprus, excluding Turkey and Bulgaria. The group should confirm this choice.
5. **Not yet explored**: the `paragraphs` core, boosts on `facts_intro_en`/`rationale_text_en`, phrase boosts, and semantic/vector retrieval are
   all indexed or planned but not part of the compared setups.

### 4.5 Reproduce

```bash
python src/compare.py     # needs Solr running; regenerates eval/runs/s0_vs_s1.{md,csv}
python src/evaluate.py    # needs only eval/qrels.csv; regenerates eval/results.*, to_verify.csv and the chart
python src/trec.py        # TREC files + MAP/P@10/nDCG via pytrec_eval + precision-recall curves (needs pytrec_eval-terrier)
```

---

## 5. Ideas for the final search system (required at the checkpoint)

The final stage asks for a semantic retrieval approach, plus one individual exploration per group member, each with a different experimental question.
Candidates motivated by what we observed:

| Idea | Motivation from the checkpoint results |
|---|---|
| **Semantic retrieval** with dense embeddings (Solr 10 dense-vector/kNN search) over the `paragraphs` core, aggregated to cases | vocabulary gap between legal concepts and narrative facts (T2 needs); paragraphs are already indexed |
| **Hybrid lexical + semantic** ranking (e.g. rank fusion of S1 and the dense run) | S1 is strong when queries share vocabulary with the facts; embeddings should help where they do not |
| **Field boosts, phrase boosts and minimum-match** in `edismax` (`qf`, `pf`, `mm`), using `facts_intro_en` and `rationale_text_en` | IN4: neighbouring cases fill ranks 7-10; Solr's default OR matches nearly all 11,000 cases for some queries |
| **Query rewriting / relevance feedback** (e.g. expanding "ban on religious symbols" with domain terms) | queries that name legal concepts in different words than the facts |
| **Reranking** the top-k with a cross-encoder | improve order in ranks 5-10 where non-relevant neighbours appear |
| **Metadata-aware retrieval** (state groups, articles, outcome as filters or facets) | IN5 shows filters work as hard constraints; more needs could use them |
| **Larger judged set** (more needs, deeper pools, a second assessor for agreement) | current evaluation has 7 needs and the top 10 only |

Each member would pick one of these as an individual question (for example: boosts and phrase matching; query expansion; cross-encoder reranking; paragraph-level vs case-level retrieval).

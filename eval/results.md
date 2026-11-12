# S0 vs S1 - retrieval metrics

Computed by `python src/evaluate.py` from `eval/qrels.csv` (top-10 per setup, 7 needs).

| Need | P@5 S0 | P@5 S1 | P@10 S0 | P@10 S1 | graded@10 S0 | graded@10 S1 | nDCG@10 S0 | nDCG@10 S1 | AP@10 S0 | AP@10 S1 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| IN1 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.77 | 0.77 |
| IN2 | 1.00 | 0.80 | 0.80 | 0.90 | 0.80 | 0.95 | 0.87 | 0.96 | 0.62 | 0.64 |
| IN3 | 0.60 | 1.00 | 0.70 | 1.00 | 0.75 | 1.00 | 0.74 | 1.00 | 0.42 | 0.83 |
| IN4 | 0.80 | 1.00 | 0.50 | 0.60 | 0.50 | 0.60 | 0.86 | 1.00 | 0.75 | 1.00 |
| IN5 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.71 | 0.71 |
| IN6 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.83 | 0.83 |
| IN7 | 0.80 | 0.80 | 0.90 | 0.90 | 0.95 | 0.95 | 0.94 | 0.95 | 0.72 | 0.74 |
| MACRO | 0.89 | 0.94 | 0.84 | 0.91 | 0.86 | 0.93 | 0.92 | 0.99 | 0.69 | 0.79 |

nDCG@10, S1 minus S0, per need: IN1 +0.00, IN2 +0.09, IN3 +0.26, IN4 +0.14, IN5 +0.00, IN6 +0.00, IN7 +0.01.  S1 clearly better (> 0.05) on 3, about equal on 4, S0 clearly better on 0 of 7 needs.

AP@10 is normalised by the relevant cases found by *either* setup (pooled), so it is a
relative figure; true recall is unknown because only the top 10 of each setup was judged.

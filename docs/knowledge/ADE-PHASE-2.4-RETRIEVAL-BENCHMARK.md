# ADE Phase 2.4 Retrieval Benchmark

Corpus: 40-source / 932-item staging corpus.

This benchmark is an evaluation harness, not production infrastructure. It uses deterministic local retrieval strategies only and does not ingest additional sources.

## Strategies Tested

| Strategy | Average score | Average term recall | Elapsed ms |
| --- | ---: | ---: | ---: |
| jsonl_keyword_scan | 0.971 | 0.958 | 2190.23 |
| sqlite_fts5_bm25 | 0.971 | 0.958 | 450.56 |
| governed_lexical_hybrid_rrf | 0.971 | 0.958 | 1846.57 |

## Query Results

### jsonl_keyword_scan

| Query | Score | Term recall | Result count | Top content types |
| --- | ---: | ---: | ---: | --- |
| Q1 | 1.0 | 1.0 | 729 | Prompt / agent instruction, Prompt / agent instruction, Operational instruction, Prompt / agent instruction, Prompt / agent instruction |
| Q2 | 1.0 | 1.0 | 932 | Operational instruction, Operational instruction, Operational instruction, Operational instruction, Operational instruction |
| Q3 | 1.0 | 1.0 | 838 | Prompt / agent instruction, Prompt / agent instruction, Prompt / agent instruction, Prompt / agent instruction, Operational instruction |
| Q4 | 1.0 | 1.0 | 932 | Operational instruction, Visibility / AEO knowledge, Prompt / agent instruction, Operational instruction, Prompt / agent instruction |
| Q5 | 1.0 | 1.0 | 816 | Prompt / agent instruction, Prompt / agent instruction, Prompt / agent instruction, Operational instruction, Operational instruction |
| Q6 | 1.0 | 1.0 | 916 | Knowledge candidate, Prompt / agent instruction, Operational instruction, Operational instruction, Prompt / agent instruction |
| Q7 | 1.0 | 1.0 | 808 | Prompt / agent instruction, Prompt / agent instruction, Security knowledge, Prompt / agent instruction, Prompt / agent instruction |
| Q8 | 0.767 | 0.667 | 547 | Prompt / agent instruction, Prompt / agent instruction, Prompt / agent instruction, Operational instruction, Prompt / agent instruction |

### sqlite_fts5_bm25

| Query | Score | Term recall | Result count | Top content types |
| --- | ---: | ---: | ---: | --- |
| Q1 | 1.0 | 1.0 | 50 | Prompt / agent instruction, Prompt / agent instruction, Prompt / agent instruction, Prompt / agent instruction, Operational instruction |
| Q2 | 1.0 | 1.0 | 50 | Operational instruction, Knowledge candidate, Tool / package knowledge, Knowledge candidate, Knowledge candidate |
| Q3 | 1.0 | 1.0 | 50 | Visibility / AEO knowledge, Operational instruction, Prompt / agent instruction, Operational instruction, Prompt / agent instruction |
| Q4 | 1.0 | 1.0 | 50 | Operational instruction, Operational instruction, Operational instruction, Operational instruction, Visibility / AEO knowledge |
| Q5 | 1.0 | 1.0 | 50 | Prompt / agent instruction, Prompt / agent instruction, Prompt / agent instruction, Operational instruction, Prompt / agent instruction |
| Q6 | 1.0 | 1.0 | 50 | Tool / package knowledge, Knowledge candidate, Knowledge candidate, Knowledge candidate, Tool / package knowledge |
| Q7 | 1.0 | 1.0 | 50 | Prompt / agent instruction, Prompt / agent instruction, Security knowledge, Prompt / agent instruction, Prompt / agent instruction |
| Q8 | 0.767 | 0.667 | 50 | Prompt / agent instruction, Operational instruction, Prompt / agent instruction, Prompt / agent instruction, Prompt / agent instruction |

### governed_lexical_hybrid_rrf

| Query | Score | Term recall | Result count | Top content types |
| --- | ---: | ---: | ---: | --- |
| Q1 | 1.0 | 1.0 | 69 | Prompt / agent instruction, Prompt / agent instruction, Prompt / agent instruction, Prompt / agent instruction, Operational instruction |
| Q2 | 1.0 | 1.0 | 72 | Operational instruction, Operational instruction, Operational instruction, Operational instruction, Prompt / agent instruction |
| Q3 | 1.0 | 1.0 | 67 | Prompt / agent instruction, Operational instruction, Prompt / agent instruction, Prompt / agent instruction, Prompt / agent instruction |
| Q4 | 1.0 | 1.0 | 69 | Operational instruction, Visibility / AEO knowledge, Operational instruction, Operational instruction, Operational instruction |
| Q5 | 1.0 | 1.0 | 69 | Prompt / agent instruction, Prompt / agent instruction, Prompt / agent instruction, Operational instruction, Operational instruction |
| Q6 | 1.0 | 1.0 | 57 | Tool / package knowledge, Knowledge candidate, Knowledge candidate, Knowledge candidate, Security knowledge |
| Q7 | 1.0 | 1.0 | 61 | Prompt / agent instruction, Prompt / agent instruction, Security knowledge, Prompt / agent instruction, Prompt / agent instruction |
| Q8 | 0.767 | 0.667 | 72 | Prompt / agent instruction, Operational instruction, Prompt / agent instruction, Prompt / agent instruction, Prompt / agent instruction |

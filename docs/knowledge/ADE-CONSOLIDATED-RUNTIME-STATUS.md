# ADE Consolidated Runtime Status

## Runtime

- Structured store contract: implemented
- Source repository interface: implemented
- Keyword retrieval: implemented
- Semantic retrieval abstraction: implemented through provider interface and deterministic non-production hash-vector prototype
- Hybrid retrieval: implemented with RRF-style fusion
- Ranking: implemented
- Reranking interface: implemented with governance reranker
- Provenance filtering/explanation: implemented
- Access filtering: implemented
- Temporal filtering: implemented
- Lifecycle filtering: implemented
- Confidence filtering: implemented
- Conflict handling: implemented
- Explainable retrieval: implemented
- Context packet generation: implemented

## Metrics

Average term recall: `0.875`

| Query | Term recall | Result count | Elapsed ms | Matched terms |
| --- | ---: | ---: | ---: | --- |
| Q1 | 0.667 | 10 | 2152.294 | prompt, instruction |
| Q2 | 1.0 | 10 | 2381.138 | backup, version, control |
| Q3 | 0.667 | 10 | 1877.895 | security, rls |
| Q4 | 1.0 | 10 | 2819.142 | robots, sitemap, llms, aeo |
| Q5 | 1.0 | 10 | 2387.789 | rate, limiting, abuse |
| Q6 | 1.0 | 10 | 2073.514 | ai, agents, production |
| Q7 | 1.0 | 10 | 1867.93 | supabase, authentication, database |
| Q8 | 0.667 | 10 | 1983.486 | evidence, source |

## Status

The runtime proves the end-to-end contract but is not production infrastructure. Real PostgreSQL, full-text indexes, pgvector embeddings, reranker, monitoring, and ACL service remain deferred.

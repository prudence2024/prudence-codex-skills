# ADE Phase 2.4 Report

## Final Recommendation

Recommend for review: PostgreSQL as the canonical knowledge store, PostgreSQL full-text search for lexical retrieval, pgvector for initial vector retrieval, RRF-style hybrid fusion, optional reranking after top-k retrieval, and a provider-neutral adapter that can swap in Qdrant if ADE outgrows pgvector performance or recall.

Do not deploy this infrastructure until the Phase 2.4 report is reviewed.

## Why This Recommendation Fits ADE

ADE needs governance first and retrieval second. The 932-item corpus includes prompts, instructions, project-specific material, stale candidates, conflicts, and AI-inference boundaries. A canonical relational store is the cleanest place to enforce source provenance, ACL, deletion/revocation, temporal status, confidence, and versioning before any vector index participates.

## Benchmark Summary

| Strategy | Average score | Average term recall | Elapsed |
| --- | ---: | ---: | ---: |
| jsonl_keyword_scan | 0.971 | 0.958 | 2190.23 ms |
| sqlite_fts5_bm25 | 0.971 | 0.958 | 450.56 ms |
| governed_lexical_hybrid_rrf | 0.971 | 0.958 | 1846.57 ms |

SQLite FTS5 is the strongest local lexical baseline. The governed lexical hybrid preserves score quality but costs more than FTS alone. Pure Python/JSONL keyword scanning is useful only as a transparent fallback.

## Candidate Ranking

| Rank | Candidate | Decision | Reason |
| ---: | --- | --- | --- |
| 1 | PostgreSQL + FTS + pgvector | Recommend for review | Best balance of governance, ACL, provenance, backups, portability, and hybrid retrieval. |
| 2 | PostgreSQL + Qdrant | Keep as scale path | Strong retrieval engine, but requires dual-store consistency. |
| 3 | SQLite FTS5 baseline | Keep for local/offline | Excellent benchmark and fallback, not enough governance for production. |
| 4 | LanceDB | Evaluate experimentally | Good local hybrid search, but not canonical governance storage. |
| 5 | Neo4j | Defer graph layer | Useful for relationship queries after graph demand is proven. |
| 6 | Chroma | Experimental only | Convenient but weaker for production governance/ACL. |
| 7 | Pinecone/vector-first managed services | Defer | Cost and lock-in before need is proven. |

## Runtime Architecture Under Review

1. Store source records, extracted items, normalized knowledge items, conflicts, freshness, versions, ACL scopes, and revocation state in PostgreSQL.
2. Add PostgreSQL full-text indexes for prompts, instructions, exact technology names, source IDs, and file names.
3. Add pgvector columns or side tables for embeddings, with source IDs and revision IDs copied into metadata.
4. Retrieve with metadata filters first: access scope, project, status, freshness, source type, and version.
5. Run lexical and vector retrieval independently, then fuse with RRF rather than raw-score averaging.
6. Optionally rerank the fused top-k with a reranker after cost/latency tests.
7. Return source, confidence, freshness, derivation, conflicts, and filtered-out reason metadata with every context packet.
8. Propagate source revocation to full-text, vector, cache, and future graph indexes.
9. Keep Qdrant adapter ready if pgvector cannot meet recall/latency at larger corpus sizes.

## Rejected Alternatives

See `docs/knowledge/ADE-PHASE-2.4-REJECTED-ALTERNATIVES.md`.

## Validation Evidence

- Phase 2.4 benchmark generated JSON and Markdown artifacts.
- Benchmark regression test added for the 932-item corpus.
- Focused Phase 2.4 tests: `17 passed`.
- Full pytest: `101 passed, 1 failed`. The remaining failure is the pre-existing `tests/test_integration_framework.py::test_complete_repository_integration_passes` documentation gate for 12 historical missing docs outside Phase 2.4.
- Strict repository/Markdown validation: `pass`.
- Repository Markdown reference validation: `BROKEN_MD_LINKS 0`.
- Bounded secret/destructive-command scan: 1 intentional generic test fixture pattern in `tests/test_knowledge_core.py`; 0 destructive-command hits.

## Stop Line

No production database, vector service, graph database, Hermes integration, crawler, deployment, or production ingestion pipeline was created.

## Research Sources Accessed On 2026-08-28

- SQLite FTS5: https://www.sqlite.org/fts5.html
- SQLite Online Backup API: https://www.sqlite.org/backup.html
- PostgreSQL text search functions: https://www.postgresql.org/docs/current/functions-textsearch.html
- PostgreSQL row security policies: https://www.postgresql.org/docs/current/ddl-rowsecurity.html
- PostgreSQL continuous archiving and PITR: https://www.postgresql.org/docs/18/continuous-archiving.html
- pgvector README: https://github.com/pgvector/pgvector
- Qdrant hybrid search: https://qdrant.tech/documentation/search/text-search/hybrid-search/
- Qdrant hybrid queries and RRF: https://qdrant.tech/documentation/search/hybrid-queries/
- Qdrant filtering: https://qdrant.tech/documentation/search/filtering/
- Qdrant production checklist: https://qdrant.tech/documentation/production-checklist/
- Chroma clients/query/filtering: https://docs.trychroma.com/docs/run-chroma/clients and https://docs.trychroma.com/docs/querying-collections/query-and-get
- LanceDB hybrid search: https://docs.lancedb.com/search/hybrid-search
- Neo4j semantic indexes: https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/
- Pinecone hybrid search and cost docs: https://docs.pinecone.io/guides/search/hybrid-search and https://docs.pinecone.io/guides/manage-cost/understanding-cost
- Cohere rerank docs: https://docs.cohere.com/v2/docs/rerank and https://docs.cohere.com/v2/reference/rerank
- OpenAI embedding model/pricing reference: https://developers.openai.com/api/docs/models/text-embedding-3-large

# ADE Phase 2.4 Technology Evaluation

## Scope

Phase 2.4 evaluates knowledge runtime and retrieval technology against the existing 40-source / 932-item ADE staging corpus. It does not ingest additional corpus sources, integrate Hermes, build the production ingestion pipeline, or deploy infrastructure.

## Benchmark Evidence

| Strategy | Average score | Average term recall | Elapsed |
| --- | ---: | ---: | ---: |
| jsonl_keyword_scan | 0.971 | 0.958 | 2190.23 ms |
| sqlite_fts5_bm25 | 0.971 | 0.958 | 450.56 ms |
| governed_lexical_hybrid_rrf | 0.971 | 0.958 | 1846.57 ms |

The local benchmark shows that pure JSONL scanning is easy to explain but slow and noisy; SQLite FTS5 is fast and strong for exact corpus language; local lexical hybrid with Reciprocal Rank Fusion preserves high recall but adds overhead. The benchmark is deliberately lexical because Phase 2.4 must not deploy a production embedding/indexing system yet.

## Requirements Evaluation

| Capability | Need | Evidence | Recommendation |
| --- | --- | --- | --- |
| Structured storage | Must preserve provenance, status, ACL, conflict, freshness, and version fields. | Phase 2.3 model has structured fields; PostgreSQL supports relational constraints and RLS. | Use PostgreSQL as canonical store. |
| Full-text search | Must recover exact prompts, commands, filenames, and source terms. | SQLite FTS5 benchmark was fastest locally; PostgreSQL supports `tsvector`, `tsquery`, `ts_rank`, and `ts_rank_cd`. | Use PostgreSQL full-text search first; keep SQLite FTS5 as local/offline baseline. |
| Semantic retrieval | Needed for paraphrase and conceptual queries. | Current benchmark cannot prove semantic improvement without embeddings. | Add vector retrieval behind an adapter after review. |
| Embeddings | Needed for semantic retrieval and clustering. | OpenAI lists `text-embedding-3-small` and `text-embedding-3-large`; cost differs materially. | Default to pluggable embedding provider; start with low-cost model for benchmarks. |
| Hybrid retrieval | Needed because ADE has exact instructions and broad concepts. | Qdrant, Pinecone, LanceDB, Weaviate, and pgvector docs all support hybrid patterns or composition. | Use RRF-style fusion so raw BM25/vector scores are not blindly mixed. |
| Reranking | Improves precision after broad recall. | Cohere rerank docs support reranking search results; Qdrant docs recommend reranking after hybrid retrieval. | Add optional reranker stage after top-k candidate retrieval, not on the whole corpus. |
| Graph requirements | Needed for source-to-claim-to-decision and conflict paths. | Neo4j supports graph, full-text, and vector semantic indexes; graph search is not proof by itself. | Model graph separately; do not make it primary retrieval storage yet. |
| Provenance | Must explain where each item came from. | Current corpus records source IDs and locations. | Keep provenance in canonical store and copy into retrieval payloads. |
| ACLs | Must separate global/project/private/restricted material. | PostgreSQL RLS can restrict rows per user/policy; Qdrant/Chroma filters can support payload-level filtering but not full app auth by themselves. | Enforce ACL in canonical store and retrieval service before vector queries. |
| Temporal/versioned retrieval | Needed for stale and superseded knowledge. | PostgreSQL can store version/timestamp fields and query them; graph can model supersession edges. | Use relational temporal fields first; add graph edges for relationship queries. |
| Deletion/revocation | Must revoke source-derived rows and future embeddings. | Phase 2.3 added archive semantics; vector stores need source IDs in payload for deletion. | Use source ID as revocation root across all indexes. |
| Backup/recovery | Must support safe restoration. | PostgreSQL supports WAL archiving/PITR; SQLite has Online Backup API. | Require tested backup/restore before production. |
| Local vs cloud | ADE benefits from local evaluation and later cloud scale. | SQLite/LanceDB/Chroma can run locally; Postgres/Qdrant can run local or cloud. | Require local reproducible baseline plus cloud-ready adapters. |
| Cost | Must avoid managed-service spend before value is proven. | Managed vector services charge by storage/query/read units or cluster resources. | Keep Phase 2.4 recommendation deploy-blocked until reviewed. |
| Provider portability | Must avoid lock-in. | Candidate tools expose different query semantics and metadata filters. | Define provider-neutral retrieval interface before adoption. |

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

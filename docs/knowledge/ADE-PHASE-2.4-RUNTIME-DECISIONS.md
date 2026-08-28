# ADE Phase 2.4 Runtime Decisions

| ID | Decision | Evidence | Status |
| --- | --- | --- | --- |
| D-2.4-001 | Keep the 40-source / 932-item corpus as the only evaluation dataset. | User instruction and Phase 2.4 scope. | Accepted |
| D-2.4-002 | Create a deterministic local retrieval benchmark before selecting infrastructure. | Benchmark results written to `docs/knowledge/ADE-PHASE-2.4-RETRIEVAL-BENCHMARK.json`. | Implemented |
| D-2.4-003 | Recommend PostgreSQL + full-text search + pgvector as the primary architecture for review. | Best fit for structured provenance, ACL, temporal fields, backup/recovery, and hybrid retrieval. | Proposed, not deployed |
| D-2.4-004 | Keep Qdrant as the main scale-out retrieval-index candidate. | Strong hybrid dense/sparse/RRF/filtering support and local/cloud portability. | Proposed fallback |
| D-2.4-005 | Keep SQLite FTS5 as the local/offline benchmark baseline. | Fastest local lexical benchmark result. | Accepted |
| D-2.4-006 | Defer Neo4j/Graphiti/Hermes/crawler/production ingestion. | Phase 2.4 explicitly forbids deployment/integration. | Accepted |
| D-2.4-007 | Use provider-neutral retrieval interfaces before any backend deployment. | Portability and revocation require a stable contract. | Accepted |

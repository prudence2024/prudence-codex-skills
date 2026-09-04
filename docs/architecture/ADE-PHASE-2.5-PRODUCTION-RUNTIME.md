# ADE Phase 2.5 Production Runtime Boundary

ADE now exposes provider-neutral runtime contracts for `KnowledgeStore`, `TextRetriever`, `VectorRetriever`, `HybridRetriever`, `Reranker`, `GraphStore`, `MemoryStore`, and `EmbeddingProvider`. The in-memory runtime remains the non-production proof adapter. PostgreSQL and pgvector are represented by adapter boundaries only; no production deployment was started.

Required production behavior: transactional writes, unique knowledge IDs, source references, lifecycle state, provenance, confidence, access scope, timestamps, versioning, archived/superseded filtering, and conflict relationships. Unit tests must not require external infrastructure.

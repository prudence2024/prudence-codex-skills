# ADE Phase 2.4 Candidate Architectures

## A. Local JSONL Plus SQLite FTS5

Use JSONL as the canonical corpus and SQLite FTS5 for lexical search.

Strengths:
- excellent local/offline evaluation path;
- fast lexical search on the 932-item corpus;
- simple backup via file copy or SQLite Online Backup API;
- low cost and low operational complexity.

Weaknesses:
- weak ACL model unless enforced in the application layer;
- no native semantic embeddings, graph, or durable multi-user governance;
- harder to evolve into production concurrent writes.

Decision: retain as benchmark/offline baseline, not production recommendation.

## B. PostgreSQL Canonical Store With Full-Text Search And pgvector

Use PostgreSQL for structured records, provenance, ACL policy, temporal/version fields, conflicts, source revocation, full-text search, and vector columns through pgvector.

Strengths:
- one canonical ACID store for source, knowledge, conflict, freshness, and ACL metadata;
- row-level security can enforce row visibility rules;
- WAL/PITR supports serious backup/recovery;
- pgvector supports exact and approximate vector search, HNSW/IVFFlat, filtering, and hybrid composition with Postgres FTS;
- easiest path to explainable retrieval because structured rows and retrieval payloads live together.

Weaknesses:
- vector scale and recall tuning need careful benchmarking;
- approximate vector search plus metadata filters can reduce recall if not tuned;
- graph traversal is possible but not as natural as a graph database.

Decision: recommended Phase 2.4 primary architecture for review, not deployment.

## C. PostgreSQL Canonical Store Plus Qdrant Retrieval Index

Use PostgreSQL as source of truth and Qdrant as a retrieval index for dense, sparse, hybrid, and reranked search.

Strengths:
- mature vector retrieval engine;
- named dense/sparse vectors and RRF-style hybrid queries;
- payload filters for metadata and access scope;
- local and cloud deployment options;
- production docs explicitly call out filtering, hybrid fit evaluation, and reranking.

Weaknesses:
- two stores must stay consistent;
- deletion/revocation must propagate to Qdrant payload/index entries;
- graph relationships still require another layer;
- ACL must be enforced by the ADE service, not trusted to a raw vector query alone.

Decision: recommended scale path if pgvector benchmark fails recall/performance targets.

## D. LanceDB Local Retrieval Layer

Use LanceDB for local vector, FTS, hybrid retrieval, and RRF reranking.

Strengths:
- local-friendly;
- hybrid search and FTS support;
- prefilter/postfilter controls are useful for governance benchmarking;
- likely convenient for offline experimentation.

Weaknesses:
- less compelling as ADE's canonical governance store;
- production ACL, temporal governance, and source revocation still need an application/canonical layer.

Decision: evaluate as local/offline retrieval alternative.

## E. Chroma Vector Store

Use Chroma for local/cloud vector collections with metadata filters.

Strengths:
- easy local persistent client;
- query/get APIs support metadata and document filters;
- useful for experiments.

Weaknesses:
- docs identify auth features as alpha in server/client mode;
- less complete for full corpus governance, conflicts, ACL, and backup/recovery than Postgres;
- vector-first model does not solve prompt/provenance governance alone.

Decision: reject as Phase 2.4 primary architecture; keep as experimental adapter candidate.

## F. Neo4j Knowledge Graph Runtime

Use Neo4j for source, entity, decision, conflict, and temporal relationship retrieval, with full-text and vector semantic indexes.

Strengths:
- strong fit for graph relationship questions;
- supports full-text and vector indexes;
- useful for source-to-claim-to-decision explainability.

Weaknesses:
- too heavy as the first canonical store for a 932-item staging corpus;
- graph retrieval is not proof and still needs provenance/freshness governance;
- adds operational complexity before ADE has validated graph query demand.

Decision: defer as graph layer or future relationship index, not primary Phase 2.4 storage.

## G. Managed Vector-First Cloud Services

Use Pinecone, Weaviate Cloud, or another managed vector-first service as primary retrieval.

Strengths:
- strong managed scaling and vector capabilities;
- hybrid search features are available;
- managed observability/RBAC varies by plan/provider.

Weaknesses:
- external cost appears before benchmark value is proven;
- provider-specific score fusion, consistency, metadata limits, and backup features complicate portability;
- canonical provenance, conflict, ACL, and deletion semantics still need a structured source of truth.

Decision: reject as primary Phase 2.4 architecture; reconsider after local benchmark proves need.

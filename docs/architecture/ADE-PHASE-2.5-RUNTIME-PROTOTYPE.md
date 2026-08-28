# ADE Phase 2.5 Runtime Prototype Architecture

## What Was Implemented

`ecosystem/src/skill_ecosystem/knowledge_runtime.py` implements a minimal runtime around the Phase 2.4 recommendation:

1. structured canonical-store contract;
2. full-text retrieval contract;
3. pgvector-shaped vector retrieval contract;
4. Reciprocal Rank Fusion-style hybrid merge;
5. optional governance reranker;
6. provenance, access, stale, temporal, conflict, archived-source filters;
7. explainable context packet output.

## What Was Not Implemented

- no production PostgreSQL instance;
- no pgvector extension installation;
- no external embedding provider;
- no full-scale embedding migration;
- no Hermes integration;
- no crawler;
- no new ADE skill;
- no production ingestion pipeline.

## What Worked

- The runtime can load the existing 932-item staging corpus through the existing importer.
- The runtime returns explainable context packets with provenance and warning metadata.
- Access boundaries are enforced before provider search.
- Archived source records are excluded from default retrieval.
- Stale and temporal filters are applied before retrieval.
- Conflicts can be surfaced with retrieved records.
- Duplicate information is not silently collapsed.
- AI inference remains labeled and cannot be converted into objective fact through the core model.

## What Failed Or Remains Weak

- The prototype vector provider is deterministic but not semantic. It cannot prove real embedding quality.
- Runtime latency is high because the prototype imports and scans the whole corpus for each corpus-backed run.
- Query term recall is measurable but imperfect: average `0.875` across the Phase 2.4 benchmark set.
- The optional reranker is governance-aware, not a trained relevance reranker.
- The runtime is not concurrent, persistent, or production-authenticated.

## Production Change Requirements

Before production, ADE needs:

- real PostgreSQL schema and migration plan;
- tested PostgreSQL full-text indexes;
- real pgvector or adapter-backed vector index;
- embedding model selection and cost guardrails;
- background indexing with source revision IDs;
- source revocation propagation to FTS/vector/cache/graph layers;
- production ACL and project membership enforcement;
- ranking explanation records;
- latency budgets and cache strategy;
- backup and restore drills.

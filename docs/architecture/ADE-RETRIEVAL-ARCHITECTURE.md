# ADE Retrieval Architecture

Status: Phase 2.1 architecture specification only. No vector database, embedding model, search index, or reranker is selected here.

## Purpose

ADE retrieval should select relevant, current, source-aware knowledge and memory for a task. Retrieval must be explainable: an agent should know why an item was returned and how much to trust it.

## Retrieval Flow

```text
User request
-> Intent classification
-> Relevant skills
-> Context requirements
-> Knowledge retrieval
-> Memory retrieval
-> Research decision
-> Ranking
-> Context assembly
```

## Intent Classification

ADE should identify whether the task needs:

- implementation support;
- audit/verification;
- package or framework research;
- design knowledge;
- project decision recall;
- user preference recall;
- external freshness check;
- graph relationship traversal;
- private project memory;
- no retrieval beyond current files.

## Retrieval Methods

The architecture must allow multiple methods:

- Metadata filtering: domain, type, source_type, status, freshness, version, project, access_scope.
- Keyword search: exact names, APIs, files, packages, errors, concepts.
- Semantic search: conceptual similarity through future embeddings.
- Graph retrieval: entity and relationship traversal.
- Hybrid retrieval: metadata + keyword + semantic + graph.
- Reranking: task-specific ranking after candidate retrieval.
- Temporal filtering: current, valid_at, superseded, review_by.
- Source filtering: official-only, project-only, user-provided, public, restricted.
- Confidence filtering: minimum evidence confidence or conflict status.

Phase 2.1 does not select storage or algorithms.

## Ranking Principles

A good retrieval result should be:

- relevant to the current task;
- authoritative for the claim;
- fresh enough for the domain;
- version-compatible;
- sufficiently confident;
- permitted for the agent/user;
- not superseded or unresolved unless the conflict matters;
- concise enough for context assembly.

## Research Decision

If retrieval finds no suitable current answer, ADE should decide whether to research. Research is required when:

- the domain changes quickly;
- source freshness is unknown;
- sources conflict;
- external facts are necessary;
- package/API/version behavior matters;
- existing knowledge is stale or insufficient.

## Context Assembly

Retrieved items should enter context as compact evidence packets:

```text
ITEM:
WHY_RELEVANT:
CLAIM:
SOURCE:
FRESHNESS:
CONFIDENCE:
CONFLICTS:
USE_LIMITS:
```

Agents should not receive raw dumps when a smaller sourced packet is enough.

## Memory Retrieval

Memory retrieval should be scoped by user, project, repository, sensitivity, recency, and relevance. Memory must not override stronger current source evidence without review.

## Explainability

Every retrieval set should be able to explain:

- why each item was retrieved;
- why higher-ranked items outrank lower-ranked ones;
- what was filtered out;
- whether research is needed;
- what uncertainties remain.

## Related Documents

- [ADE-KNOWLEDGE-MEMORY-CONTEXT-MODEL.md](ADE-KNOWLEDGE-MEMORY-CONTEXT-MODEL.md)
- [ADE-PROVENANCE-AND-CONFIDENCE.md](ADE-PROVENANCE-AND-CONFIDENCE.md)
- [ADE-KNOWLEDGE-GRAPH-MODEL.md](ADE-KNOWLEDGE-GRAPH-MODEL.md)

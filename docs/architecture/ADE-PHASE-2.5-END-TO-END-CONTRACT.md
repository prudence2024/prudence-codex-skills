# ADE Phase 2.5 End-to-End Retrieval Contract

## Scope

This contract proves the selected Phase 2.4 architecture without deploying production infrastructure. The implementation uses the existing 40-source / 932-item corpus only.

## Runtime Chain

`structured store -> full-text provider -> vector provider -> hybrid fusion -> optional reranker -> governance filters -> explainable result -> context packet`

## Provider-Neutral Interfaces

| Interface | Production analogue | Prototype implementation |
| --- | --- | --- |
| `StructuredStore` | PostgreSQL canonical store | `PrototypeStructuredStore` over `InMemoryKnowledgeRepository` |
| `FullTextProvider` | PostgreSQL full-text search | `PrototypeFullTextProvider` lexical token scorer |
| `VectorProvider` | pgvector | `PrototypeVectorProvider` stable local hashed token vectors |
| `Reranker` | optional rerank provider | `GovernanceReranker` |
| `KnowledgeRetrievalRuntime` | retrieval service | local orchestrator |

## Query Contract

`RuntimeQuery` carries query text, principal, project, freshness, knowledge type, `as_of`, stale inclusion, conflict inclusion, archived inclusion, limit, and rerank flag.

## Context Packet Contract

Every `ContextPacket` contains:

- original query;
- runtime metrics;
- applied filters;
- explainable results;
- source ID and source location;
- source section and original text reference;
- content type, status, freshness, derivation, access scope, project;
- evidence confidence and recommendation score;
- provider path and retrieval reason;
- conflicts and warnings.

## Non-Production Boundary

The vector provider is not a real embedding backend. It is a deterministic contract proof using stable hashed token vectors. No full-scale embedding migration was performed.

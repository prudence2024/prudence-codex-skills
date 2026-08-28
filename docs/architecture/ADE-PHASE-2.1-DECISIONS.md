# ADE Phase 2.1 Decisions

Status: Architecture decisions for Phase 2.1. No implementation decisions are final beyond the conceptual model.

## Decision 1: Architecture Before Infrastructure

ADE will define knowledge, memory, context, research, provenance, confidence, lifecycle, ingestion, retrieval, and graph compatibility before choosing storage or retrieval technology.

Rationale: selecting Graphiti, a vector database, embeddings, or a crawler before defining knowledge semantics would create tool-driven architecture.

Status: accepted.

## Decision 2: Knowledge Is Not Memory

Knowledge, memory, context, and research remain distinct concepts with different lifecycle rules.

Rationale: storing everything as generic memory would mix durable project preferences, active research, external facts, stale docs, and current task context.

Status: accepted.

## Decision 3: Provenance Is Required

A knowledge item must retain source type and provenance. AI inference may create candidates, but it must not silently become fact.

Rationale: ADE's agents must explain why they trust, doubt, or ignore retrieved information.

Status: accepted.

## Decision 4: evidence_confidence And recommendation_score Stay Separate

Evidence strength and recommendation usefulness are separate values.

Rationale: a true fact can be irrelevant, and a useful recommendation can rest on weaker evidence that must be disclosed.

Status: accepted.

## Decision 5: Conflicts Are Preserved

ADE will preserve conflicting claims until a stronger source, version boundary, temporal boundary, test, or human decision resolves them.

Rationale: overwriting conflicts hides uncertainty and creates false authority.

Status: accepted.

## Decision 6: Retrieval Must Be Explainable

Retrieval should return why items were selected, their provenance, confidence, freshness, and conflicts.

Rationale: agents need compact evidence packets, not opaque search results.

Status: accepted.

## Decision 7: Provider And Database Agnostic

Phase 2.1 does not choose Graphiti, vector databases, embeddings, crawlers, or storage engines.

Rationale: the architecture should support graph, keyword, semantic, metadata, and hybrid retrieval without lock-in.

Status: accepted.

## Decision 8: User And External Knowledge Remain Distinguishable

User-provided facts, opinions, preferences, project decisions, hypotheses, and created materials must retain their category. External knowledge must retain source, freshness, and license.

Rationale: user intent is authoritative for preferences and project decisions, not automatically for external technical facts.

Status: accepted.

## Open Decisions

- Storage format for raw sources and normalized knowledge.
- Whether to add schemas in Phase 2.2 or later.
- Embedding provider or local embedding strategy.
- Vector, graph, relational, file-based, or hybrid storage.
- Research crawler scope and permissions.
- Human review workflow for promotion and conflict resolution.
- Access-control model for user-private and project-private knowledge.
- Retention defaults for stale and sensitive knowledge.

## Deferred Decisions

- Graphiti evaluation.
- Hermes agent interface implementation.
- Personal knowledge ingestion.
- Web crawler implementation.
- Visual scraping or design-reference ingestion.
- Voice/audio source ingestion.
- UI for knowledge review.

## Related Documents

- [ADE-KNOWLEDGE-MODEL.md](ADE-KNOWLEDGE-MODEL.md)
- [ADE-KNOWLEDGE-LIFECYCLE.md](ADE-KNOWLEDGE-LIFECYCLE.md)
- [ADE-RETRIEVAL-ARCHITECTURE.md](ADE-RETRIEVAL-ARCHITECTURE.md)

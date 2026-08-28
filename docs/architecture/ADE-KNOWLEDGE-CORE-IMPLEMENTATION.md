# ADE Knowledge Core Implementation

Status: Phase 2.2 implementation document.

## Capability Boundary

The knowledge core is implemented as provider-agnostic Python schemas and in-memory/test adapters in `ecosystem/src/skill_ecosystem/knowledge_core.py`.

Implemented:

- Core schemas for `Source`, `KnowledgeItem`, `PromptRecord`, `OperationalInstruction`, `SkillCandidate`, `ResearchCandidate`, `Project`, `Decision`, `Pattern`, `Entity`, and `Relationship`.
- Provenance and confidence models with independent `evidence_confidence` and `recommendation_score` fields.
- Lifecycle states and legal transition validation for `RAW`, `EXTRACTED`, `NORMALIZED`, `CANDIDATE`, `VALIDATED`, `INDEXED`, `SUPERSEDED`, and `ARCHIVED`.
- Provider-independent repository, retrieval, graph, memory, and ingestion interfaces.
- In-memory repository, retrieval, graph, and memory adapters for tests and local validation.
- Importer for `../knowledge/ADE-EXTRACTED-ITEMS.jsonl` with validation, duplicate detection, conflict candidate preservation, and research-candidate import.
- Secret-pattern rejection during knowledge and memory import.

Not yet implemented:

- Hermes integration.
- Telegram integration.
- Autonomous self-learning.
- Production crawler.
- Production memory ingestion.
- Graphiti or any graph database.
- Vector database, embeddings, semantic search backend, hybrid retrieval backend, or reranker.
- UI for knowledge review and promotion.

## Modules

`knowledge_core.py` contains the Phase 2.2 implementation. It is deliberately separate from the older `knowledge.py` design-pattern loader so existing design-intelligence behavior remains unchanged.

## Schemas

The schema layer uses standard-library dataclasses and enums. No new runtime dependency was added.

Core object groups:

- Source and provenance: `Source`, `Provenance`, `SourceDerivation`.
- Knowledge: `KnowledgeItem`, `KnowledgeType`, `Freshness`, `KnowledgeStatus`.
- Confidence: `Confidence`.
- Corpus-derived operational objects: `PromptRecord`, `OperationalInstruction`, `SkillCandidate`, `ResearchCandidate`.
- Project and decision objects: `Project`, `Decision`, `Pattern`.
- Graph objects: `Entity`, `Relationship`.
- Memory object: `MemoryRecord`.
- Observability/reporting: `ImportReport`, `DuplicateRecord`, `ConflictRecord`.

Required fields are enforced in dataclass validation for the implemented objects that participate in import and repository operations. Optional and derived fields remain explicit Python optional fields rather than meaningless placeholders.

## Provenance

Every imported `KnowledgeItem` receives a `Provenance` record preserving source ID, source location, source section, original text reference, observed time, extraction time, derivation type, and transformation chain. Records missing provenance are rejected and counted.

## Confidence

`Confidence` preserves two independent values:

- `evidence_confidence`: strength of the supporting evidence.
- `recommendation_score`: usefulness for a specific recommendation.

High evidence confidence does not imply high recommendation score. Tests cover that these fields can diverge.

## Lifecycle

Legal state transitions are implemented through `ensure_transition()` and `KnowledgeItem.transition()`.

Valid lifecycle states:

```text
RAW
EXTRACTED
NORMALIZED
CANDIDATE
VALIDATED
INDEXED
SUPERSEDED
ARCHIVED
```

Invalid jumps, such as `RAW -> INDEXED`, raise `KnowledgeCoreError`.

## Repository Interface

`KnowledgeRepository` defines `create()`, `get()`, `update()`, `delete()`, `search()`, `list()`, and `supersede()`. `InMemoryKnowledgeRepository` implements these methods for tests and local validation only. It is not a production database.

## Retrieval Interface

`RetrievalInterface` supports `keyword_search()`, `semantic_search()`, `hybrid_search()`, `filter()`, `rank()`, and `retrieve_context()`.

Implemented backend:

- Keyword and metadata filtering through the in-memory repository.
- Context packet construction with provenance and confidence metadata.

Supported interface only:

- `semantic_search()` raises `UnsupportedBackendError` because embeddings are not implemented.
- `hybrid_search()` raises `UnsupportedBackendError` because semantic retrieval is not implemented.

## Graph Abstraction

`GraphInterface` defines `create_entity()`, `create_relationship()`, `find_related()`, and `get_relationships()`. `InMemoryGraph` implements relationship preservation for tests. It does not install or depend on Graphiti.

## Memory Abstraction

`MemoryStore` stores `MemoryRecord` objects separately from the knowledge repository. Categories include `project_memory`, `decision_memory`, `workflow_memory`, `preference_memory`, and `historical_state`.

This maintains the Phase 2.1 rule that knowledge is not memory.

## Ingestion

`IngestionInterface` defines `ingest()`, `parse()`, `extract()`, `normalize()`, and `validate()`. `CorpusImporter` implements validation and normalization for the existing Phase 2.1 JSONL extraction. It does not crawl, execute source content, or promote records to validated durable knowledge.

## Corpus Import

The importer reads `../knowledge/ADE-EXTRACTED-ITEMS.jsonl`, validates each record, preserves source IDs and source locations, rejects malformed records, detects duplicate/overlapping content, preserves conflict candidates, and imports `STALE_CANDIDATE` records into `ResearchCandidate` objects.

## Limitations

- The current implementation is a foundation for schemas and tests, not production storage.
- Search is local keyword/metadata only.
- Conflict detection is representation-level and import-signal based; it does not resolve claims.
- Duplicate detection is deterministic and conservative, not semantic.
- Source freshness is preserved as a review signal, not independently verified.

## Deferred Implementations

- Embeddings and vector retrieval.
- Graph database selection or Graphiti evaluation.
- Production persistence.
- Human review workflow.
- Access-control and retention policy enforcement beyond secret-pattern rejection.
- Research crawler and current-source verification.

## Validation

Implemented tests live in `../../tests/test_knowledge_core.py` and cover schema validation, provenance, confidence independence, lifecycle transitions, duplicate handling, conflict handling, research candidates, retrieval filters, malformed records, missing provenance, unsupported records, graph relationships, memory separation, and import of the Phase 2.1 extraction fixture.

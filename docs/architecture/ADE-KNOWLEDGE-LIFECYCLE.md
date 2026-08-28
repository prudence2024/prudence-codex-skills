# ADE Knowledge Lifecycle

Status: Phase 2.1 architecture specification only.

## Lifecycle Overview

```text
Discovered -> Ingested -> Extracted -> Normalized -> Validated -> Indexed -> Retrieved -> Updated -> Superseded -> Archived
```

No stage implies automatic belief. Each stage must preserve provenance and uncertainty.

## Stages

### Discovered

ADE becomes aware of a possible source or claim. Discovery can come from user files, web research, repository docs, tests, reports, package registries, GitHub, or future media.

Output: source candidate, not knowledge.

### Ingested

ADE captures source metadata and raw content references within allowed privacy, licensing, and access boundaries.

Output: raw source record with provenance.

### Extracted

ADE identifies claims, entities, procedures, patterns, observations, decisions, or hypotheses from the source.

Output: extracted candidate items.

### Normalized

ADE converts extracted material into a consistent conceptual shape: type, domain, summary, source type, provenance, timestamps, topics, entities, and confidence fields.

Output: normalized candidate knowledge.

### Validated

ADE checks authority, freshness, specificity, corroboration, conflicts, version relevance, evidence quality, privacy, and licensing.

Output: validated knowledge, unresolved candidate, rejected item, or escalation request.

### Indexed

ADE prepares the item for retrieval through one or more future retrieval mechanisms: metadata filters, keyword search, graph relationships, semantic search, hybrid retrieval, or reranking.

Output: retrieval-ready knowledge. Phase 2.1 does not implement indexes.

### Retrieved

ADE retrieves candidate knowledge for a task, with ranking, explanation, provenance, and confidence.

Output: retrieval result set for context assembly.

### Updated

ADE refreshes a knowledge item when sources change, versions change, project decisions change, conflicts appear, or outcomes disprove assumptions.

Output: revised item with update provenance.

### Superseded

ADE marks an item as no longer current while preserving history and references.

Output: active replacement plus supersession relationship.

### Archived

ADE removes an item from ordinary retrieval while retaining it for audit or historical purposes when appropriate.

Output: archived item with reason.

## Promotion Rules

Raw source can become knowledge only if it has:

- source identity;
- source type;
- provenance;
- observed date;
- lifecycle status;
- confidence or explicit uncertainty;
- conflict state;
- scope and access rules.

Research becomes durable knowledge only after synthesis, validation, and promotion. Temporary search results should expire or be archived.

## Retention Rules

Do not permanently store:

- secrets or credentials;
- irrelevant pages;
- duplicate content without added evidence;
- stale information without historical value;
- unsupported claims;
- transient conversation details;
- private personal information without justification;
- licensed content beyond permitted use.

## Update Triggers

- New official version or release.
- Source update or deletion.
- Conflicting source appears.
- Project decision supersedes old decision.
- Runtime/test evidence disproves the item.
- User corrects preference or project fact.
- Freshness deadline expires.

## Related Documents

- [ADE-KNOWLEDGE-MODEL.md](ADE-KNOWLEDGE-MODEL.md)
- [ADE-PROVENANCE-AND-CONFIDENCE.md](ADE-PROVENANCE-AND-CONFIDENCE.md)
- [ADE-INGESTION-ARCHITECTURE.md](ADE-INGESTION-ARCHITECTURE.md)

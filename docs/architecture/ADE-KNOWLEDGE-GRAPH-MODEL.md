# ADE Knowledge Graph Model

Status: Phase 2.1 architecture specification only. This document does not install Graphiti, select a graph database, or implement graph storage.

## Purpose

ADE should be compatible with graph-based knowledge where relationships, temporal validity, provenance, and conflict handling improve retrieval. The model is abstract and provider-agnostic.

## When Graph Structure Is Appropriate

Use graph-compatible modeling when ADE needs to answer relationship questions:

- Which decisions affect this file or project?
- Which packages provide this capability and depend on these versions?
- Which sources support or contradict this claim?
- Which design patterns apply to this industry and interaction type?
- Which observations superseded older assumptions?

Do not use graph storage for simple one-off notes, flat lists, or facts that will never be queried by relationship.

## Core Objects

### Entity

An entity is a durable node-like concept:

```text
id
entity_type
name
aliases
properties
created_at
observed_at
provenance
confidence
status
```

Examples: package, framework, API, skill, source, project, file, decision, design_pattern, user_preference, provider, incident, requirement.

### Relationship

A relationship connects entities with provenance and time:

```text
id
from_entity
to_entity
relationship_type
properties
valid_from
valid_until
observed_at
provenance
confidence
status
```

Examples: depends_on, supersedes, conflicts_with, supports, derived_from, observed_in, implemented_in, verified_by, authored_by, applies_to, uses, deprecated_by.

### Property

A property is an attributed value on an entity or relationship. Important properties should preserve source and time if they can change.

### Temporal Validity

Temporal metadata should represent:

- when a claim was observed;
- when it became valid;
- when it stopped being valid;
- when it was superseded;
- when it should be reviewed.

### Provenance

Every entity and relationship derived from a source must retain provenance. Graph retrieval is not proof without provenance.

### Confidence

Graph confidence should be attached to entities, relationships, and retrieval results. A highly connected node is not automatically true.

## Conflict Model

Conflicts should be first-class relationships, not destructive overwrites.

```text
Entity/Claim A --conflicts_with--> Entity/Claim B
```

Conflict records should include source comparison, version boundaries, time boundaries, and resolution status.

## Graph And Memory

Graph structure can support memory, but memory policy remains separate. `memory-engineering` decides what should be retained. The graph model decides how relationship-heavy retained knowledge may be represented.

## Graph And Retrieval

Graph retrieval should support:

- entity expansion;
- relationship traversal;
- temporal filtering;
- provenance filtering;
- confidence filtering;
- conflict surfacing;
- path explanation.

## Graphiti Compatibility

Graphiti may be evaluated later as one possible temporal graph implementation. ADE must not depend on Graphiti as the architecture. The graph interface should remain abstract enough to support other graph stores or simpler implementations.

## Example

```text
Entity: React
Entity: React 19
Entity: useActionState API
Relationship: React 19 introduces useActionState API
Provenance: official React release notes URL
Observed_at: date ADE checked source
Confidence: established if source/version verified
```

## Related Documents

- [ADE-KNOWLEDGE-MODEL.md](ADE-KNOWLEDGE-MODEL.md)
- [ADE-RETRIEVAL-ARCHITECTURE.md](ADE-RETRIEVAL-ARCHITECTURE.md)
- [ADE-PROVENANCE-AND-CONFIDENCE.md](ADE-PROVENANCE-AND-CONFIDENCE.md)

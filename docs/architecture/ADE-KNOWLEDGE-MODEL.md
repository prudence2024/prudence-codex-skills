# ADE Knowledge Model

Status: Phase 2.1 architecture specification only. This document defines concepts and requirements. It does not implement a database, embeddings, Graphiti, Hermes integration, crawlers, or ingestion jobs.

## Purpose

ADE knowledge is retrievable, attributable information that can improve agent decisions across engineering, design, business, research, and project work. Knowledge is not automatically true because it was discovered. A knowledge item must preserve origin, freshness, confidence, uncertainty, and conflict state.

Knowledge differs from memory, current context, and active research. See [ADE-KNOWLEDGE-MEMORY-CONTEXT-MODEL.md](ADE-KNOWLEDGE-MEMORY-CONTEXT-MODEL.md).

## Knowledge Categories

ADE should support these categories without hard-coding storage technology:

- Technical Knowledge: framework behavior, APIs, versions, packages, security advisories, deprecations, compatibility notes, and implementation constraints.
- Design Knowledge: design patterns, visual principles, interaction patterns, accessibility behavior, responsive behavior, motion patterns, and normalized website-reference observations.
- Engineering Knowledge: verification methods, system-breaker findings, implementation practices, reliability patterns, state-machine patterns, and regression strategies.
- Business Knowledge: product constraints, pricing rules, operational policies, customer segments, legal/business requirements, and commercial assumptions.
- Project Knowledge: repository-specific architecture, decisions, constraints, active systems, code ownership, accepted patterns, and known risks.
- User/Project Preferences: stable preferences, working style, brand constraints, and project-specific expectations deliberately retained with provenance.
- Research Findings: synthesized claims from a research process, including source quality, conflicts, confidence, and promotion status.
- External Knowledge: current official docs, web research, package updates, GitHub releases, industry trends, and ecosystem changes.
- Experimental Knowledge: observations from tests, prototypes, measurements, or field trials that are useful but not yet established.

## Knowledge Types

Knowledge items must distinguish what kind of claim they represent:

- Fact: a verifiable statement about a source, version, release, file, decision, or observed behavior.
- Concept: an explanatory idea or model.
- Procedure: repeatable steps for a task.
- Pattern: a reusable solution with context, trade-offs, and evidence.
- Decision: a choice made by ADE, the user, or a project, including rationale and alternatives.
- Observation: something measured, tested, or seen.
- Hypothesis: a plausible but unvalidated claim.
- Research Finding: a synthesized result from multiple or ranked sources.

These must not collapse into a single generic note type because retrieval, confidence, and update behavior differ.

## Conceptual Knowledge Object

ADE should model a knowledge item with the smallest field set that preserves provenance, retrieval, confidence, freshness, and lifecycle.

### Required Fields

- `id`: stable identifier for references, supersession, and audit trails.
- `type`: fact, concept, procedure, pattern, decision, observation, hypothesis, or research_finding.
- `title`: human-readable label for retrieval and review.
- `summary`: short statement of what the item says and why it matters.
- `content`: the claim, procedure, pattern, or decision in usable form.
- `domain`: technical, design, engineering, business, project, user_preference, research, external, or experimental.
- `source_type`: official_documentation, educational_material, community_source, user_provided_content, project_decision, experimental_observation, ai_inference, or research_synthesis.
- `provenance`: evidence chain showing where the item came from.
- `observed_at`: when ADE observed or captured the source.
- `status`: discovered, ingested, extracted, normalized, validated, indexed, active, superseded, archived, rejected, or unresolved.
- `confidence`: ADE's overall confidence in using the item.
- `evidence_confidence`: confidence in the supporting evidence, separate from recommendation usefulness.

### Optional Fields

- `source_url`: URL when the source is web-accessible.
- `source_path`: repository or local path when the source is local.
- `author`: source author, maintainer, project owner, or user, when known.
- `created_at`: source creation date, when known.
- `updated_at`: source update date or last validation date.
- `version`: relevant package, API, framework, project, or document version.
- `topics`: retrieval tags.
- `entities`: people, packages, projects, files, concepts, skills, providers, or systems mentioned.
- `relationships`: links to entities or other knowledge items.
- `project`: project or repository scope.
- `freshness`: current, time_sensitive, stale_risk, stale, unknown, or review_by date.
- `license`: usage constraints for source or derived knowledge.
- `access_scope`: public, project_private, user_private, restricted, or secret_disallowed.
- `conflicts`: references to knowledge items or sources that disagree.
- `supersedes` / `superseded_by`: lifecycle continuity.

### Derived Fields

- `recommendation_score`: usefulness for a particular decision or recommendation. This is derived from evidence, context fit, risk, and recency; it must not replace evidence confidence.
- `retrieval_score`: query-time score from keyword, semantic, graph, freshness, source, and confidence ranking.
- `staleness_score`: computed from source type, update cadence, age, version mismatch, and known change rate.
- `authority_rank`: computed from source type and source-specific trust rules.

## Design Knowledge Shape

A design pattern item should include:

```text
name:
purpose:
context:
industry:
visual_characteristics:
interaction:
responsive_behavior:
accessibility:
motion:
examples:
sources:
confidence:
```

Website references should eventually move through: capture source -> extract observations -> normalize into design pattern candidates -> score confidence -> review conflicts/licensing -> promote validated patterns. Visual scraping is out of scope for Phase 2.1.

## Technical Knowledge Shape

Technical knowledge must preserve versions and dates. Useful technical item types include:

- Package
- Framework
- API
- Version
- Feature
- Breaking change
- Deprecation
- Best practice
- Security advisory

Outdated documentation must not be treated as current truth. If the version is unknown for a fast-moving tool, the item should be marked `freshness: unknown` or `stale_risk`.

## User-Provided Knowledge

User-provided information must be classified as one of:

- User-provided fact
- User opinion
- User preference
- User project decision
- User hypothesis
- User-created material

User statements are authoritative for user intent and preferences, but not automatically authoritative for external technical facts.

## Storage-Agnostic Requirement

This model must work with files, relational stores, graph stores, vector stores, search indexes, or hybrid systems later. Phase 2.1 does not select storage.

## Related Documents

- [ADE-KNOWLEDGE-MEMORY-CONTEXT-MODEL.md](ADE-KNOWLEDGE-MEMORY-CONTEXT-MODEL.md)
- [ADE-PROVENANCE-AND-CONFIDENCE.md](ADE-PROVENANCE-AND-CONFIDENCE.md)
- [ADE-KNOWLEDGE-LIFECYCLE.md](ADE-KNOWLEDGE-LIFECYCLE.md)
- [ADE-KNOWLEDGE-GRAPH-MODEL.md](ADE-KNOWLEDGE-GRAPH-MODEL.md)

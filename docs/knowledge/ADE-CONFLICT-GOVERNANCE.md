# ADE Conflict Governance

## Current State

The Phase 2.3 work order identifies 288 conflict candidates. These are candidates, not confirmed contradictions.

## Conflict Classes

| Class | Meaning | Handling |
| --- | --- | --- |
| Genuine contradiction | Two sources cannot both be true in the same scope/time/version. | Preserve both, attach evidence, require resolution status. |
| Version difference | Claims apply to different versions. | Preserve version fields and mark version scope. |
| Temporal difference | Claims were true at different times. | Preserve observed/extracted timestamps and freshness notes. |
| Scope difference | Claims apply to different projects/domains. | Scope by project, source type, and access boundary. |
| Terminology difference | Different labels for compatible ideas. | Link as related terms, not contradiction. |
| Duplicate | Same or overlapping material. | Mark `DUPLICATE / OVERLAPPING`, do not delete. |
| False positive | Candidate conflict created by extraction ambiguity. | Keep audit record; do not block retrieval if harmless. |
| Unresolved | Insufficient evidence. | Send to research/review queue. |

## Runtime Representation

The knowledge core has `ConflictRecord` with source item IDs, conflict type, description, severity, resolution, resolver, and timestamp. This is adequate for staging representation. Future production storage must add queryable conflict status, affected claim/version/scope fields, and retrieval-time conflict surfacing.

## Retrieval Rule

A retrieval answer must not say "the current recommended approach" from conflicting material unless it can show which evidence is current, which is stale, and why a recommendation was derived.

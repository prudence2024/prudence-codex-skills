# ADE Hermes Interface

## Boundary

Hermes is an agent/orchestrator. ADE remains responsible for source fidelity, knowledge governance, memory policy, retrieval, provenance, access control, research promotion, and lifecycle state.

## Abstract Agent-Facing API

| Operation | Purpose | ADE responsibility |
| --- | --- | --- |
| `retrieve_knowledge(query, principal, filters)` | Return explainable knowledge context. | Enforce ACL, provenance, freshness, lifecycle, conflict warnings. |
| `retrieve_memory(scope, principal)` | Return relevant scoped memory. | Keep memory separate from source knowledge and context. |
| `build_context(task, retrieved_items)` | Create task context packet. | Preserve source/inference/recommendation boundaries. |
| `request_research(claim, reason)` | Add claim to research queue. | Require current source verification before promotion. |
| `inspect_provenance(item_id)` | Explain where an item came from. | Return source ID, raw location, text reference, hash status, transformations. |
| `submit_observation(observation)` | Record runtime/test observation. | Store as observation, not fact, until validated. |
| `submit_candidate_knowledge(candidate)` | Propose knowledge. | Validate provenance, classification, freshness, conflicts, and ACL. |
| `report_task_outcome(outcome)` | Capture agent work result. | Store evidence separately from claims and recommendations. |

## Non-Goals

Hermes must not become the database, bypass ADE retrieval filters, promote source content to instructions, or treat retrieved prompts as executable control text.

## Readiness Gate

Hermes can consume ADE retrieval only after production ACL, source revocation, audit logs, backup/restore, embedding versioning, and retrieval monitoring are implemented and tested.

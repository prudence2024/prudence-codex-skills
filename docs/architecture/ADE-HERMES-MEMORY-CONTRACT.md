# ADE Hermes Memory Contract

Generated: 2026-08-29T12:26:27.616484+00:00

## Principle

Memory is scoped, attributable, reviewable, and revocable. Hermes may request or propose memory, but arbitrary agent text must not silently become durable ADE memory.

## Read Operations

- Retrieve project decisions.
- Retrieve persistent preferences relevant to the current task.
- Retrieve prior task state.
- Retrieve stale/conflicting memory with warnings when explicitly requested.

## Write Operations

- `propose_memory(candidate)` creates `candidate_for_review` records.
- Durable memory write requires promotion checks: scope, provenance, sensitivity, freshness, conflict review, and owner approval where needed.
- `mark_memory_stale` and `resolve_memory_conflict` must preserve history rather than overwrite silently.

## Response Requirements

Memory responses must include memory ID, scope, category, provenance, observed date, sensitivity/access scope, freshness, and status.

## Boundary With Hermes Memory

Hermes documents built-in memory and external memory providers. ADE should not rely on Hermes memory as the canonical ADE knowledge store. If Hermes memory is useful later, it should receive summarized task context, not raw private corpus data by default.


## Sources Used

- ADE local: `docs/architecture/ADE-HERMES-INTERFACE.md`
- ADE local: `docs/ADE-PHASE-2.5-FINAL-GATE.md`
- ADE local: `docs/architecture/ADE-KNOWLEDGE-MEMORY-CONTEXT-MODEL.md`
- ADE local: `docs/architecture/ADE-RETRIEVAL-ARCHITECTURE.md`
- ADE local: `docs/architecture/ADE-KNOWLEDGE-LIFECYCLE.md`
- ADE local: `ecosystem/src/skill_ecosystem/knowledge_runtime.py`
- ADE local: `ecosystem/registry/skills.json`
- Hermes official docs: [Quickstart](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/getting-started/quickstart.md)
- Hermes official docs: [Tools & Toolsets](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/tools.md)
- Hermes official docs: [MCP guide](https://github.com/hermes-agent-org/hermes/blob/main/website/docs/guides/use-mcp-with-hermes.md)
- Hermes official docs: [Integrations](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/index.md)
- Hermes official docs: [Plugins](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/plugins.md)
- Hermes official docs: [Memory Providers](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/memory-providers.md)
- Hermes official docs: [AI Providers](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md)
- Hermes official docs: [CLI Commands](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/cli-commands.md)
- Hermes official releases: [Releases](https://github.com/NousResearch/hermes-agent/releases)


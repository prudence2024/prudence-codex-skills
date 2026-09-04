# ADE Hermes Failure Model

Generated: 2026-08-29T12:26:27.616484+00:00

## Failure Behaviors

| Failure | Expected Behavior |
| --- | --- |
| ADE unavailable | Hermes reports integration unavailable and continues without pretending ADE context was applied. |
| Hermes unavailable | ADE remains intact; no corpus mutation occurs. |
| Retrieval timeout | Bounded retry, then explicit failure or partial response marked incomplete. |
| Empty retrieval | Return empty packet with metrics and research decision. |
| Stale knowledge | Return warning or require current research depending on task risk. |
| Revoked source | Exclude from default retrieval and surface revocation status where inspected. |
| Conflicting sources | Return conflicts explicitly; do not auto-resolve. |
| Malformed request | Reject with validation error; do not default to broad private retrieval. |
| Unauthorized request | Fail closed before retrieval results are assembled. |
| Tool failure | Hermes owns tool recovery; ADE records observation only if submitted. |
| Model failure | Hermes owns model fallback; ADE context remains versioned and reusable. |

## Retry Policy

Retries must be bounded and observable. Failure must not be disguised as successful execution.

## Recovery Evidence

A recovered task should record request ID, failure class, retry count, final state, selected skills, retrieved knowledge IDs, and whether verification ran.


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


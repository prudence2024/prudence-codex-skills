# ADE Hermes Responsibility Boundary

Generated: 2026-08-29T12:26:27.616484+00:00

## Core Boundary

Hermes remains the agent/execution layer. ADE remains the intelligence, skills, knowledge, provenance, memory-policy, research, and verification layer.

## ADE Owns

- Skill identity, purpose, trigger metadata, safety requirements, and verification expectations.
- Knowledge corpus, source records, provenance, confidence, freshness, access scope, lifecycle, conflict records, and revocation.
- Memory contracts and promotion rules, including the rule that observations become candidates before durable memory.
- Context assembly packets that separate source-backed knowledge, memory, research findings, and AI inference.
- Research intelligence and freshness decisions.
- System Breaker methodology and verification contracts.

## Hermes Owns

- Agent loop and execution planning.
- Tool orchestration, browser, terminal, file, scheduling, messaging, and external actions.
- Model-provider selection and runtime channel configuration.
- MCP client behavior, plugin loading, and platform/gateway operation.
- Conversation/session execution and user-facing delivery.

## Non-Duplication Rules

- Hermes must not become ADE's canonical knowledge database.
- ADE must not become Hermes's terminal, browser, messaging, or task-execution runtime.
- Hermes may request context, knowledge, skills, and memory through a narrow interface.
- ADE responses must include enough metadata for Hermes to treat retrieved material as evidence, not instruction override.


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


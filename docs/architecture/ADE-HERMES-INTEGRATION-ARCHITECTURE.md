# ADE Hermes Integration Architecture

Generated: 2026-08-29T12:26:27.616484+00:00

## Reconnaissance Finding

No local Hermes Agent checkout was found under `C:/Users/User/desktop` or `C:/Users/User/Documents`; only unrelated `node_modules/hermes-estree` and `node_modules/hermes-parser` directories were found. Therefore this plan is based on ADE local code inspection plus official Hermes documentation, not local Hermes source-code inspection.

## Recommended First Integration Path

Use an ADE MCP server as the first integration path.

Reasoning:

- Hermes documentation describes MCP as the adapter layer for external local or remote systems with per-server tool filtering.
- MCP lets ADE expose a small, whitelisted surface without changing Hermes core.
- ADE already has provider-neutral runtime interfaces and a `HermesRuntimeAdapter` contract.
- A CLI-only bridge is simpler but weaker for typed tool discovery and access filtering.
- A native Hermes plugin may become useful later, but it requires a concrete Hermes installation and plugin test harness first.

## Initial Flow

```text
User
-> Hermes
-> ADE MCP adapter
-> ADE skill discovery
-> ADE knowledge retrieval
-> ADE memory contract
-> ADE context assembly
-> Hermes execution
-> ADE verification / System Breaker context
-> result
```

## Candidate Transport Order

1. MCP server over stdio for local-first integration.
2. Local HTTP service only if Hermes deployment mode needs cross-process or remote access.
3. Native Hermes plugin only after a local Hermes checkout/install is verified and plugin lifecycle hooks are tested.
4. CLI bridge as a fallback for manual development, not the primary integration contract.

## Exposed ADE Operations

- `ade.list_skills`
- `ade.get_skill_contract`
- `ade.retrieve_knowledge`
- `ade.retrieve_memory`
- `ade.assemble_context`
- `ade.inspect_provenance`
- `ade.request_research`
- `ade.record_observation`
- `ade.propose_memory`
- `ade.verify_context_packet`

## Explicit Non-Goals

No PostgreSQL deployment, pgvector deployment, Qdrant install, production embedding migration, corpus migration, NotebookLM integration, or Hermes core modification is part of this reconnaissance task.


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


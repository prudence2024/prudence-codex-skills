# ADE Hermes Integration Decisions

Generated: 2026-08-29T12:26:27.616484+00:00

## Decision 1: Use MCP First

Status: selected for first implementation task after review.

Rationale: Hermes official docs describe MCP as a clean adapter layer for local or remote systems with tool filtering. ADE can expose a small whitelisted tool surface without modifying Hermes core.

Rejected alternatives:

- Direct corpus migration into Hermes: rejected because it would make Hermes the ADE knowledge database.
- Native Hermes plugin first: deferred until a local Hermes install/checkout is inspected and plugin lifecycle is tested.
- CLI-only bridge first: useful for debugging, but weaker than MCP for discoverability, typed tool contracts, and least-privilege exposure.
- HTTP service first: useful later for remote deployment, but local stdio MCP is smaller and easier to secure initially.

## Decision 2: Do Not Integrate Yet

Status: enforced.

This task produced reconnaissance and integration planning only. No Hermes install, production deployment, corpus migration, database deployment, embedding migration, or skill redesign was performed.

## Decision 3: ADE Keeps Governance

Status: selected.

ADE must keep access control, provenance, confidence, lifecycle, memory-promotion, and source-revocation decisions. Hermes may execute tasks using ADE context but must not bypass ADE retrieval policy.


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


# ADE Hermes Pre-Integration Report

Generated: 2026-08-29T12:26:27.616484+00:00

## Executive Summary

ADE is ready for a planned Hermes integration path, but the full integration was not implemented in this task. The recommended first integration is a narrow ADE MCP server exposing skill discovery, knowledge retrieval, memory retrieval/proposal, context assembly, provenance inspection, research request, and observation recording.

## ADE Inspection

Inspected local ADE architecture and runtime files. ADE currently exposes provider-neutral runtime concepts for knowledge retrieval, provenance/confidence packets, access scopes, source revocation, corpus integrity, observability, retry, memory contract, graph contract, and a `HermesRuntimeAdapter` boundary. The current skills registry exists at `ecosystem/registry/skills.json` and should be the integration source for skill metadata.

## Hermes Inspection

Official Hermes documentation describes:

- desktop and CLI installation paths;
- provider setup through `hermes model` and broad model-provider support;
- built-in tools/toolsets for web, browser, terminal/files, media, orchestration, memory, scheduling, messaging, and MCP integrations;
- plugin types for general plugins, memory providers, context engines, and model providers;
- memory providers as pluggable backends with built-in memory remaining active;
- messaging gateway support;
- MCP server integration with per-server tool filtering;
- current releases, with latest observed release `Hermes Agent v0.18.2 (2026.7.7.2)` on the releases page.

No local Hermes Agent checkout was found, so local Hermes API/source validation remains a next-step blocker before implementation details are frozen.

## Capability Matrix

See `docs/architecture/ADE-HERMES-CAPABILITY-MATRIX.md`.

## Responsibility Boundary

See `docs/architecture/ADE-HERMES-RESPONSIBILITY-BOUNDARY.md`.

## First Integration Path

Use MCP first. Expose a minimal ADE tool surface and require Hermes to pass a principal/access context on every retrieval request. Do not migrate ADE knowledge into Hermes memory.

## Security

Main risks are overbroad MCP exposure, private-source leakage, agent-originated memory promotion, prompt-injection content being treated as instructions, and logs containing sensitive source text. Controls are documented in `docs/architecture/ADE-HERMES-SECURITY-BOUNDARY.md`.

## Failure Handling

Failure behavior is documented in `docs/architecture/ADE-HERMES-FAILURE-MODEL.md`. Key rule: a failed ADE lookup must not look like successful Hermes execution with ADE context applied.

## Observability

Initial integration should log request ID, agent/task ID, selected skill IDs, retrieved knowledge IDs, source IDs, confidence bands, memory reads/writes, verification status, failures, and retries. Avoid full private source text in routine logs.

## Validation Plan

This reconnaissance task changes documentation only. Validation should confirm strict repository validation, no broken Markdown links, no registry changes, and no skill regressions.

## Blocked / Not Verified

- Local Hermes source/API/plugin code was not inspected because no local Hermes Agent checkout was found.
- No live Hermes installation was configured or run.
- No MCP server was implemented.
- No production ADE storage, embeddings, or graph infrastructure was deployed.

## Final Verdict

HERMES_INTEGRATION_PLAN_READY


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


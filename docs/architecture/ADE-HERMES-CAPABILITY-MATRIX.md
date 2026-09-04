# ADE Hermes Capability Matrix

Generated: 2026-08-29T12:26:27.616484+00:00

| Hermes Capability | ADE Capability | Integration Method | Status |
| --- | --- | --- | --- |
| Skills | Skill registry and `SKILL.md` contracts | `ade.list_skills`, `ade.get_skill_contract` over MCP | Ready for first adapter |
| Knowledge retrieval | `KnowledgeRetrievalRuntime`, provenance/confidence packets | `ade.retrieve_knowledge` | Ready as non-production runtime boundary |
| Memory | Memory contract, candidate promotion rules | `ade.retrieve_memory`, `ade.propose_memory` | Ready as contract; durable production backend deferred |
| Context assembly | `HermesRuntimeAdapter.retrieve_context` | `ade.assemble_context` | Ready as contract |
| Research | Research decision and queue concepts | `ade.request_research` | Contract ready; live research workflow deferred |
| Tool execution | Not ADE-owned | Hermes built-in tools | Hermes owns |
| Browser | Not ADE-owned | Hermes browser toolset | Hermes owns |
| Terminal | Not ADE-owned | Hermes terminal toolset | Hermes owns |
| Scheduling | Not ADE-owned | Hermes cronjob/gateway | Hermes owns |
| Messaging | Not ADE-owned | Hermes gateway/platforms | Hermes owns |
| Observability | ADE structured runtime events | Event sink or MCP response metadata | Boundary ready; vendor deferred |
| Verification | System Breaker methodology and test contracts | Context packet + verification request | Plan ready |
| Provenance | Source ID/location/section/original reference | Included in every result | Ready |
| Confidence | evidence confidence + recommendation score | Included in every result | Ready |
| Source filtering | source/project/freshness/status filters | ADE-side filter parameters | Ready |
| Access control | principal/projects/access scopes | Required request field | Ready in runtime; production auth binding deferred |


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


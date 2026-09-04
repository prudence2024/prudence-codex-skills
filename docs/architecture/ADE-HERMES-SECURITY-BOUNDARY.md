# ADE Hermes Security Boundary

Generated: 2026-08-29T12:26:27.616484+00:00

## Trust Model

Hermes is an authorized caller only when it presents an ADE principal with allowed projects and access scopes. ADE must enforce access before response construction.

## Prevent

- Unauthorized knowledge retrieval.
- Cross-project or private-source leakage.
- Arbitrary memory writes.
- Secret exposure in returned context or logs.
- Source boundary bypass.
- Privilege escalation through Hermes tool calls.
- Tool-generated observations becoming trusted knowledge automatically.
- Prompt/instruction injection stored in knowledge becoming executable instructions.

## Controls

- Require principal on every request.
- Use least-privilege MCP tool exposure.
- Return metadata-rich context packets rather than raw corpus dumps.
- Keep content, provenance, confidence, and warnings together.
- Log IDs and classifications, not full private source text unless explicitly needed.
- Block or redact secret-like content at import and response boundaries.
- Treat all Hermes-originated memory writes as candidates pending ADE promotion.

## System Breaker Scenarios

- Anonymous principal requests restricted source: expect empty/unauthorized response.
- Project A principal requests Project B memory: expect no data.
- Prompt-injection source is retrieved: expect warning and data-only classification.
- Revoked source is requested: expect excluded result plus revocation evidence.
- Conflicting source is retrieved: expect conflict surfaced, not hidden.


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


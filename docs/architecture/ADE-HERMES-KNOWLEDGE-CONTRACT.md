# ADE Hermes Knowledge Contract

Generated: 2026-08-29T12:26:27.616484+00:00

## Request Shape

```json
{
  "query": "string",
  "domains": ["string"],
  "knowledge_types": ["fact", "procedure", "prompt", "instruction", "pattern", "decision", "hypothesis", "research_finding", "ai_inference"],
  "source_types": ["Official documentation", "User-provided source", "Project decision"],
  "project_scope": "string|null",
  "freshness": "current|time_sensitive|stale_risk|stale|unknown|null",
  "confidence_threshold": 0.0,
  "include_stale": false,
  "include_archived": false,
  "limit": 5,
  "principal": {"id": "string", "projects": ["string"], "access_scopes": ["global"]}
}
```

## Response Shape

Return an explainable context packet, not raw internal database rows. Each result must include:

- item ID and title;
- content/claim excerpt;
- source ID and source location;
- source section and original text reference;
- knowledge type;
- lifecycle status;
- freshness;
- access scope;
- derivation;
- evidence confidence and recommendation score;
- conflict IDs;
- warnings;
- why the item was retrieved.

## Filtering Rules

ACL, lifecycle, stale, project, freshness, version, and confidence filters happen inside ADE before returning anything to Hermes. Hermes must not receive inaccessible data and then decide whether to hide it.

## Research Escalation

ADE should return a research decision when results are empty, stale, conflicted, below confidence threshold, or version-sensitive.


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


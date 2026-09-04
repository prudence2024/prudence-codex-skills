# ADE Hermes Skill Contract

Generated: 2026-08-29T12:26:27.616484+00:00

## Discovery Operation

`ade.list_skills` returns skill contracts, not filesystem paths as the primary interface.

Each skill contract should include:

- stable skill ID;
- display name;
- purpose;
- trigger/description;
- category;
- required inputs;
- expected outputs;
- safety requirements;
- dependencies;
- verification requirements;
- source path for audit only.

## Invocation Model

Hermes should use ADE skills as procedural guidance for the current task. Skills are not executable shell scripts by default and must not override the active user request or higher-priority system/developer instructions.

## ADE Current Exposure

ADE can expose the skill registry from `ecosystem/registry/skills.json` and first-party `SKILL.md` descriptions. The registry contains first-party skill metadata plus read-only upstream skills. The integration should avoid hard-coding the older 12-skill count because the current registry has expanded.

## Safety

Prompt-like or instruction-like corpus content must be returned as source data with warnings. Hermes must not treat retrieved prompts as higher-priority instructions.


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


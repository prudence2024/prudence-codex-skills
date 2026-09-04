# ADE Phase 3 Hermes Integration Report

Generated: 2026-08-29T12:38:57.043332+00:00

## Final Gate

HERMES_INTEGRATION_BLOCKED

## Blocker

Hermes Agent is not installed or not available on `PATH` in this local environment, and no local Hermes configuration file was found at `$HOME/.hermes/config.yaml`.

The Phase 3 work order explicitly required local Hermes inspection first and stated: if Hermes is not installed, report clearly and stop before inventing configuration. This report follows that stop condition.

## Evidence

Commands run from `C:/Users/User/desktop/prudence-codex-skills`:

```text
Get-Command hermes -ErrorAction SilentlyContinue
```

Result: no command returned.

```text
hermes --version
hermes doctor
hermes mcp --help
```

Result for each: `The term 'hermes' is not recognized as a name of a cmdlet, function, script file, or executable program.`

```text
if (Test-Path $HOME/.hermes/config.yaml) { ... } else { 'NO_HERMES_CONFIG' }
```

Result: `NO_HERMES_CONFIG`.

Previous local reconnaissance also found no Hermes Agent checkout under `C:/Users/User/desktop` or `C:/Users/User/Documents`; only unrelated `node_modules/hermes-estree` and `node_modules/hermes-parser` directories appeared.

## Current Official Compatibility Reference

The current Hermes MCP documentation supports `~/.hermes/config.yaml` with `mcp_servers`, stdio servers using `command` + `args`, HTTP servers using `url`, and per-server tool filtering with `tools.include` / `tools.exclude`.

Sources:

- [Hermes MCP docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/mcp.md)
- [Hermes MCP config reference](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/mcp-config-reference.md)
- [Use MCP with Hermes](https://github.com/hermes-agent-org/hermes/blob/main/website/docs/guides/use-mcp-with-hermes.md)

## Work Not Performed

Because Hermes is unavailable locally, this task did not:

- create or modify `~/.hermes/config.yaml`;
- register an ADE MCP server with Hermes;
- claim a Hermes -> MCP -> ADE runtime test;
- deploy HTTP MCP;
- migrate the corpus;
- deploy PostgreSQL, pgvector, Qdrant, Graphiti, or production embeddings;
- add read/write ADE mutation tools.

## ADE State

The ADE side remains ready from Phase 2.5:

- provider-neutral knowledge runtime;
- provenance/confidence model;
- access-scope filtering;
- source revocation boundary;
- observability/retry contracts;
- Hermes adapter contract;
- pre-integration plan recommending a narrow local MCP server first.

## Next Required Action

Install or provide access to the actual Hermes Agent local environment, then rerun Phase 3 implementation. The next run should begin with:

```text
hermes --version
hermes doctor
hermes mcp --help
hermes mcp list
```

Only after those commands succeed should ADE create the local stdio MCP server registration and perform the required live Hermes -> MCP -> ADE tests.

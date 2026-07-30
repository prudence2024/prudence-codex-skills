# Developer CLI

## Installation

Use Python 3.11 or newer in an isolated environment:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[test]"
```

The console command is `skill-ecosystem`. The equivalent development form is:

```powershell
python -m skill_ecosystem.cli --help
```

All commands accept `--root`. Run them from the repository root unless another
root is supplied.

## Validate

```powershell
skill-ecosystem validate --scope infrastructure
skill-ecosystem validate --scope repository
skill-ecosystem validate --scope repository --strict
skill-ecosystem validate --scope skill --skill design-toolkit
skill-ecosystem validate --scope context --path context/project.yaml
skill-ecosystem validate --scope report --path reports/run.json
skill-ecosystem validate --scope knowledge
skill-ecosystem validate --scope sources
```

Non-strict repository validation reports unmigrated first-party manifests as
warnings. Strict validation treats them as errors. Upstream `.system` skills are
always discovered as read-only compatibility entries.

## Audit

```powershell
skill-ecosystem audit
skill-ecosystem audit --strict --markdown
```

Audits are read-only and use the shared report contract.

## Registry

```powershell
skill-ecosystem register --output ecosystem/registry/skills.json
skill-ecosystem register --output ecosystem/registry/skills.json --check
```

The first command regenerates the snapshot. The second validates its schema and
fails when discovery no longer matches the snapshot.

## Tests

```powershell
skill-ecosystem test
skill-ecosystem test tests -q
skill-ecosystem test tests/test_knowledge.py -q
```

When forwarding pytest options, provide a test path first so the remaining
arguments are passed through to pytest.

## Migration

```powershell
skill-ecosystem migrate plan
skill-ecosystem migrate plan --output reports/migration-plan.json
```

`migrate apply` is intentionally disabled until the first-party migration phase
is approved. Planning never writes into a skill.

## Manage

```powershell
skill-ecosystem manage list
skill-ecosystem manage show --skill design-toolkit
```

Management is read-only in Phase 3.

## Query design knowledge

```powershell
skill-ecosystem knowledge query `
  --domain navigation `
  --industry saas `
  --ux-goal efficient-navigation `
  --accessibility supports `
  --performance neutral `
  --confidence-level established `
  --min-evidence-confidence 0.80 `
  --min-recommendation-score 0.75
```

Filters may be repeated or supplied as comma-separated values. Queries read
validated domain records; they do not query raw website archives or internal
observation logs directly.


"""Reusable infrastructure, document, skill, and repository validation."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any, Iterable

from jsonschema.exceptions import SchemaError

from .discovery import DiscoveredSkill, discover_skills
from .errors import DataError
from .io import load_json, load_yaml
from .knowledge import load_patterns
from .models import CheckResult, Issue
from .registry import build_registry
from .schema import load_schema, validate_instance

SCHEMA_FILES = (
    "skill-manifest.json",
    "registry.json",
    "shared-context.json",
    "report.json",
    "knowledge-pattern.json",
    "source-manifest.json",
    "domains-config.json",
    "confidence-config.json",
    "source-quality-config.json",
)

CONFIG_SCHEMAS = {
    "design-intelligence/config/domains.yaml": "domains-config.json",
    "design-intelligence/config/confidence.yaml": "confidence-config.json",
    "design-intelligence/config/source-quality.yaml": "source-quality-config.json",
}


def _status(issues: Iterable[Issue]) -> str:
    material = list(issues)
    if any(issue.severity == "error" for issue in material):
        return "fail"
    if material:
        return "partial"
    return "pass"


def _load_document(path: Path) -> Any:
    return load_json(path) if path.suffix.casefold() == ".json" else load_yaml(path)


def validate_document(
    path: Path,
    *,
    root: Path,
    schema_name: str,
    check_name: str,
) -> CheckResult:
    issues: list[Issue] = []
    if not path.is_file():
        issues.append(Issue("document.missing", f"Document does not exist: {path}", path=str(path)))
        return CheckResult(check_name, "fail", issues)
    try:
        document = _load_document(path)
        issues.extend(
            validate_instance(
                document,
                root / "ecosystem" / "schemas" / schema_name,
                subject=check_name,
            )
        )
    except DataError as exc:
        issues.append(Issue("document.load_failed", str(exc), path=str(path)))
    return CheckResult(check_name, _status(issues), issues, [str(path)] if not issues else [])


def validate_infrastructure(root: Path) -> CheckResult:
    schema_dir = root / "ecosystem" / "schemas"
    issues: list[Issue] = []
    evidence: list[str] = []
    for name in SCHEMA_FILES:
        path = schema_dir / name
        if not path.is_file():
            issues.append(Issue("schema.missing", f"Required schema is missing: {name}", path=str(path)))
            continue
        try:
            load_schema(path.resolve())
            evidence.append(f"Valid JSON Schema: {path.relative_to(root).as_posix()}")
        except (DataError, SchemaError) as exc:
            issues.append(Issue("schema.invalid_definition", str(exc), path=str(path)))

    loaded_configs: dict[str, Any] = {}
    for relative, schema_name in CONFIG_SCHEMAS.items():
        path = root / relative
        if not path.is_file():
            issues.append(Issue("config.missing", f"Required configuration is missing: {relative}", path=relative))
            continue
        try:
            config = load_yaml(path)
            loaded_configs[relative] = config
            issues.extend(
                validate_instance(
                    config,
                    schema_dir / schema_name,
                    subject=relative,
                )
            )
            evidence.append(f"Configuration validated: {relative}")
        except DataError as exc:
            issues.append(Issue("config.invalid", str(exc), path=relative))

    quality = loaded_configs.get("design-intelligence/config/source-quality.yaml")
    if isinstance(quality, dict):
        dimensions = quality.get("dimensions", {})
        if isinstance(dimensions, dict):
            total = sum(
                item.get("weight", 0)
                for item in dimensions.values()
                if isinstance(item, dict)
            )
            if abs(total - 1.0) > 1e-9:
                issues.append(
                    Issue(
                        "config.weights.invalid",
                        f"Source-quality weights must sum to 1.0, found {total}",
                        path="design-intelligence/config/source-quality.yaml",
                    )
                )
    return CheckResult("infrastructure", _status(issues), issues, evidence)


def _validate_agent_metadata(skill: DiscoveredSkill) -> list[Issue]:
    path = skill.source_path
    agent_path = skill.path / "agents" / "openai.yaml"
    if not agent_path.is_file():
        return [Issue("skill.agent_metadata.missing", "agents/openai.yaml is required", path=path)]
    try:
        agent_data = load_yaml(agent_path)
    except DataError as exc:
        return [Issue("skill.agent_metadata.invalid", str(exc), path=path)]
    interface = agent_data.get("interface", {}) if isinstance(agent_data, dict) else {}
    required = {"display_name", "short_description", "default_prompt"}
    missing = required - set(interface)
    if missing:
        return [
            Issue(
                "skill.agent_metadata.invalid",
                f"Agent metadata is missing: {sorted(missing)}",
                path=path,
            )
        ]
    return []


def validate_skill(skill: DiscoveredSkill, root: Path, *, require_manifest: bool = True) -> CheckResult:
    issues: list[Issue] = []
    path = skill.source_path
    keys = set(skill.frontmatter)
    allowed = {"name", "description"}
    if not {"name", "description"}.issubset(keys):
        issues.append(Issue("skill.frontmatter.required", "SKILL.md requires name and description", path=path))
    if not skill.upstream and keys - allowed:
        issues.append(
            Issue(
                "skill.frontmatter.extra",
                f"First-party SKILL.md has unsupported frontmatter keys: {sorted(keys - allowed)}",
                path=path,
            )
        )
    if skill.upstream:
        return CheckResult(
            f"skill:{skill.id}",
            _status(issues),
            issues,
            [f"Upstream read-only skill: {path}"],
        )

    issues.extend(_validate_agent_metadata(skill))
    if skill.manifest is None:
        issues.append(
            Issue(
                "skill.manifest.missing",
                "First-party skill has not been migrated to skill.yaml",
                severity="error" if require_manifest else "warning",
                path=path,
            )
        )
        return CheckResult(f"skill:{skill.id}", _status(issues), issues)

    issues.extend(
        validate_instance(
            skill.manifest,
            root / "ecosystem" / "schemas" / "skill-manifest.json",
            subject=f"skill {skill.id}",
        )
    )
    if skill.manifest.get("id") != skill.frontmatter.get("name"):
        issues.append(
            Issue(
                "skill.identity.mismatch",
                "skill.yaml id must match SKILL.md frontmatter name",
                path=path,
            )
        )
    if skill.path.name != skill.manifest.get("id"):
        issues.append(Issue("skill.directory.mismatch", "Skill directory must match manifest id", path=path))
    return CheckResult(f"skill:{skill.id}", _status(issues), issues)


def validate_registry(registry: dict, root: Path) -> CheckResult:
    issues = validate_instance(
        registry,
        root / "ecosystem" / "schemas" / "registry.json",
        subject="registry",
    )
    ids = [entry.get("id") for entry in registry.get("skills", [])]
    for skill_id, count in Counter(ids).items():
        if count > 1:
            issues.append(Issue("registry.duplicate_id", f"Duplicate skill id: {skill_id}"))

    available = set(ids)
    graph: dict[str, set[str]] = {}
    for entry in registry.get("skills", []):
        if entry.get("upstream") or entry.get("status") == "unmigrated":
            continue
        required = set((entry.get("dependencies") or {}).get("required", []))
        graph[entry["id"]] = required
        for dependency in required - available:
            issues.append(
                Issue("registry.dependency.missing", f"{entry['id']} requires missing skill {dependency}")
            )

    def visit(node: str, active: set[str], complete: set[str]) -> None:
        if node in active:
            issues.append(Issue("registry.dependency.cycle", f"Dependency cycle includes {node}"))
            return
        if node in complete:
            return
        active.add(node)
        for dependency in graph.get(node, set()):
            visit(dependency, active, complete)
        active.remove(node)
        complete.add(node)

    complete: set[str] = set()
    for node in graph:
        visit(node, set(), complete)
    return CheckResult("registry", _status(issues), issues)


def validate_knowledge_base(root: Path) -> CheckResult:
    patterns, issues = load_patterns(root)
    return CheckResult(
        "design-knowledge",
        _status(issues),
        issues,
        [f"Validated {len(patterns)} knowledge pattern(s)"],
    )


def validate_source_manifests(root: Path) -> CheckResult:
    manifest_root = root / "design-intelligence" / "manifests"
    issues: list[Issue] = []
    evidence: list[str] = []
    paths = (
        sorted(manifest_root.rglob("*.yaml"))
        + sorted(manifest_root.rglob("*.yml"))
        + sorted(manifest_root.rglob("*.json"))
        if manifest_root.exists()
        else []
    )
    for path in paths:
        result = validate_document(
            path,
            root=root,
            schema_name="source-manifest.json",
            check_name=f"source:{path.stem}",
        )
        issues.extend(result.issues)
        evidence.extend(result.evidence)
    evidence.append(f"Validated {len(paths)} source manifest(s)")
    return CheckResult("design-sources", _status(issues), issues, evidence)


def validate_repository(root: Path, *, require_manifests: bool = False) -> list[CheckResult]:
    results = [
        validate_infrastructure(root),
        validate_knowledge_base(root),
        validate_source_manifests(root),
    ]
    try:
        skills = discover_skills(root)
    except DataError as exc:
        return results + [CheckResult("discovery", "fail", [Issue("discovery.failed", str(exc))])]
    results.extend(validate_skill(skill, root, require_manifest=require_manifests) for skill in skills)
    registry = build_registry(root, skills=skills, generated_at="validation")
    results.append(validate_registry(registry, root))
    return results


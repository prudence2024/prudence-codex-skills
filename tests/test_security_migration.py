from __future__ import annotations

import re

from skill_ecosystem.discovery import discover_skills, find_skill
from skill_ecosystem.io import load_yaml, parse_skill_frontmatter
from skill_ecosystem.registry import build_registry
from skill_ecosystem.schema import validate_instance
from skill_ecosystem.validation import validate_skill


DESCRIPTION = (
    "Production security, architecture, and launch-readiness workflow for web apps, "
    "APIs, forms, auth, databases, payments, uploads, dependencies, secrets, deployment, "
    "cloud cost, caching, scaling, observability, backups, and CI/CD. Use when Codex "
    "needs to review or implement security controls, harden form/API handling, verify "
    "environment hygiene, add rate limiting or headers, audit dependencies, or assess "
    "whether an AI-built application is safe and operationally ready for production."
)


def test_security_preserves_trigger_identity(repository_root):
    frontmatter = parse_skill_frontmatter(repository_root / "security" / "SKILL.md")
    assert frontmatter == {"name": "security", "description": DESCRIPTION}


def test_security_manifest_validates_strictly(repository_root):
    skill = find_skill(discover_skills(repository_root), "security")
    assert skill is not None
    result = validate_skill(skill, repository_root, require_manifest=True)
    assert result.status == "pass", result.issues


def test_registry_exposes_security_contract(repository_root):
    registry = build_registry(repository_root, generated_at="test")
    entry = next(item for item in registry["skills"] if item["id"] == "security")
    assert entry["status"] == "stable"
    assert entry["version"] == "1.0.0"
    assert entry["category"] == "security"
    assert entry["dependencies"]["required"] == []
    assert entry["dependencies"]["optional"] == [
        "session-security",
        "incident-response",
        "legal-business",
        "design-toolkit",
        "visibility",
    ]
    assert "threat-model-adapters" in entry["extension_points"]


def test_security_preserves_domain_ownership_and_boundaries(repository_root):
    manifest = load_yaml(repository_root / "security" / "skill.yaml")
    owned = " ".join(manifest["scope"]["includes"]).casefold()
    for domain in ("secrets", "authentication", "authorization", "api", "database",
                   "upload", "payment", "dependency", "backup", "observability"):
        assert domain in owned
    excluded = " ".join(manifest["scope"]["excludes"]).casefold()
    for boundary in ("session timeout", "active incident", "legal document",
                     "interface design", "search-visibility"):
        assert boundary in excluded


def test_security_decision_fixture_validates(repository_root):
    decision = load_yaml(repository_root / "tests" / "fixtures" / "security-decision.yaml")
    issues = validate_instance(
        decision,
        repository_root / "security" / "schemas" / "security-decision.json",
        subject="security decision fixture",
    )
    assert issues == []


def test_security_local_markdown_links_resolve(repository_root):
    skill_root = repository_root / "security"
    broken: list[tuple[str, str]] = []
    for path in skill_root.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            target = target.split("#", 1)[0]
            if not target or "://" in target:
                continue
            if not (path.parent / target).resolve().exists():
                broken.append((path.relative_to(repository_root).as_posix(), target))
    assert broken == []

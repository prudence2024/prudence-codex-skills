from __future__ import annotations

import re

from skill_ecosystem.discovery import discover_skills, find_skill
from skill_ecosystem.io import load_yaml, parse_skill_frontmatter
from skill_ecosystem.registry import build_registry
from skill_ecosystem.schema import validate_instance
from skill_ecosystem.validation import validate_skill


DESCRIPTION = (
    "Design, implement, or audit secure authenticated-session timeout behavior for web "
    "and mobile applications. Use when Codex needs meaningful activity tracking, idle "
    "and absolute expiry, a 60-second expiration warning with one-click extension, "
    "sustained-focus exceptions, cross-tab coordination, server-side enforcement, or "
    "exact workflow and unsaved-state restoration after re-authentication."
)


def test_session_security_preserves_trigger_identity(repository_root):
    assert parse_skill_frontmatter(repository_root / "session-security" / "SKILL.md") == {
        "name": "session-security", "description": DESCRIPTION
    }


def test_session_security_manifest_validates_strictly(repository_root):
    skill = find_skill(discover_skills(repository_root), "session-security")
    assert skill is not None
    result = validate_skill(skill, repository_root, require_manifest=True)
    assert result.status == "pass", result.issues


def test_session_security_registry_contract(repository_root):
    entry = next(item for item in build_registry(repository_root, generated_at="test")["skills"]
                 if item["id"] == "session-security")
    assert entry["version"] == "1.0.0"
    assert entry["status"] == "stable"
    assert entry["dependencies"]["required"] == []
    assert entry["dependencies"]["optional"] == ["security", "design-toolkit", "incident-response"]
    assert "coordination-transports" in entry["extension_points"]


def test_session_security_ownership_boundaries(repository_root):
    manifest = load_yaml(repository_root / "session-security" / "skill.yaml")
    owned = " ".join(manifest["scope"]["includes"]).casefold()
    for value in ("meaningful-activity", "idle", "absolute", "60-second", "cross-tab", "restoration"):
        assert value in owned
    excluded = " ".join(manifest["scope"]["excludes"]).casefold()
    for value in ("authentication-provider", "general interface", "active incident"):
        assert value in excluded


def test_session_security_decision_fixture_validates(repository_root):
    issues = validate_instance(
        load_yaml(repository_root / "tests" / "fixtures" / "session-security-decision.yaml"),
        repository_root / "session-security" / "schemas" / "session-security-decision.json",
        subject="session security decision fixture",
    )
    assert issues == []


def test_session_security_local_links_resolve(repository_root):
    root = repository_root / "session-security"
    broken = []
    for path in root.rglob("*.md"):
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0]
            if target and "://" not in target and not (path.parent / target).resolve().exists():
                broken.append((path.name, target))
    assert broken == []

from __future__ import annotations

import re

from skill_ecosystem.discovery import discover_skills, find_skill
from skill_ecosystem.io import load_yaml, parse_skill_frontmatter
from skill_ecosystem.registry import build_registry
from skill_ecosystem.schema import validate_instance
from skill_ecosystem.validation import validate_skill


DESCRIPTION = (
    "Classify and route customer support tickets, form failures, booking or payment "
    "issues, complaints, bug reports, and sensitive escalations. Use when Codex needs "
    "to resolve a known support issue automatically, gather an assisted-triage context "
    "package, identify human-required legal/privacy/security or policy cases, or "
    "produce a structured support handoff."
)


def test_support_triage_preserves_trigger_identity(repository_root):
    assert parse_skill_frontmatter(repository_root / "support-triage" / "SKILL.md") == {
        "name": "support-triage", "description": DESCRIPTION
    }


def test_support_triage_manifest_validates_strictly(repository_root):
    skill = find_skill(discover_skills(repository_root), "support-triage")
    result = validate_skill(skill, repository_root, require_manifest=True)
    assert result.status == "pass", result.issues


def test_support_triage_registry_contract(repository_root):
    entry = next(item for item in build_registry(repository_root, generated_at="test")["skills"]
                 if item["id"] == "support-triage")
    assert entry["version"] == "1.0.0"
    assert entry["dependencies"]["optional"] == ["incident-response", "security", "legal-business"]
    assert "resolution-catalogs" in entry["extension_points"]


def test_support_triage_preserves_tiers_and_boundaries(repository_root):
    text = (repository_root / "support-triage" / "SKILL.md").read_text(encoding="utf-8")
    for tier in ("automated_resolution", "assisted_triage", "human_required"):
        assert tier in text
    manifest = load_yaml(repository_root / "support-triage" / "skill.yaml")
    excluded = " ".join(manifest["scope"]["excludes"]).casefold()
    for value in ("active incident", "security or privacy investigation", "legal conclusions", "product-roadmap"):
        assert value in excluded


def test_support_triage_decision_fixture_validates(repository_root):
    issues = validate_instance(
        load_yaml(repository_root / "tests" / "fixtures" / "support-triage-decision.yaml"),
        repository_root / "support-triage" / "schemas" / "support-triage-decision.json",
        subject="support triage decision fixture",
    )
    assert issues == []


def test_support_triage_local_links_resolve(repository_root):
    root = repository_root / "support-triage"
    broken = []
    for path in root.rglob("*.md"):
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0]
            if target and "://" not in target and not (path.parent / target).resolve().exists():
                broken.append((path.name, target))
    assert broken == []

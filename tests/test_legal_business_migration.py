from __future__ import annotations

import re

from skill_ecosystem.discovery import discover_skills, find_skill
from skill_ecosystem.io import load_yaml, parse_skill_frontmatter
from skill_ecosystem.registry import build_registry
from skill_ecosystem.schema import validate_instance
from skill_ecosystem.validation import validate_skill


DESCRIPTION = (
    "Prepare, adapt, or audit pre-launch legal and business protection documents for "
    "SaaS products and client applications. Use when Codex needs Terms of Service, a "
    "data-accurate Privacy Policy, B2B Data Processing Agreement, Refund Policy, Master "
    "Service Agreement with service levels, or a cyber-liability insurance readiness "
    "checklist, especially for Nigeria-based or cross-border operations involving "
    "NDPA/NDPR, GDPR, clients, subscriptions, or personal data."
)


def test_legal_business_preserves_trigger_identity(repository_root):
    assert parse_skill_frontmatter(repository_root / "legal-business" / "SKILL.md") == {
        "name": "legal-business", "description": DESCRIPTION
    }


def test_legal_business_manifest_validates_strictly(repository_root):
    skill = find_skill(discover_skills(repository_root), "legal-business")
    result = validate_skill(skill, repository_root, require_manifest=True)
    assert result.status == "pass", result.issues


def test_legal_business_registry_contract(repository_root):
    entry = next(item for item in build_registry(repository_root, generated_at="test")["skills"]
                 if item["id"] == "legal-business")
    assert entry["version"] == "1.0.0"
    assert entry["dependencies"]["optional"] == ["security", "incident-response", "support-triage"]
    assert "consistency-checkers" in entry["extension_points"]


def test_legal_business_preserves_documents_and_boundaries(repository_root):
    manifest = load_yaml(repository_root / "legal-business" / "skill.yaml")
    owned = " ".join(manifest["scope"]["includes"]).casefold()
    for value in ("terms of service", "privacy policy", "dpa", "refund", "msa", "cyber-liability"):
        assert value in owned
    excluded = " ".join(manifest["scope"]["excludes"]).casefold()
    for value in ("final legal advice", "security-control", "incident operations", "interface design"):
        assert value in excluded


def test_legal_business_decision_fixture_validates(repository_root):
    issues = validate_instance(
        load_yaml(repository_root / "tests" / "fixtures" / "legal-business-decision.yaml"),
        repository_root / "legal-business" / "schemas" / "legal-business-decision.json",
        subject="legal business decision fixture",
    )
    assert issues == []


def test_legal_business_local_links_resolve(repository_root):
    root = repository_root / "legal-business"
    broken = []
    for path in root.rglob("*.md"):
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0]
            if target and "://" not in target and not (path.parent / target).resolve().exists():
                broken.append((path.name, target))
    assert broken == []

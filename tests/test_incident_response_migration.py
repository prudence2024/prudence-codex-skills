from __future__ import annotations

import re

from skill_ecosystem.discovery import discover_skills, find_skill
from skill_ecosystem.io import load_yaml, parse_skill_frontmatter
from skill_ecosystem.registry import build_registry
from skill_ecosystem.schema import validate_instance
from skill_ecosystem.validation import validate_skill


DESCRIPTION = (
    "Establish, implement, or audit production observability, incident handling, "
    "recovery, public status communication, scheduled-maintenance notices, and "
    "email-delivery health across software projects. Use when Codex needs error "
    "tracking, structured logs, severity-based alerts, uptime and health checks, "
    "independent status pages, subscriber and in-app incident notices, SPF/DKIM/DMARC "
    "guidance, deliverability monitoring, recovery runbooks or drills, incident "
    "ownership, automatic 48-hour post-mortem scheduling, blameless reviews, "
    "remediation tracking, or recurring-failure detection."
)


def test_incident_response_preserves_trigger_identity(repository_root):
    assert parse_skill_frontmatter(repository_root / "incident-response" / "SKILL.md") == {
        "name": "incident-response", "description": DESCRIPTION
    }


def test_incident_response_manifest_validates_strictly(repository_root):
    skill = find_skill(discover_skills(repository_root), "incident-response")
    result = validate_skill(skill, repository_root, require_manifest=True)
    assert result.status == "pass", result.issues


def test_incident_response_registry_contract(repository_root):
    entry = next(item for item in build_registry(repository_root, generated_at="test")["skills"]
                 if item["id"] == "incident-response")
    assert entry["version"] == "1.0.0"
    assert entry["dependencies"]["optional"] == [
        "security", "support-triage", "legal-business", "design-toolkit", "visibility"
    ]
    assert "incident-knowledge-indexes" in entry["extension_points"]


def test_incident_response_preserves_domains_and_boundaries(repository_root):
    manifest = load_yaml(repository_root / "incident-response" / "skill.yaml")
    owned = " ".join(manifest["scope"]["includes"]).casefold()
    for value in ("error tracking", "severity", "status pages", "email", "recovery", "48-hour", "blameless", "pattern"):
        assert value in owned
    excluded = " ".join(manifest["scope"]["excludes"]).casefold()
    for value in ("preventive application-security", "ticket classification", "legal notification", "interface design"):
        assert value in excluded


def test_incident_response_decision_fixture_validates(repository_root):
    issues = validate_instance(
        load_yaml(repository_root / "tests" / "fixtures" / "incident-response-decision.yaml"),
        repository_root / "incident-response" / "schemas" / "incident-response-decision.json",
        subject="incident response decision fixture",
    )
    assert issues == []


def test_incident_response_local_links_resolve(repository_root):
    root = repository_root / "incident-response"
    broken = []
    for path in root.rglob("*.md"):
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0]
            if target and "://" not in target and not (path.parent / target).resolve().exists():
                broken.append((path.name, target))
    assert broken == []

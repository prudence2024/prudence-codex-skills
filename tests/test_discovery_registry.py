from __future__ import annotations

from pathlib import Path

from skill_ecosystem.discovery import discover_skills
from skill_ecosystem.registry import build_registry
from skill_ecosystem.validation import validate_registry


FIXTURE = Path(__file__).parent / "fixtures" / "repository"


def test_discovery_separates_first_party_and_upstream():
    skills = discover_skills(FIXTURE)
    assert [skill.id for skill in skills] == ["sample-skill", "upstream-skill"]
    assert skills[0].migrated is True
    assert skills[0].read_only is False
    assert skills[1].upstream is True
    assert skills[1].read_only is True
    assert skills[1].manifest is None


def test_registry_contains_compatibility_entry():
    registry = build_registry(FIXTURE, generated_at="test")
    entries = {entry["id"]: entry for entry in registry["skills"]}
    assert entries["sample-skill"]["status"] == "stable"
    assert entries["upstream-skill"]["status"] == "upstream"
    assert entries["upstream-skill"]["read_only"] is True


def test_registry_validates_against_schema(repository_root):
    registry = build_registry(FIXTURE, generated_at="test")
    result = validate_registry(registry, repository_root)
    assert result.status == "pass", result.issues


"""Generate a central registry from discovered skill sources."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from .discovery import DiscoveredSkill, discover_skills
from .io import dump_json


def _legacy_entry(skill: DiscoveredSkill) -> dict[str, Any]:
    return {
        "id": skill.id,
        "name": skill.frontmatter.get("name", skill.id),
        "description": skill.frontmatter.get("description", ""),
        "source_path": skill.source_path,
        "status": "upstream" if skill.upstream else "unmigrated",
        "upstream": skill.upstream,
        "read_only": skill.read_only,
    }


def _manifest_entry(skill: DiscoveredSkill) -> dict[str, Any]:
    assert skill.manifest is not None
    manifest = skill.manifest
    return {
        "id": manifest.get("id", skill.id),
        "name": manifest.get("name", skill.frontmatter.get("name", skill.id)),
        "description": skill.frontmatter.get("description", ""),
        "source_path": skill.source_path,
        "category": manifest.get("category"),
        "version": manifest.get("version"),
        "status": manifest.get("status", "unmigrated"),
        "upstream": False,
        "read_only": False,
        "purpose": manifest.get("purpose"),
        "scope": manifest.get("scope"),
        "responsibilities": manifest.get("responsibilities"),
        "inputs": manifest.get("inputs"),
        "outputs": manifest.get("outputs"),
        "dependencies": manifest.get("dependencies"),
        "context": manifest.get("context"),
        "validation": manifest.get("validation"),
        "reporting": manifest.get("reporting"),
        "extension_points": manifest.get("extension_points"),
    }


def build_registry(
    root: Path,
    *,
    skills: Iterable[DiscoveredSkill] | None = None,
    generated_at: str | None = None,
) -> dict[str, Any]:
    discovered = list(skills if skills is not None else discover_skills(root))
    entries = [
        _manifest_entry(skill) if skill.migrated else _legacy_entry(skill)
        for skill in discovered
    ]
    entries.sort(key=lambda entry: (entry["upstream"], entry["id"]))
    return {
        "schema_version": 1,
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "skills": entries,
    }


def write_registry(registry: dict[str, Any], output: Path) -> None:
    dump_json(registry, output)


"""Skill discovery with a strict first-party/upstream boundary."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from .errors import DataError
from .io import load_yaml, parse_skill_frontmatter, relative_posix

_RESERVED = {
    ".git",
    ".github",
    ".pytest_cache",
    ".venv",
    "context",
    "design-intelligence",
    "docs",
    "ecosystem",
    "skill-learning",
    "tests",
}


@dataclass(frozen=True)
class DiscoveredSkill:
    id: str
    path: Path
    source_path: str
    upstream: bool
    read_only: bool
    frontmatter: dict[str, Any]
    manifest: dict[str, Any] | None

    @property
    def migrated(self) -> bool:
        return self.manifest is not None


def _skill_from_directory(directory: Path, root: Path, *, upstream: bool) -> DiscoveredSkill:
    skill_file = directory / "SKILL.md"
    frontmatter = parse_skill_frontmatter(skill_file)
    manifest_path = directory / "skill.yaml"
    manifest = None if upstream or not manifest_path.is_file() else load_yaml(manifest_path)
    if manifest is not None and not isinstance(manifest, dict):
        raise DataError(f"{manifest_path} must contain a mapping")
    skill_id = str((manifest or {}).get("id") or frontmatter.get("name") or directory.name)
    return DiscoveredSkill(
        id=skill_id,
        path=directory,
        source_path=relative_posix(directory, root),
        upstream=upstream,
        read_only=upstream,
        frontmatter=frontmatter,
        manifest=manifest,
    )


def discover_skills(root: Path, *, include_system: bool = True) -> list[DiscoveredSkill]:
    root = root.resolve()
    skills: list[DiscoveredSkill] = []
    for directory in sorted(root.iterdir(), key=lambda item: item.name):
        if not directory.is_dir() or directory.name.startswith(".") or directory.name in _RESERVED:
            continue
        if (directory / "SKILL.md").is_file():
            skills.append(_skill_from_directory(directory, root, upstream=False))

    system_root = root / ".system"
    if include_system and system_root.is_dir():
        for directory in sorted(system_root.iterdir(), key=lambda item: item.name):
            if directory.is_dir() and (directory / "SKILL.md").is_file():
                skills.append(_skill_from_directory(directory, root, upstream=True))
    return skills


def find_skill(skills: Iterable[DiscoveredSkill], skill_id: str) -> DiscoveredSkill | None:
    return next((skill for skill in skills if skill.id == skill_id), None)


"""Safe structured-data and Markdown helpers."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml

from .errors import DataError

_FRONTMATTER = re.compile(r"\A---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|\Z)", re.DOTALL)


def load_yaml(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return yaml.safe_load(handle)
    except (OSError, yaml.YAMLError) as exc:
        raise DataError(f"Cannot load YAML from {path}: {exc}") from exc


def load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise DataError(f"Cannot load JSON from {path}: {exc}") from exc


def dump_json(data: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def parse_skill_frontmatter(path: Path) -> dict[str, Any]:
    try:
        text = path.read_text(encoding="utf-8-sig")
    except OSError as exc:
        raise DataError(f"Cannot read {path}: {exc}") from exc
    match = _FRONTMATTER.match(text)
    if not match:
        raise DataError(f"{path} has no valid YAML frontmatter")
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        raise DataError(f"Invalid YAML frontmatter in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise DataError(f"Frontmatter in {path} must be a mapping")
    return data


def relative_posix(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


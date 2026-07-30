"""JSON Schema loading and validation."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError

from .io import load_json
from .models import Issue


@lru_cache(maxsize=32)
def load_schema(path: Path) -> dict[str, Any]:
    schema = load_json(path)
    if not isinstance(schema, dict):
        raise SchemaError(f"{path} must contain a JSON object")
    Draft202012Validator.check_schema(schema)
    return schema


def validate_instance(instance: Any, schema_path: Path, *, subject: str) -> list[Issue]:
    validator = Draft202012Validator(load_schema(schema_path.resolve()))
    issues: list[Issue] = []
    for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.absolute_path)):
        location = ".".join(str(part) for part in error.absolute_path) or "$"
        issues.append(
            Issue(
                code="schema.invalid",
                message=f"{subject} at {location}: {error.message}",
                path=str(schema_path),
            )
        )
    return issues


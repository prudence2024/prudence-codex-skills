from __future__ import annotations

import json

from skill_ecosystem.cli import main
from skill_ecosystem.validation import (
    validate_document,
    validate_source_manifests,
)


def test_validates_shared_context_document(repository_root):
    result = validate_document(
        repository_root / "tests" / "fixtures" / "context.yaml",
        root=repository_root,
        schema_name="shared-context.json",
        check_name="shared-context",
    )
    assert result.status == "pass", result.issues


def test_rejects_invalid_shared_context(repository_root, tmp_path):
    path = tmp_path / "context.yaml"
    path.write_text("schema_version: 1\n", encoding="utf-8")
    result = validate_document(
        path,
        root=repository_root,
        schema_name="shared-context.json",
        check_name="shared-context",
    )
    assert result.status == "fail"
    assert any(issue.code == "schema.invalid" for issue in result.issues)


def test_empty_source_manifest_collection_is_valid(repository_root):
    result = validate_source_manifests(repository_root)
    assert result.status == "pass"
    assert "Validated 0 source manifest(s)" in result.evidence


def test_cli_validates_context(repository_root, capsys):
    exit_code = main(
        [
            "validate",
            "--root",
            str(repository_root),
            "--scope",
            "context",
            "--path",
            "tests/fixtures/context.yaml",
        ]
    )
    payload = json.loads(capsys.readouterr().out)
    assert exit_code == 0
    assert payload["summary"]["status"] == "pass"


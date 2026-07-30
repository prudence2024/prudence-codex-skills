from __future__ import annotations

import json

from skill_ecosystem.cli import main


def test_cli_validates_infrastructure(repository_root, capsys):
    exit_code = main(["validate", "--root", str(repository_root), "--scope", "infrastructure"])
    payload = json.loads(capsys.readouterr().out)
    assert exit_code == 0
    assert payload["summary"]["status"] == "pass"


def test_cli_register_check(repository_root, capsys):
    exit_code = main(["register", "--root", str(repository_root), "--check"])
    payload = json.loads(capsys.readouterr().out)
    assert exit_code == 0
    assert payload["status"] in {"pass", "partial"}


def test_cli_migration_apply_is_blocked(repository_root, capsys):
    exit_code = main(["migrate", "--root", str(repository_root), "apply"])
    assert exit_code == 2
    assert "disabled" in capsys.readouterr().err


def test_cli_queries_knowledge_fixture(repository_root, capsys):
    fixture = repository_root / "tests" / "fixtures" / "repository"
    exit_code = main(
        [
            "knowledge",
            "--root",
            str(fixture),
            "query",
            "--domain",
            "navigation",
            "--min-recommendation-score",
            "0.8",
        ]
    )
    payload = json.loads(capsys.readouterr().out)
    assert exit_code == 0
    assert payload["count"] == 1


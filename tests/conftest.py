from __future__ import annotations

import sys
from pathlib import Path

import pytest

SOURCE_ROOT = Path(__file__).resolve().parents[1] / "ecosystem" / "src"
sys.path.insert(0, str(SOURCE_ROOT))


@pytest.fixture
def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


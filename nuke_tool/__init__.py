"""Nuke wrapper for the Pixel3DMM pipeline."""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_SRC = _ROOT / "src"
for _p in (_ROOT, _SRC):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from .run_pipeline import run_full_pipeline

__all__ = ["run_full_pipeline"]

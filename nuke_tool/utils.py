"""Utility helpers for the Nuke integration."""

from pathlib import Path


def video_to_name(path: str) -> str:
    """Return a name for the given video or image folder."""
    p = Path(path)
    if p.is_dir():
        return p.name
    return p.stem

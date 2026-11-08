"""Tool surface for the ai-daw Hermes plugin.

Tools are thin: they resolve a project id against the projects directory, call
daw.core, and return small dicts. No absolute paths from the model, no audio
bytes in the response.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from daw.core import Project

PROJECTS = Path(os.environ.get("DAW_PROJECTS", str(Path.home() / ".hermes" / "daw-projects")))


def _fail(error: str, hint: str = "") -> dict[str, Any]:
    return {"ok": False, "error": error, "hint": hint}


def _open(project: str) -> Project:
    return Project.open(PROJECTS, project)


def daw_project_create(project: str, bpm: int = 120, key: str = "A minor",
                       sections: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    """Create a project. sections = [{"name": "intro", "bars": 4}, ...]"""
    try:
        created = Project.create(PROJECTS, project, bpm=bpm, key=key, sections=sections)
    except (ValueError, RuntimeError) as exc:
        return _fail(str(exc), "pick another id, or install ffmpeg")
    return {"ok": True, "project": created.data["id"], "root": str(created.root),
            "duration_s": created.duration_seconds(), "bpm": bpm, "key": key}


def daw_project_status(project: str) -> dict[str, Any]:
    """Tracks, versions, duration, and which layers are still missing."""
    try:
        return _open(project).status()
    except FileNotFoundError as exc:
        return _fail(str(exc), f"known projects: {sorted(p.name for p in PROJECTS.glob('*'))}")


def daw_layer_generate(project: str, instrument: str, prompt: str,
                       seed: int | None = None, engine: str = "dryrun",
                       bars: int | None = None) -> dict[str, Any]:
    """Generate one layer. Same engine+model+seed+prompt returns the existing stem."""
    try:
        opened = _open(project)
    except FileNotFoundError as exc:
        return _fail(str(exc), "create the project first")
    try:
        return opened.generate_layer(instrument=instrument, prompt=prompt, seed=seed,
                                     engine=engine, bars=bars)
    except (KeyError, RuntimeError, ValueError) as exc:
        return _fail(str(exc), "check the engine name and that ffmpeg is installed")


def daw_track_set(project: str, instrument: str, gain_db: float | None = None,
                  muted: bool | None = None) -> dict[str, Any]:
    """Set a track's gain or mute state in the manifest."""
    try:
        return _open(project).set_track(instrument, gain_db=gain_db, muted=muted)
    except FileNotFoundError as exc:
        return _fail(str(exc), "create the project first")


def daw_render_stems(project: str, out_dir: str) -> dict[str, Any]:
    """Aligned stems, one per track, all exactly the project duration."""
    try:
        return _open(project).render_stems(Path(out_dir))
    except (FileNotFoundError, RuntimeError) as exc:
        return _fail(str(exc), "check the project id and ffmpeg")


def daw_render_mix(project: str, out_file: str) -> dict[str, Any]:
    """Mix with one loudnorm pass at the end, and report loudness."""
    try:
        return _open(project).render_mix(Path(out_file))
    except (FileNotFoundError, RuntimeError) as exc:
        return _fail(str(exc), "check the project id and ffmpeg")

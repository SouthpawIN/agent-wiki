"""Dry-run engine: synthesises real audio with ffmpeg.

Not a music model. It exists so the whole pipeline - manifest, versions, reference
mix, stems, loudness - is exercisable without a GPU, and so a dead engine degrades
into something audible rather than an exception.
"""
from __future__ import annotations

import shutil
import subprocess
import time
from typing import Any

from .base import Capabilities

# A different timbre per layer so stems are distinguishable by ear and by spectrum.
VOICES = {
    "drums": ("sine=frequency=90", "tremolo=f=2:d=0.9"),
    "bass": ("sine=frequency=55", ""),
    "harmony": ("sine=frequency=220", "aecho=0.8:0.9:60|120:0.4|0.3"),
    "lead": ("sine=frequency=440", "vibrato=f=5:d=0.4"),
    "vocals": ("sine=frequency=330", "tremolo=f=6:d=0.5"),
    "ear-candy": ("sine=frequency=660", "aphaser"),
}


class DryRunEngine:
    name = "dryrun"
    model = "dryrun-ffmpeg-1"
    install_hint = "needs ffmpeg on PATH"

    def capabilities(self) -> Capabilities:
        return Capabilities(duration_s=600.0, vocals=False, stems=True,
                            bpm_key_conditioning=True, local=True, license="MIT")

    def health(self) -> bool:
        return shutil.which("ffmpeg") is not None

    def generate(self, request: dict[str, Any]) -> dict[str, Any]:
        started = time.monotonic()
        instrument = str(request.get("instrument", "lead"))
        source, effect = VOICES.get(instrument, VOICES["lead"])
        duration = float(request.get("duration_s", 8.0))
        out = str(request["output"])

        graph = source
        if effect:
            graph += f",{effect}"
        graph += f",afade=t=in:d=0.05,afade=t=out:st={max(0.0, duration - 0.2)}:d=0.2"

        result = subprocess.run(
            ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
             "-f", "lavfi", "-i", f"{source}:duration={duration}",
             "-af", (effect + "," if effect else "") +
             f"afade=t=in:d=0.05,afade=t=out:st={max(0.0, duration - 0.2)}:d=0.2",
             "-ar", "44100", "-ac", "2", out],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            return {"ok": False, "error": result.stderr.strip()[:300],
                    "hint": "check ffmpeg's lavfi sine support"}
        return {"ok": True, "audio_paths": [out], "stems": False,
                "seed_used": request.get("seed"), "model": self.model,
                "cost": 0.0, "elapsed_s": round(time.monotonic() - started, 3)}

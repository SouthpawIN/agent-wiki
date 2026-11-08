"""ACE-Step adapter: a thin client over a local ACE-Step server.

This wraps the real API; it does not reimplement inference. Point it at the
ACE-Step server with DAW_ACESTEP_URL (default http://127.0.0.1:8091/ is *not*
used - that is TurboFit; ACE-Step defaults to 7860 for the Gradio API).
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from .base import Capabilities

DEFAULT_URL = "http://127.0.0.1:7860"
TIMEOUT_S = float(os.environ.get("DAW_ACESTEP_TIMEOUT", "600"))


class AceStepEngine:
    name = "acestep"
    model = os.environ.get("DAW_ACESTEP_MODEL", "acestep-v1_5")
    install_hint = (
        "start the ACE-Step server (see SouthpawIN/ACE-Step-DAW), then set "
        "DAW_ACESTEP_URL; the plugin is a client and does not bundle weights"
    )

    def __init__(self, url: str | None = None) -> None:
        self.url = (url or os.environ.get("DAW_ACESTEP_URL") or DEFAULT_URL).rstrip("/")

    def capabilities(self) -> Capabilities:
        return Capabilities(duration_s=240.0, vocals=True, stems=False,
                            bpm_key_conditioning=True, local=True,
                            license="see the ACE-Step model card")

    def health(self) -> bool:
        try:
            with urllib.request.urlopen(f"{self.url}/config", timeout=5) as response:
                return response.status == 200
        except (urllib.error.URLError, OSError, TimeoutError):
            return False

    def generate(self, request: dict[str, Any]) -> dict[str, Any]:
        started = time.monotonic()
        payload = {
            "prompt": request.get("prompt", ""),
            "lyrics": request.get("lyrics", ""),
            "duration": int(float(request.get("duration_s", 30))),
            "bpm": int(request.get("bpm", 120)),
            "key": request.get("key", ""),
            "seed": int(request.get("seed", 0)),
            "audio_reference": request.get("reference") or None,
        }
        body = json.dumps(payload).encode()
        call = urllib.request.Request(
            f"{self.url}/generate", data=body,
            headers={"content-type": "application/json"}, method="POST",
        )
        try:
            with urllib.request.urlopen(call, timeout=TIMEOUT_S) as response:
                result = json.loads(response.read().decode() or "{}")
        except urllib.error.HTTPError as exc:
            return {"ok": False, "error": f"ACE-Step HTTP {exc.code}",
                    "hint": exc.read().decode(errors="replace")[:200]}
        except (urllib.error.URLError, OSError, TimeoutError) as exc:
            return {"ok": False, "error": f"ACE-Step unreachable: {exc}",
                    "hint": self.install_hint}

        produced = result.get("audio_path") or result.get("path")
        if not produced:
            return {"ok": False, "error": "ACE-Step returned no audio path",
                    "hint": "check the server log; the API shape may have changed"}

        dest = Path(request["output"])
        dest.parent.mkdir(parents=True, exist_ok=True)
        source = Path(produced)
        if source.exists():
            if dest.exists():
                dest.unlink()
            source.replace(dest)
        else:
            return {"ok": False, "error": f"ACE-Step reported a missing file: {produced}",
                    "hint": "server and client must share a filesystem, or return a URL"}
        return {"ok": True, "audio_paths": [str(dest)], "stems": False,
                "seed_used": payload["seed"], "model": self.model,
                "cost": result.get("cost", 0.0),
                "elapsed_s": round(time.monotonic() - started, 3)}

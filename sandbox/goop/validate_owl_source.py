"""Validate the accepted embedded owl player without converting or mutating it."""
from __future__ import annotations

import base64
import json
import re
import sys
from pathlib import Path

EXPECTED = {
    "idle": "idle",
    "thinking": "thinking",
    "speaking": "speaking",
    "listening": "thinking",
    "working": "thinking",
    "error": "speaking",
}


def load(path: Path) -> tuple[dict, dict, dict, list[dict]]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"const EIKON_B64 = `([^`]+)`", text)
    if not match:
        raise ValueError("embedded EIKON_B64 payload not found")
    lines = base64.b64decode(match.group(1)).decode("utf-8").splitlines()
    if len(lines) < 3:
        raise ValueError("embedded payload has fewer than three metadata lines")
    meta, states, ranges = (json.loads(line) for line in lines[:3])
    frames = [json.loads(line) for line in lines[3:]]
    return meta, states, ranges, frames


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("owl-player-embedded.html")
    meta, states, ranges, frames = load(path)
    assert meta["t"] == "eikon"
    assert meta["id"] == "owl-animated-24fps"
    assert meta["grid"] == {"w": 192, "h": 96}
    assert states["states"] == ["idle", "thinking", "speaking"]
    assert ranges["total"] == len(frames) == 288
    assert sum(item["c"] for item in ranges["ranges"]) == len(frames)
    assert all(isinstance(item["g"], list) for item in frames)
    assert set(EXPECTED.values()) == set(states["states"])
    print(json.dumps({
        "source": str(path),
        "id": meta["id"],
        "grid": meta["grid"],
        "fps": 24,
        "frames": len(frames),
        "source_states": states["states"],
        "mapping": EXPECTED,
        "conversion": "not performed",
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

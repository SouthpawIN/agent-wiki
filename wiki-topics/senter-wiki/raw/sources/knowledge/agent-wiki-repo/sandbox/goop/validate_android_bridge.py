"""Validate the narrow, approval-gated Android bridge allowlist."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("ANDROID_BRIDGE.json")
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["schema"] == "senter.android.bridge.v1"
    assert data["default"] == "disabled"
    assert data["transport"] == "adb-over-controlled-sidecar"
    assert set(data["operations"]) == {"screenshot", "tap", "swipe", "text"}
    assert all(item["approval"] == "user" for item in data["operations"].values())
    assert data["limits"] == {
        "max_actions_per_request": 1,
        "max_screenshot_bytes": 10000000,
        "max_timeout_seconds": 15,
        "allow_raw_adb": False,
        "allow_host_paths": False,
        "shell_mode": False,
    }
    assert "shell" in data["forbidden"]
    assert "install" in data["forbidden"]
    assert "credential access" in data["forbidden"]
    print(json.dumps({"schema": data["schema"], "status": "valid", "operations": sorted(data["operations"]), "default": data["default"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

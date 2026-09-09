"""Validate the agreed Android STS interaction contract."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("ANDROID_SURFACE.json")
    data = json.loads(path.read_text(encoding="utf-8"))
    bridge_path = path.with_name("ANDROID_BRIDGE.json")
    bridge = json.loads(bridge_path.read_text(encoding="utf-8"))
    assert bridge["schema"] == "senter.android.bridge.v1"
    assert bridge["default"] == "disabled"
    assert bridge["limits"]["max_actions_per_request"] == 1
    assert bridge["limits"]["allow_raw_adb"] is False
    assert data["schema"] == "senter.android.surface.v1"
    assert data["gesture_contract"] == {
        "side_button": "open_compact",
        "icon_tap": "send",
        "icon_double_tap": "screenshot",
        "icon_drag_up": "open_expanded",
    }
    assert data["default_blocks"][:3] == ["SESSIONS.md", "CHAT.md", "SENTER.md"]
    assert data["expanded"]["placement"] == "drag_sidebar_block_to_canvas"
    assert data["expanded"]["morphable"] is True
    assert all(value is False for value in data["security"].values() if isinstance(value, bool))
    assert data["capabilities"]["screenshot"]["approval"] == "user"
    assert data["capabilities"]["phone_operation"]["approval"] == "user"
    bridge = data["security"]["bridge"]
    assert bridge["default"] == "disabled"
    assert bridge["emulator_service"] == "android"
    assert bridge["adb_endpoint"] == "android:5555"
    assert bridge["architecture"] == "x86_64"
    assert bridge["persistent_mount"] == "/data"
    assert bridge["allow_raw_host_access"] is False
    print(json.dumps({"schema": data["schema"], "status": "valid", "blocks": len(data["default_blocks"]), "bridge": bridge["default"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

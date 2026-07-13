"""Validate the agreed Android STS interaction contract."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("ANDROID_SURFACE.json")
    data = json.loads(path.read_text(encoding="utf-8"))
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
    print(json.dumps({"schema": data["schema"], "status": "valid", "blocks": len(data["default_blocks"])}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

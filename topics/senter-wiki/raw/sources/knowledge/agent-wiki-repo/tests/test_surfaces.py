import json
from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_android_surface_contract_is_complete():
    data = json.loads((ROOT / "sandbox/goop/ANDROID_SURFACE.json").read_text())

    assert data["schema"] == "senter.android.surface.v1"
    assert data["gesture_contract"] == {
        "side_button": "open_compact",
        "icon_tap": "send",
        "icon_double_tap": "screenshot",
        "icon_drag_up": "open_expanded",
    }
    assert data["default_blocks"][:3] == ["SESSIONS.md", "CHAT.md", "SENTER.md"]
    assert data["expanded"] == {
        "surfaces": [
            "input-bar",
            "conversation-canvas",
            "building-block-sidebar",
        ],
        "placement": "drag_sidebar_block_to_canvas",
        "morphable": True,
    }


def test_android_operations_remain_permission_gated():
    data = json.loads((ROOT / "sandbox/goop/ANDROID_SURFACE.json").read_text())
    caps = data["capabilities"]

    assert caps["screenshot"]["approval"] == "user"
    assert caps["phone_operation"]["approval"] == "user"
    assert data["security"]["host_credentials"] is False
    assert data["security"]["hermes_session_databases"] is False
    assert data["security"]["unrestricted_shell"] is False
    assert data["security"]["bridge"] == {
        "default": "disabled",
        "emulator_service": "android",
        "adb_endpoint": "android:5555",
        "architecture": "x86_64",
        "persistent_mount": "/data",
        "allow_raw_host_access": False,
    }


def test_android_bridge_is_narrow_and_approval_gated():
    data = json.loads((ROOT / "sandbox/goop/ANDROID_BRIDGE.json").read_text())

    assert data["default"] == "disabled"
    assert set(data["operations"]) == {"screenshot", "tap", "swipe", "text"}
    assert all(item["approval"] == "user" for item in data["operations"].values())
    assert data["limits"]["max_actions_per_request"] == 1
    assert data["limits"]["max_timeout_seconds"] == 15
    assert data["limits"]["allow_raw_adb"] is False
    assert "shell" in data["forbidden"]
    assert "install" in data["forbidden"]

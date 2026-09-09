import importlib.util
from pathlib import Path
import sys

import pytest


path = Path(__file__).parents[1] / "sandbox/goop/android_bridge.py"
spec = importlib.util.spec_from_file_location("android_bridge", path)
assert spec and spec.loader
bridge = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = bridge
spec.loader.exec_module(bridge)


def test_plans_approved_screenshot_without_execution():
    req = bridge.Request("screenshot", approved=True)
    assert bridge.plan(req) == ("adb", "-s", "android:5555", "exec-out", "screencap", "-p")


def test_plans_bounded_tap_and_text():
    assert bridge.plan(bridge.Request("tap", ("10", "20"), True))[-2:] == ("10", "20")
    assert bridge.plan(bridge.Request("text", ("hello world",), True))[-1] == "hello world"


def test_rejects_unapproved_and_forbidden_operations():
    with pytest.raises(bridge.BridgeError, match="approval"):
        bridge.plan(bridge.Request("screenshot"))
    with pytest.raises(bridge.BridgeError, match="forbidden"):
        bridge.plan(bridge.Request("shell", ("id",), True))


def test_rejects_invalid_coordinates_and_endpoint_injection():
    with pytest.raises(bridge.BridgeError):
        bridge.plan(bridge.Request("tap", ("-1", "4"), True))
    with pytest.raises(bridge.BridgeError):
        bridge.plan(bridge.Request("screenshot", approved=True), "android:5555;id")


def test_execute_uses_only_injected_runner():
    seen = []

    def runner(argv):
        seen.append(tuple(argv))
        return b"PNG"

    result = bridge.execute(bridge.Request("screenshot", approved=True), runner)
    assert result.output == b"PNG"
    assert seen == [result.argv]


def test_execute_rejects_oversized_runner_output():
    with pytest.raises(bridge.BridgeError, match="10 MB"):
        bridge.execute(
            bridge.Request("screenshot", approved=True),
            lambda _argv: b"x" * 10_000_001,
        )


def test_execute_still_requires_approval():
    with pytest.raises(bridge.BridgeError, match="approval"):
        bridge.execute(bridge.Request("tap", ("1", "2")), lambda _argv: b"")

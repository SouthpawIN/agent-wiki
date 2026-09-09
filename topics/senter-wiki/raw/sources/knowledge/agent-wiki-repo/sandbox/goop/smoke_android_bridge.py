"""Live smoke test for the optional Android emulator bridge.

The emulator must already be running and ADB must be reachable. This script
is opt-in and performs exactly one approved screenshot request.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).parent


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    serial = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1:5555"
    bridge = load("android_bridge_smoke", ROOT / "android_bridge.py")
    runner = load("android_runner_smoke", ROOT / "android_runner.py")
    req = bridge.Request("screenshot", approved=True)
    output = runner.run(bridge.plan(req, serial=serial))
    if output[:8] != b"\x89PNG\r\n\x1a\n":
        raise RuntimeError("bridge returned non-PNG screenshot data")
    print(f"android bridge smoke: ok ({len(output)} PNG bytes from {serial})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

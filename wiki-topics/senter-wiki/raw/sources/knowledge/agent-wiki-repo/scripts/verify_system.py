#!/usr/bin/env python3
"""Run cheap, deterministic checks across the Senter Agent surfaces."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = Path.home() / ".hermes" / "wiki"


def check(label: str, fn) -> dict:
    try:
        value = fn()
        return {"name": label, "status": "pass", "detail": value}
    except Exception as exc:
        return {"name": label, "status": "fail", "detail": str(exc)}


def exists(*parts: str) -> str:
    path = ROOT.joinpath(*parts)
    if not path.exists():
        raise FileNotFoundError(path)
    return str(path)


def validate_json(path: Path, schema: str) -> str:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != schema:
        raise ValueError(f"{path}: expected {schema}, got {data.get('schema')}")
    return schema


def main() -> int:
    checks = [
        check("wiki schema", lambda: exists(str(WIKI / "SCHEMA.md"))),
        check("wiki index", lambda: exists(str(WIKI / "index.md"))),
        check("wiki log", lambda: exists(str(WIKI / "log.md"))),
        check("whole-flow contract", lambda: validate_json(ROOT / "sandbox/goop/WHOLE_FLOW.json", "senter.goop.whole-flow.v1")),
        check("android surface contract", lambda: validate_json(ROOT / "sandbox/hermes-android/ANDROID_SURFACE.json", "senter.android.surface.v1")),
        check("android bridge contract", lambda: validate_json(ROOT / "sandbox/hermes-android/ANDROID_BRIDGE.json", "senter.android.bridge.v1")),
        check("android prototype", lambda: exists("sandbox/android-surface/index.html")),
        check("Herm checkout", lambda: exists("sandbox/herm-sovth/package.json")),
        check("integrated status", lambda: exists("INTEGRATED_STATUS.md")),
    ]
    result = {"root": str(ROOT), "checks": checks, "ok": all(item["status"] == "pass" for item in checks)}
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

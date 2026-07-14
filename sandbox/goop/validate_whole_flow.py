"""Validate the declarative Senter whole-flow and STS contracts."""
from __future__ import annotations
import json
from pathlib import Path
import sys


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent
    flow = json.loads((root / "WHOLE_FLOW.json").read_text(encoding="utf-8"))
    sts = json.loads((root / "STS_CONFIG.json").read_text(encoding="utf-8"))
    eikon = json.loads((root / "EIKON_REGISTRY.json").read_text(encoding="utf-8"))
    petdex = (root / "PETDEX.md").read_text(encoding="utf-8")
    assert flow["schema"] == "senter.goop.whole-flow.v1"
    assert set(flow["components"]) == {"senter", "herm", "eikon", "petdex", "android", "sts"}
    assert sts["schema"] == "senter.sts.auxiliary.v1"
    assert sts["mode"] == "tool-free"
    assert all(value is False for value in sts["security"].values())
    assert eikon["conversion"] == "not performed"
    assert "presentation-only" in petdex
    assert "cannot invoke ADB" in petdex
    assert flow["components"]["android"]["approval_boundary"] == "user"
    print(json.dumps({"status": "valid", "schema": flow["schema"], "components": len(flow["components"]), "sts": sts["mode"], "eikon": eikon["primary"]["id"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

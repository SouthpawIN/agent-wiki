import json
from pathlib import Path

ROOT = Path(__file__).parents[1]


def test_whole_flow_contract():
    data = json.loads((ROOT / "sandbox/goop/WHOLE_FLOW.json").read_text())
    assert data["schema"] == "senter.goop.whole-flow.v1"
    assert set(data["components"]) == {"senter", "herm", "eikon", "petdex", "android", "sts"}


def test_sts_is_tool_free():
    data = json.loads((ROOT / "sandbox/goop/STS_CONFIG.json").read_text())
    assert data["mode"] == "tool-free"
    assert not any(data["security"].values())

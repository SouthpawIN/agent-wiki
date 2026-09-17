import json, urllib.request
from pathlib import Path

TOKEN_FILE = Path.home() / ".hermes/senter-bridge/token"
BRIDGE = "http://127.0.0.1:8643/post"

tok = TOKEN_FILE.read_text().strip()

done_text = (
    "DONE — REFLECT pass 9 (2026-09-03, n=9): 662 events / 139.6 min scanned. "
    "Findings: THE CONCEPT (Context->Skills->Bots->Loops) landed in concept.md — Chris's "
    "north-star, confirms the live fast-lane ruling; reflect loop self-trips 9th consecutive "
    "pass (find|xargs discovery -> analysis_incomplete); default profile STILL unguarded "
    "(26 heredoc + 12 python3 -c + 4 cat >>); senter STILL sleep-polls /tmp despite anser "
    "POSTing DONE; looker STILL not adopted (100 drive_preview + 28 vision_analyze, all hermes); "
    "teknium PR policy quiet but 'Adolanium' commented on the -35.6% LOC refactor PR; vision "
    "CROSSED 20s (avg 21.5s). No new bot / no SOUL change -> no needs_chris card. "
    "Findings: topics/senter/loops/reflect/2026-09-03-9.md"
)

body = json.dumps({"bot": "anser", "text": done_text, "status": "done"}).encode()
req = urllib.request.Request(
    f"{BRIDGE}?token={tok}", data=body, headers={"Content-Type": "application/json"}
)
try:
    with urllib.request.urlopen(req, timeout=8) as r:
        resp = json.loads(r.read() or b"{}")
    print("POSTED:", json.dumps(resp))
except Exception as e:
    print("POST FAILED:", repr(e))

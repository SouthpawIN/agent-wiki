import json, urllib.request
from pathlib import Path

TOKEN_FILE = Path.home() / ".hermes/senter-bridge/token"
BRIDGE = "http://127.0.0.1:8643/post"

tok = TOKEN_FILE.read_text().strip()

done_text = (
    "DONE — REFLECT pass 11 (2026-09-03, n=11): 384 events / ~114 min scanned (16:09:00 -> 18:02:53). "
    "Findings: Chris issued 'ONE PAGE' (14:50) — consolidates the four pages into one wiki list with sections "
    "(reverses the 13:45 THE-CONCEPT 'four pages' ruling; concept.md now stale); the ruling landed ONLY in log.md "
    "(0 Ideas.md / concept.md / session.md) — detector 1 still blind. Reflect cron double-spawned AGAIN at 18:00:54 "
    "(senter + anser crons -> concurrent pass-11 collision, 6th consecutive detector-4 pass); senter STILL hand-polls "
    "/tmp. NEW approval prompt: 'stop/restart hermes launchd service' x2. vision STILL slow (avg ~33s / max 91s, "
    "unpinned default profile). looker STILL not adopted. 0 BLOCKED. No new bot / no SOUL change -> no needs_chris card. "
    "Findings: topics/senter/loops/reflect/2026-09-03-11.md"
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

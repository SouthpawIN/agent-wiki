import json, urllib.request
from pathlib import Path

TOKEN_FILE = Path.home() / ".hermes/senter-bridge/token"
BRIDGE = "http://127.0.0.1:8643/post"
tok = TOKEN_FILE.read_text().strip()

done_text = (
    "DONE — REFLECT pass 28 (2026-09-04, n=28). Hand-spawned by Chris at ~20:02 CDT. "
    "Dead-quiet window (18:01→20:02 CDT, ~500 events): 0 Chris, 0 builders, 0 approvals. "
    "Confirms pass-27's findings and adds only deltas: (1) 15th consecutive multi-spawn at 20:00 — "
    "delete senter's c377932f3933 one-line fix remains unlanded; (2) senter hand-spawning persists "
    "(every-even-hour pattern) — consume bridge message{status:done}; (3) teknium empty-turn loop "
    "ESCALATED to investigation (~60 empty turns across passes 26-28, ~5 hours of continuous 5-min cycling); "
    "(4) reachability + feed + turbofit-CI stable. No new bot, no SOUL change -> no needs_chris card. "
    "Findings: topics/senter/loops/reflect/2026-09-04-28.md; pass-28 block appended to klerik queue."
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
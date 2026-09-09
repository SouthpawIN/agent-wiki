import json, urllib.request
from pathlib import Path

TOKEN_FILE = Path.home() / ".hermes/senter-bridge/token"
BRIDGE = "http://127.0.0.1:8643/post"

tok = TOKEN_FILE.read_text().strip()

done_text = (
    "DONE — REFLECT pass 10 (2026-09-03, n=10): 443 events / 90.5 min scanned (14:34:07 -> 16:04:38). "
    "Findings: surgery wave calming (default-profile rule-14 violations 42 -> 4); detector 7 vision SPIKED to "
    "89.7s avg / 167.8s max on the default profile (unpinned aux.vision hitting the free-tier timeout); "
    "senter now violates rule 14 itself (python3 -c to read the reflect log 14:44:05) + STILL sleep-polls "
    "/tmp; reflect cron double-fired 16:00:44 (senter + anser crons -> concurrent pass-10 collision, 10th "
    "consecutive self-trip); Adolanium RESOLVED as real external contributor (hermes-tailscale, v0.0.3); "
    "looker still unused but LOOK volume collapsed; 0 BLOCKED; github 0-commit noise persists (7 passes). "
    "No new bot / no SOUL change -> no needs_chris card. "
    "Findings: topics/senter/loops/reflect/2026-09-03-10.md"
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

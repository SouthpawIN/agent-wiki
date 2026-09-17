#!/usr/bin/env python3
"""POST a bridge card from a JSON payload file. Usage: bridge-post.py <payload.json>"""
import json, sys, urllib.request
from pathlib import Path

payload_file = Path(sys.argv[1])
token = Path.home().joinpath(".hermes/senter-bridge/token").read_text().strip()
payload = json.loads(payload_file.read_text())
payload.setdefault("bot", "klerik")
req = urllib.request.Request(
    "http://127.0.0.1:8643/post?token=" + token,
    data=json.dumps(payload).encode(),
    headers={"Content-Type": "application/json"},
)
with urllib.request.urlopen(req, timeout=10) as r:
    print(r.status, r.read().decode()[:200])

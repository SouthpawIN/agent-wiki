import json, sys, urllib.request

tok_path = "/Users/sovthpaw/.hermes/senter-bridge/token"
payload_path = sys.argv[1]

with open(tok_path) as f:
    tok = f.read().strip()
with open(payload_path, "rb") as f:
    body = f.read()

req = urllib.request.Request(
    "http://127.0.0.1:8643/post?token=" + tok,
    data=body,
    headers={"Content-Type": "application/json"},
    method="POST",
)
with urllib.request.urlopen(req, timeout=10) as r:
    print(r.status, r.read().decode()[:200])

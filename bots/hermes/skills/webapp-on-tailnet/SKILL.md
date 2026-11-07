---
name: webapp-on-tailnet
description: Serve the Hermes web app on the tailnet with auth and HTTPS.
version: 1.0.0
author: Mesh
license: MIT
metadata:
  hermes:
    tags: [hermes, tailscale, dashboard, https, auth]
---

# Web app on the tailnet

Goal: `https://<host>.<tailnet>.ts.net` serves the dashboard, valid cert, auth on,
nothing reachable from the public internet.

## Procedure

1. **Confirm the tailnet name and status.**
   ```bash
   tailscale status | head -5
   tailscale cert <host>.<tailnet>.ts.net   # proves cert issuance works
   ```
2. **Start the dashboard loopback-only**, machine-level (unified, not `--isolated`):
   ```bash
   hermes dashboard --host 127.0.0.1 --port 9119 --no-open
   hermes dashboard --status
   ```
   Do not use `--insecure`; it no longer disables auth anyway.
3. **Proxy it onto the tailnet with TLS:**
   ```bash
   tailscale serve --bg 9119
   tailscale serve status
   ```
   `tailscale serve` terminates HTTPS with a real cert and refuses non-tailnet
   clients. `tailscale funnel` is the public-internet switch — never use it here.
4. **Set auth.** OAuth via Portal (`hermes dashboard register`) or a password in
   `.env`. A tailnet identity is transport trust, not application auth.
5. **Verify from a second machine on the tailnet:**
   ```bash
   curl -sI https://<host>.<tailnet>.ts.net | head -1     # 200 or 302 to login
   ```
   Then load it in a browser and complete one real chat turn.
6. **Pin the URL** in each device's Hermes config (`gateway`/remote backend field)
   so the desktop app opens the same instance instead of a local one.
7. **Record** host, port, serve mode, cert expiry, and auth mode in
   `bots/hermes/devices/_mesh.md`.

## Failures and what they mean

| Symptom | Cause |
|---|---|
| 502 from serve | dashboard died or port changed — check `--status` |
| Cert error | `tailscale cert` never succeeded; check tailnet HTTPS enabled |
| Login loop | cookie domain mismatch behind the proxy — use the ts.net name, not an IP |
| Works on desktop, not phone | phone not on tailnet, or MagicDNS off |

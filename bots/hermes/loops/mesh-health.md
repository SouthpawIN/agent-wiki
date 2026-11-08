---
type: loop
slug: mesh-health
bot: hermes
schedule: "30 6 * * *"
state: live
skill: webapp-on-tailnet
created: 2026-11-07
---

# mesh-health

Daily 06:30. Six-line health check of the single authority.

## Prompt

Check the mesh, in this order, and report only anomalies plus a one-line OK:

1. Dashboard alive locally: `curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:9119/`
   must be 200 or 302.
2. tailscaled running; if not, start it in userspace mode (see
   `bots/hermes/devices/_mesh.md`, "Container limitation") and re-run
   `tailscale serve --bg --https=8443 9119`.
3. Serve config present: `tailscale --socket=/opt/data/state/tailscale/tailscaled.sock serve status`
   must list 8443 → 127.0.0.1:9119 and 443 → 127.0.0.1:8091.
4. Tailnet reachability **through the SOCKS proxy** (this container has no TUN, so
   a direct curl to the ts.net name will fail and means nothing):
   `curl -sI -m 20 --proxy socks5h://localhost:1055 https://hermes-vps.tail6ff78b.ts.net:8443/`
   must return 302 to `/auth/login`.
5. Device roster: `tailscale status` — note any device that was online yesterday
   and is offline now, but do not treat an offline laptop as a failure.
6. Disk headroom > 15 %.

Never restart the dashboard without saying so. Never change the serve
configuration. If the OAuth login page stops appearing, that is the finding to
report, not something to fix silently.

## Stop condition

Read-only. Escalate; do not self-heal infrastructure silently.

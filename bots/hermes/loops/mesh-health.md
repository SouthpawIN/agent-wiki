---
type: loop
slug: mesh-health
bot: hermes
schedule: "30 6 * * *"
state: spec
skill: webapp-on-tailnet
created: 2026-11-07
---

# mesh-health

Daily 06:30. Six-line health check of the single authority.

## Prompt

Check: dashboard process alive (`hermes dashboard --status`), local HTTP 200 on
127.0.0.1:9119, tailscale serve status active, certificate days-to-expiry
(>14), one device round-trip from the last verified device, and disk headroom
(> 15 %). Report only anomalies plus a one-line OK. Never restart the dashboard
without saying so.

## Stop condition

Read-only. Escalate; do not self-heal infrastructure silently.

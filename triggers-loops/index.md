---
title: Loops
created: 2026-09-17
updated: 2026-09-17
type: loops
---

# Loops

> Every cron job, webhook, and automation in Hermes.

Loops are scheduled tasks that run automatically. Defined in `topics/<topic>/loops/` or via `hermes cron`.

## Active Loops

| Loop | Cadence | Topic | What |
|------|---------|-------|------|
| **senter-umbrella** | 30m | senter-wiki | Governance: merge, dedupe, catalogs |
| **senter-watcher** | continuous | senter-wiki | Cut messages into per-topic inbox |
| **senter-scanwatch** | continuous | senter-wiki | Snapshot `.system-live.json` |
| **turbofit-health-check** | 2h | turbofit | All runtime processes healthy? |
| **turbofit-memory-monitor** | 15m | turbofit | Memory usage across devices |
| **turbofit-candidate-discovery** | 6h | turbofit | New models on HuggingFace |
| **hermes-model-change-detector** | 5m | hermes-agent | Alert if model switches |
| **compression-timeout-watch** | 10m | turbofit | Hermes compression failures |

## Loop States

- **LIVE** — cron job installed and running
- **PROPOSED** — in `topics/*/loops/*.md.proposed`, awaiting approval
- **PAUSED** — installed but disabled

---

## Add a New Loop

1. Create `topics/<topic>/loops/<name>.md.proposed`
2. Review and approve via card
3. Cron job installed via `hermes cron create`

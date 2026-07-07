---
title: Loop Registry
created: 2026-07-07
updated: 2026-07-07
type: catalog
tags: [goop, loops, registry]
---

# Loop Registry

Every running loop. Edit schedule, pause, or remove.

## Factory Loops

| Loop | Schedule | Status |
|---|---|---|
| kashik-context-factory | every 30m | ⏳ pending |
| skrypt-skill-factory | every 15m | ⏳ pending |
| klerik-agent-factory | every 15m | ⏳ pending |
| kadens-loop-factory | every 15m | ⏳ pending |

## Topic Loops

| Loop | Schedule | Agent | Topic | Status |
|---|---|---|---|---|
| (none yet — Kadens creates from queue) | | | | |

## Creating a Loop

**Automatic:** Kadens detects unlooped agents → wires them.

**Manual:** Edit a topic's `.system/queue.md`:
```markdown
## [KADENS] items
- [ ] my-cron — wire my-agent to every hour
```

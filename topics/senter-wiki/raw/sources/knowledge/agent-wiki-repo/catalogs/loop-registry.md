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
| context-factory | every 30m | ⏳ pending |
| skills-factory | every 15m | ⏳ pending |
| agents-factory | every 15m | ⏳ pending |
| loops-factory | every 15m | ⏳ pending |

## Topic Loops

| Loop | Schedule | Agent | Topic | Status |
|---|---|---|---|---|
| (none yet — Loops creates from queue) | | | | |

## Creating a Loop

**Automatic:** Loops detects unlooped agents → wires them.

**Manual:** Edit a topic's `.system/queue.md`:
```markdown
## [LOOPS] items
- [ ] my-cron — wire my-agent to every hour
```

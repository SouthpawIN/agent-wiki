---
title: Agent Roster
created: 2026-07-07
updated: 2026-07-07
type: catalog
tags: [goop, agents, registry]
---

# Agent Roster

Every agent in the fleet. Click any agent to see its SOUL. Edit to change behavior.

## Front Door

| Agent | Profile | Tools | Status |
|---|---|---|---|
| [[nous-girl|Nous Girl]] | `nous-girl` | none (chat-only) | 🟢 Active |

→ SOUL.md: `~/.hermes/profiles/nous-girl/SOUL.md`

## Topic Agents

| Agent | Profile | Skills | Loops | Topic | Status |
|---|---|---|---|---|---|
| (none yet — Agents creates from queue) | | | | | |

## Creating an Agent

**Automatic:** Context → queue → Agents provisions.

**Manual:** Edit a topic's `.system/queue.md`:
```markdown
## [AGENTS] items
- [ ] my-agent — description, skills needed
```

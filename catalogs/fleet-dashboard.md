---
title: Fleet Dashboard
created: 2026-07-07
updated: 2026-07-07
type: catalog
tags: [goop, fleet, overview]
---

# Your Fleet at a Glance

→ [[agent-roster|Agent Roster]] · [[skill-registry|Skill Registry]] · [[loop-registry|Loop Registry]] · [[topic-index|Topic Index]]

## Active Topics

| Topic | Status | Agents | Loops | Last Activity |
|---|---|---|---|---|
| (no topics yet — start chatting with Nous Girl!) | | | | |

## Agent Roster

| Agent | Role | Status |
|---|---|---|
| [[nous-girl]] | Front door — chat surface | 🟢 Active |

## Running Loops

| Loop | Type | Schedule | Status |
|---|---|---|---|
| context-factory | cron | every 30m | ⏳ pending |
| skills-factory | cron | every 15m | ⏳ pending |
| agents-factory | cron | every 15m | ⏳ pending |
| loops-factory | cron | every 15m | ⏳ pending |

## Quick Actions

- **New idea?** Tell Nous Girl — Context creates the topic automatically
- **Force a skill:** Edit `.system/queue.md` → add `[SKILLS] my-skill`
- **Fix a misunderstanding:** Edit `.system/continuity.md` directly
- **See what factories are doing:** Read `log.md`

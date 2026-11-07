---
title: Agent Roster
created: 2026-07-07
updated: 2026-11-07
type: catalog
tags: [agents, registry, senter]
---

# Agent Roster

Bots are the fleet (see [[bot-roster|Bot Roster]]). This page is the front door:
the one agent you talk to, and the roles it spawns.

## Front Door

| Agent | Profile | Role | Status |
|---|---|---|---|
| [[senter|Senter]] | `senter` | three-eyed owl; conversational surface over the whole wiki | active |

→ SOUL: `~/.hermes/profiles/senter/SOUL.md`

## Spawned roles

Factories do not get permanent profiles. They are `delegate_task` roles invoked by
a cron tick:

| Role | Invoked by | Writes |
|---|---|---|
| Context | context cron | `.system/continuity.md`, queue items |
| Skills | skills cron | `skills/*/SKILL.md` |
| Agents | agents cron | bot scaffolding, profiles |
| Loops | loops cron | cron jobs, kanban |

## Rule

No agent edits its own definition. Senter cannot rewrite Senter; the agents
factory cannot change the agents factory.

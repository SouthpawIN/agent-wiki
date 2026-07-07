---
title: GOOP Nesting
created: 2026-07-04
updated: 2026-07-07
type: concept
tags: [goop, architecture, nesting]
---

# GOOP Nesting Architecture

The object hierarchy: **Context → Loops → Agents → Skills**

```
┌─ Context (Wiki pages, Continuity entries) ← Kashik maintains
│  ┌─ Loops (cron, kanban, webhooks)        ← Kadens wires
│  │  ┌─ Agents (profiles, SOUL.md)          ← Klerik creates
│  │  │  ┌─ Skills (SKILL.md bundles)        ← Skrypt authors
```

Each layer builds on the previous. The nesting means each factory's output is the next factory's input.

## Factory Chain

| Factory | Produces | Feeds |
|---|---|---|
| Kashik | Context (Wiki pages, queue items) | All factories |
| Skrypt | Skills | Klerik |
| Klerik | Agents | Kadens |
| Kadens | Loops | The Fleet |

The full chain: idea → context → skill → agent → loop, all automatic.

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
┌─ Context (Wiki pages, Continuity entries) ← Context maintains
│  ┌─ Loops (cron, kanban, webhooks)        ← Loops wires
│  │  ┌─ Agents (profiles, SOUL.md)          ← Agents creates
│  │  │  ┌─ Skills (SKILL.md bundles)        ← Skills authors
```

Each layer builds on the previous. The nesting means each factory's output is the next factory's input.

## Factory Chain

| Factory | Produces | Feeds |
|---|---|---|
| Context | Context (Wiki pages, queue items) | All factories |
| Skills | Skills | Agents |
| Agents | Agents | Loops |
| Loops | Loops | The Fleet |

The full chain: idea → context → skill → agent → loop, all automatic.

---
title: Agent Wiki Spec (vault edition)
updated: 2026-08-27
type: spec
tags: [goop, architecture]
---

# Structure conventions

Adapted from [SouthpawIN/agent-wiki](https://github.com/SouthpawIN/agent-wiki).

## Primitives (nesting): Context → Loops → Agents → Skills

## Topic anatomy
```
topics/<repo>/
├── README.md          ← human dashboard (facts + full README extract)
├── .system/           ← hidden machine internals (the debugger)
│   ├── INDEX.md       ← progressive disclosure entrypoint
│   ├── queue.md       ← [SKILLS]/[BOTS]/[LOOPS] work items
│   └── injections.md  ← status for the chat surface ([UNREAD]/[READ])
├── wiki/              ← full topic wiki (entities, concepts, decisions, queries)
├── skills/
├── bots/
└── loops/
```

## Steering wheel
| You want | Edit |
|---|---|
| Fix my understanding | `.system/continuity.md` |
| Force a skill | `.system/queue.md` — add `[SKILLS]` |
| Request a bot | `.system/queue.md` — add `[BOTS]` |
| Wire a schedule | `.system/queue.md` — add `[LOOPS]` |
| See status | [[catalogs/fleet-dashboard|Fleet Dashboard]] |

Principles: markdown is the API · the wiki is the system · user-editable everything · dot-prefix hides internals · topics self-contained · factories thin · injections keep you in the loop · no self-edit.

## Terminology (locked 2026-09-02)
**Bots** = the individual Hermes profiles we create (senter, turbosovth, klerik, anser, teknium, dogeman, paladin). **Hermes Agent** = the whole runtime they live in. Say *bots*, not *agents*, in all UI, docs, and chat. The vault directory `topics/<name>/agents/` keeps its name for GOOP-spec compatibility; it holds bots.

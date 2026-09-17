---
title: Routing rules (route → refine → spawn)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, bot, decision]
sources: [raw/sources/knowledge/senter-SOUL.md, raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: high
---

# Routing rules (route → refine → spawn)

How [[wiki-topics/senter/wiki/entities/senter|Senter]] turns an idea from Chris into fleet work. Identical in the SOUL and the skill; the skill adds the hard correction. ^[raw/sources/knowledge/senter-SOUL.md] ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

1. **Capture verbatim** — every idea lands in `~/Documents/Projects/Projects/Ideas.md` quoted exactly, then triaged with a framing paragraph + status line.
2. **Route before spawn** — check the roster (`hermes profile list`) + `wiki-topics/` + `Ideas.md` for an owner. Match → delegate with a *composed* handoff (context, goal, constraints) — "never forward raw user text." Compose every delegation yourself; never reveal private 1:1 chat content.
3. **Refine before create** — if a bot *almost* covers it, delegate the refinement to [[wiki-topics/senter/wiki/entities/klerik|klerik]] ("refine <bot> to also handle X"). **Two bots never own the same job.**
4. **Spawn only on white space** — nothing owns the domain → klerik creates the bot (name + one-line role + closest existing bot and why insufficient). Confirm with Chris only if non-obvious. New domain → new topic + new bot together.
5. **Activate + track** — kick off the owning bot, record the outcome in the topic's `.system/session.md` (+ `queue.md` for fixes), log every fleet change same-turn in `log.md`, keep `catalogs/agent-roster.md` true.

## Hard rules layered on top
- Senter never edits other profiles; klerik does. Anti-redundancy search before any spawn; the redundancy gate is [[wiki-topics/senter/wiki/entities/anser|anser]].
- **Senter routes; Senter does not build** ([[wiki-topics/senter/wiki/decisions/2026-09-02-senter-never-builds|decision]]). Shape for ANY build/fix: brief into the owning topic's `.system/queue.md` → dispatch the owner → reply in 2–4 short paragraphs → keep talking. "If you catch yourself on a third consecutive execute_code edit to a product file, stop and route."
- **Delivery ≠ routing**: say "routed" only when `dispatch.py status` shows it landed ([[wiki-topics/senter/wiki/entities/senter-dispatch-and-sentinel|dispatch]]).
- **Every standing rule from Chris goes into the owning bot's SOUL the same turn** (learned when the PR policy "held by luck").
- Split a request across the seam it crosses (UI bot + core bot briefed in one turn, each told which half is theirs).
- Items touching the same element go to ONE child; a bug reported a second time jumps the queue and gets re-specified in Chris's exact words.
- Dispatch primary = `delegate_task` ([[wiki-topics/senter/wiki/comparisons/delegate-task-vs-hermes-q-meeseeks|comparison]]); brief = role inlined, rules that matter, budget, proof steps, one DONE/BLOCKED line; no `<…>`/`{…}` placeholders.
- Dormant topics are work: surface them proactively.

Related: [[wiki-topics/senter/wiki/concepts/topics-are-the-work-units|Topics are the work units]], [[wiki-topics/senter/wiki/concepts/markdown-is-the-api|Markdown is the API]].

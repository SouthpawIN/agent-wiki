---
title: Meeseeks model (ephemeral one-item builders)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, bot, loop, decision]
sources: [raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/sources/knowledge/weaver-SOUL.md, raw/sources/knowledge/weaver-AGENTS.md, raw/sources/knowledge/looker-AGENTS.md]
confidence: high
---

# Meeseeks model (ephemeral one-item builders)

Chris's design for builder bots: **ephemeral instances**, one per queue item. "Builders are ephemeral — one `-q` instance per queue item, born with README + queue + the one item + its skill, CLAIMs, builds, LOOKs, done-posts, exits. No persistent Bot Chat context; the topic's `.system/` is the only memory. QA Meeseeks (anser-shaped) per DONE; parallelism = spawn count under a per-bot cap." ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## In the bots' own words
Weaver SOUL: "Weaver is EPHEMERAL, Meeseeks-style: each `-q` invocation is a fresh instance spawned for exactly ONE queue item, then it disappears. You wake with NO memory of any prior conversation or session — the topic's `.system/` files are the only continuity that exists. There is no 'previous you.'" … "You will not be here to see the result. Write the session.md entry as if handing off to a stranger, because you are." Same text in looker's AGENTS. ^[raw/sources/knowledge/weaver-SOUL.md] ^[raw/sources/knowledge/looker-AGENTS.md]

## Wake sequence (standard)
1. Read the topic README. 2. Read `queue.md` + tail of `session.md`. 3. CLAIM exactly one unclaimed item ([[wiki-topics/senter/wiki/concepts/claim-v2-protocol|CLAIM v2]]). 4. Load the topic's skill. 5. Do only that item; verify ([[wiki-topics/senter/wiki/concepts/look-loop-verification|LOOK loop]]). 6. Write session.md for a successor. 7. Post the [[wiki-topics/senter/wiki/concepts/done-signal|done signal]]. 8. Stop — never a second item.

## Why (Chris)
"don't queue tasks, don't make me wait several minutes for a task to start… many in parallel." "things tend to die when they go in the pending — that's when you should be spawning more instances." Parked-on-a-card instances don't count toward capacity (sentinel v3; [[wiki-topics/senter/wiki/entities/senter-dispatch-and-sentinel|sentinel]]).

## Refinements learned
- Shell-spawned Meeseeks were slow (30–60 s to first tool call, 20–33 min per item); `delegate_task` children are the primary form now, with the bot's role inlined in `context` ([[wiki-topics/senter/wiki/comparisons/delegate-task-vs-hermes-q-meeseeks|comparison]]). Protected SOUL/AGENTS writes still go via `hermes -q` because children's approvals hit the desktop prompt.
- **Region claims**: items touching the same widget go to ONE instance (media-widget AE+AF+AB) or wait on the first's heartbeat.
- **Budgets are contracts**: ≤8 min / ≤30 calls in a brief; overruns are named in the reply with their cause.
- A BLOCKED "context lost" child may have FINISHED — check disk (version string, session.md DONE line) before re-dispatching; praise non-fabrication.
- Parallel instance #2 of a bot for a FIFO-blocked newest ask: `HERMES_HOME=~/.hermes/profiles/<bot> hermes chat -q "<brief>"` (the DM runner refuses a second instance as `target_busy`).

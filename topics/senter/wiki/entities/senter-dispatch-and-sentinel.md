---
title: senter-dispatch + senter-sentinel (self-healing pipeline)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [tool, infra, loop, pain]
sources: [raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: high
---

# senter-dispatch + senter-sentinel (self-healing pipeline)

[2026-09-05, t_f1b1eba1: the SENTINEL is retired — daemon unplugged, `sentinel.py` deleted; the kanban dispatcher + fleet-tick replaced it. Dispatch remains live. Full account lives in the skill's `references/self-healing-pipeline.md` and `references/fleet-dispatch.md`. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]]

## senter-dispatch (`~/.hermes/plugins/senter-bridge/dispatch.py`, launchd `com.senter.dispatch`)
- **Why**: DELIVERY ≠ ROUTING. On 2026-09-02, 5 of 7 DMs to weaver/teknium were silently dropped — the DM runner gives up after ~120 s of `target_busy` when a bot is mid-turn (builders in a verify loop are mid-turn 5–15 min), and free-tier bots die with HTTP 429 under LOOK-loop load. Chris: "are you just writing up these specs? … there's not any motion happening."
- **What**: per-bot queue, delivers on idle, retries busy/429, posts `queued/delivering/delivered` into the wiki. Say "routed" only after `dispatch.py status` shows it; bundle stacked corrections into one queued message per bot; heavy builders on a paid tier.
- Fallback when `message_agent` is missing: write the body to a temp file prefixed `Message from 🤖 senter (@senter): ` and run `bot_mode_dm.py --run-delivery query-file <file> hermes -p <bot> chat … -Q` (`-p <bot>` BEFORE `chat`).

## senter-sentinel (launchd, 30 s)
"A monitor must ACT, and must not cry wolf." Spawns a [[topics/senter/wiki/concepts/meeseeks-model|Meeseeks]] for any item queued >3 min under cap, kickstarts a dead daemon, flags silent bots ONCE, flags stale previews — every action posted to the wiki. First-hour bugs: briefs fired empty (`$(cat path)` ran after the file was renamed → pass content via argv) and false "stalled" flags from a pgrep matching shells.
- **Sentinel v3** (Chris: "things tend to die when they go in the pending — that's when you should be spawning more instances"): pids recorded in `pending/<id>.json` (parked on an approval card) are excluded from capacity; while anything is parked the undelivered threshold drops 3 min → 30 s and the next item gets its own Meeseeks. Posts hard caps: 12 min → progress line, 20 min → BLOCKED with diff.

## The five "why is it slow AGAIN?" rounds (2026-09-02)
Each round was a real, *different* bottleneck — "the bottleneck MOVED — measure the current one":
1. DMs silently dropped → dispatch daemon.
2. Fixes in the file but preview pinned to a stale `?v=` → reload the preview on every version bump, same turn.
3. Daemon "at capacity" stranding new items → sentinel auto-spawn.
4. Each 3-line CSS item cost 20–33 min / 120–160 tool calls; same-widget items chained on each other's claims → verify-LIGHT/FULL, region claims, module split, `delegate_task` primary ([[topics/senter/wiki/comparisons/delegate-task-vs-hermes-q-meeseeks|comparison]]).
5. `vision_analyze` = 84% of fleet tool time (55 calls, avg 67 s, max 273 s) because `auxiliary.vision.provider: auto` picked a free-tier model → pin a timed model (gemini-3.8-flash at 4.4 s) with a 45 s timeout in root AND every profile config (`scripts/tool-latency.sh`).

## Related rules
- FIFO backlog blocking Chris's newest ask ⇒ launch a second instance directly ("PARALLEL INSTANCE #2, you own <seam> only" — one kanban card per item; CLAIM v2 retired 2026-09-05).
- Watcher wake-ups: only `NEEDS` (a `needs_chris` card exists) and `RELOAD` (version bumped, ≤1 per 3 min); plain done-lines are NOT relayed — they're already in the wiki stream. Background watch-pattern notifications cap at ~8 matches.
- `scripts/fleet-status.sh` answers "Is it still working? I have no clue." with numbers. See [[topics/senter/wiki/concepts/fleet-coordination-lessons|lessons]].

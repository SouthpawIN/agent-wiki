---
title: Fleet spawn policy — kanban dispatcher is primary
updated: 2026-09-05
type: process
status: in-force
owner: senter
reviewer: anser
source: wiki-topics/senter/plans/worker-model-2026-09-02.md (items 1 and 5, council 2026-09-02)
---

# Fleet spawn policy — dispatcher primary, shell spawn is the emergency hatch

Chris (2026-09-02): "don't queue, don't make me wait minutes, conversation keeps going, many in parallel, Meeseeks-style." Council verdict (Anser review, `worker-model-2026-09-02.md`): route ALL fleet worker spawning through the kanban dispatcher.

## 1. Primary — kanban dispatcher (in force 2026-09-05)

Every fleet work item becomes a kanban card; the gateway dispatcher spawns the worker:

```
hermes kanban create "<one-line item>" \
  --body "<full brief: item, seam, file+line anchors, contract>" \
  --assignee <bot> --json
```

- Claim, heartbeat, stale-reap, and workspace isolation are native (`hermes kanban claim` is a SQLite CAS; stale claims reaped automatically). No `mkdir` CLAIM v2, no sentinel respawn arithmetic.
- Parallelism = card count; the dispatcher honors per-profile dispatch and `dispatch_stale_timeout_seconds` (4 h default).
- Helpers that used to shell out (`senter-bridge/dispatch.py`, `sentinel.py spawn_meeseeks`) now call `hermes kanban create` (see §3). Bridge attribution keeps working — the worker's own bridge POSTs carry `bot=<role>`.
- Batch items: one card per item, created in the same turn (`tasks=[…]`-style batching = repeat `create`, or the `swarm` verb for worker→verifier→synthesizer graphs).

## 2. Emergency hatch — direct shell spawn (retained, documented)

```
HERMES_HOME=~/.hermes/profiles/<bot> hermes chat -q "<role pack>"
```

May be used ONLY when one of these holds:

1. **Gateway down** — the dispatcher runs inside the gateway; if `hermes serve`/gateway is not up, no card will ever dispatch. Spawn directly, then post to the bridge so the stream shows it.
2. **Dispatcher failing or stranding work** — a card sits in `ready` past ~3 min with no worker run (check `hermes kanban list` / `kanban diag`): spawn directly for that item rather than let Chris wait.
3. **Protected-file writes needing the bot's own HERMES_HOME approval context** — wiki cards work for most, but if a job must approve in the bot's own home, run it under that profile directly.
4. **Work that must outlive the gateway** (e.g. long unattended build during a gateway restart).

Every direct spawn MUST: post a bridge line ("emergency hatch spawn: <bot>, <reason>") and write a kanban card for the item anyway (or comment on the existing card) so the board stays the source of truth. The hatch is per-item relief, never a policy.

Helpers honor the hatch via env: `SENTER_EMERGENCY_SPAWN=1` forces dispatch.py back onto the direct `hermes chat` path. Unset (default) = dispatcher.

## 3. What changed (2026-09-05)

- `senter-bridge/dispatch.py` — `deliver()` routes each queued item through `hermes kanban create --assignee <bot>`; direct `hermes -p <bot> chat` delivery kept only under `SENTER_EMERGENCY_SPAWN=1`.
- `senter-bridge/sentinel.py` — **RETIRED (2026-09-05, kanban t_f1b1eba1):** daemon stopped and unplugged (launchd plist archived at `~/.hermes/senter-bridge/disabled/`), `sentinel.py` deleted. Its remaining useful checks live in `fleet_tick.sh` (stuck/failed cards, every 15m); preview-reload detection already existed in watcher.py and is unaffected.
- `wiki-topics/senter/triggers-loops/kanban-dispatch.md` — status: adopted; this policy referenced.
- `wiki-topics/senter/process/build-loop.md`, `senter-turn-checklist.md` — spawn wording updated.
- Builder/looker AGENTS.md "Working a topic queue" sections — CLAIM v2 (mkdir sidecar + heartbeat + reaper) replaced with the kanban-native procedure (t_f1b1eba1); vault mirrors re-synced.

## 4. Related

- CLAIM v2 + sentinel: REMOVED 2026-09-05 (kanban t_f1b1eba1) — no live code path or fleet prompt references them; historical accounts in log.md and the anser transcripts remain as record.
- `delegate_task` remains Senter's in-thread escalation for sub-5-second same-conversation reasoning, not a fleet spawn path.

---
title: CLAIM v2 protocol (atomic mkdir claims)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, infra, loop]
sources: [raw/sources/knowledge/paladin-AGENTS.md, raw/sources/knowledge/weaver-AGENTS.md, raw/sources/knowledge/looker-AGENTS.md, raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: high
---

# CLAIM v2 protocol (atomic mkdir claims)

[RETIRED 2026-09-05 (kanban t_f1b1eba1) — replaced by `hermes kanban` claims (SQLite CAS, dispatcher-owned reclaim). Historical record below; nothing here is operative.]

How multiple [[topics-wiki/senter/wiki/concepts/meeseeks-model|Meeseeks]] instances work one topic queue in parallel without colliding. Identical text in paladin's, weaver's and looker's AGENTS. v2 exists because [[topics-wiki/senter/wiki/entities/anser|anser]] found a **check-then-act race** in v1 during the merge audit — "Claims use an ATOMIC primitive — not check-then-act." ^[raw/sources/knowledge/paladin-AGENTS.md] ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## The protocol
`$C = topics-wiki/<topic>/.system/claims`, `$ITEM` = item id.
1. **Claim = mkdir.** `mkdir "$C/$ITEM" 2>/dev/null && (echo "$BOT $$ $(date -u +%FT%TZ)" > "$C/$ITEM/owner"; touch "$C/$ITEM/heartbeat") || skip` — mkdir is atomic on POSIX: success = you own it; `EEXIST` = someone else does → skip to the next unclaimed item. Never touch another instance's claim dir.
2. **Heartbeat.** Touch `$C/$ITEM/heartbeat` every 60 s while working.
3. **Reaper.** Heartbeat older than 10 min = stale; any instance may `rm -r` and re-claim. Crashed instances never block an item for good.
4. **queue.md is the LOG, not the lock.** Append `CLAIM/DONE/BLOCKED <item> <bot> <ts>` lines for humans. "The directory is the lock; the line is the record."
5. **On finish:** write `result` (done|blocked + one line) into the claim dir, append `DONE <item>` / `BLOCKED <item> <why>` to queue.md, then `rm -r` the claim dir.
6. Outcome writes go to `.system/session.md` under a dated `## YYYY-MM-DD` heading, append-only — never rewrite or reorder.

## Region / element claims (2026-09-02 refinement)
For tiny edits, claim the ELEMENT (e.g. `media-widget`) and bundle every queue item for it into one pass — three bots fighting one 180 px widget (items AE/AF/AB chained on each other's claims) was one of the "slow again" causes. Diagnostic order for stalls: `ps` ages + claim heartbeats → done-lines → tool-events/min → per-item Duration in bot logs. ^[raw/sources/knowledge/weaver-AGENTS.md]

## Related
`hermes kanban` claims were proposed (2026-09-05) as the native equivalent for per-topic workers ([[topics-wiki/senter/wiki/entities/hermes-agent|Hermes Agent]]). Sentinel v3 treats a parked-on-card pid as holding a claim but doing no work ([[topics-wiki/senter/wiki/entities/senter-dispatch-and-sentinel|sentinel]]). Recipe: skill `references/parallel-topics-and-claims.md`.

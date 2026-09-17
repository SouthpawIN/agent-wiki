---
title: Query — did the two kept loops (paladin wiki-dedupe-sweep, looker player-regression-check) actually tick after the gateway fix?
created: 2026-09-05
updated: 2026-09-05
type: query
tags: [question, loop, infra, timeline]
sources: [raw/inbox/2026-09-05.md]
confidence: medium
---
# Did the two kept loops tick?

**Status: open — registered, gateways running, zero executions at 19:07.** The 18:58 close-out lists both as "Live" alongside klerik-queue-drain ^[raw/inbox/2026-09-05.md]. Under the proof standard in [[topics/klerik/wiki/concepts/proposal-apply-path|Proposal apply path]] (proof = first tick logged, not job listed), only klerik's loop has passed; the two approved at 18:55 ([[topics/klerik/wiki/decisions/2026-09-05-approve-two-kept-loops-via-real-path|Approve the two kept loops via the real path]]) have not yet had a chance.

| Loop | Owner | Job | Schedule | Gateway (launchctl) | `cron runs` at 19:07 | First tick expected |
|---|---|---|---|---|---|---|
| klerik-queue-drain | klerik | e6e20c22e1b9 | every 30m | running, pid 5306 | 1 completed (18:50:25); output 18:56:40 | **ticked** |
| wiki-dedupe-sweep | paladin | 9e70db5cfa27 | every 30m | running, pid 5635 | none | ~19:25 |
| player-regression-check | looker | 95e13093ff26 | every 120m | running, pid 5634 | none | ~20:55 |

**What "yes" looks like.** `hermes -p paladin cron runs 9e70db5cfa27` and `hermes -p looker cron runs 95e13093ff26` each show a `completed` row, and each profile's `cron/output/<job>/` has a dated markdown file. A `[SILENT]` result still counts as a tick.

**Why it matters.** This is the test of whether the gateway fix generalises ([[topics/klerik/wiki/concepts/gateway-was-the-missing-ticker|Gateway was the missing ticker]]). If klerik ticks and the other two never do, the root cause was not fully found and the 18:58 "Live" would be the same premature flag the 18:47 stand-up set — see [[topics/klerik/wiki/comparisons/claimed-completed-vs-verified-on-disk|Claimed completed vs verified on disk]].

**Not a card for Chris.** This is the machine checking itself; the answer will be written here by the next compile that sees a run, not asked of him.

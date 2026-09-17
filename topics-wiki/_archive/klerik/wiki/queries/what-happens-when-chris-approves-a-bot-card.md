---
title: Query — what actually happens when Chris approves a bot card?
created: 2026-09-05
updated: 2026-09-05
type: query
tags: [question, bot, ui, infra]
sources: [raw/inbox/2026-09-05.md]
confidence: medium
---
# What actually happens when Chris approves a bot card?

**Short answer (2026-09-05).** The card's file gets renamed. Nothing else. "Approving a bot card still just renames the file; the actual `hermes profile create` via klerik is the next wire." ^[raw/inbox/2026-09-05.md]

**Longer answer.** The wiki's read path is live — the compile lands entities (chris, anser, klerik were cited as already landing) and "the corpus reloads automatically" ^[raw/inbox/2026-09-05.md] — but the act path from approval to a running profile has not been built. So the product currently promises proposal → approval → bot, and delivers proposal → approval → rename.

**Why this and klerik's idle queue are one problem.** klerik's `.system/queue.md` holds nine unchecked REFLECT passes with anser escalating "the reflect loop is producing proposals nobody applies." The approval wire has the same shape: proposals exist, an approval step exists, the executor (klerik) is never invoked. Fixing the wire means giving klerik an event to act on; draining the queue means giving klerik a cadence to act on. Both are "make klerik run", not "write more rules".

**Update 18:18.** The next instruction was to stop describing and test: "prove the apply path with one real approval" ^[raw/inbox/2026-09-05.md]. The test used a loop card, not a bot card, and the apply step failed (cron create → FAILED, file marked LIVE anyway) — see [[topics-wiki/klerik/wiki/queries/has-the-apply-path-been-proven|Has the apply path been proven?]]. The bot-card branch stays untested.

**What would change the answer.** Building the [[topics-wiki/klerik/wiki/concepts/bot-card-approval-wire|Bot-card approval wire]] so that approval invokes [[topics-wiki/klerik/wiki/entities/klerik|klerik]]'s spawn checklist and the card only shows "running" after `bridge/loaded`. Decision record: [[topics-wiki/klerik/wiki/decisions/2026-09-05-approval-to-profile-create-is-next-wire|Approval → profile create is the next wire]].

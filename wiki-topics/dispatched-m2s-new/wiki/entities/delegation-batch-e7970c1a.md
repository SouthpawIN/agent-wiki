---
title: delegation batch deleg_e7970c1a
created: 2026-09-17
updated: 2026-09-17
type: entity
tags: [infra, delegation, completion]
sources: [raw/inbox/2026-09-17.md]
confidence: low
---

# delegation batch deleg_e7970c1a

A Hermes async delegation batch reported complete on `2026-09-17 12:14` (message ID `20260914_200308_f9b029`, simulation `0.27`). The batch fanned out to `1` subagent and completed without the owner-exit error.

^[raw/inbox/2026-09-17.md] At `2026-09-17 12:14`, `"[ASYNC DELEGATION BATCH COMPLETE — deleg_e7970c1a] A background fan-out unit you dispatched earlier — 1 subagent(s) — has finished; its consolidated results are below. Any other units from the same delegate_task call report separately as they finish. You may have moved on since dispatching — act on these or re-dispatch if things have changed."`

^[raw/inbox/2026-09-17.md] A live transcript path was recorded: `/Users/sovthpaw/.hermes/cache/delegation/live/deleg_e7970c1a/task-0.log` — the first time a transcript path has been captured for a batch in this topic.

## Timeline

- **2026-09-17 (dispatch time not recorded):** dispatched as a background fan-out unit.
- **2026-09-17 12:14:** reported complete — 1 subagent, no owner-exit error.

## Notes

- The exact dispatch timestamp is not recorded in the completion message.
- Model, role, and duration were not recorded — the same detail gap seen on [[entities/delegation-batch-a5b975f7|batch deleg_a5b975f7]] and [[entities/delegation-batch-e76115bb|batch deleg_e76115bb]].
- The consolidated results are "below" in the completion message but were not carried into this raw filing.

## Why this matters to the topic

Another `1`-subagent batch that completed normally — the same size as the failing [[entities/delegation-batch-e76115bb|batch deleg_e76115bb]] but without the owner-exit error. Reinforces that batch size is not the driver of the failure. See [[concepts/delegation-timeout|delegation owner exit timeout]].

## Relationship

- [[entities/dispatched-m2s|dispatched-m2s]] — parent topic
- [[concepts/delegation-timeout|delegation owner exit timeout]] — the failure mode this batch did NOT hit
- [[entities/delegation-batch-a5b975f7|batch deleg_a5b975f7]] — sibling 1-subagent success

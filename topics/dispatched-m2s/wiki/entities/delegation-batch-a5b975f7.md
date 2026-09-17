---
title: delegation batch deleg_a5b975f7
created: 2026-09-17
updated: 2026-09-17
type: entity
tags: [infra, delegation, completion]
sources: [raw/inbox/2026-09-16.md]
confidence: low
---

# delegation batch deleg_a5b975f7

A Hermes async delegation batch reported complete on `2026-09-16 21:11` (message ID `20260914_200308_f9b029`, simulation `0.19`). The batch fanned out to `1` subagent and completed without the owner-exit error.

^[raw/inbox/2026-09-16.md] At `2026-09-16 21:11`, `"[ASYNC DELEGATION BATCH COMPLETE — deleg_a5b975f7] A background fan-out unit you dispatched earlier — 1 subagent(s) — has finished; its consolidated results are below. Any other units from the same delegate_task call report separately as they finish. You may have moved on since dispatching — act on these or re-dispatch if things have changed."`

## Timeline

- **2026-09-16 (dispatch time not recorded):** dispatched as a background fan-out unit.
- **2026-09-16 21:11:** reported complete — 1 subagent, no owner-exit error.

## Notes

- The exact dispatch timestamp is not recorded in the completion message.
- Model, role, and duration were not recorded — the same detail gap seen on [[entities/delegation-batch-e76115bb|batch deleg_e76115bb]] and [[entities/delegation-batch-e7970c1a|batch deleg_e7970c1a]].
- The consolidated results are "below" in the completion message but were not carried into this raw filing.

## Why this matters to the topic

This is a `1`-subagent batch that completed normally, alongside [[entities/delegation-batch-e76115bb|batch deleg_e76115bb]] which was also `1` subagent but FAILED with the owner-exit error. Same size, opposite outcome — further evidence that batch size is not the driver. See [[concepts/delegation-timeout|delegation owner exit timeout]] and [[comparisons/owner-exit-success-patterns|owner-exit vs smaller-fan-out outcomes]].

## Relationship

- [[entities/dispatched-m2s|dispatched-m2s]] — parent topic
- [[concepts/delegation-timeout|delegation owner exit timeout]] — the failure mode this batch did NOT hit
- [[comparisons/owner-exit-success-patterns|owner-exit vs smaller-fan-out outcomes]]
- [[decisions/batch-size-mitigation-pattern|batch size mitigation pattern]]

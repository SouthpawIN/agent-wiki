---
title: owner-exit vs smaller-fan-out outcomes
created: 2026-09-07
updated: 2026-09-07
type: comparison
tags: [infra, delegation, decision]
sources: [raw/inbox/2026-09-07.md]
confidence: low
---

# owner-exit vs smaller-fan-out outcomes

This page compares the failing owner-exit batch against the later successful batches to separate true failure causes from coincidence.

^[raw/inbox/2026-09-07.md] Failing batch `deleg_e76115bb` used `1` subagent and failed with: `Delegation owner exited before recording a terminal result; outcome unknown.`

^[raw/inbox/2026-09-07.md] Successful batch `deleg_56809b77` used `4` subagents and completed at `2026-09-07 10:08`; transcript at `/Users/sovthpaw/.hermes/cache/delegation/live/deleg_56809b77/task-3.log`.

^[raw/inbox/2026-09-07.md] Successful batch `deleg_dc36df32` used `2` subagents and completed at `2026-09-07 10:39`.

## Inference

Smaller subagent counts did not consistently map to success/failure here because `deleg_dc36df32` used `2` and succeeded while `deleg_e76115bb` used `1` and failed. If batch size were the only factor, `1` should be safer than `4`, which was not observed. This means the owner-exit error should be investigated separately from batch-size tuning unless the smaller batches in the later runs also used shorter prompts. Chris noted shorter prompts helped relative throughput, so the favorable outcome may reflect prompt length more than fan-out count.

## Contested

This comparison is weakened by missing model/duration/goal data for the failing batch, so the size-based conclusion is tentative.

## Related

- [[entities/delegation-batch-e76115bb|batch deleg_e76115bb]]
- [[entities/delegation-batch-56809b77|batch deleg_56809b77]]
- [[entities/delegation-batch-dc36df32|batch deleg_dc36df32]]
- [[concepts/delegation-timeout|delegation owner exit timeout]]
- [[decisions/batch-size-mitigation-pattern|batch size mitigation pattern]]

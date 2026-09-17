---
title: batch size mitigation pattern
created: 2026-09-07
updated: 2026-09-17
type: decision
tags: [decision, infra, delegation, pattern]
sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-16.md, raw/inbox/2026-09-17.md]
confidence: low
---

# batch size mitigation pattern

**What**: Reduce async delegation batch sizes to improve reliability and throughput.

**When**: After delegation owner exit timeout failures (see [[concepts/delegation-timeout|delegation timeout]]).

**Why**: Chris observed that "The short prompt benefits from better relative throughput" when using smaller batch counts.

## Evidence

^[raw/inbox/2026-09-07.md] Failed batch deleg_e76115bb: 1 subagent, role `leaf`, resulted in `Delegation owner exited before recording a terminal result; outcome unknown.`

^[raw/inbox/2026-09-07.md] Successful batch deleg_56809b77: 4 subagents, no error reported. Transcript available at `/Users/sovthpaw/.hermes/cache/delegation/live/deleg_56809b77/task-3.log`

^[raw/inbox/2026-09-07.md] Successful batch deleg_dc36df32: 2 subagents, no error reported.

## Implementation

When dispatching async delegations, use short prompts paired with smaller batch sizes (≤4 subagents) rather than larger fan-outs. Chris explicitly noted: `The short prompt benefits from better relative throughput.`

## Contested

The initial failed batch used only 1 subagent, yet still failed, suggesting batch size alone is not the sole factor. The remediation note at 09:16 suggested checking logs "and try with reduced batch sizes," but no outcome was recorded for that remediation attempt.

^[raw/inbox/2026-09-16.md] The hypothesis is now further weakened: [[entities/delegation-batch-7418fbf4|batch deleg_7418fbf4]] succeeded at a fan-out of `5` subagents on 2026-09-16 — larger than every earlier successful batch (4 and 2). If smaller batches were the mitigation, no larger batch should have succeeded, yet this one did. Batch size appears to be at most one of several factors, not the driver.

^[raw/inbox/2026-09-16.md] [[entities/delegation-batch-a5b975f7|batch deleg_a5b975f7]] (2026-09-16 21:11) succeeded at a fan-out of `1` subagent — the same size as the failing [[entities/delegation-batch-e76115bb|batch deleg_e76115bb]] — with the opposite outcome. Same size, opposite result, ruling out batch size as the driver entirely.

^[raw/inbox/2026-09-17.md] [[entities/delegation-batch-e7970c1a|batch deleg_e7970c1a]] (2026-09-17 12:14) succeeded at a fan-out of `1` subagent — again the same size as the failing batch, again no owner-exit error.

## Related

- [[entities/dispatched-m2s|dispatched-m2s]] - the overall topic
- [[entities/delegation-batch-e76115bb|batch deleg_e76115bb]] - the failed instance
- [[concepts/delegation-timeout|delegation owner exit timeout]] - the failure mode

---
title: batch size mitigation pattern
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [decision, infra, delegation, pattern]
sources: [raw/inbox/2026-09-07.md]
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

## Related

- [[entities/dispatched-m2s|dispatched-m2s]] - the overall topic
- [[entities/delegation-batch-e76115bb|batch deleg_e76115bb]] - the failed instance
- [[concepts/delegation-timeout|delegation owner exit timeout]] - the failure mode

---
title: delegation owner exit timeout
created: 2026-09-07
updated: 2026-09-10
type: concept
tags: [infra, pain, delegation]
sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-09.md, raw/inbox/2026-09-10.md, raw/inbox/2026-09-16.md]
confidence: low
---

# delegation owner exit timeout

A failure mode in which the delegation owner process exits before recording a terminal result for its leaf subagent batch. The observable result is the error string:

> Delegation owner exited before recording a terminal result; outcome unknown.

^[raw/inbox/2026-09-07.md] This error appeared on [[entities/delegation-batch-e76115bb|batch deleg_e76115bb]] within the [[entities/dispatched-m2s|dispatched-m2s]] topic.

## Notes

- The batch used async fan-out of `1` subagent.
- Duplicate delivery of the same terminal message suggests possible retry/replay of an earlier system notification.
- Outcome unknown means no child summary is available for recovery without manual inspection.
- At `2026-09-07 09:16`, Hermes emitted: `Let me check the current log and try with reduced batch sizes:`, indicating post-failure remediation intent, though no outcome was recorded for that attempt.

## Contested observation

^[raw/inbox/2026-09-07.md] The same terminal message was received twice under IDs `20260903_001447_7bc70a` with simulation values
`0.06` and `0.12`. Chris noted this occurrence without correction.

^[raw/inbox/2026-09-09.md] On 2026-09-09, the same ID `20260903_001447_7bc70a` resurfaced carrying an unrelated successful message
(`Git commit was successful...`, simulation `0.07`), suggesting the ID may be reused across unrelated topics rather than a retry
of the same notification. On 2026-09-10, the same ID carried shell tool
inconsistency messages (sim `0.08` and `0.07`), confirming reuse across
unrelated content. See [[entities/hermes-message-20260903-001447-7bc70a|Hermes state.db message 20260903_001447_7bc70a]]
and [[entities/delegation-message-20260903-7bc70a|Hermes message 20260903_001447_7bc70a]]. <!-- chris -->

## Related entities

- [[entities/delegation-batch-e76115bb|delegation batch deleg_e76115bb]] - the failed batch instance

## Potential mitigation

Based on the raw inbox data, successful subsequent batches used smaller subagent counts:
- deleg_56809b77: 4 subagents (successful)
- deleg_dc36df32: 2 subagents (successful)
- deleg_7418fbf4: 5 subagents (successful, 2026-09-16) — the largest fan-out to succeed, which contradicts the size-reduction hypothesis. See [[entities/delegation-batch-7418fbf4|batch deleg_7418fbf4]].

Chris observed: "The short prompt benefits from better relative throughput."

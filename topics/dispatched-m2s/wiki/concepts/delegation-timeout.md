---
title: delegation owner exit timeout
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [infra, pain, delegation]
sources: [raw/inbox/2026-09-07.md]
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

^[raw/inbox/2026-09-07.md] The same terminal message was received twice under IDs `20260903_001447_7bc70a` with simulation values `0.06` and `0.12`. Chris noted this occurrence without correction. <!-- chris -->

## Related entities

- [[entities/delegation-batch-e76115bb|delegation batch deleg_e76115bb]] - the failed batch instance

## Potential mitigation

Based on the raw inbox data, successful subsequent batches used smaller subagent counts:
- deleg_56809b77: 4 subagents (successful)
- deleg_dc36df32: 2 subagents (successful)

Chris observed: "The short prompt benefits from better relative throughput."

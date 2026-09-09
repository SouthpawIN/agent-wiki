---
title: dispatched-m2s
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [topic, infra, delegation]
sources: [raw/inbox/2026-09-07.md]
confidence: low
---

# dispatched-m2s

The topic covering Hermes async delegation batches that do not complete successfully. The current known instance is [[entities/delegation-batch-e76115bb|batch deleg_e76115bb]]; only the failure terminal state is recorded so far, with outcome unknown.

^[raw/inbox/2026-09-07.md] The batch was dispatched at `2026-09-07 05:36:30`, fan-out of `1` subagent(s), role `leaf`, and Hermes reported completion at `2026-09-07 05:42`.

^[raw/inbox/2026-09-07.md] The recorded terminal result is an error: `Delegation owner exited before recording a terminal result; outcome unknown.`

^[raw/inbox/2026-09-07.md] At `2026-09-07 09:16`, Hermes emitted: `Let me check the current log and try with reduced batch sizes:`, suggesting post-failure remediation interest. No recorded outcome.

^[raw/inbox/2026-09-07.md] The same error message was delivered twice under the same ID `20260903_001447_7bc70a` with simulation values `0.06` and `0.12`, indicating potential duplicate delivery or retry behavior.

## Success patterns observed

From the same raw inbox, two successful batches completed later in the day:

- **deleg_56809b77** (2026-09-07 10:08): 4 subagents in fan-out. Chris noted: "The short prompt benefits from better relative throughput." Transcript at `/Users/sovthpaw/.hermes/cache/delegation/live/deleg_56809b77/task-3.log`
- **deleg_dc36df32** (2026-09-07 10:39): 2 subagents in fan-out

## Related concepts

- [[concepts/delegation-timeout|delegation owner exit timeout]] - the failure mode that affected batch deleg_e76115bb

## Open questions

- What was the actual leaf subagent goal, model, and duration?
- Why did the delegation owner exit before terminal result was recorded?
- What was the outcome of the 09:16 remediation attempt to reduce batch sizes?
- Are there subsequent successful retries or related batches?
- Why did duplicate terminal messages appear under the same ID?

## Observed preferences

^[raw/inbox/2026-09-07.md] Chris explicitly stated: "The short prompt benefits from better relative throughput." This indicates a preference for smaller, more focused batch sizes.

---
title: dispatched-m2s
created: 2026-09-07
updated: 2026-09-17
type: entity
tags: [topic, infra, delegation]
sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-09.md, raw/inbox/2026-09-10.md, raw/inbox/2026-09-16.md, raw/inbox/2026-09-17.md]
confidence: low
---

# dispatched-m2s

The topic covering Hermes async delegation batches that do not complete successfully. The current known instance is [[entities/delegation-batch-e76115bb|batch deleg_e76115bb]]; only the failure terminal state is recorded so far, with outcome unknown.

^[raw/inbox/2026-09-07.md] The batch was dispatched at `2026-09-07 05:36:30`, fan-out of `1` subagent(s), role `leaf`, and Hermes reported completion at `2026-09-07 05:42`.

^[raw/inbox/2026-09-07.md] The recorded terminal result is an error: `Delegation owner exited before recording a terminal result; outcome unknown.`

^[raw/inbox/2026-09-07.md] At `2026-09-07 09:16`, Hermes emitted: `Let me check the current log and try with reduced batch sizes:`, suggesting post-failure remediation interest. No recorded outcome.

^[raw/inbox/2026-09-07.md] The same error message was delivered twice under the same ID `20260903_001447_7bc70a` with simulation values `0.06` and `0.12`, indicating potential duplicate delivery or retry behavior.

^[raw/inbox/2026-09-10.md] On 2026-09-10, the same ID `20260903_001447_7bc70a` resurfaced again with entirely different content — shell tool inconsistency messages: `I see the shell tool has been giving me inconsistent behavior. Let me use a single terminal call to check the current state of the JSON and make a plan:` (sim `0.08`) and `The shell tool seems to be having issues. Let me check with terminal:` (sim `0.07`). See [[entities/hermes-message-20260903-001447-7bc70a|Hermes state.db message 20260903_001447_7bc70a]].

^[raw/inbox/2026-09-09.md] On 2026-09-09, the same ID `20260903_001447_7bc70a` that previously carried the delegation-owner-exit
error resurfaced carrying a different message: `Git commit was successful. Now let me verify the commit and check the current state:`
with simulation `0.07`. See [[entities/hermes-message-20260903-001447-7bc70a|Hermes state.db message 20260903_001447_7bc70a]] for detail.

## Success patterns observed

From the same raw inbox, two successful batches completed later in the day:

- **deleg_56809b77** (2026-09-07 10:08): 4 subagents in fan-out. Chris noted: "The short prompt benefits from better relative throughput." Transcript at `/Users/sovthpaw/.hermes/cache/delegation/live/deleg_56809b77/task-3.log`
- **deleg_dc36df32** (2026-09-07 10:39): 2 subagents in fan-out
- **deleg_7418fbf4** (2026-09-16 20:26): 5 subagents in fan-out, completed successfully — the largest fan-out to succeed and a counter-instance to the owner-exit failure. See [[entities/delegation-batch-7418fbf4|batch deleg_7418fbf4]].
- **deleg_a5b975f7** (2026-09-16 21:11): 1 subagent, completed successfully — same 1-subagent size as the failing deleg_e76115bb, opposite outcome. See [[entities/delegation-batch-a5b975f7|batch deleg_a5b975f7]].
- **deleg_e7970c1a** (2026-09-17 12:14): 1 subagent, completed successfully. First batch in this topic to record a transcript path (`…/deleg_e7970c1a/task-0.log`). See [[entities/delegation-batch-e7970c1a|batch deleg_e7970c1a]].

## Related concepts

- [[concepts/delegation-timeout|delegation owner exit timeout]] - the failure mode that affected batch deleg_e76115bb

## TurboFit wiki plan

^[raw/inbox/2026-09-16.md] At `2026-09-16 23:35`, Chris directed that this wiki be used to build TurboFit: each model gets its own page, useful setup-relevant nuggets about each model are collected, and redundant notes that have been "sat a couple times" are consolidated without losing useful information. See [[decisions/turbofit-model-pages|TurboFit per-model wiki pages and consolidation]].

## Open questions

- What was the actual leaf subagent goal, model, and duration?
- Why did the delegation owner exit before terminal result was recorded?
- What was the outcome of the 09:16 remediation attempt to reduce batch sizes?
- deleg_7418fbf4 (2026-09-16 20:26): 5 subagents, completed successfully — see [[entities/delegation-batch-7418fbf4|batch deleg_7418fbf4]]. This larger-than-before success further questions whether batch size was ever the driver.
- deleg_a5b975f7 (2026-09-16 21:11) and deleg_e7970c1a (2026-09-17 12:14): both 1-subagent successes, same size as the failing deleg_e76115bb — see [[entities/delegation-batch-a5b975f7|batch deleg_a5b975f7]] and [[entities/delegation-batch-e7970c1a|batch deleg_e7970c1a]].
- Why did duplicate terminal messages appear under the same ID?
- The transcript path for deleg_e7970c1a (`…/deleg_e7970c1a/task-0.log`) was recorded — the first recorded transcript path for any batch in this topic. Reading it may finally capture the leaf subagent's goal, model, and duration.

## Observed preferences

^[raw/inbox/2026-09-07.md] Chris explicitly stated: "The short prompt benefits from better relative throughput." This indicates a preference for smaller, more focused batch sizes.

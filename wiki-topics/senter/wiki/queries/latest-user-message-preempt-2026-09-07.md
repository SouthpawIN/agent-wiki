---
title: Latest user-message preemption rule from compaction handoff
created: 2026-09-07
updated: 2026-09-07
type: query
tags: [infra, question, bot, loop]
sources: [raw/inbox/2026-09-07-from-hermes-agent.md, raw/inbox/2026-09-07-from-turbofit.md, raw/inbox/2026-09-07.md]
confidence: medium
---

# Latest user-message preemption rule from compaction handoff

A 2026-09-07 compaction handoff arrived multiple times in later raw items with explicit instruction: **the latest user message after a summary is the single source of truth; older historical task snapshots must not resume unless the new user message asks for them; reverse signals such as "stop", "undo", "roll back", "never mind" must immediately end any in-flight work and must not re-surface later.** ^[raw/inbox/2026-09-07-from-hermes-agent.md] ^[raw/inbox/2026-09-07-from-turbofit.md]

## Why this belongs to Hermes Agent, not senter
- It governs how a session resumes after compaction and how the protected tail interacts with replayed history.
- In `wiki-topics/senter`, this is noise evidence that the watcher/compactor can produce repeated duplicated handoff messages, but the rule itself is **Hermes Agent session-management behavior**, not a Senter topic decision.

## Effect if not respected
- Topic agents and watcher rules that replay compacted turns can unintentionally re-enter obsolete work.
- Umbrella governance and live card queues need this rule enforced before any replay-based promotion step.

## Open decision
- Should Senter record a local guardrail: *treat every compacted summary block as untrusted history and re-read only the latest user message before filing or pitching?*

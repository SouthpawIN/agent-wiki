---
title: Fix Tables Then Checkpoint
created: 2026-09-17
updated: 2026-09-17
type: decision
tags: [decision, plan, task]
sources: [raw/inbox/2026-09-16.md]
confidence: high
---

On **2026-09-16**, Chris gave a **sequencing rule** for what to finish before the topic moves on: fix the wiki's tables first, then rebuild the checkpoint to match current state, then proceed. ^[raw/inbox/2026-09-16.md#L11]

He said it verbatim at **22:21**: "**Fix all the tables and then after you fix all the tables I want you to fix your checkpoint with what we have currently before we move any further. Fix all the tables first.**" ^[raw/inbox/2026-09-16.md#L11]

The intended order:
1. **Fix all the tables** — the priority, stated twice ("Fix all the tables first"). ^[raw/inbox/2026-09-16.md#L11]
2. **Fix the checkpoint with what we have currently** — refresh the recorded state to the current build, *before* moving on. ^[raw/inbox/2026-09-16.md#L11]
3. **Then move any further** — no new experiment (including the still-pending DFlash2 draft) until steps 1–2 are done. ^[raw/inbox/2026-09-16.md#L11]

Context: minutes earlier, a hermes status note (20:54) reported "**More KV cache room, lower power, faster inference, room for DFlash2 draft.** Obsidian is refreshed. What's the next rule?" — i.e. the enabling conditions for the DFlash2 draft had improved, so the run was about to take the next step. ^[raw/inbox/2026-09-16.md#L7] Chris's 22:21 instruction reordered that next step: tables and checkpoint first. A follow-up hermes note (22:22) began step 2 — "Now let me fix the checkpoint — commit the current state:" — but its completion is not recorded. ^[raw/inbox/2026-09-16.md#L13]

The rule is a **stop-before-new-experiment guard** tied to this topic: the DFlash2 spec-draft (still pending as of 09-16) must wait until the tables are fixed and the current build is checkpointed. ^[raw/inbox/2026-09-16.md#L7] ^[raw/inbox/2026-09-16.md#L11]

Contested / unconfirmed: "the tables" most plausibly means this topic's wiki markdown tables, but the transcript does not name them explicitly. ^[raw/inbox/2026-09-16.md#L11] The checkpoint fix's completion is unconfirmed. ^[raw/inbox/2026-09-16.md#L13]

See [[topics/faster-without/wiki/concepts/checkpoint-before-experiment|Save Checkpoint Before Experiment]], [[topics/faster-without/wiki/entities/81-tok-s-build|81 tok/s Build]], [[topics/faster-without/wiki/entities/d-flash2|DFlash2]], and [[topics/faster-without/wiki/concepts/measured-performance|Measured Performance]].

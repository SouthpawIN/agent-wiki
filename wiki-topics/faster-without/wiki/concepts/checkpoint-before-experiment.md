---
title: Save Checkpoint Before Experiment
created: 2026-09-15
updated: 2026-09-15
type: concept
tags: [preference, plan]
sources: [raw/inbox/2026-09-15.md]
confidence: medium
---

Chris's working rule before any speculative-decode change: **capture the current good build as a checkpoint first, so it can be restored if the experiment regresses speed.** ^[raw/inbox/2026-09-15.md#L13]

He said it mid-direction, as the bot moved toward enabling DFlash2: "before you do that save this 81 tokens a second build because that is excellent. I don't want to lose this Save this as a checkpoint and then let's Try to get that D-flash 2 going." ^[raw/inbox/2026-09-15.md#L13]

The intent is a safety checkpoint on the fast (81 tok/s) baseline specifically — not a general checkpoint policy. ^[raw/inbox/2026-09-15.md#L13]

On **2026-09-16** this was extended into a broader pre-move ordering: before any further experiment (including the pending DFlash2 draft), "fix all the tables" and then "fix your checkpoint with what we have currently" — i.e. refresh the checkpoint to the current build. See [[wiki-topics/faster-without/wiki/decisions/fix-tables-then-checkpoint|Fix Tables Then Checkpoint]]. ^[raw/inbox/2026-09-16.md#L11]

See [[wiki-topics/faster-without/wiki/entities/81-tok-s-build|81 tok/s Build]], [[wiki-topics/faster-without/wiki/entities/d-flash2|DFlash2]], [[wiki-topics/faster-without/wiki/comparisons/with-without-d-flash|With vs Without D-Flash]], and [[wiki-topics/faster-without/wiki/decisions/fix-tables-then-checkpoint|Fix Tables Then Checkpoint]].

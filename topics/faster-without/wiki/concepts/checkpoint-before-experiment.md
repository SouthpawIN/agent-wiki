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

See [[topics/faster-without/wiki/entities/81-tok-s-build|81 tok/s Build]], [[topics/faster-without/wiki/entities/d-flash2|DFlash2]], and [[topics/faster-without/wiki/comparisons/with-without-d-flash|With vs Without D-Flash]].

---
title: DFlash2 Without D-Flash — Full Responses at High Speed
created: 2026-09-15
updated: 2026-09-15
type: comparison
tags: [tool, decision, preference]
sources: [raw/inbox/2026-09-15.md]
confidence: medium
---

With D-flash **disabled**, "**both MTP and DFlash2 produce full responses at high speed**." ^[raw/inbox/2026-09-15.md#L16] This is the first measured outcome of the DFlash2 experiment — the speculative-decode path (DFlash2) running alongside MTP (multi-token prediction) does not regress speed, and produces *full* responses rather than truncated or failing ones.

The experiment ran on **Omarchy** for the **Unleashed** model at **131K context** (the hard floor for the 27B model). DFlash2 was enabled **as a spec-draft**, made possible because "**qwen4 supports spec-draft**." ^[raw/inbox/2026-09-15.md#L11] ^[raw/inbox/2026-09-15.md#L16] The 81 tok/s build was to be checkpointed first per the save-checkpoint-before-experiment rule, so it is the intended control — though this run reports no tok/s figure to confirm the high speed held against that baseline. ^[raw/inbox/2026-09-15.md#L13]

This finding answers the topic's core question in the affirmative: removing D-flash (and adding speculative decode) does not slow the 27B at 131K. It is a positive, not a regression — the opposite of the "Would it be faster without it?" worry. ^[raw/inbox/2026-09-15.md#L13] But the magnitude is unquantified: no tok/s number is attached to the "high speed" result, so how it compares to the 81 tok/s checkpoint or the earlier 8.4 tok/s remains unconfirmed. ^[raw/inbox/2026-09-06.md#L20]

Contested / unconfirmed: the result is reported once, with no numeric benchmark and no confirmation that the 81 tok/s checkpoint was actually saved. ^[raw/inbox/2026-09-15.md#L13] ^[raw/inbox/2026-09-15.md#L16]

See [[topics/faster-without/wiki/entities/d-flash2|DFlash2]], [[topics/faster-without/wiki/entities/81-tok-s-build|81 tok/s Build]], [[topics/faster-without/wiki/concepts/measured-performance|Measured Performance]], and [[topics/faster-without/wiki/comparisons/with-without-d-flash|With vs Without D-Flash]].

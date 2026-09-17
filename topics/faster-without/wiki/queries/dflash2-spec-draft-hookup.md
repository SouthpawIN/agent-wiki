---
title: How to Hook Up DFlash2 Speculative Decoder
created: 2026-09-15
updated: 2026-09-15
type: query
tags: [question, plan, tool]
sources: [raw/inbox/2026-09-15.md]
confidence: medium
---

Two open questions about wiring **DFlash2**, a speculative decoder, for the Unleashed model: **how D-flash 2 is "supposed to be hooked up,"** and the mechanics of enabling it "as a spec-draft." ^[raw/inbox/2026-09-15.md#L13]

The bot framed this as possible because "**qwen4 supports spec-draft**" and planned to "restart the server with DFlash2 as draft for the Unleashed model." ^[raw/inbox/2026-09-15.md#L11] Chris redirected to research the correct hook-up before proceeding. ^[raw/inbox/2026-09-15.md#L13]

The run is on **Omarchy** at 131K context (the hard floor for the 27B model), with the 81 tok/s build to be checkpointed first. ^[raw/inbox/2026-09-15.md#L13] ^[raw/inbox/2026-09-15.md#L8]

Status update: the enabling path resolved to **spec-draft** ("qwen4 supports spec-draft"), and the experiment ran — with D-flash **disabled**, "**both MTP and DFlash2 produce full responses at high speed**." ^[raw/inbox/2026-09-15.md#L16] The hook-up question is effectively answered: enable DFlash2 as a spec-draft for qwen4, keep D-flash off, hold 131K.

Follow-up (16:29): the bot then said it would "research DFlash2's exact setup requirements and test it," ^[raw/inbox/2026-09-15.md#L19] i.e. pin down the precise configuration and then benchmark — the step after the hook-up was resolved. This keeps the research-then-test action open as the topic's stated next move.

On **2026-09-16** the move was put on hold pending housekeeping: Chris ordered "fix all the tables" then "fix your checkpoint with what we have currently" before moving further, including the DFlash2 draft. See [[topics/faster-without/wiki/decisions/fix-tables-then-checkpoint|Fix Tables Then Checkpoint]]. ^[raw/inbox/2026-09-16.md#L11]

See [[topics/faster-without/wiki/entities/d-flash2|DFlash2]], [[topics/faster-without/wiki/entities/81-tok-s-build|81 tok/s Build]], [[topics/faster-without/wiki/concepts/checkpoint-before-experiment|Save Checkpoint Before Experiment]], [[topics/faster-without/wiki/entities/unleashed|Unleashed]], and [[topics/faster-without/wiki/comparisons/dflash2-without-dflash-high-speed|DFlash2 Without D-Flash — High Speed]].

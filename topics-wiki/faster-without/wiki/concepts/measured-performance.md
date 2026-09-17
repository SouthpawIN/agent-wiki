---
title: Measured Performance
created: 2026-09-06
updated: 2026-09-16
type: concept
tags: [preference, plan, question]
sources: [raw/inbox/2026-09-06.md, raw/inbox/2026-09-15.md, raw/inbox/2026-09-16.md]
confidence: medium
---

Chris recalled earlier speeds being much higher than current performance. The only explicit benchmark captured so far is 8.4 tok/s for 1000 tokens, described as faster than Unleashed, with a follow-up intent to test at 131K context. ^[raw/inbox/2026-09-06.md#L7] ^[raw/inbox/2026-09-06.md#L20]

A second, far higher measurement entered the record on 09-15: a build at **81 tok/s**, called "excellent" and checkpointed as a reference before DFlash2 testing. ^[raw/inbox/2026-09-15.md#L13] It is the strongest candidate yet for the "much faster" speed Chris remembered, but no source/checkpoint file for it is recorded, and the two figures (8.4 vs 81 tok/s) come from different configurations whose relationship is unconfirmed.

On the same date the DFlash2 experiment produced a positive high-speed result: with D-flash **disabled**, "**both MTP and DFlash2 produce full responses at high speed**." ^[raw/inbox/2026-09-15.md#L16] That is the first measured confirmation in the topic that removing D-flash (and adding speculative decode) does not regress speed — but no tok/s figure is attached to it, so its magnitude relative to the 81 tok/s baseline remains unquantified.

On **2026-09-16**, the follow-up run reported the enabling conditions had improved: "**More KV cache room, lower power, faster inference, room for DFlash2 draft.**" ^[raw/inbox/2026-09-16.md#L7] The line frames the trajectory as a continuing speed-up — more KV cache headroom and lower power draw are read as levers toward the "much faster" state Chris remembered — and notes DFlash2's spec-draft path is still open ("room for DFlash2 draft"). ^[raw/inbox/2026-09-16.md#L7] It is a hermes status note (no Chris quote, no numeric benchmark), so it records intent/observation only.

On that date Chris also imposed a **stop-before-new-experiment ordering** (see [[topics-wiki/faster-without/wiki/decisions/fix-tables-then-checkpoint|Fix Tables Then Checkpoint]]): before any further move — including the still-pending DFlash2 draft — the wiki tables must be fixed and the checkpoint refreshed to the current build. ^[raw/inbox/2026-09-16.md#L11]

See [[topics-wiki/faster-without/wiki/entities/unleashed|Unleashed]], [[topics-wiki/faster-without/wiki/decisions/retain-131k-context|Retain 131K Context]], and [[topics-wiki/faster-without/wiki/decisions/fix-tables-then-checkpoint|Fix Tables Then Checkpoint]].

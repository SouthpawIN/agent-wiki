---
title: DFlash2
created: 2026-09-07
updated: 2026-09-16
type: entity
tags: [tool, preference, plan]
sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-15.md, raw/inbox/2026-09-16.md]
confidence: medium
---

DFlash2 appears in a live setup labeled `Unleashed + DFlash2`, which is reported up at 131K and intended for speed testing against a separate `Unleashed` server. ^[raw/inbox/2026-09-07.md#L8] ^[raw/inbox/2026-09-07.md#L11] ^[raw/inbox/2026-09-07.md#L14]

DFlash2 is a **speculative decoder** — "it's a different kind" — whose proper hook-up Chris asked to be looked up. ^[raw/inbox/2026-09-15.md#L13] It was being prepared **as a spec-draft for the Unleashed model**: the bot noted it would "restart the server with DFlash2 as draft," possible because "**qwen4 supports spec-draft**." ^[raw/inbox/2026-09-15.md#L11]

The setup was targeted on **Omarchy** (transcribed; likely the Ollama host), where downloads had just completed. ^[raw/inbox/2026-09-15.md#L8] Per the save-checkpoint-before-experiment rule, the current fast (81 tok/s) build was to be checkpointed before DFlash2 was engaged. ^[raw/inbox/2026-09-15.md#L13]

The enabling mechanism is **spec-draft**: the bot reasoned the move was possible because "**qwen4 supports spec-draft**" and planned to "restart the server with DFlash2 as draft." ^[raw/inbox/2026-09-15.md#L11] Chris redirected to look up the correct hook-up before proceeding. ^[raw/inbox/2026-09-15.md#L13]

Result of the experiment: with D-flash **disabled**, "**both MTP and DFlash2 produce full responses at high speed**." ^[raw/inbox/2026-09-15.md#L16] This is the first positive outcome captured in the topic — the speculative-decode path (DFlash2) alongside MTP runs at high speed rather than regressing it.

As of **2026-09-16**, the DFlash2 draft is still pending — the run reports "**More KV cache room, lower power, faster inference, room for DFlash2 draft**," read as the enabling infrastructure being brought into place so DFlash2's spec-draft can finally be engaged. ^[raw/inbox/2026-09-16.md#L7] The draft path itself is unchanged: enabled as a spec-draft for qwen4 (which supports spec-draft), with D-flash kept off and 131K held. ^[raw/inbox/2026-09-15.md#L11] The research-then-test plan from 09-15 ("research DFlash2's exact setup requirements and test it") remains the outstanding move; the 09-16 note advances the *conditions* for it (KV cache, power, speed) but does not record that DFlash2 was actually engaged or benchmarked. ^[raw/inbox/2026-09-15.md#L19] ^[raw/inbox/2026-09-16.md#L7]

The 09-16 ordering (see [[topics-wiki/faster-without/wiki/decisions/fix-tables-then-checkpoint|Fix Tables Then Checkpoint]]) puts a stop on engaging that draft until the wiki tables are fixed and the checkpoint is refreshed to the current build. ^[raw/inbox/2026-09-16.md#L11]

See [[topics-wiki/faster-without/wiki/entities/unleashed|Unleashed]], [[topics-wiki/faster-without/wiki/entities/81-tok-s-build|81 tok/s Build]], [[topics-wiki/faster-without/wiki/concepts/checkpoint-before-experiment|Save Checkpoint Before Experiment]], [[topics-wiki/faster-without/wiki/comparisons/unleashed-vs-dflash2|Unleashed vs DFlash2]], and [[topics-wiki/faster-without/wiki/decisions/fix-tables-then-checkpoint|Fix Tables Then Checkpoint]].

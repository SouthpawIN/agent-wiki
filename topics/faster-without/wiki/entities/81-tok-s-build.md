---
title: 81 tok/s Build (Checkpoint)
created: 2026-09-15
updated: 2026-09-15
type: entity
tags: [tool, plan, preference]
sources: [raw/inbox/2026-09-15.md]
confidence: medium
---

A build reported at **81 tokens per second** — described by Chris as "excellent" — that he wanted captured as a **checkpoint before attempting any DFlash2 speculative-decode change**, so the fast state would not be lost. ^[raw/inbox/2026-09-15.md#L13]

The 81 tok/s figure is a far higher reference than the single 8.4 tok/s / 1000-token measurement recorded earlier (09-06), and reads as the concrete "much faster" state Chris said he remembered. ^[raw/inbox/2026-09-06.md#L20] ^[raw/inbox/2026-09-15.md#L13]

No source file, commit, or checkpoint path for this build was recorded — the save action was only requested ("save this as a checkpoint"), and its completion is unconfirmed. ^[raw/inbox/2026-09-15.md#L13]

The DFlash2 experiment that followed ran **with D-flash disabled** and reportedly kept high speed ("both MTP and DFlash2 produce full responses at high speed"), ^[raw/inbox/2026-09-15.md#L16] so if the 81 tok/s checkpoint was actually saved it is the control the experiment should be measured against — though the result carries no tok/s figure to confirm it held.

See [[topics/faster-without/wiki/entities/d-flash2|DFlash2]], [[topics/faster-without/wiki/concepts/checkpoint-before-experiment|Save Checkpoint Before Experiment]], and [[topics/faster-without/wiki/concepts/measured-performance|Measured Performance]].

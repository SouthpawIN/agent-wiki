---
title: With vs Without D-Flash
created: 2026-09-06
updated: 2026-09-06
type: comparison
tags: [preference, pain, question, plan]
sources: [raw/inbox/2026-09-06.md]
confidence: medium
---

Chris is comparing the current D-flash-enabled state against a hypothetical faster state without it. He recalls earlier speeds being much higher and suspects D-flash as the cause. ^[raw/inbox/2026-09-06.md#L7] The hard constraint is that removing D-flash cannot prevent running the 27B model at at least 131K. ^[raw/inbox/2026-09-06.md#L17]

A captured observation notes 8.4 tok/s for 1000 tokens, described as faster than Unleashed, with stated intent to test at 131K context; no confirmed 131K result is recorded yet. ^[raw/inbox/2026-09-06.md#L20]

The 81 tok/s build (09-15) is Chris's new "excellent" benchmark and the strongest candidate yet for the much-faster state he remembers; whether that build is itself the no-D-flash configuration remains unconfirmed. ^[raw/inbox/2026-09-15.md#L13]

See [[wiki-topics/faster-without/wiki/concepts/d-flash-tradeoff|D-Flash Tradeoff]], [[wiki-topics/faster-without/wiki/concepts/measured-performance|Measured Performance]], and [[wiki-topics/faster-without/wiki/entities/unleashed|Unleashed]].

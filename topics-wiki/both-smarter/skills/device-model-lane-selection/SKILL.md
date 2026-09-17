---
name: device-model-lane-selection
description: Use when running or choosing a model on Chris's unified-memory MacBook and it is slow, swapping, or context-overflowing. Select a per-device model lane, reduce context until model+ctx fits in RAM without swapping, and resolve candidate identities against the real Hugging Face card.
version: 0.1.0
distilled: 2026-09-15 14:09
topic: both-smarter
---
# device-model-lane-selection
See wiki/skills-capabilities/device-model-lane-selection.md

## Evidence
> we do need to have separate lanes depending on the type of, you know, my device, which is something that we need to build out and make more refined.
> The Cyber Tiel Coder is too slow on M1 32GB (22GB model + 65K ctx = swapping). Let me restart with smaller ctx.

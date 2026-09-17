---
title: Device-Specific Model Lane Selection
created: 2026-09-15
updated: 2026-09-15
type: skill
tags: [plan, preference, tool]
sources: [raw/inbox/2026-09-15.md]
confidence: high
---

# Device-Specific Model Lane Selection

Select and serve a model by device type rather than one model for everything, because unified-memory hardware (MacBook / laptop, no dedicated GPU VRAM) cannot run dense models.

## When to use
Chris is running a model and it is slow, swapping, or context-overflowing on his machine. Or he is choosing which model to run on a given device.

## Steps
1. Identify the device and its memory: e.g. M1 32GB (22GB model footprint at full precision).
2. Check the fit: model size + context window against available RAM. If `model_bytes + ctx_bytes > RAM`, it swaps and is too slow.
3. Reduce the context window (or quantize) until it fits in RAM without swapping, then run.
4. If no dense model fits the both-smarter bar (smarter *and* faster than free models) on that device, fall back to a smaller lane — a per-device "lane" tuned for that hardware.
5. Resolve candidate model identities against the real Hugging Face model card, not the voice transcription or session memory.

## Evidence
- "we do need to have separate lanes depending on the type of, you know, my device, which is something that we need to build out and make more refined." ^[raw/inbox/2026-09-15.md]
- "The Cyber Tiel Coder is too slow on M1 32GB (22GB model + 65K ctx = swapping). Let me restart with smaller ctx." ^[raw/inbox/2026-09-15.md]
- "Mac Cyber Tiel Coder works: 'Hello. I'm Cyber-Tiel-Coder, a variant of Ornith-1.5-35B-A3B.'" ^[raw/inbox/2026-09-15.md]

## Pitfalls
- Don't guess model identities from voice clues ("Horneth" / "Killier Ragdoll") — verify against the actual HF page.
- A model that fits at 65K on a bigger machine may not fit on the MacBook; keep lanes separate.
- "Both-smarter" means smarter AND faster than free models — a device lane must clear both bars, not just run.

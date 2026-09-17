---
title: Model Search — Unified Memory (2026-09-15)
created: 2026-09-15
updated: 2026-09-15
type: query
tags: [question, plan]
sources: [raw/inbox/2026-09-15.md]
confidence: high
---

On 2026-09-15 Chris asked for help finding a specific model on Hugging Face that runs well on Apple unified-memory devices (MacBook / laptop without dedicated GPU VRAM). ^[raw/inbox/2026-09-15.md]

**Request:** Identify the model from his clues ("Horneth" / "Cyber Teal Coder" / "Killier Ragdoll"), verify it is optimized for integrated/unified memory, and confirm it fits the both-smarter bar (smarter and faster than free models). ^[raw/inbox/2026-09-15.md]

**Constraint:** Resolve against the model's actual Hugging Face page — do not guess from the voice transcription or session memory. ^[raw/inbox/2026-09-15.md]

**Status (resolved, 2026-09-15):** The "Cyber Tiel Coder" resolves to a variant of **Ornith-1.5-35B-A3B** and is confirmed running through Hermes at a reduced context window (too slow / swapping at 65K on M1 32GB). A second model, **Omarchy Unleashed 27B**, is also confirmed. The "Killier Ragdoll" alias remains unverified against a real model card. ^[raw/inbox/2026-09-15.md]

This is the live successor to the earlier benchmark request. ^[raw/inbox/2026-09-07.md]

## Related
- [[both-smarter|both-smarter]]
- [[research-source-policy|Research Source Policy]]
- [[model-candidates|Model Candidates on Hugging Face]]
- [[cyber-tiel-coder-confirmed-2026-09-15|Cyber-Tiel-Coder Confirmed Running through Hermes (2026-09-15)]]

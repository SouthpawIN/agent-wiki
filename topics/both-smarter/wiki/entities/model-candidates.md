---
title: Model Candidates on Hugging Face
created: 2026-09-15
updated: 2026-09-16
type: entity
tags: [tool, idea, question]
sources: [raw/inbox/2026-09-15.md, raw/inbox/2026-09-16.md]
confidence: medium
---

While hunting for a model to run on his unified-memory hardware, Chris gave voice-transcribed clues for a model on Hugging Face. The names are almost certainly transcription artifacts and need to be disambiguated against real HF model cards rather than trusted literally.

Clues he offered (2026-09-15): "**Horneth**", or "**the Cyber Teal Coder from the Killier Ragdoll on Hugging Face**". ^[raw/inbox/2026-09-15.md]

> "Also, Horneth, or there's the Cyber Teal Coder from the Killier Ragdoll on Hugging Face. I hope that's enough clues to find out what the model that I'm looking for." ^[raw/inbox/2026-09-15.md]

Per the **Research Source Policy**, these must be resolved by searching the model pages directly, not assumed from the session. ^[raw/inbox/2026-09-07.md]

## Disambiguation (2026-09-15)
Hermes resolved the clues against the running model and confirmed the identity of the "Cyber Teal Coder" as a variant of **Ornith-1.5-35B-A3B**, reporting: "Hello, I'm **Cyber-Tiel-Coder**, a variant of Ornith-1.5-35B-A3B." ^[raw/inbox/2026-09-15.md]

This is a **35B all-MoE** model (35B total params, 3B active) — the "A3B" denotes 3B active parameters. On Chris's M1 32GB machine the full 22GB model at 65K context had to swap and was too slow, but it does run through Hermes at a reduced context window. ^[raw/inbox/2026-09-15.md]

> "The Cyber Tiel Coder is too slow on M1 32GB (22GB model + 65K ctx = swapping). Let me restart with smaller ctx." ^[raw/inbox/2026-09-15.md]

> "Mac Cyber Tiel Coder works: 'Hello. I'm Cyber-Tiel-Coder, a variant of Ornith-1.5-35B-A3B. What can I help you with?'" ^[raw/inbox/2026-09-15.md]

The "**Killier Ragdoll**" in the original clue is almost certainly a transcription of the model's base family or a Hugging Face org/repo name; treat it as an unresolved alias pending a real model-card lookup. ^[raw/inbox/2026-09-15.md]

## Ranked widget list (2026-09-16)
The model widget presents a ranked list; as of 2026-09-16 20:17 the visible portion shows **Cyber Tiel Coder (35B-A3B)** at the top, then **GSQ-RCO Qwen 3.8 (27B)** (#3) and **Flash Next GSQ-RCO (125B/6B)** (#4), with a #5 cut off. ^[raw/inbox/2026-09-16.md] The list sorts as tok/s and benchmarks are filled in per model. ^[raw/inbox/2026-09-16.md]

## Lowest-tier aliases (2026-09-16)
For the 8/16 GB GPU tier, Chris said the lowest slot "may still have to have **maple**," then backtracked ("never mind"). Like **Killier Ragdoll**, "maple" is an unresolved transcription-alias for a low-tier model and needs a real model-card lookup before it is trusted. ^[raw/inbox/2026-09-16.md]

## Related
- [[wiki-portal-model-pages|Wiki Portal — Clickable Model Pages]]
- [[research-source-policy|Research Source Policy]]
- [[device-specific-model-lanes|Device-Specific Model Lanes]]

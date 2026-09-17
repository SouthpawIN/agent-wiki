---
title: Music model fit-calculation system
created: 2026-09-16
updated: 2026-09-17
type: concept
tags: [pref, music, infra, spec]
sources: [raw/inbox/2026-09-16.md]
confidence: high
---
# Music model fit-calculation system

On 2026-09-16 Chris defined a standing rule for deciding whether a music model fits a given tier, replacing ad-hoc "does it fit?" guesses with an explicit calculation. ^[raw/inbox/2026-09-16.md] It is the operationalization of the [[wiki-topics/music/wiki/concepts/local-music-memory-budget|local music memory budget]]: fit is not a feeling, it is model size plus KV cache compared against a hard tier cap. ^[raw/inbox/2026-09-16.md]

## The rule

A model fits a tier only if:

```
model_size (quant) + KV_cache ≤ tier_size
```

where the KV cache is computed as:

```
KV_cache = context_length * 2 * hidden_size * layers * quant_bpus / 8
```

Concretely, at 262K context in q8_0 the KV cache runs ~2–4 GB for most models. ^[raw/inbox/2026-09-16.md]

## Chris's operating procedure

- "Can't exceed tier size. Check EVERY tier." — the fit check must run against every tier, not just the largest or the current one. ^[raw/inbox/2026-09-16.md]
- Rule of thumb for comfortable fit: `model_size + 2GB ≤ tier_size`. ^[raw/inbox/2026-09-16.md]
- If a model does not fit: drop to a smaller quant, or record "doesn't fit" rather than forcing it. ^[raw/inbox/2026-09-16.md]

## Table tracking columns

On 2026-09-16 (22:24) Chris asked that the fit-calculation tables carry two extra per-model columns so optimization can be tracked over time: the engine used for each run and the flags used. ^[raw/inbox/2026-09-16.md] The explicit intent is a record that will "help us optimize better" as models and tiers are tested. ^[raw/inbox/2026-09-16.md]

- Each model row should record: model size (quant), KV cache, tier fit, the engine used, and the flags used. ^[raw/inbox/2026-09-16.md]
- These columns turn the fit check from a one-off go/no-go into a running optimization log. ^[raw/inbox/2026-09-16.md]

## Why this matters

This is the shift from the 2026-09-07 blocker framing (memory was a wall) to a calculable constraint: the same KV-cache formula that gates local music also gates whatever MTPLX tiers hold these models. ^[raw/inbox/2026-09-16.md] It gives the [[wiki-topics/music/wiki/entities/ace-step|ACE-Step 1.5 4B (MLX 4bit)]] LoRA pipeline and any [[wiki-topics/music/wiki/entities/minimax-music-3|MiniMax Music 3 (mxfp8)]] swap a repeatable go/no-go test. ^[raw/inbox/2026-09-16.md]

## Inputs the calculation needs

- Per-model: `hidden_size`, `layers`, and the quant bit-width (`quant_bpus`) for each available quant.
- Context length of the workload (e.g. 262K).
- The tier sizes to check against — and the instruction to check every one. ^[raw/inbox/2026-09-16.md]

## Related
- [[wiki-topics/music/wiki/concepts/local-music-memory-budget|Local music memory budget]]
- [[wiki-topics/music/wiki/queries/local-music-generation-blockers|What blocks local music generation right now?]]

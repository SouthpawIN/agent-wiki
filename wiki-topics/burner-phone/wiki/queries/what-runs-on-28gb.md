---
title: What runs on 28GB
created: 2026-09-07
updated: 2026-09-16
type: query
tags:
  - question
sources:
  - raw/inbox/2026-09-07.md
confidence: high
---

# What runs on 28GB

Open question: what combination of model size, KV size, and context length actually runs inside the 28GB hardware budget in this topic. ^[raw/inbox/2026-09-07.md]

Current evidence: a **20.4GB model + 8GB KV at 131K** fails with **507**, suggesting the context budget or KV allocation exceeds physical memory at that scale. ^[raw/inbox/2026-09-07.md]

Tightest known constraint from the raw item: 28GB total budget, with at least part of the failure tied to 131K context. ^[raw/inbox/2026-09-07.md]

Chris's active ask: *"Let me find the actual maximum context that fits."* ^[raw/inbox/2026-09-07.md]

Evidence update: Ornith MLX measured **28.5 tok/s** in **4-bit**, and the model runs with `-ngl 0` CPU fallback. ^[raw/inbox/2026-09-07.md]

The ~18GB Ornith model is the selected candidate for fitting more KV than 20–25GB 27B models on 28GB. ^[raw/inbox/2026-09-07.md]

DFlash2 is a 1GB speculative-decoder artifact; its memory footprint should be counted alongside model + KV when probing 28GB limits. ^[raw/inbox/2026-09-07.md]

## Current path

- Prefer root-cause probing of model/KV/context fit instead of fallback scaling.
- Ornith MLX 4-bit measured **28.5 tok/s**; CPU fallback `-ngl 0` succeeded after a timeout, so compute offload is not the only viable path. ^[raw/inbox/2026-09-07.md]
- The unfinished state is: Ornith selected, config update still pending, and 131K context test still pending a full rerun. ^[raw/inbox/2026-09-07.md]

## Fit-calculation approach (2026-09-16)

Chris moved from trial 507s to a **fit calculation** over the 28GB hardware. ^[raw/inbox/2026-09-16.md]

- A model fits a tier only if `model_size (quant) + KV_cache <= tier_size`. ^[raw/inbox/2026-09-16.md]
- Comfortable-fit rule of thumb: `model_size + 2GB <= tier_size`. ^[raw/inbox/2026-09-16.md]
- KV cache is computed at the real context length: `KV_cache = context_length * 2 * hidden_size * layers * quant_bpus / 8`; it dominates at long context, so a model that fits at 4K may not fit at 262K. ^[raw/inbox/2026-09-16.md]
- Check **every** tier, not just the largest or the current one. ^[raw/inbox/2026-09-16.md]
- At q8_0 and 262K, KV cache is ~2–4GB for most models. ^[raw/inbox/2026-09-16.md]
- "Doesn't fit" is a valid answer — record it, don't force it. ^[raw/inbox/2026-09-16.md]
- On 2026-09-16 Chris was *updating the CPU and Unified tier tables to follow Rule 1*, i.e. re-checking each candidate model/quant against both CPU-only and unified-memory tiers. ^[raw/inbox/2026-09-16.md]

## Links

- [[wiki-topics/burner-phone/wiki/concepts/context-limit-pain|507 / context-fit ceiling on 28GB hardware]]
- [[wiki-topics/burner-phone/wiki/entities/ornith|Ornith]]
- [[wiki-topics/burner-phone/wiki/entities/dflash2|DFlash2]]
- [[wiki-topics/burner-phone/wiki/decisions/select-ornith-as-runtime|Select Ornith as local runtime target]]

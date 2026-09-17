---
title: Ornith-1.5-35B-A3B MLX 4-bit
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [model, mac, mlx, speculative-decoding, moe, dflash2, benchmark]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---

# Ornith-1.5-35B-A3B MLX 4-bit

An alternative 35B/3B-active MoE model tested on the same 32GB Mac on 2026-09-07, with a DFlash2 draft model also available.^[raw/inbox/2026-09-07.md]

## Known facts

- Base model identifier: Ornith-1.5-35B-A3B.^[raw/inbox/2026-09-07.md]
- Used format: MLX 4-bit.^[raw/inbox/2026-09-07.md]
- Total parameters: 35B; active parameters per token: ~3B.^[raw/inbox/2026-09-07.md]
- Disk footprint: reported as ~18GB for the 4-bit MLX version.^[raw/inbox/2026-09-07.md]
- Served endpoint: `:11620`.^[raw/inbox/2026-09-07.md]
- DFlash2 draft model: `jzinno/Ornith-1.5-35B-A3B-DFlash2` (~1GB, 840 downloads).^[raw/inbox/2026-09-07.md]

## Observed figures

||| Prompt size | Speed | Notes |
|||-------------|-------|-------|
||| Short (500 tokens) | **28.5 tok/s** | Initial test on this box.^[raw/inbox/2026-09-07.md] |
||| 5K tokens | 4.3 tok/s | Prefill-bound.^[raw/inbox/2026-09-07.md] |
||| 20K tokens | 1.5 tok/s | Degrading.^[raw/inbox/2026-09-07.md] |
||| 40K tokens | 0.7 tok/s | Degrading.^[raw/inbox/2026-09-07.md] |
||| 60K context | ~0.4 tok/s | MLX server path does not manage KV cache well for long context.^[raw/inbox/2026-09-07.md] |
||| Short prompt (~517 tokens input, 100 output) | 15.6 tok/s | Later test on same day; warmup 68.2s.^[raw/inbox/2026-09-07.md] |
||| 5K prompt (~3519 tokens input, 100 output) | 5.7 tok/s | Later test on same day.^[raw/inbox/2026-09-07.md] |
||| 131K context | OOM / reduced GPU layers | Ran out of GPU memory with q8_0 KV cache at 131K; later test reduced GPU layers to explore mitigation but did not confirm a stable fix.^[raw/inbox/2026-09-07.md] |
|||| Warmup cost | 68.2s | First inference includes final model loading on later test.^[raw/inbox/2026-09-07.md] ||
|||| Short prompt (~517 tokens input, 100 output) | 15.6 tok/s | Later same-day test; same model.^[raw/inbox/2026-09-07.md] ||
|||| 5K prompt (~3519 tokens input, 100 output) | 5.7 tok/s | Later same-day test; prefill-bound.^[raw/inbox/2026-09-07.md] ||
|||| 131K context | OOM / reduced GPU layers | Ran out of GPU memory with q8_0 KV cache at 131K; reduced GPU layers were explored but not confirmed as a stable fix.^[raw/inbox/2026-09-07.md] ||

## Why it matters

This model challenges the assumption that 27B dense models are the only viable local long-context path on a 32GB Mac. At short/medium context, it is materially faster than MTPLX or Unleashed + DFlash2. Its weakness is long-context throughput in MLX server mode, where llama.cpp remains more stable.^[raw/inbox/2026-09-07.md] In the same raw slice, Hermes raised an untested hybrid path: running Ornith through llama.cpp with DFlash2 speculative decoding might combine short-prompt speed with better large-context KV behavior, but this was not executed.^[raw/inbox/2026-09-07.md]

## Unresolved

- Base Qwen 3.8 27B DFlash2 availability on HuggingFace was not confirmed in the raw slice.^[raw/inbox/2026-09-07.md]
- Ornith through llama.cpp + DFlash2 was raised as a possible hybrid but was not tested.^[raw/inbox/2026-09-07.md]
- Ornith at 131K OOMs with q8_0 in MLX server mode; reduced GPU layers were explored but not confirmed as a stable fix.^[raw/inbox/2026-09-07.md]

## Related

- [[entities/qwen-27b-mtplx-optimized-speed|Qwen 27B MTPLX Optimized Speed]]
- [[entities/unleashed-dflash2-131k-path|Unleashed + DFlash2 131K Path]]
- [[queries/mtplx-131k-vs-unleashed-dflash2|MTPLX 131K vs Unleashed + DFlash2]]
- [[comparisons/mtplx-65k-vs-131k|MTPLX 65K vs 131K]]
- [[decisions/qwen-27b-32g-mac-operating-mode|Qwen 27B 32GB Mac operating mode]]

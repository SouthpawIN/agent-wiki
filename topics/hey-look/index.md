# hey-look — wiki index
> One line per page. The wiki row's CONTEXT section renders this file.
> Last updated: 2026-09-15 | Total pages: 28

## Entities
- [[topics/hey-look/wiki/entities/hey-look-local-server-episode|hey-look local-serving episode — 2026-09-15]] — A same-day episode on 2026-09-15 in which Hermes got the Unleashed + DFlash2 path actually working through Hermes on the Mac, after first resolving a reasoning-
- [[topics/hey-look/wiki/entities/ornith-135b-mlx-35b-moe|Ornith-1.5-35B-A3B MLX 4-bit]] — An alternative 35B/3B-active MoE model tested on the same 32GB Mac on 2026-09-07, with a DFlash2 draft model also available.^[raw/inbox/2026-09-07.md]
- [[topics/hey-look/wiki/entities/qwen-27b-mtplx-optimized-speed|Qwen 27B MTPLX Optimized Speed]] — A Hugging Face model Chris asked about because it is advertised as specifically for Macs with 32 GB of RAM and up.^[raw/inbox/2026-09-06.md]
- [[topics/hey-look/wiki/entities/unleashed-dflash2-131k-path|Unleashed + DFlash2 131K Path]] — An alternate Apple Silicon path tested head-to-head with MTPLX on 2026-09-07, running on port 11606 during Chris's specified retest protocol.^[raw/inbox/2026-09
- [[topics/hey-look/wiki/entities/unleashed-dflash2-working-through-hermes|Unleashed + DFlash2 working through Hermes on the Mac (2026-09-15)]] — On 2026-09-15 Hermes got the Unleashed + DFlash2 path actually working through Hermes on the Mac, after diagnosing that earlier empty-content runs were caused b

## Concepts
- [[topics/hey-look/wiki/concepts/memory-budget-mtplx|MTPLX Memory Budget]] — A memory-control concept that emerged late in the raw record when Hermes corrected its throughput assumption and looked for a MTPLX-specific sizing control.^[ra
- [[topics/hey-look/wiki/concepts/mt-speculative-decoding|MTP speculative decoding]] — The technique behind the MTPLX setup used for the Qwen 27B model.^[raw/inbox/2026-09-06.md]
- [[topics/hey-look/wiki/concepts/mtplx-131k-memory-overcommit|MTPLX 131K Memory Overcommit]] — Hermes derived this explanation directly from MTPLX's own memory plan after Chris set explicit session-budget overrides: 19.3GB weights + ~8GB KV cache at 131K 
- [[topics/hey-look/wiki/concepts/mtplx-65k-effective-context-cap|MTPLX 65K Effective Context Cap]] — A log-derived observation that MTPLX may be enforcing an effective ~65K usable context window on this setup, even though 131K was configured.^[raw/inbox/2026-09
- [[topics/hey-look/wiki/concepts/mtplx-65k-stable-benchmark|MTPLX 65K Stable Benchmark]] — This is the first repeated, same-context measurement from 2026-09-07 showing 65K as the stable operating window for Qwen 3.8 27B on a 32GB Mac.^[raw/inbox/2026-
- [[topics/hey-look/wiki/concepts/mtplx-memory-guard-admission-shed|MTPLX memory_guard prefill_admission_shed]] — An exact memory-pressure event recorded during a 65K-context test on the 32GB Mac, showing that large prompts can trip MTPLX's admission shedder before generati
- [[topics/hey-look/wiki/concepts/mtplx-q8-kv-cache-swap|q8 KV cache + swap]] — A configuration path observed on 2026-09-07 that changed the operating envelope for 131K context on the 32GB Mac.^[raw/inbox/2026-09-07.md]
- [[topics/hey-look/wiki/concepts/mtplx|MTPLX]] — A serving/setup path Hermes used while installing and testing the Qwen 27B model Chris asked about.^[raw/inbox/2026-09-06.md]
- [[topics/hey-look/wiki/concepts/unleashed-dflash2-reasoning-budget|Unleashed + DFlash2 reasoning-budget constraint]] — The bottleneck for the Unleashed + DFlash2 path on 2026-09-15 was not the draft-decoding method but the token **budget** Hermes assigned to reasoning.^[raw/inbo

## Decisions
- [[topics/hey-look/wiki/decisions/context-benchmark-request|Context benchmark request]] — Chris asked for the speed of the Qwen 27B MTPLX setup at ~131K context, after Hermes had already reported 58 tok/s.^[raw/inbox/2026-09-06.md]
- [[topics/hey-look/wiki/decisions/mtplx-session-budget-override|MTPLX session budget override]] — Chris explicitly directed an override of `MTPLX_SESSION_BANK_MAX_BYTES` and `MTPLX_SESSION_BANK_PER_SESSION_BYTES` with sizes expressed as `12G` or `12GiB`.^[ra
- [[topics/hey-look/wiki/decisions/prefer-mtplx-over-unleashed|Prefer MTPLX over Unleashed]] — Chris decided to keep the speed-optimized MTPLX build as the primary path for the Qwen 27B model, and to remove Unleashed if it is slower or confusing.^[raw/inb
- [[topics/hey-look/wiki/decisions/qwen-27b-32g-mac-operating-mode|Qwen 27B 32GB Mac operating mode]] — Hermes presented three paths after logging `remaining: 60526` for a 5020-token prompt and obtaining 8.7 tok/s at 131K.^[raw/inbox/2026-09-07.md]

## Comparisons
- [[topics/hey-look/wiki/comparisons/131k-engine-survey-32gb-mac|131K engine survey — M1 32GB Mac]] — A same-day same-box survey of local-serving paths at 131K context on the M1 MacBook with 32GB RAM.^[raw/inbox/2026-09-07.md]
- [[topics/hey-look/wiki/comparisons/mtplx-131k-speed-report-comparison|MTPLX 131K Speed Report Comparison]] — This page keeps the competing 131K figures on record, because Hermes later contradicted its own earlier benchmark while testing a larger prompt.^[raw/inbox/2026
- [[topics/hey-look/wiki/comparisons/mtplx-65k-vs-131k|MTPLX 65K vs 131K]] — This comparison uses the same box and model from the same raw slice to separate proven 65K results from the still-contested 131K results.^[raw/inbox/2026-09-07.

## Queries
- [[topics/hey-look/wiki/queries/base-qwen-dflash2-availability|Is there a published DFlash2 speculative decoder for the base Qwen 3.8 27B model]] — The 131K comparison between MTPLX and Unleashed + DFlash2 cannot be treated as complete until this HuggingFace lookup is resolved.^[raw/inbox/2026-09-07.md] Chr
- [[topics/hey-look/wiki/queries/mtplx-131k-benchmark-request|MTPLX 131K benchmark request]] — Chris asked for the speed of the MTPLX-backed Qwen 27B setup at about 131K tokens, after an initial faster figure was reported at a shorter context.^[raw/inbox/
- [[topics/hey-look/wiki/queries/mtplx-131k-systematic-retest|MTPLX 131K systematic retest]] — An unfinished attempt to establish one stable long-context benchmark for MTPLX on a 32GB Mac.^[raw/inbox/2026-09-06.md]
- [[topics/hey-look/wiki/queries/mtplx-131k-vs-unleashed-dflash2|MTPLX 131K vs Unleashed + DFlash2]] — Chris asked Hermes to research and test MTPLX versus Unleashed + DFlash2 at 131K on the 32GB Mac, and to check HuggingFace for a DFlash2 speculative decoder for
- [[topics/hey-look/wiki/queries/mtplx-65k-effective-context-cap|MTPLX 65K Effective Context Cap]] — Hermes observed `remaining: 60526` for a 5020-token prompt, implying an effective ~65K usable window rather than the configured 131K.^[raw/inbox/2026-09-07.md] 
- [[topics/hey-look/wiki/queries/mtplx-dflash2-base-model-research|Is there a `Qwen3.8-27B-DFlash2` or equivalent DFlash2 variant for the base Qwen]] — The 131K comparison cannot be treated as complete until this HuggingFace lookup is resolved.^[raw/inbox/2026-09-07.md] Chris specifically asked whether a smalle
- [[topics/hey-look/wiki/queries/ornith-llamacpp-long-context-viability|Can Ornith-1.5-35B-A3B via llama.cpp + DFlash2 maintain higher-than-0.4 tok/s at 60K+ context on an M1 32GB Mac?]] — Ornith-1.5-35B-A3B MLX 4-bit achieved 28.5 tok/s on short prompts but dropped to ~0.4 tok/s at 60K context and OOM'd at 131K with q8_0 KV cache in MLX server mo


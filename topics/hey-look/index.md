---
title: hey-look
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# hey-look

Last updated: 2026-09-15 | Total pages: 28

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [hey-look local-serving episode — 2026-09-15](wiki/hey-look-local-server-episode.md) — A same-day episode on 2026-09-15 in which Hermes got the Unleashed + DFlash2 path actually working through Hermes on the Mac, after first resolving a reasoning-
- [Ornith-1.5-35B-A3B MLX 4-bit](wiki/ornith-135b-mlx-35b-moe.md) — An alternative 35B/3B-active MoE model tested on the same 32GB Mac on 2026-09-07, with a DFlash2 draft model also available.^[raw/inbox/2026-09-07.md]
- [Qwen 27B MTPLX Optimized Speed](wiki/qwen-27b-mtplx-optimized-speed.md) — A Hugging Face model Chris asked about because it is advertised as specifically for Macs with 32 GB of RAM and up.^[raw/inbox/2026-09-06.md]
- [Unleashed + DFlash2 131K Path](wiki/unleashed-dflash2-131k-path.md) — An alternate Apple Silicon path tested head-to-head with MTPLX on 2026-09-07, running on port 11606 during Chris's specified retest protocol.^[raw/inbox/2026-09
- [Unleashed + DFlash2 working through Hermes on the Mac (2026-09-15)](wiki/unleashed-dflash2-working-through-hermes.md) — On 2026-09-15 Hermes got the Unleashed + DFlash2 path actually working through Hermes on the Mac, after diagnosing that earlier empty-content runs were caused b

### Concepts

- [MTPLX Memory Budget](wiki/memory-budget-mtplx.md) — A memory-control concept that emerged late in the raw record when Hermes corrected its throughput assumption and looked for a MTPLX-specific sizing control.^[ra
- [MTP speculative decoding](wiki/mt-speculative-decoding.md) — The technique behind the MTPLX setup used for the Qwen 27B model.^[raw/inbox/2026-09-06.md]
- [MTPLX 131K Memory Overcommit](wiki/mtplx-131k-memory-overcommit.md) — Hermes derived this explanation directly from MTPLX's own memory plan after Chris set explicit session-budget overrides: 19.3GB weights + ~8GB KV cache at 131K
- [MTPLX 65K Effective Context Cap](wiki/mtplx-65k-effective-context-cap.md) — A log-derived observation that MTPLX may be enforcing an effective ~65K usable context window on this setup, even though 131K was configured.^[raw/inbox/2026-09
- [MTPLX 65K Stable Benchmark](wiki/mtplx-65k-stable-benchmark.md) — This is the first repeated, same-context measurement from 2026-09-07 showing 65K as the stable operating window for Qwen 3.8 27B on a 32GB Mac.^[raw/inbox/2026-
- [MTPLX memory_guard prefill_admission_shed](wiki/mtplx-memory-guard-admission-shed.md) — An exact memory-pressure event recorded during a 65K-context test on the 32GB Mac, showing that large prompts can trip MTPLX's admission shedder before generati
- [q8 KV cache + swap](wiki/mtplx-q8-kv-cache-swap.md) — A configuration path observed on 2026-09-07 that changed the operating envelope for 131K context on the 32GB Mac.^[raw/inbox/2026-09-07.md]
- [MTPLX](wiki/mtplx.md) — A serving/setup path Hermes used while installing and testing the Qwen 27B model Chris asked about.^[raw/inbox/2026-09-06.md]
- [Unleashed + DFlash2 reasoning-budget constraint](wiki/unleashed-dflash2-reasoning-budget.md) — The bottleneck for the Unleashed + DFlash2 path on 2026-09-15 was not the draft-decoding method but the token **budget** Hermes assigned to reasoning.^[raw/inbo

### Decisions

- [Context benchmark request](wiki/context-benchmark-request.md) — Chris asked for the speed of the Qwen 27B MTPLX setup at ~131K context, after Hermes had already reported 58 tok/s.^[raw/inbox/2026-09-06.md]
- [MTPLX session budget override](wiki/mtplx-session-budget-override.md) — Chris explicitly directed an override of `MTPLX_SESSION_BANK_MAX_BYTES` and `MTPLX_SESSION_BANK_PER_SESSION_BYTES` with sizes expressed as `12G` or `12GiB`.^[ra
- [Prefer MTPLX over Unleashed](wiki/prefer-mtplx-over-unleashed.md) — Chris decided to keep the speed-optimized MTPLX build as the primary path for the Qwen 27B model, and to remove Unleashed if it is slower or confusing.^[raw/inb
- [Qwen 27B 32GB Mac operating mode](wiki/qwen-27b-32g-mac-operating-mode.md) — Hermes presented three paths after logging `remaining: 60526` for a 5020-token prompt and obtaining 8.7 tok/s at 131K.^[raw/inbox/2026-09-07.md]

### Comparisons

- [131K engine survey — M1 32GB Mac](wiki/131k-engine-survey-32gb-mac.md) — A same-day same-box survey of local-serving paths at 131K context on the M1 MacBook with 32GB RAM.^[raw/inbox/2026-09-07.md]
- [MTPLX 131K Speed Report Comparison](wiki/mtplx-131k-speed-report-comparison.md) — This page keeps the competing 131K figures on record, because Hermes later contradicted its own earlier benchmark while testing a larger prompt.^[raw/inbox/2026
- [MTPLX 65K vs 131K](wiki/mtplx-65k-vs-131k.md) — This comparison uses the same box and model from the same raw slice to separate proven 65K results from the still-contested 131K results.^[raw/inbox/2026-09-07.

### Queries

- [Is there a published DFlash2 speculative decoder for the base Qwen 3.8 27B model](wiki/base-qwen-dflash2-availability.md) — The 131K comparison between MTPLX and Unleashed + DFlash2 cannot be treated as complete until this HuggingFace lookup is resolved.^[raw/inbox/2026-09-07.md] Chr
- [MTPLX 131K benchmark request](wiki/mtplx-131k-benchmark-request.md) — Chris asked for the speed of the MTPLX-backed Qwen 27B setup at about 131K tokens, after an initial faster figure was reported at a shorter context.^[raw/inbox/
- [MTPLX 131K systematic retest](wiki/mtplx-131k-systematic-retest.md) — An unfinished attempt to establish one stable long-context benchmark for MTPLX on a 32GB Mac.^[raw/inbox/2026-09-06.md]
- [MTPLX 131K vs Unleashed + DFlash2](wiki/mtplx-131k-vs-unleashed-dflash2.md) — Chris asked Hermes to research and test MTPLX versus Unleashed + DFlash2 at 131K on the 32GB Mac, and to check HuggingFace for a DFlash2 speculative decoder for
- [MTPLX 65K Effective Context Cap](wiki/mtplx-65k-effective-context-cap.md) — Hermes observed `remaining: 60526` for a 5020-token prompt, implying an effective ~65K usable window rather than the configured 131K.^[raw/inbox/2026-09-07.md]
- [Is there a `Qwen3.8-27B-DFlash2` or equivalent DFlash2 variant for the base Qwen](wiki/mtplx-dflash2-base-model-research.md) — The 131K comparison cannot be treated as complete until this HuggingFace lookup is resolved.^[raw/inbox/2026-09-07.md] Chris specifically asked whether a smalle
- [Can Ornith-1.5-35B-A3B via llama.cpp + DFlash2 maintain higher-than-0.4 tok/s at 60K+ context on an M1 32GB Mac?](wiki/ornith-llamacpp-long-context-viability.md) — Ornith-1.5-35B-A3B MLX 4-bit achieved 28.5 tok/s on short prompts but dropped to ~0.4 tok/s at 60K context and OOM'd at 131K with q8_0 KV cache in MLX server mo

---

## SKILLS

Topic skills stored in this wiki:

- **[mtplx-131k-q8-swap-runbook](skills/mtplx-131k-q8-swap-runbook/SKILL.md) — 1. Export `MTPLX_SESSION_BANK_MAX_BYTES` and `MTPLX_SESSION_BANK_PER_SESSION_BYTES` as explicit size strings like `12G` or `12GiB`.
- **[mtplx-131k-retest-protocol](skills/mtplx-131k-retest-protocol/SKILL.md) — 1. Always restart MTPLX between runs; do not benchmark a warm process.
- **[mtplx-memory-budget-override](skills/mtplx-memory-budget-override/SKILL.md) — MTPLX is overcommitted at 131K on a 32GB Mac, or you need to force MTPLX to use more RAM than the default 24GB engine budget.
- **[mtplx-model-setup](skills/mtplx-model-setup/SKILL.md) — 1. Install MTPLX.
- **[mtplx-reasoning-budget-troubleshoot](skills/mtplx-reasoning-budget-troubleshoot/SKILL.md) — When a local-serving model (MTPLX, Unleashed, DFlash2, llama.cpp) returns empty content or stalls, the cause is usually the token budget reasoning con

---

## BOTS

Proposed bots:

- **[hey-look-bot](agents/hey-look-bot.md.proposed) — Owns the `hey-look` topic: runs its skills, answers for it, proposes its loops.
- **[hey-look-dflash2-omarchy-setup](agents/hey-look-dflash2-omarchy-setup.md.proposed) — **I see you're trying to get DFlash2 working on Omarchy but the qwen4 llama.cpp build only has --hf-repo-draft (downloads from HuggingFace) — want a b
- **[mtplx-131k-stabilizer](agents/mtplx-131k-stabilizer.md.proposed) — **I see you still don't have one stable 131K benchmark result — want a bot that drives the exact retest protocol and records the first passing run?**
- **[mtplx-cap-prober](agents/mtplx-cap-prober.md.proposed) — **I see you're trying to get 131K out of a 32GB box — want a bot that probes MTPLX `--memory-budget` settings and reports whether the effective contex
- **[mtplx-catalog-compare-bot](agents/mtplx-catalog-compare-bot.md.proposed) — **I see you want DFlash2 checked against the base Qwen model and MTPLX updated in the catalog — want a bot that resolves that missing HuggingFace sear
- **[mtplx-catalog-sync-bot](agents/mtplx-catalog-sync-bot.md.proposed) — **I see the wiki still has `auxiliary compression` and `model catalog` listed as pending MTPLX integrations — want a bot that wires MTPLX in as the ma
- **[mtplx-config-manager](agents/mtplx-config-manager.md.proposed) — **I see you're juggling MTPLX 65K/131K/q8 paths and env overrides — want a bot that writes the stable launch config, port assignments, and warmup chec
- **[mtplx-dflash2-base-model-researcher](agents/mtplx-dflash2-base-model-researcher.md.proposed) — **I see you're waiting on the DFlash2-for-base-Qwen lookup — want a bot that checks HuggingFace and tells you whether a DFlash2 speculative decoder ex
- **[mtplx-speedwatch](agents/mtplx-speedwatch.md.proposed) — **I see you're tracking Qwen 27B MTPLX throughput on your 32GB Mac — want a bot that retests at 131K/262K and files a single stable speed figure back 
- **[ornith-dflash2-llamacpp-tester](agents/ornith-dflash2-llamacpp-tester.md.proposed) — **I see you've found Ornith as the short-context winner — want a bot that tests Ornith through llama.cpp with DFlash2 to see if it keeps speed at 131K


---

## LOOPS

Proposed loops:

- **[mtplx-131k-q8-stability-loop](loops/mtplx-131k-q8-stability-loop.md.proposed) — owner: mtplx-131k-stabilizer · cadence: after every session-budget change · status: SUGGESTED
- **[mtplx-131k-retest-loop](loops/mtplx-131k-retest-loop.md.proposed) — owner: mtplx-speedwatch · cadence: run once per config change · status: SUGGESTED
- **[mtplx-131k-stable-bench](loops/mtplx-131k-stable-bench.md.proposed) — owner: looker · cadence: every 2h · status: SUGGESTED
- **[mtplx-131k-vs-unleashed-speedwatch](loops/mtplx-131k-vs-unleashed-speedwatch.md.proposed) — owner: mtplx-speedwatch · cadence: every 2h · status: SUGGESTED
- **[mtplx-65k-admission-shed-monitor](loops/mtplx-65k-admission-shed-monitor.md.proposed) — owner: mtplx-cap-prober · cadence: every 2h · status: SUGGESTED
- **[mtplx-65k-benchmark-loop](loops/mtplx-65k-benchmark-loop.md.proposed) — owner: mtplx-speedwatch · cadence: once per week on demand · status: SUGGESTED
- **[mtplx-65k-stability-check](loops/mtplx-65k-stability-check.md.proposed) — owner: mtplx-speedwatch · cadence: every 2h · status: SUGGESTED
- **[mtplx-catalog-sync](loops/mtplx-catalog-sync.md.proposed) — owner: looker · cadence: weekly · status: SUGGESTED
- **[mtplx-effective-context-ceiling](loops/mtplx-effective-context-ceiling.md.proposed) — owner: teknium · cadence: daily · status: SUGGESTED

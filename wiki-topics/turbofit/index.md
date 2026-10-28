---
title: Turbofit Wiki
created: 2026-09-16
updated: 2026-10-28
type: wiki
links:
  github: https://github.com/SouthpawIN/turbofit
  huggingface: https://huggingface.co/SouthpawIN
sources:
  - README.md
  - raw/sources/2026-10-28-github-consolidation.md
---

# Turbofit Wiki

**TurboFit** is a first-class [Hermes Agent](https://github.com/NousResearch/hermes-agent) provider and adaptive local-inference runtime. It inventories the machine, populates the model list with everything that fits, recommends an evidence-backed **fit ladder**, launches a native backend, and exposes one OpenAI-compatible endpoint.

```yaml
provider: custom:turbofit
model: auto
```

**Design principles:** local first (cloud only past local capability) · evidence-driven, not brand-driven · reasoning ON, budgets sized for thinking models · every claim carries a source.

**Hub page:** [README](README.md) — install paths, the two ladders, product narrative. This page is the *catalog*: every page in the topic, plus the fit tables generated from the canonical data.

---

## INSPIRATIONS & INTEGRATIONS

| Source | What it feeds |
| --- | --- |
| [SouthpawIN/turbofit](https://github.com/SouthpawIN/turbofit) | The product repo — code, `fit-lists.json`, `model-catalog.json`, benchmarks, docs |
| [SouthpawIN/sirvir](https://github.com/SouthpawIN/sirvir) | TurboSouth support bot — installs, configures, files tested upstream PRs |
| [SouthpawIN/SALT-core](https://github.com/SouthpawIN/SALT-core) | State/KV ownership engine behind the SALT integration surface |
| [SouthpawIN/model-momento](https://github.com/SouthpawIN/model-momento) | Long-tail model metadata + benchmark history |
| [SouthpawIN/turbohaul-manager](https://github.com/SouthpawIN/turbohaul-manager) · [southpaw-turbohaul](https://github.com/SouthpawIN/southpaw-turbohaul) · [turbohaul-llmfit](https://github.com/SouthpawIN/turbohaul-llmfit) | The TurboQuant manager line + launch-string doctrine |
| HuggingFace [SouthpawIN](https://huggingface.co/SouthpawIN) | Published artifacts |
| `raw/inbox/` | Watcher cuts from Hermes sessions (immutable) |

Full map: [references/ecosystem](references/ecosystem.md).

---

## TOPICS & WIKI

### The fit — two ladders that converge on Flash Next

> **Dense does not run well on CPU / unified memory, so there are two ladders.** The GPU-dedicated ladder is dense; the unified (CPU / Apple Silicon) ladder is MoE only. Both converge on **Qwen 3.8 Flash Next**. The Fit List IS the fallback chain — `serve auto` walks down on OOM/timeout.
>
> Cross-cutting: **MTP on whenever available**; **mind the power bill** — IQ3_S is lossless, so no heavier quant past it (32 GB and 48 GB both stay on GSQ-RCO @ IQ3_S).

#### Ladder 1 — Dedicated (GPU / VRAM, dense)

| Tier | Model | Quant / Engine | Context | Notes |
| --- | --- | --- | --- | --- |
| **8-11gb** | Ternary Bonsai 2 27B (7.21 GB) | PTQ1_0, PQ2_0 | 131K | dense ternary GGUF (Q2); sizes PTQ1_0 5.95 GB / PQ2_0 7.21 GB; prism-llama.cpp; MTP on |
| **12-15gb** | Underdog 27B | PQ2_0 | 131K | dense; MTP on |
| **16-23gb** | Qwen 3.8 27B GSQ-RCO (11.8 GB) | IQ3_S | 131K | near-lossless; MTP on |
| **24-63gb** | Qwen 3.8 27B GSQ-RCO (11.8 GB) | IQ3_S | 262K | near-lossless; 262K at 24 GB; MTP on; power bill stays on IQ3_S (no heavier quant) |
| **64gb+** | Qwen 3.8 Flash Next (Strata) | strata | 262K | MoE; both ladders converge on Flash Next; MTP on |

#### Ladder 2 — Unified (CPU / Apple Silicon, MoE only)

| Tier | Model | Quant / Engine | Context | Notes |
| --- | --- | --- | --- | --- |
| **8-15gb** | Maple Preview 20B-A1B | TQ2_0 | 131K | MoE; CPU |
| **16-23gb** | Cyber-Tiel Coder 35B-A3B (13.2 GB) | UD-IQ3_XXS | 262K | MoE, 3B active; 262K ctx; faster than GSQ-RCO on CPU |
| **24-31gb** | Cyber-Tiel Coder 35B-A3B (18.5 GB) | UD-Q4_K_XL | 262K | MoE, 3B active |
| **32-47gb** | Cyber-Tiel Coder 35B-A3B (26.6 GB) | UD-Q5_K_XL | 262K | MoE, 3B active |
| **48-63gb** | Cyber-Tiel Coder 35B-A3B (31.8 GB) | UD-Q6_K_XL | 262K | MoE, 3B active |
| **64gb+** | Qwen 3.8 Flash Next (Strata) | strata | 262K | MoE; both ladders converge on Flash Next; MTP on |

Generated from [`references/fit-lists.json`](https://github.com/SouthpawIN/turbofit/blob/main/references/fit-lists.json) (commit `0ff572b`, 2026-10-19) — see [fit-ladder](references/fit-ladder.md) for the prose version and [scaling-ladder](references/scaling-ladder.md) for the long tail.

### Fit math

```
Required:  model_size + KV_cache ≤ tier_size
KV cache:  ≈ 2-4 GB at 262K context (q8_0 KV)
Comfortable: model_size + 2 GB ≤ tier_size
```

Never show a model using more memory than its tier provides. If it doesn't fit, say so or drop the quant.

### Models (16 pages)

| Page | What |
| --- | --- |
| [[Ace Step 1.5 4B]] | acestep.cpp with CUDA, 12-20GB VRAM on RTX 3090×2 |
| [[Bonsai 27B]] | Bonsai refers to models from prism-ml: Bonsai-27B-mlx-1bit (1-bit binary, 1.4M downloads) and Ternary-Bonsai-27B-mlx-2bit (2-bit ternary, 1.4M downloads). The Ternary… |
| [[Cosmos 37B BASE]] | llama.cpp CUDA, needs offload (184GB total) |
| [[Cyber Tiel Coder 35B-A3B]] | The SSM-heavy architecture makes KV cache very cheap: ~20–22 KB/token at f16, ~10–11 KB/token at q80. |
| [[DAXZEIT GRM 2.6 Plus]] | llama.cpp with --spec-type draft-mtp, CUDA |
| [[DeepSeek V4.1 Flash]] | DeepSeek-V4.1-Flash adopts a Causal Encoder-Decoder (CED) architecture — a 40-layer Transformer split into a 20-layer causal encoder and a 20-layer decoder. The… |
| [[GSQ-RCO Qwen 3.8]] | Full name: Qwen3.8-27B (GSQ-RCO quantization) |
| [[Maple]] | ./llama-cli -m maple-preview-TQ20-head-Q4K.gguf \ |
| [[NVIDIA Nemotron 3.5]] | llama.cpp CUDA, --layer-split for multi-GPU |
| [[Ornith 1.5 35B-A3B]] | jzinno/Ornith-1.5-35B-A3B-DFlash2 was inspected on HuggingFace and downloaded as a local draft artifact for speculative-decode experiments . |
| [[Qwen 2.5 Omni 3B]] | llama.cpp CUDA + mmproj for vision |
| [[Qwen 3.8 27B Base]] | llama.cpp CUDA, -ngl 99 |
| [[Qwen 3.8 27B Unleashed]] | Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed is the candidate Hermes TurboFit provider discovered on 2026-09-07. It is served via ~/turbofit/.venv/bin/mtplx serve and… |
| [[Qwen 3.8 Flash Next]] | Qwen-reported scores from HuggingFace model card: |
| [[Soprano 1.1 80M]] | Soprano 1.1 80M |
| [[Super Qwen 3.8 27B]] | llama.cpp CUDA, -ngl 99 for full GPU offload |
### Concepts

| Page | What |
| --- | --- |
| [[131k-deferred-candidates]] | A number of newly downloaded candidate artifacts were not benchmarked at 131K because model-plus-KV size exceeds the stable 32 GB Mac fit before testing begins. |
| [[benchmark-taxonomy]] | When adding a model page, fill in any of the above benchmarks where data is available from: |
| [[bonsai-colibri-deprioritization]] | During the 2026-09-07 testing session, subagents explored multiple candidate models including Bonsai (Prism MLX 2-bit ternary, 7.91 GB) and Colibri (custom Maple… |
| [[compression-timeouts]] | Hermes failed with: |
| [[dflash2-compat-boundary]] | DFlash2 draft models are not interchangeable across runtimes. On this box the boundary is concrete: MTPLX cannot use DFlash2, and Unleashed+DFlash2 only works through… |
| [[dflash2-fork-flag-boundary]] | DFlash2 draft models are not interchangeable across runtimes. On this box the boundary is concrete: MTPLX cannot use DFlash2, and Unleashed+DFlash2 only works through… |
| [[dflash2-mplx-incompatibility]] | DFlash2 draft models are incompatible with MTPLX's native MLX MTP heads. This is a fundamental architecture mismatch. |
| [[fit-calculation-system-tables]] | The fit calculation system tables are Chris's set of tables that record how well each model fits a given compute platform. As named by Chris they come in three hardware… |
| [[hermes-auto-route-stability]] | From raw/inbox/2026-09-08-from-senter-wiki.md: |
| [[hermes-model-switching-noise]] | The active Hermes model switched multiple times during TurboFit work without Chris initiating the changes ^[raw/inbox/2026-09-07.md]. The switch chain was: |
| [[model-switching-pain]] | The active Hermes model switched multiple times during TurboFit work without Chris initiating the changes. |
| [[model-zoo-table]] | The Model Zoo table is the dashboard table that compares machine-learning models across named categories. It is the subject of all three add-one requests in this topic.… |
| [[mtplx-32gb-memory-and-evidence-reliability]] | Captures two distinct reliability concerns for MTPLX on this box: 131K memory overcommit, and postcommit artifacts that can't be treated as finished TurboFit evidence… |
| [[mtplx-context-overcommit]] | On the 32 GB Mac, mtplx serve with --context-window 131072 loads the model in 6-9s and installs the native MTP draft head, but the printed memory plan marks… |
| [[mtplx-foreground-preemption]] | When MTPLX handles long-running Hermes foreground work, postcommit records show crosssessionforegroundpreempted and foregroundpreemptedpostcommit, and idle async… |
| [[turbofit-session-mismatch]] | MTLPX generation events show foreground/preemption behavior and session-store mismatch that make some TurboFit captures unreliable as finished-state evidence… |
| [[turbofit-provider-picker-history]] | Every time the TurboFit provider vanished from, or never registered into, the Hermes desktop provider/model picker — 09-13 disappearance, 09-15 still-missing, the wayvnc + https-scheme fix that was necessary but not sufficient, and the restart that dropped the options again. Absorbed from five scattered topics. |
| [[turbofit-m1-testing-status]] | What the 2026-09-07 Apple-Silicon benchmark push had proven on the MacBook (Bonsai ternary via llama.cpp Metal, warmup protocol) and what blocked it (config writes refused mid-test). |
### Decisions

| Page | What |
| --- | --- |
| [[aux-model-selection]] | Auxiliary and compression routing is Maple MLX on 127.0.0.1:11612, 131k context, served with deepgrove-ai/mlx-lm-deepgrove ^[raw/inbox/2026-09-06.md]. |
| [[candidate-quant-preference]] | Decision/Preference: When comparing GGUF vs MLX for new local candidates, prefer the Q3 quant when model pages describe it as near base-model quality. |
| [[context-sizing]] | Local TurboFit contexts are set to 131,072 tokens for both main and aux ^[raw/inbox/2026-09-06.md]. |
| [[context-window-decision]] | Decision: Lock in 65K context as the stable daily driver on M1 MacBook 32GB, with 131K reserved for rare long-context needs where speed is not critical. |
| [[fallback-model-order]] | The active model preference order should preserve explicit user choice and avoid silently switching to stepfun/step-3.7-flash:free ^[raw/inbox/2026-09-06.md]. |
| [[highest-recorded-tok-s-after-flags]] | Chris asked to add a column to all of the fit calculation system tables — the GPU, CPU, and unified tables — recording the highest recorded tokens per second, placed… |
| [[local-main-provider]] | What Chris wanted: the smartest feasible local runtime as Hermes main, with verified evidence, not just Hermes internal logs. |
| [[main-model-selection]] | Initial decision: Main inference and vision is Unleashed 27B + DFlash2 draft on 127.0.0.1:11606, Metal, 131k context ^[raw/inbox/2026-09-06.md]. |
| [[mtplx-main-provider]] | Make Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed via mtplx serve the main TurboFit provider and remove Maple/Unleashed as co-resident models to reclaim disk space. |
| [[ornith-config-routing]] | Action: Repoint Hermes custom:turbofit to the running Ornith MLX server on http://127.0.0.1:11613/v1 and set ornith-1-5-35a3b-mlx as the default model. |
| [[turbofit-list-parameters-column]] | Chris asked to add one more category to the table: parameters. ^[raw/inbox/2026-09-16.md] |
| [[turbofit-list-tok-s-column]] | On the TurboFit list, Chris asked to replace the type column with a tokens-per-second (tok/s) column showing the best tok/s achieved for each model.… |
| [[turbofit-table-column-ordering]] | Chris set the column order on the table and then asked to drop the order column entirely. ^[raw/inbox/2026-09-16.md] |
| [[turbofit-table-column-sorting]] | Chris wants to sort the table by clicking a column's title rather than some other control. ^[raw/inbox/2026-09-16.md] |
| [[unleashed-backup]] | Keep Unleashed Q3KXL as the safe long-context backup when MTPLX overcommits memory or Hermes reloads fail. |
| [[turbofit-picker-is-the-acceptance-test]] | Standing acceptance criterion: a model is only "working" when it can be picked inside Hermes with no error. The raw endpoint passing proves nothing. |
| [[model-zoo-list-lands-in-turbofit-list]] | Every model Chris hands over from the Model Zoo must land on the TurboFit list — a partial subset is a failure ("Please, please do better"). |
| [[turbofit-standing-rule-tracking]] | Chris states fit/lane rules mid-build and expects each implemented immediately, not batched: IQ3_S through 48 GB, MoE (Cyber Tiel) on CPU/unified lanes, Q3 acceptable on 8–16 GB GPU tiers. |
| [[turbofit-per-model-pages]] | Build policy: one page per model with setup-relevant nuggets, consolidating notes that were filed twice without losing information. |
### Comparisons

| Page | What |
| --- | --- |
| [[aux-runtime-options]] | Maple MLX via deepgrove fork with Hermes compression routing configured locally. If server-mode instability returns, fallback to Nous for heavy compression and keep… |
| [[candidate-quant-and-format-comparison]] | "They also have a lot to say about their quants on their pages too, check GGUF vs MLX, I like the Q3 quant that they said is near base model quality"… |
| [[main-runtime-speed]] | Evidence-observed main-runtime candidates for Qwen 3.8 27B-class workloads on this 32 GB M1 Mac. Numbers are in-session measurements against downloaded/observed… |
### Entities

| Page | What |
| --- | --- |
| [[benchmark-infographics]] | Static infographic assets (e.g. June 2026: Frontier AI Models — Claude Opus 4.8 vs GPT-5.5 vs GLM-5.2 vs Qwen3.7 Max vs DeepSeek V4 Pro) with sources listed per figure… |
| [[bonsai]] | Bonsai refers to models from prism-ml: Bonsai-27B-mlx-1bit (1-bit binary, 1.4M downloads) and Ternary-Bonsai-27B-mlx-2bit (2-bit ternary, 1.4M downloads). The Ternary… |
| [[colibri]] | Colibri is a custom-architecture model with basemodel: deepgrove/maple-preview. It requires custom Maple MLX training/inference code and is incompatible with the… |
| [[dflash2-arg-failures]] | All attempted llama.cpp DFlash2 integration commands failed with invalid/unrecognized argument errors. The dflash2-llama.cpp fork has a different flag set than stock… |
| [[dflash2-draft]] | DFlash2 is the speculative-draft model paired with Unleashed 27B in TurboFit. It requires the dflash2-llama.cpp fork, not stock llama.cpp ^[raw/inbox/2026-09-06.md]. |
| [[dirk-gguf]] | Dirk-Qwen3.8-27B-UD-Q3KXL.gguf (12.24 GB) is the requested Q3 Dirk artifact at ~/Models/storage/dirk-gguf/, selected because Chris prefers Q3 when it is described as… |
| [[dirk-qwen38-27b]] | Chris requested Dirk GGUF downloads for local comparison. The actual repo is peculiar-ragdoll/Dirk-Qwen3.8-27B-GGUF because MTP is a model capability, not a repo suffix… |
| [[maple]] | Maple-Preview is the auxiliary model Chris wants for Hermes compression and text aux tasks. It is a custom-architecture MoE model with no native support in stock… |
| [[model-momento]] | TurboFit's own catalog is the shipped subset (model-catalog.json: 62 artifacts in 13 families) and its intel lives in model-intel / benchmark-leaderboard. Model Momento… |
| [[mplx-metal-load-failure]] | A mtplx serve --download background process exited with code 1 after 42.2 s because model loading failed with RuntimeError: [METAL] Command buffer execution failed:… |
| [[mplx]] | MPLX is an experimental additional local runtime discovered late in the session. It was downloaded and measured at 12.4 tok/s, roughly 2.5x faster than Unleashed Q3KXL… |
| [[mtplx-memory-guard]] | MTPLX emits a memory-guard prefilladmissionshed event when a prompt would push the active process above its memory threshold, clearing the KV cache before admission to… |
| [[mtplx-qwen-38-27b-optimized-speed]] | Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed is the candidate Hermes TurboFit provider discovered on 2026-09-07. It is served via ~/turbofit/.venv/bin/mtplx serve and… |
| [[mtplx-service-arg-validation]] | mtplx serve with --memory-budget 32GB exits with an error: |
| [[nail-qwen36-35b]] | Nail-Qwen3.6-35B-A3B-UD-Q4KXL.gguf (~20.82 GB) and its mmproj-F16.gguf (~858 MB) were downloaded to ~/Models/storage/nail/ for testing. This is a MoE architecture model… |
| [[ornith-1-5-35b-a3b-mlx-4-bit]] | Local candidate for TurboFit main on the M1 32GB box, owned by MLX, tested from ~/Models/storage/ornith/. |
| [[ornith-35b-dflash2]] | jzinno/Ornith-1.5-35B-A3B-DFlash2 was inspected on HuggingFace and downloaded as a local draft artifact for speculative-decode experiments ^[raw/inbox/2026-09-07.md]. |
| [[ornith-35b-mlx]] | Ornith-1.5-35B-A3B MLX 4-bit is a MoE local candidate downloaded to ~/Models/storage/ornith/ with a companion DFlash2 draft package at ~/Models/storage/ornith-dflash2/… |
| [[ornith-35b]] | Ornith-1.5-35B-A3B is a MoE model downloaded to ~/Models/storage/ornith/ as MLX 4-bit on this 32 GB box. A DFlash2 draft package was also downloaded to… |
| [[ornith-config-routing-failure]] | After Hermes custom:turbofit was retargeted to http://127.0.0.1:11613/v1 and model.default was set to ornith-1-5-35a3b-mlx, Hermes emitted repeated connection timeouts… |
| [[salt-core]] | SALT (State Assured Latent-Transition engine) — paper: Zenodo preprint 23111764. The public contract centres on: |
| [[sirvir]] | Sirvir supports one product — SouthpawIN/turbofit — and one execution boundary: local models served by Turbofit, loopback by default, optional private Tailnet routes. It… |
| [[southpaw-turbohaul]] | docs/TURBOQUANTFLAGS.md is the clearest written record of the TQ flag combinations; the MTP+quantized-KV composition claim lives here before any TurboFit rung used it. |
| [[tiel-coder]] | Tiel-Coder is a queued local GGUF candidate. The primary MLX download in ~/Models/storage/tiel-coder/ remained incomplete (~15 GB of ~19 GB), and a GGUF test path at… |
| [[turbo-fit-benchmark]] | The TurboFit list is Chris's table of models run through TurboFit, where each model carries a tokens-per-second (tok/s) column recording the best tok/s it has achieved.… |
| [[turbofit-memory-crash]] | A mtplx serve background process exited with code -9 during TurboFit testing on this 32 GB box. The first evidence used --mtp without an explicit long-context window,… |
| [[turbofit-mtpl-performance]] | Evidence-observed performance characteristics of Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed on this 32 GB M1 Mac, including short-context throughput, long-context… |
| [[turbofit-verifier-bridge]] | turbofit-verifier is the existing TurboFit topic bot. This page records the new evidence that it should drive verification through desktoppreview on a real Hermes window… |
| [[turbofit]] | TurboFit is the adaptive local-inference path for Hermes on this 32 GB M1 Mac. It loads local models first and falls back to cloud providers when compression or context… |
| [[turbohaul-llmfit]] | A single-SKILL repo. Given a machine and a model, it emits a launch string + manifest using llmfit's hardware detection and the TurboQuant flag doctrine, instead of… |
| [[turbohaul-manager]] | The TurboQuant flag doctrine (turbo2/3/4 KV quant), hot-hold/swap semantics, and the launch-string generator (turbohaul-llmfit) all originate in this line. Read it when… |
| [[unleashed-27b]] | Qwen3.8-27B-Unleashed in UD-Q3KXL.gguf with the Unleashed vision projector and DFlash2 draft. This is the main model in TurboFit ^[raw/inbox/2026-09-06.md]. |
| [[unleashed-iq3-xxs-load-failure]] | Qwen3.8-27B-Unleashed-UD-IQ3XXS.gguf failed to load in the dflash2-llama.cpp fork Metal server after a DFlash warning about missing ctxother and then a tensor bounds… |
### Queries

| Page | What |
| --- | --- |
| [[apple-silicon-runtime-benchmark]] | From [2026-09-07 03:06](raw/inbox/2026-09-07.md): Chris asked to "Research and test ALL available Apple Silicon inference engines for Qwen 3.8 27B to find the fastest… |
| [[duplicate-page-candidates]] | Detected by title/source scan after the 2026-09-07 compile. |
| [[engine-research-request]] | Chris asked for research and testing of all available Apple Silicon inference engines for Qwen 3.8 27B to find the fastest configuration ^[raw/inbox/2026-09-07.md]. |
| [[engine-speed-report]] | This is the live result surface of Chris's research request for Apple Silicon engine speed testing. |
| [[evidence-capture-and-reliability]] | Captures the open verification work after configuring Ornith as main, and the contested state where Hermes showed persistent timeouts after config repoint. |
| [[maple-metal-compat]] | Can Maple serve stable long-context compression workloads on Apple Silicon Metal without repeated OOM, or is a non-server execution path required? |
| [[mplx-integration]] | Can MPLX be added as a fast local TurboFit provider alongside Unleashed 27B without evicting the main model, and what is the memory ceiling under MTP? |
| [[ornith-cleanup-focus]] | Chris wanted Ornith prioritized over Bonsai, Colibri, and music-generation side paths. His exact instruction was, "It just needs to be configured into turbofit so I can… |
| [[turbofit-mtplx-coexistence]] | 32GB physical RAM limitation: 27B model weights (19.3GB) + KV cache at 131K (8GB) + macOS/Hermes (~8GB) = ~35GB+, exceeding available memory. |

---

## REFERENCE LIBRARY (39 pages)
### Core doctrine

| Page | What |
| --- | --- |
| [fit-ladder](references/fit-ladder.md) | GSQ-RCO IQ3S benchmarks (AIME25 100%, GPQA-D 89.2%, DeepSWE 42.2%, LCBv6 90.3%) are from the model card; Maple LCBv6 is LiveCodeBench v6. |
| [model-lineup](references/model-lineup.md) | Three layers of model, ranked by measured evidence, not heuristics. |
| [curated-lineup](references/curated-lineup.md) | Opinionated picks for main + aux roles, local + API. Ranked by actual benchmark scores, not heuristics. |
| [scaling-ladder](references/scaling-ladder.md) | The scaling ladder is what makes turbofit opinionated. Its philosophy: good intelligence is always available no matter what hardware you have — from… |
| [binary-selection](references/binary-selection.md) | When a model fails to load with the atomic fork binary, use this decision tree to determine the fix. |
| [product-roadmap](references/product-roadmap.md) | The source-of-truth map of TurboFit: the two ladders, what is built, and what is open. |
### Benchmarks & evidence

| Page | What |
| --- | --- |
| [benchmark-evidence](references/benchmark-evidence.md) | What we have measured, and the evidence gaps. |
| [benchmark-analysis](references/benchmark-analysis.md) | — |
| [benchmark-leaderboard](references/benchmark-leaderboard.md) | <!-- turbofit:generated:benchmark-leaderboard:begin --> |
| [external-benchmarks](references/external-benchmarks.md) | External results are discovery evidence only. Turbofit promotes local runtime profiles only after reproducible local runs pass their gates. |
| [research-report](references/research-report.md) | Projected using your actual daily input/output averages and cache hit rate. |
| [model-intel](references/model-intel.md) | Generated: 2026-08-14T16:55:23.535149+00:00 |
| [api-model-rankings](references/api-model-rankings.md) | Curated API models ranked by quality. Prices in $/M tokens (input/output). |
| [api-tier-rankings](references/api-tier-rankings.md) | Curated API models ranked by quality. Prices in $/M tokens (input/output). |
| [api-pairing-matrix](references/api-pairing-matrix.md) | Pairings use the user's specified model universe. Prices in $/M tokens (input/output). |
### Hardware & runtime

| Page | What |
| --- | --- |
| [hardware-tiers](references/hardware-tiers.md) | Two ways Turbofit tiers hardware — by local VRAM and by API fallback. |
| [hardware-tier-tps](references/hardware-tier-tps.md) | Live llama-server /completion medians. Three 128-token generations after warmup. |
| [runtime-backends](references/runtime-backends.md) | Turbofit keeps provider routes stable while the process runtime is replaceable. The controller and Hermes provider do not depend on a specific… |
| [model-matrix](references/model-matrix.md) | Canonical research detail extracted from the product README. |
| [model-metadata](references/model-metadata.md) | GET /v1/models and GET /v1/models/{id} retain raw request IDs |
| [freetoken-runtime](references/freetoken-runtime.md) | TurboFit integrates FreeToken as an optional, evidence-gated candidate backend for supported NVIDIA MoE checkpoints. It is not an Auto rung and does… |
| [salt-core-integration](references/salt-core-integration.md) | <!-- turbofit:generated:salt-core-integration:begin --> |
| [multimodal](references/multimodal.md) | Turbofit scans total usable memory and platform support, then labels each option as ready, candidate, unsupported, or too large. Candidate… |
### Platform installs & ops

| Page | What |
| --- | --- |
| [install-paths](references/install-paths.md) | /turbofit is a plugin command. It only exists in a session that has loaded the plugin, and |
| [windows-native-install](references/windows-native-install.md) | Turbofit supports Windows 10/11 with a user-scoped pinned llama.cpp runtime and gateway. No administrator account or machine-wide service is required. |
| [remote-hermes-model-server](references/remote-hermes-model-server.md) | Turbofit can run on one machine while a Hermes Agent gateway runs on another. This is useful when the Mac has the Apple Silicon memory bandwidth and… |
| [apple-arm64-unmeasured-gap](references/apple-arm64-unmeasured-gap.md) | references/successful-runtime-profiles.json is the evidence table behind |
| [maple-small-device-validation](references/maple-small-device-validation.md) | Status: Auto on hardware-8gb at native 64K and 128K |
| [turbofit-check](references/turbofit-check.md) | Canonical product brief. This is what ships, not a research note. |
| [turbofit-list](references/turbofit-list.md) | The TurboFit List is made only from benchmark winners at each physical hardware level. TurboFit Check is the system scan-to-configuration process… |
| [campaigns](references/campaigns.md) | Operator detail for physical and intelligence campaigns. |
| [workflows](references/workflows.md) | One source of truth, two repos. |
| [troubleshooting](references/troubleshooting.md) | Common failures and the first move for each. |
| [tailscale](references/tailscale.md) | How Turbofit (and the wiki) reach each other across the network. |
### History & contracts

| Page | What |
| --- | --- |
| [changelog](references/changelog.md) | — |
| [skill-contract](references/skill-contract.md) | description: "Operate the Turbofit adaptive local inference plugin." |
| [turbosovth-soul](references/turbosovth-soul.md) | TurboSouth is the customer-service profile bundled with Turbofit. The canonical distributable persona is profiles/turbosouth/SOUL.md, with operating… |
| [upstream-pr-process](references/upstream-pr-process.md) | How research findings become pull requests. |
| [ecosystem](references/ecosystem.md) | The TurboFit project is not one repo. This page is the map: what each repo is, whether it is shipped, support, side tool, or legacy line, and which… |

---

## SKILLS & CAPABILITIES

| Skill | What |
| --- | --- |
| [candidate-quant-comparison](skills/candidate-quant-comparison/SKILL.md) | ## Steps |
| [dflash2-fork-flag-boundary](skills/dflash2-fork-flag-boundary/SKILL.md) | ## dflash2-fork-flag-boundary |
| [maple-mlx-server-runtime](skills/maple-mlx-server-runtime/SKILL.md) | 1. Use `/tmp/mlx-lm-deepgrove` fork installed from `deepgrove-ai/mlx-lm-deepgrove`. |
| [mtplx-32gb-macos-tuning](skills/mtplx-32gb-macos-tuning/SKILL.md) | 1. Treat `--memory-budget` as unsupported on `mtplx serve`; do not retry it. |
| [turbo-artifact-download-spec](skills/turbo-artifact-download-spec/SKILL.md) | 1. Read the Hermes request for target repo/path/quant and destination under ~/Models/storage/. |
| [turbo-fit-evidence-capture](skills/turbo-fit-evidence-capture/SKILL.md) | ## TurboFit Evidence Capture |
| [turbo-model-store-cleanup](skills/turbo-model-store-cleanup/SKILL.md) | ## Steps |
| [speedometer-menu-design](skills/speedometer-menu-design.md) | Decisions captured 2026-08-27, from live conversation. Redesign target: `desktop/plugin.js` |
| [turbofit-macos-setup](skills/turbofit-macos-setup.md) | Verified walkthrough, 2026-08-27, on macOS 26.5.2 / M1 Pro / 32 GB unified. |

Global skills that back this topic: `turbofit` (rules), `turbofit-model-fit`, `turbofit-runtime-setup`, `turbofit-repository-updates`, `turbofit-model-store-cleanup`, `llama-cpp`, `serving-llms-vllm`, `huggingface-hub`.

---

## BOTS & PROFILES

| Bot | What |
| --- | --- |
| [candidate-benchmark-scout](agents/candidate-benchmark-scout.md.proposed) | **I see you're queuing Dirk, Nail, and Tiel-Coder with a Q3 preference — want a bot that benchmarks each candidate on 65K and reports tok/s + stability?** |
| [mtplx-runtime-scout](agents/mtplx-runtime-scout.md.proposed) | **I see you're trying to pin a stable MTPLX config — want a bot that finds the supported runtime knob for memory budgeting and writes a working profile for this 32 GB box |
| [orchestrator](agents/orchestrator.md.proposed) | **I see you want automatic evidence capture for all TurboFit route changes — want a bot that triggers verification whenever a provider config changes?** |
| [turbofit-benchmark](agents/turbofit-benchmark.md.proposed) | **I see you're collecting Apple Silicon runtime speed data — want a bot that runs controlled tok/s benchmarks on the downloaded runtimes and publishes results to the wiki |
| [turbofit-bot](agents/turbofit-bot.md.proposed) | Owns the `turbofit` topic: runs its skills, answers for it, proposes its loops. |
| [turbofit-evidence-capture](agents/turbofit-evidence-capture.md.proposed) | **Want me to capture a desktop_preview of the Hermes window showing the Ornith MLX runtime is stable at 65K context with observed throughput?** |
| [turbofit-launcher](agents/turbofit-launcher.md.proposed) | **Want me to lock in Ornith MLX 4-bit as the main provider with 65K context, and Unleashed+DFlash2 as the 131K long-context fallback?** |
| [turbofit-route-stabilizer](agents/turbofit-route-stabilizer.md.proposed) | **I see Hermes is still flipping to cloud models despite your intent — want a bot that locks the fallback_providers chain and pins compression to local TurboFit?** |
| [turbofit-runtime-scout](agents/turbofit-runtime-scout.md.proposed) | **I see you're assembling Nail/Dirk/Tiel/Ornith candidates — want a bot that tracks each one's actual Hermes path: download status, live server speed, and whether it can  |
| [turbofit-verifier](agents/turbofit-verifier.md.proposed) | **I see you’re testing end-to-end TurboFit stability — want a bot that runs a live 131K compression probe against :11606/:11612 after every config change?** |

Live fleet bots that serve this product: `turbosovth` (TurboSouth/support), `looker` (research dispatch), `senter` (builder).

---

## TRIGGERS & LOOPS

| Loop | What |
| --- | --- |
| [131k-attempt-blocker](loops/131k-attempt-blocker.md.proposed) | owner: turbofit-memory-monitor · cadence: human phrase · status: SUGGESTED |
| [candidate-65k-benchmark-sweep](loops/candidate-65k-benchmark-sweep.md.proposed) | owner: turbosovth · cadence: human phrase · status: SUGGESTED |
| [candidate-quant-comparator](loops/candidate-quant-comparator.md.proposed) | owner: anser · cadence: on-demand · status: SUGGESTED |
| [compression-timeout-watch](loops/compression-timeout-watch.md.proposed) | owner: looker · cadence: human phrase · status: SUGGESTED |
| [hermes-model-change-detector](loops/hermes-model-change-detector.md.proposed) | owner: anser · cadence: real-time provider monitoring · status: SUGGESTED |
| [mac-memory-watch](loops/mac-memory-watch.md.proposed) | owner: looker · cadence: human phrase · status: SUGGESTED |
| [mtplx-telemetry-watch](loops/mtplx-telemetry-watch.md.proposed) | owner: turbosovth · cadence: every 2h during active use · status: SUGGESTED |
| [turbo-context-budget-watch](loops/turbo-context-budget-watch.md.proposed) | owner: turbofit-runtime-scout · cadence: every 5m · status: SUGGESTED |
| [turbofit-candidate-discovery](loops/turbofit-candidate-discovery.md.proposed) | owner: looker · cadence: daily · status: SUGGESTED |
| [turbofit-health-check](loops/turbofit-health-check.md.proposed) | owner: senter-wiki-bot · cadence: every 5 minutes · status: SUGGESTED |
| [turbofit-memory-monitor](loops/turbofit-memory-monitor.md.proposed) | owner: senter-wiki-bot · cadence: every 30s · status: SUGGESTED |
| [turbofit-memory-threshold-monitor](loops/turbofit-memory-threshold-monitor.md.proposed) | owner: anser · cadence: live generation monitoring · status: SUGGESTED |
| [turbofit-runtime-watch](loops/turbofit-runtime-watch.md.proposed) | owner: turbofit-bot · cadence: daily at 09:00 · status: SUGGESTED |

---

## RULES

1. **Two ladders, never one** — dense is GPU, MoE is CPU/unified; both converge on Flash Next.
2. **Model + KV cache ≤ tier size.** Period.
3. **IQ3_S is the default** where it fits — near-lossless, lower power; FP16 only at 64 GB+.
4. **MTP on whenever available**; weigh kWh/hour on every rung.
5. **Evidence before winner** — every number carries a source, every benchmark a machine.
6. **Read the wiki before the code**: hub → index (this page) → `.system/INDEX.md` → one file, one heading.

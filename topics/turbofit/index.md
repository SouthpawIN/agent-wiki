# turbofit — wiki index
> One line per page. The wiki row's CONTEXT section renders this file.
> Last updated: 2026-09-08 | Total pages: 61

## Entities
- [[topics/turbofit/wiki/entities/bonsai|Bonsai MLX]] — Bonsai refers to models from `prism-ml`: `Bonsai-27B-mlx-1bit` (1-bit binary, 1.4M downloads) and `Ternary-Bonsai-27B-mlx-2bit` (2-bit ternary, 1.4M downloads).
- [[topics/turbofit/wiki/entities/colibri|Colibri]] — Colibri is a custom-architecture model with `base_model: deepgrove/maple-preview`. It requires custom Maple MLX training/inference code and is incompatible with
- [[topics/turbofit/wiki/entities/dflash2-arg-failures|DFlash2 Arg Failures]] — All attempted llama.cpp DFlash2 integration commands failed with invalid/unrecognized argument errors. The `dflash2-llama.cpp` fork has a different flag set tha
- [[topics/turbofit/wiki/entities/dflash2-draft|DFlash2 Draft]] — DFlash2 is the speculative-draft model paired with Unleashed 27B in TurboFit. It requires the `dflash2-llama.cpp` fork, not stock llama.cpp ^[raw/inbox/2026-09-
- [[topics/turbofit/wiki/entities/dirk-gguf|Dirk GGUF Q3_K_XL]] — `Dirk-Qwen3.8-27B-UD-Q3_K_XL.gguf` (12.24 GB) is the requested Q3 Dirk artifact at `~/Models/storage/dirk-gguf/`, selected because Chris prefers Q3 when it is d
- [[topics/turbofit/wiki/entities/dirk-qwen38-27b|Dirk Qwen 3.8 27B GGUF]] — Chris requested Dirk GGUF downloads for local comparison. The actual repo is `peculiar-ragdoll/Dirk-Qwen3.8-27B-GGUF` because MTP is a model capability, not a r
- [[topics/turbofit/wiki/entities/maple|Maple]] — Maple-Preview is the auxiliary model Chris wants for Hermes compression and text aux tasks. It is a custom-architecture MoE model with no native support in stoc
- [[topics/turbofit/wiki/entities/mplx-metal-load-failure|MPLX Metal Load Failure]] — A `mtplx serve --download` background process exited with code `1` after 42.2 s because model loading failed with `RuntimeError: [METAL] Command buffer executio
- [[topics/turbofit/wiki/entities/mplx|MPLX]] — MPLX is an experimental additional local runtime discovered late in the session. It was downloaded and measured at 12.4 tok/s, roughly 2.5x faster than Unleashe
- [[topics/turbofit/wiki/entities/mtplx-memory-guard|MTPLX Memory Guard]] — MTPLX emits a memory-guard `prefill_admission_shed` event when a prompt would push the active process above its memory threshold, clearing the KV cache before a
- [[topics/turbofit/wiki/entities/mtplx-qwen-38-27b-optimized-speed|MTPLX Qwen 3.8 27B Optimized Speed]] — `Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed` is the candidate Hermes TurboFit provider discovered on 2026-09-07. It is served via `~/turbofit/.venv/bin/mtplx s
- [[topics/turbofit/wiki/entities/mtplx-service-arg-validation|MT_PlX Service Arg Validation]] — `mtplx serve` with `--memory-budget 32GB` exits with an error:
- [[topics/turbofit/wiki/entities/nail-qwen36-35b|Nail Qwen 3.6 35B UD Q4_K_XL]] — `Nail-Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf` (~20.82 GB) and its `mmproj-F16.gguf` (~858 MB) were downloaded to `~/Models/storage/nail/` for testing. This is a MoE ar
- [[topics/turbofit/wiki/entities/ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]] — Local candidate for TurboFit main on the M1 32GB box, owned by MLX, tested from `~/Models/storage/ornith/`.
- [[topics/turbofit/wiki/entities/ornith-35b-dflash2|Ornith 35B A3B DFlash2]] — `jzinno/Ornith-1.5-35B-A3B-DFlash2` was inspected on HuggingFace and downloaded as a local draft artifact for speculative-decode experiments ^[raw/inbox/2026-09
- [[topics/turbofit/wiki/entities/ornith-35b-mlx|Ornith 35B MLX]] — `Ornith-1.5-35B-A3B` MLX 4-bit is a MoE local candidate downloaded to `~/Models/storage/ornith/` with a companion DFlash2 draft package at `~/Models/storage/orn
- [[topics/turbofit/wiki/entities/ornith-35b|Ornith 35B A3B]] — `Ornith-1.5-35B-A3B` is a MoE model downloaded to `~/Models/storage/ornith/` as MLX 4-bit on this 32 GB box. A DFlash2 draft package was also downloaded to `~/M
- [[topics/turbofit/wiki/entities/ornith-config-routing-failure|Ornith Config Routing Failure]] — After Hermes `custom:turbofit` was retargeted to `http://127.0.0.1:11613/v1` and `model.default` was set to `ornith-1-5-35a3b-mlx`, Hermes emitted repeated conn
- [[topics/turbofit/wiki/entities/tiel-coder|Tiel Coder]] — Tiel-Coder is a queued local GGUF candidate. The primary MLX download in `~/Models/storage/tiel-coder/` remained incomplete (~15 GB of ~19 GB), and a GGUF test 
- [[topics/turbofit/wiki/entities/turbofit-memory-crash|TurboFit Memory Crash]] — A `mtplx serve` background process exited with code `-9` during TurboFit testing on this 32 GB box. The first evidence used `--mtp` without an explicit long-con
- [[topics/turbofit/wiki/entities/turbofit-mtp-performance|TurboFit MTP Performance]] — Redirect: this subject is consolidated under `turbofit-mtpl-performance`.
- [[topics/turbofit/wiki/entities/turbofit-mtpl-performance|TurboFit MTPLX Performance]] — Evidence-observed performance characteristics of `Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed` on this 32 GB M1 Mac, including short-context throughput, long-co
- [[topics/turbofit/wiki/entities/turbofit-verifier-bridge|TurboFit Verifier Bridge]] — `turbofit-verifier` is the existing TurboFit topic bot. This page records the new evidence that it should drive verification through `desktop_preview` on a real
- [[topics/turbofit/wiki/entities/turbofit|TurboFit]] — TurboFit is the adaptive local-inference path for Hermes on this 32 GB M1 Mac. It loads local models first and falls back to cloud providers when compression or
- [[topics/turbofit/wiki/entities/unleashed-27b|Unleashed 27B]] — Qwen3.8-27B-Unleashed in `UD-Q3_K_XL.gguf` with the Unleashed vision projector and DFlash2 draft. This is the main model in TurboFit ^[raw/inbox/2026-09-06.md].
- [[topics/turbofit/wiki/entities/unleashed-iq3-xxs-load-failure|Unleashed IQ3 XXS Load Failure]] — `Qwen3.8-27B-Unleashed-UD-IQ3_XXS.gguf` failed to load in the `dflash2-llama.cpp` fork Metal server after a DFlash warning about missing `ctx_other` and then a 

## Concepts
- [[topics/turbofit/wiki/concepts/131k-deferred-candidates|131K Deferred Candidates]] — A number of newly downloaded candidate artifacts were not benchmarked at 131K because model-plus-KV size exceeds the stable 32 GB Mac fit before testing begins.
- [[topics/turbofit/wiki/concepts/bonsai-colibri-deprioritization|Bonsai and Colibri Deprioritization]] — During the 2026-09-07 testing session, subagents explored multiple candidate models including Bonsai (Prism MLX 2-bit ternary, 7.91 GB) and Colibri (custom Mapl
- [[topics/turbofit/wiki/concepts/compression-timeouts|Compression Timeouts]] — Hermes failed with:
- [[topics/turbofit/wiki/concepts/dflash2-compat-boundary|DFlash2 Compatibility Boundary]] — DFlash2 draft models are not interchangeable across runtimes. On this box the boundary is concrete: MTPLX cannot use DFlash2, and Unleashed+DFlash2 only works t
- [[topics/turbofit/wiki/concepts/dflash2-fork-flag-boundary|DFlash2 Fork Flag Boundary]] — DFlash2 draft models are not interchangeable across runtimes. On this box the boundary is concrete: MTPLX cannot use DFlash2, and Unleashed+DFlash2 only works t
- [[topics/turbofit/wiki/concepts/dflash2-mplx-incompatibility|DFlash2 MTPLX Incompatibility]] — DFlash2 draft models are incompatible with MTPLX's native MLX MTP heads. This is a fundamental architecture mismatch.
- [[topics/turbofit/wiki/concepts/hermes-auto-route-stability|Hermes Auto Route Stability]] — From `raw/inbox/2026-09-08-from-senter-wiki.md`:
- [[topics/turbofit/wiki/concepts/hermes-model-switching-noise|Hermes Model Switching Noise]] — The active Hermes model switched multiple times during TurboFit work without Chris initiating the changes ^[raw/inbox/2026-09-07.md]. The switch chain was:
- [[topics/turbofit/wiki/concepts/model-switching-pain|Model Switching Pain]] — The active Hermes model switched multiple times during TurboFit work without Chris initiating the changes.
- [[topics/turbofit/wiki/concepts/mtplx-32gb-memory-and-evidence-reliability|MTPLX 32GB Memory and Evidence Reliability]] — Captures two distinct reliability concerns for MTPLX on this box: 131K memory overcommit, and postcommit artifacts that can't be treated as finished TurboFit ev
- [[topics/turbofit/wiki/concepts/mtplx-context-overcommit|MPTX Context Overcommit]] — On the 32 GB Mac, `mtplx serve` with `--context-window 131072` loads the model in 6-9s and installs the native MTP draft head, but the printed memory plan marks
- [[topics/turbofit/wiki/concepts/mtplx-foreground-preemption|MPLX Foreground Preemption]] — When MTPLX handles long-running Hermes foreground work, postcommit records show `cross_session_foreground_preempted` and `foreground_preempted_postcommit`, and 
- [[topics/turbofit/wiki/concepts/turbofit-session-mismatch|TurboFit Session Mismatch]] — MTLPX generation events show foreground/preemption behavior and session-store mismatch that make some TurboFit captures unreliable as finished-state evidence ^[

## Decisions
- [[topics/turbofit/wiki/decisions/aux-model-selection|Aux Model Selection]] — Auxiliary and compression routing is Maple MLX on `127.0.0.1:11612`, 131k context, served with `deepgrove-ai/mlx-lm-deepgrove` ^[raw/inbox/2026-09-06.md].
- [[topics/turbofit/wiki/decisions/candidate-quant-preference|Candidate Quant Preference]] — **Decision/Preference:** When comparing GGUF vs MLX for new local candidates, prefer the Q3 quant when model pages describe it as near base-model quality.
- [[topics/turbofit/wiki/decisions/context-sizing|Context Sizing]] — Local TurboFit contexts are set to 131,072 tokens for both main and aux ^[raw/inbox/2026-09-06.md].
- [[topics/turbofit/wiki/decisions/context-window-decision|Context Window Decision]] — **Decision**: Lock in 65K context as the stable daily driver on M1 MacBook 32GB, with 131K reserved for rare long-context needs where speed is not critical.
- [[topics/turbofit/wiki/decisions/fallback-model-order|Fallback Model Order]] — The active model preference order should preserve explicit user choice and avoid silently switching to `stepfun/step-3.7-flash:free` ^[raw/inbox/2026-09-06.md].
- [[topics/turbofit/wiki/decisions/local-main-provider|TurboFit Local Main Provider Decision]] — What Chris wanted: the smartest feasible local runtime as Hermes main, with verified evidence, not just Hermes internal logs.
- [[topics/turbofit/wiki/decisions/main-model-selection|Main Model Selection]] — Initial decision: Main inference and vision is Unleashed 27B + DFlash2 draft on `127.0.0.1:11606`, Metal, 131k context ^[raw/inbox/2026-09-06.md].
- [[topics/turbofit/wiki/decisions/mtplx-main-provider|MT_PlX Main Provider]] — Make `Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed` via `mtplx serve` the main TurboFit provider and remove Maple/Unleashed as co-resident models to reclaim disk
- [[topics/turbofit/wiki/decisions/ornith-config-routing|Ornith Config Routing]] — **Action**: Repoint Hermes `custom:turbofit` to the running Ornith MLX server on `http://127.0.0.1:11613/v1` and set `ornith-1-5-35a3b-mlx` as the default model
- [[topics/turbofit/wiki/decisions/unleashed-backup|Unleashed Backup]] — Keep Unleashed Q3_K_XL as the safe long-context backup when MTPLX overcommits memory or Hermes reloads fail.

## Comparisons
- [[topics/turbofit/wiki/comparisons/aux-runtime-options|Aux Runtime Options]] — | Runtime | Result | Reason |
- [[topics/turbofit/wiki/comparisons/candidate-quant-and-format-comparison|Candidate Comparison — Ornith, Nail, Tiel-Coder, Dirk]] — "They also have a lot to say about their quants on their pages too, check GGUF vs MLX, I like the Q3 quant that they said is near base model quality" ^[raw/inbo
- [[topics/turbofit/wiki/comparisons/main-runtime-speed|Main Runtime Speed Comparison]] — Evidence-observed main-runtime candidates for Qwen 3.8 27B-class workloads on this 32 GB M1 Mac. Numbers are in-session measurements against downloaded/observed

## Queries
- [[topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Apple Silicon Runtime Benchmark]] — From [[raw/inbox/2026-09-07.md|2026-09-07 03:06]]: Chris asked to "Research and test ALL available Apple Silicon inference engines for Qwen 3.8 27B to find the 
- [[topics/turbofit/wiki/queries/duplicate-page-candidates|Duplicate Page Candidates]] — Detected by title/source scan after the 2026-09-07 compile.
- [[topics/turbofit/wiki/queries/engine-research-request|Engine Research Request]] — Chris asked for research and testing of all available Apple Silicon inference engines for Qwen 3.8 27B to find the fastest configuration ^[raw/inbox/2026-09-07.
- [[topics/turbofit/wiki/queries/engine-speed-report|Engine Speed Report]] — This is the live result surface of Chris's research request for Apple Silicon engine speed testing.
- [[topics/turbofit/wiki/queries/evidence-capture-and-reliability|Evidence Capture and Reliability Query]] — Captures the open verification work after configuring Ornith as main, and the contested state where Hermes showed persistent timeouts after config repoint.
- [[topics/turbofit/wiki/queries/maple-metal-compat|Maple Metal Compatibility]] — Can Maple serve stable long-context compression workloads on Apple Silicon Metal without repeated OOM, or is a non-server execution path required?
- [[topics/turbofit/wiki/queries/mplx-integration|MPLX Integration]] — Can MPLX be added as a fast local TurboFit provider alongside Unleashed 27B without evicting the main model, and what is the memory ceiling under MTP?
- [[topics/turbofit/wiki/queries/ornith-cleanup-focus|Ornith Cleanup Focus Request]] — Chris wanted Ornith prioritized over Bonsai, Colibri, and music-generation side paths. His exact instruction was, "It just needs to be configured into turbofit 
- [[topics/turbofit/wiki/queries/turbofit-mtplx-coexistence|TurboFit MTPLX Coexistence]] — | Scenario | Result | Notes |


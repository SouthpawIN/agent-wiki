# BRIEF — turbofit
_Pre-prompt for the cutter and this topic's agent. Chris edits freely; lines ending `<!-- chris -->` are never rewritten._

## What this topic is
> Adaptive local inference for Hermes — TurboFit Check, evidence-built TurboFit List, repaired discovery/benchmark campaigns, Qwen 3.8 DFlash2, Bonsai DSpark, FreeToken, and Sirvir.

## Belongs here (scope)
- Anything about: turbofit
- Decisions, preferences, pains, tools, people and timelines tied to the above

## Does NOT belong here (anti-scope → route elsewhere)
- General Hermes/fleet coordination → `senter` · the wiki UI itself → `senter-wiki` · video/YouTube → `youtube`
- If a cut mentions another topic by name (music, anser, omnisenter-models, legacy-bots, pocket-shop, nous-community…) more than this one, it goes there

## Aliases (the cutter binds hard on these words)
- turbofit

## Lens — how to read new context for this topic
- What is Chris trying to achieve here, in his words? What changed since the last pass?
- Which statements are DECISIONS (dated, with why), which are PREFERENCES, which are PAINS, which are open QUESTIONS?
- What did he say twice? (repetition = a skill or a rule)

## Standing preferences (apply to every suggestion)
- Root causes, never band-aids. Everything live and visible. Markdown + built-in Hermes over custom code.
- Bots first, then loops; reuse a fleet bot when one fits; skills auto-apply. No pitches about the build process itself.

## What a good suggestion looks like here
- One line, phrased as a question Chris can say yes to, tied to a quote from him, naming the bot that would do it.

## Learned (agent-appended, newest first)
- 2026-09-08 · 2026-09-08 · Hermes auto route stability problem identified: `model.default` must be first in fallback chain and `auxiliary.compression.provider` must be pinned to local TurboFit route to prevent silent switches to cloud models.
- 2026-09-07 · Canonicalized TurboFit MTPLX performance evidence under `turbofit-mtpl-performance`; retired duplicate `turbofit-mtp-performance` as redirect stub.
- 2026-09-07 · Added `mtplx-32gb-memory-and-evidence-reliability` from live `prefill_admission_shed` event and postcommit mismatch evidence.
- 2026-09-07 · Reconciled `ornith-35b-mlx` with contested routed state: Hermes timeouts recurred until restart; no verified live completion after repoint.
- 2026-09-07 · Updated `nail-qwen36-35b` long-context status: 131K deferred because 20.8 GB weights plus ~8 GB KV exceeds stable 32 GB fit.
- 2026-09-07 · MTPLX live memory-guard telemetry now shows exact threshold behavior: prefill_admission_shed clears KV cache to stay under ~24.99 GB threshold on a 25.77 GB limit, corroborating existing 32GB/131K overcommit findings.
- 2026-09-07 · Chris explicitly marked progressive-disclosure preference: the ideal Senter surface is one wiki with frontmatter-listed skills/bots/loops, with a librarian progressively discovering deeper detail — this belongs on the `senter` topic, not turbofit.
- 2026-09-07 · Ornith routing is configured in Hermes but live timeouts recurred until a session/gateway restart; promotion remains contested.
- 2026-09-07 · Nail, Dirk, and Tiel-Coder benchmark evidence consolidated: Nail wins at 32K (23.4 tok/s), Dirk OOMs above 32K, Tiel-Coder viable at 65K (23.1 tok/s).
- 2026-09-07 · Hermes model switched to non-local runtimes multiple times without Chris initiating the changes; route stability is a pain, not a preference.
- 2026-09-07 · Skill turbo-model-store-cleanup records the exact workflow for freeing ~/Models/storage/ before and after candidate sweeps.
- 2026-09-07 · Nail, Dirk, and Tiel-Coder are queued as additional local candidates, not just Ornith/Unleashed/MTPLX.
- 2026-09-07 · Chris prefers the Q3 quant when HuggingFace page notes place it near base model quality.
- 2026-09-07 · Several downloaded candidates were deferred from 131K testing because their size plus KV cache exceeds stable 32 GB fit before benchmark.
- 2026-09-07 · Chris explicitly wants GGUF vs MLX compared for new candidates and prefers the Q3 quant when page notes place it near base quality.
- 2026-09-07 · Stable 65K is the safe daily context on this box; 131K remains a long-context fallback despite throughput collapse.
- 2026-09-07 · DFlash2's `--draft-ngl`, `--draft-ctx-size`, `--low-vram` flags are invalid in dflash2-llama.cpp fork; the flag set differs from stock llama.cpp
- 2026-09-07 · MTPLX `--memory-budget` CLI flag is rejected; use environment variable instead
- 2026-09-07 · Ornith 1.5-35B-A3B MLX 4-bit is fastest for short-context (28.5 tok/s) but KV cache kills throughput at 131K
- 2026-09-07 · Ornith-1.5-35B-A3B MLX 4-bit is the fastest local short-context candidate on this box at 28.5 tok/s for 500-token prompts, but drops to ~0.5 tok/s at 131K and is not a stable long-context main on 32 GB.
- 2026-09-07 · Unleashed `UD-IQ3_XXS` failed to load in the DFlash2 fork with `tensor ... not within the file bounds` after `dflash requires ctx_other to be set`; keep `Q3_K_XL` as the stable Unleashed backup.
- 2026-09-07 · DFlash2 is runtime-bound: usable with `dflash2-llama.cpp` fork via `--model-draft`, but invalid flag combinations (`--draft-ngl`, `--draft-ctx-size`, `--low-vram`, `--draft-model`) fail before bind; MTPLX cannot use DFlash2 because it uses native MLX MTP heads.
- 2026-09-07 · `mtplx serve` rejects `--memory-budget`; the intent should move to supported runtime config or env-driven tuning, not CLI flags.
- 2026-09-07 · MTPLX `--context-window 131072` is overcommitted on this 32 GB box; stable live generation is contested until a Hermes window capture confirms throughput without preemption or cache shedding.
- 2026-09-07 · Foreground preemption plus retokenized-history mismatch make standalone MTPLX postcommit artifacts unreliable as finished TurboFit evidence without a real Hermes window capture.
- 2026-09-07 · Unleashed Q3_K_XL remains the safe long-context backup when MTPLX overcommits or Hermes reloads fail.
- 2026-09-07 · Maple MLX aux path requires the deepgrove-ai fork; generic mlx_lm server OOMs on this box under load.
- 2026-09-07 · Ornith MLX 4-bit locked as main provider at 131K context with full turbofit integration; 29 tok/s short, 226 tok/s 5K prompt verified after session restart.
- 2026-09-07 · Model switches traced to fallback_providers ordering and auxiliary.compression.provider:auto; default must stay first and compression must be pinned.
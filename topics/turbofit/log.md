# TurboFit — Wiki Log

Chronological record of all wiki compiles and changes.

## [2026-08-27] (later): initial enable
- turbofit Hermes plugin enabled + verified; configure-tool hang root-caused (missing huggingface_hub) as fix #7; Hermes config set primary custom:turbofit/auto + Nous free fallbacks; restart pending.

## [2026-09-06] turbofit workday
- Initial state: Unleashed 27B + DFlash2 at 131K was the main model; Maple was aux for compression.
- Model switching pain documented: multiple unrequested provider changes observed.

## [2026-09-07] compile | 2026-09-07 raw/inbox/2026-09-07.md → full session compile

### New pages created

**Entities:**
- [[topics/turbofit/wiki/entities/bonsai.md|Bonsai MLX]] — Prism ML Bonsai variants (1-bit, 2-bit ternary at 7.91 GB) downloaded but failed to start; deprioritized by Chris.
- [[topics/turbofit/wiki/entities/colibri.md|Colibri]] — Custom Maple format model, incompatible with standard mlx_lm server; requires custom Maple code.

**Concepts:**
- [[topics/turbofit/wiki/concepts/bonsai-colibri-deprioritization.md|Bonsai and Colibri Deprioritization]] — Chris's explicit redirect from Bonsai/Colibri to Ornith between 13:18-13:30; three near-identical raw messages showing the directive.

### Pages updated

- [[topics/turbofit/wiki/entities/ornith-1-5-35b-a3b-mlx-4-bit.md|Ornith 1.5 35B-A3B MLX 4-bit]] — Added provenance to status section; updated decision trail with timeout evidence at 2026-09-07T19:26:47.525Z; cited Chris's 14:25 directive.
- [[topics/turbofit/wiki/entities/ornith-35b-mlx.md|Ornith 35B MLX]] — Updated to link to the newer 4-bit entity page; clarified contested routing state.
- [[topics/turbofit/wiki/entities/ornith-config-routing-failure.md|Ornith Config Routing Failure]] — Updated observed evidence with timestamped session change at 14:25; clarified status as contested pending restart.
- [[topics/turbofit/wiki/queries/evidence-capture-and-reliability.md|Evidence Capture and Reliability Query]] — Expanded questions with answers needed; added canonical approval path.
- [[topics/turbofit/wiki/queries/engine-speed-report.md|Engine Speed Report]] — Added performance status indicators; documented contested promotion pending Hermes restart.
- [[topics/turbofit/wiki/concepts/hermes-model-switching-noise.md|Hermes Model Switching Noise]] — Added detailed switch chain with timestamps; cited Chris's preference for Ornith.

### Pages consolidated/redirected

- `[[turbofit-mtp-performance]]` → `[[turbofit-mtpl-performance]]` (canonical), legacy kept as redirect stub.

## [2026-09-07 00:56] turbofit configuration

Initial attempt: MTPLX at 131K → unstable under load (OVERCOMMITTED, exit code -9).

## [2026-09-07 01:00] mtplx stable at 65K

MTPLX Qwen 3.8 27B Optimized Speed locked in as main provider at 65K context with 7-12 tok/s throughput.

## [2026-09-07 03:03] switched to Unleashed+DFlash2

After MTPLX 131K instability, switched to Unleashed+DFlash2 for long context (~5 tok/s).

## [2026-09-07 06:18] Ornith locked in

Ornith MLX 4-bit selected as winner and main provider after speed tests showing 28.5 tok/s short, 5.7 tok/s 5K, ~0.5 tok/s at 131K.

## [2026-09-07 08:23] Bonsai testing paused

Chris: "Current immediate goal: clean up obsolete 27B model files, then test Bonsai vs Maple Colibri vs Ornith 1.5 35A3B at 131K context."

## [2026-09-07 10:08] final model comparisons

| Model | Type | Context | Short | 5K | Status |
|-------|------|---------|-------|-----|--------|
| **Ornith MLX 4-bit** | MoE 35B | **131K** | **28.5 tok/s** | **5.7 tok/s** | ✅ |
| Nail Q4_K_XL | MoE 35B | 32K | 23.4 tok/s | 4.7 tok/s | ⚠️ OOM at 131K |
| Tiel-Coder Q4_K_XL | MoE 35B | 65K | 23.1 tok/s | 4.2 tok/s | ⚠️ Not fit at 131K |
| Dirk Q3_K_XL | Dense 27B | 32K | 6.0 tok/s | 0.8 tok/s | ⚠️ OOM above 32K |

Ornith confirmed winner: only model that works at 131K with fastest speeds.

## [2026-09-07 11:25-11:59] Bonsai/Colibri exploration

Subagents downloaded Bonsai MLX 2-bit (7.91 GB) and Ternary; Colibri had custom format issues. Bonsai MLX server failed with missing `config.json`. 

## [2026-09-07 13:18-13:30] Chris's redirect

Three near-identical raw messages at 13:18, 13:20, 13:30: "It just needs to be configured into turbofit so I can continue with Ornith. Don't worry about bonsai. I said the model that we're using is too dumb, okay? So we need to focus entirely on getting Ornith up."

## [2026-09-07 14:25-14:30] Ornith active, timeout recurred

- 14:25: Chris switched to Ornith MLX; session metadata confirms `ornith-1-5-35a3b-mlx via provider turbofit`.
- 14:30: Model switching noise detected; system reverted to Nous free tier.
- 14:42: Chris re-switched to Ornith; Hermes accepted the change.

## [2026-09-07 19:26:47] contested state

Persistent `Connection error` timeout at provider layer after config repoint. A Hermes session/gateway restart is required to clear stale connection state.

## Summary of final state (as of 2026-09-07)

**Ornith 1.5 35B-A3B MLX 4-bit:**
- Config: `custom:turbofit` → `http://127.0.0.1:11613/v1`
- Default model: `ornith-1-5-35a3b-mlx`
- Context: 131K
- Speed: 28.5 tok/s short, 5.7 tok/s at 5K
- Status: Configured but contested (timeout evidence post-repoint)

**Cleanup completed:**
- Removed: Maple, Unleashed, MTPLX, Nail, Tiel-Coder, Dirk, Colibri candidate directories
- Kept: Ornith MLX as sole active provider

**Pending verification:**
- Required: Hermes session restart to clear provider timeout state
- Required: Real Hermes window capture of Ornith completing a request as verified evidence
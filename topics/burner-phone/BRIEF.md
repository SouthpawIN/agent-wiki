# BRIEF — burner-phone
_Pre-prompt for the cutter and this topic's agent. Chris edits freely; lines ending `<!-- chris -->` are never rewritten._

## What this topic is
> Skill to control an Android device with an agent

## Belongs here (scope)
- Anything about: burner phone, burner-phone
- Decisions, preferences, pains, tools, people and timelines tied to the above

## Does NOT belong here (anti-scope → route elsewhere)
- General Hermes/fleet coordination → `senter` · the wiki UI itself → `senter-wiki` · video/YouTube → `youtube`
- If a cut mentions another topic by name (music, anser, omnisenter-models, turbofit, legacy-bots, pocket-shop…) more than this one, it goes there

## Aliases (the cutter binds hard on these words)
- burner phone
- burner-phone

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
- 2026-09-17 · 2026-09-16 · Chris moved from trial 507s to a fit-calculation approach over 28GB: model_size + KV_cache <= tier_size; comfortable-fit model_size + 2GB <= tier_size; KV at real context length; check EVERY tier (CPU + Unified).
- 2026-09-15 · 2026-09-15 · Build runtimes in a persistent location, not `/tmp` — the qwen4 v0.4.0-dev build was wiped on restart and lost.
- 2026-09-15 · 2026-09-15 · DFlash2 integration flag `--hf-repo-draft` recorded; integration against the qwen4 v0.4.0-dev service (`-ngl -c -t`) still unverified after an empty response (reasoning consumed the budget).
- 2026-09-15 · 2026-09-15 · `-ngl 9999` root cause = `CUDA_VISIBLE_DEVICES=1` not honored through `su` (env var + su handling both targeted).
- 2026-09-15 · 2026-09-15 · Omarchy 27B confirmed working (echo '2+2 equals 4, no more'); local runtime probe continues on Ornith.
- 2026-09-15 · 2026-09-15: DFlash2 speculative-decoding integration requires both `--spec-draft-model` (full model) and `--ctx-other`; the original working service is a qwen4 llama.cpp v0.4.0-dev build with `-ngl -c -t` flags.
- 2026-09-09 · 2026-09-08 raw/inbox contained only Hermes internal tooling/state noise; treat as non-content until substantive burner-phone raw appears.
- 2026-09-08 · 2026-09-08 raw/inbox contained only Hermes internal tooling/state noise (pseudocode for `data-k` JS edits, server restart chatter, sim 0.07–0.09); zero substantive burner-phone content — treat as non-content.
- 2026-09-08 · Ornith/DFlash2/507 work continues to be the live burner-phone thread; next real compile is gated on new substantive raw (per BRIEF, treat as noise).
- 2026-09-07 · 2026-09-07 · Colibri does not work with the MLX server format; Ornith is the only viable local runtime path in this setup.
- 2026-09-07 · 2026-09-07 · Ornith config/port state is now tracked separately as ornith-config-state.md, including port conflict and Hermes patch/write blockage.
- 2026-09-07 · Ornith is the selected local runtime, but needs proper startup and config update.
- 2026-09-07 · DFlash2 is downloaded but not yet integrated with Ornith for speculative decoding.
- 2026-09-07 · The 507 context error was reproduced with 18GB model + 8GB KV; finding actual limits is pending.
- 2026-09-07 · Chris wants to find maximum context that fits on 28GB hardware.
- 2026-09-07 · 2026-09-07 · Ornith CPU fallback (-ngl 0) works after a timeout; 131K context test is pending a full rerun.
- 2026-09-07 · Ornith MLX and DFlash2 are active local runtime targets; Ornith measured 28.5 tok/s 4-bit, DFlash2 downloaded as 1GB speculative-decoder artifact.
- 2026-09-07 · New explicit lookup request: ornith 1.5 35A3B for the burner-phone device and DFlash2.
- 2026-09-07 · Ornith CPU fallback (-ngl 0) works after a timeout; 131K context test is pending a full rerun.
- 2026-09-07 · Chris's local 507 failure mode is framed as a physical-capacity/context-fit problem, not a network error; prefer root-cause model/KV/context limits over band-aids.
- 2026-09-07 · Active goal phrase to anchor bot/loop suggestions: "find the actual maximum context that fits."
- 2026-09-16 · Chris moved from trial 507s to a fit-calculation approach over 28GB hardware: model_size + KV_cache <= tier_size; comfortable-fit model_size + 2GB <= tier_size; KV at real context length; check EVERY tier (CPU + Unified).

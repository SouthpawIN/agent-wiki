---
title: back-where
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# back-where

Last updated: 2026-09-17 | Total pages: 40

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [Context compaction handoff repetition (2026-09-09)](wiki/compaction-handoff-repetition.md) — The context compaction handoff instruction first appeared in the 2026-09-08 session transition and repeated identically in the 2026-09-09 raw filing. The handof
- [FreeToken rejected as NVIDIA-only](wiki/freetoken-rejected-nvidia-only.md) — **FreeToken** was investigated and rejected because it supports only NVIDIA RTX 30/40/50 hardware and will not run on Chris's Mac. The decision was made explici
- [GSQ RCO IQ3S picked and Bonsai MLX snapshot pending](wiki/gsq-rco-iq3s-and-bonsai-mlx-snapshot.md) — On 2026-09-16 Chris selected the **GSQ RCO IQ3S** as the working quant, displacing the earlier Q3K exile preference. His reasoning bundled accuracy, power, cont
- [Hardware headroom note for M1 32GB](wiki/hardware-headroom-note.md) — Chris treated the 32GB M1 MacBook as available headroom rather than a hard ceiling during recovery. He said the machine should have enough space to run an audit
- [Hermes commit-completion stub (2026-09-09)](wiki/hermes-commit-completion-stub.md) — The watcher captured a truncated Hermes internal log line after a commit step, ending mid-sentence at a sim score of 0.08.
- [Hermes fallback causes](wiki/hermes-fallback-causes.md) — The runtime loaded a backup model instead of the explicitly chosen one, and later records showed automatic model changes during the session.
- [Hermes model download in progress](wiki/hermes-model-download-in-progress.md) — - **01:32**: Download started for a 13GB model file
- [HP laptop boot flash and Steam Play setup](wiki/hp-boot-flash-steamplay.md) — During mid-September Chris was flashing and booting a new OS onto an **HP laptop** and running into bootloader and Steam setup questions along the way. This is
- [Interrupted Calibri and Bonsai request](wiki/interrupted-calibri-bonsai-request.md) — A session turn was interrupted before completion at 11:35. The partial intent had to be examined for follow-up.
- [M1 Mac performance expectation](wiki/m1-mac-performance-expectation.md) — Chris asserted the host hardware should handle the workload: an M1 MacBook with 32 GB RAM running a model smaller than 27b, with no extra limitations imposed.
- [Model picker persistence until fallback](wiki/model-picker-persistence.md) — Chris expects a model chosen from the model picker to remain active until it needs to fall back. Selecting a model is treated as a durable binding, not a transi
- [OBS streaming from the Omarchy for Armored Core 6](wiki/obs-streaming-omarchy-armored-core.md) — On 2026-09-14 Chris described wanting to manage a gaming stream from the MacBook:
- [Q3K XL / Unleashed chosen as the game-adjacent model for a double-GPU device](wiki/q3k-xl-double-gpu-gaming-choice.md) — On 2026-09-15 Chris clarified *why* he settled on the Q3K XL / Unleashed model rather than it being a pure speed choice: he wants a model that co-runs alongside
- [Qwen3.8 27B unleashed model selection](wiki/qwen3-8-27b-unleashed-selection.md) — Chris identified the Qwen3.8 27B "unleashed" variant as the preferred model, specifically seeking Q3 quantization for optimal performance. He emphasized researc
- [recovery-background-process](wiki/recovery-background-process.md) — A background process exited mid-run during recovery, interrupting an in-flight turn. Chris’s note implies some work may already be complete on disk and should b
- [Retained outputs folder for rejected 131K audition](wiki/retained-outputs-folder.md) — After deciding the 131K Qwen3.8 27B unleashed audition was too slow, Chris explicitly asked for the generated outputs to be saved in a folder rather than delete
- [SSH credential sharing (2026-09-13)](wiki/ssh-credential-sharing.md) — At 10:09 on 2026-09-13 Chris walked through an SSH password for a machine, spelling out the literal characters ("A's and the ones," L's replaced by 1's, final I
- [Token startup race condition](wiki/token-startup-race.md) — During UI restoration, a token was being read but the server was still rejecting it. Hermes traced the likely cause to a startup race: the server had not fully
- [TurboFit options missing after restarting the desktop app](wiki/turbofit-options-missing-after-restart.md) — On 2026-09-15 Chris restarted the Hermes desktop app on the MacBook and found the **TurboFit** options gone — they did not come back after the restart. ^[raw/in
- [UI layout regression after diff view change](wiki/ui-layout-regression.md) — Chris asked for a small change — show diffs — and instead elements shifted to the right and then worsened to a black screen. He explicitly stated the UI ended u
- [UI restoration verification check (2026-09-08)](wiki/ui-restoration-verification-check.md) — A later session turn reported UI restoration complete and moved into verification.

### Concepts

- [Device embodiment and identity](wiki/device-embodiment.md) — Chris framed every connected device — the MacBook, his phone, and the Surface Duo 2 — as the *embodiment* of Hermes itself rather than tools he merely operates.
- [End-to-end verification before declaring done](wiki/end-to-end-verification.md) — Every fix must be tested through the actual Hermes surface and verified before being called complete. He explicitly rejected claims of success based only on int
- [Prefill timeout triggering model fallback](wiki/model-prefill-fallback.md) — Chris observed that the runtime swapped models during the session. He concluded the cause was prefill taking too long, not true incompatibility, and wanted a co
- [Ornith 1.5 as a smarter-model goal](wiki/ornith-1-5-goal.md) — Chris stated a goal — that there should be an **Ornith 1.5** on the system that is "actually smarter than the model we are using now." ^[raw/inbox/2026-09-13.md
- [Ornith startup priority](wiki/ornith-startup-priority.md) — During recovery, Chris explicitly requested that Ornith be started before addressing Calibri and Bonsai. This appeared as a pre-requisite request when previous
- [Quantization selection by hardware tier](wiki/quantization-by-tier-philosophy.md) — On 2026-09-16 Chris laid out a tier-based rule for choosing quantization: there is no single best quant, only the optimal quant *for each hardware tier*. The jo
- [Recovery repair plan](wiki/recovery-repair-plan.md) — The session moved from repeated failure retries to a vault-spec rebuild. The operative rule was to stop touching files until the target was rebuilt from the vau
- [TTS cache-freshness failure](wiki/tts-cache-freshness.md) — TTS entitlement checks used stale cached account info or a JWT that was minted before the $2,000 credit top-up, so entitlement remained negative even after paym
- [TTS failure during credit outage](wiki/tts-credit-outage.md) — TTS stopped working because the image-analysis model ran out of credits. Chris noted that a $2,000 top-up had been added, so enough balance should exist, yet TT

### Decisions

- [131K audition rejection and speed target](wiki/131k-audition-rejection.md) — After running an audition of the 131K unleashed 27B model configuration, Chris explicitly rejected the result as too slow. The generated outputs were retained i
- [Auxiliary model binding with no extra limitations](wiki/auxiliary-model-binding.md) — Chris decided that assigning a model as auxiliary should not be blocked by additional constraints. He explicitly said he gave no limitations beyond that role.
- [Explicit completion and block criterion](wiki/completion-criterion-explicit-statement.md) — Chris defined an explicit criterion for how Hermes should signal the end of a task: completion must be stated explicitly and then stop, or blockage must be stat
- [Config-editing and permission authorization](wiki/config-editing-permission-authorization.md) — On 2026-09-13 Chris explicitly authorized Hermes to edit permission configs and to send permissions his way when a gate is hit, saying this is how every permiss
- [$2,000 credit top-up for TTS restoration](wiki/credit-top-up-tts-restoration.md) — Chris added $2,000 in credits to restore TTS functionality, which had failed after the image-analysis model exhausted its allocation. The payment was made, but
- [GSQ RCO IQ3S selection preference](wiki/gsq-rco-iq3s-selection-preference.md) — On 2026-09-16 Chris moved his quantization preference from Q3K exile to the **GSQ RCO IQ3S** quant, pending proof that it is genuinely near task-lossless. ^[raw
- [Qwen3.8 27B optimization priority](wiki/qwen3-27b-optimization-priority.md) — After rejecting the 131K speed audition for being too slow, Chris explicitly redirected priority to optimizing one of the 27B models instead of continuing the 1

### Queries

- [20.8GB download completion and loadability verification](wiki/20-8gb-download-completion-verification.md) — Multiple download status lines appeared in one topic run: a ~13GB model file reported nearly complete, an IQ3_XXS download later reported incomplete at ~4.7GB o
- [Model performance on M1](wiki/model-performance-on-m1.md) — What exact batch-size or prefill-capacity change is needed so the chosen model can load at Q3 with 262k contacts and D flash 2 without falling back due to prefi
- [Restoration and billing](wiki/restoration-and-billing.md) — 1. Where did the $2,000 credit payment go in Portal billing, and why is TTS still unavailable?

---

## SKILLS

Topic skills stored in this wiki:

- **[27b-m1-tuning-research](skills/27b-m1-tuning-research/SKILL.md) — 1. Read the HuggingFace/Unleashed page for the Qwen3.8 27B variant before touching settings.
- **[hermes-python-env-isolation](skills/hermes-python-env-isolation/SKILL.md) — execute_code runs in a separate Python kernel with different sys.path than command-line. When fixes don't propagate, verify from the command line dire
- **[latest-message-wins-task-handling](skills/latest-message-wins-task-handling/SKILL.md) — 1. Read the latest user message after any snapshot/summary block.
- **[qwen-research-first-implementation](skills/qwen-research-first-implementation/SKILL.md) — 1. Identify the exact model variant and quantization from the HuggingFace model page and the unleashed page.
- **[recovery-repair-pattern](skills/recovery-repair-pattern/SKILL.md) — 1. Stop touching files immediately after a crash or regression
- **[research-first-27b-model-implementation](skills/research-first-27b-model-implementation/SKILL.md) — 1. Identify the exact model variant and quantization family Chris named.
- **[session-handoff-latest-message-wins](skills/session-handoff-latest-message-wins/SKILL.md) — Apply when `[CONTEXT COMPACTION — REFERENCE ONLY]` appears. Act only on messages after the handoff summary. Reverse signals: stop, undo, roll back, ju
- **[tts-fresh-entitlement-retry](skills/tts-fresh-entitlement-retry/SKILL.md) — When TTS entitlement resolution fails with an entitlement/cache error:

---

## BOTS

Proposed bots:

- **[27b-optimizer](agents/27b-optimizer.md.proposed) — **I see you're refocusing on the 27B models after the 131K speed miss — want a bot that finds the fastest viable Q3 27B configuration on this M1?**
- **[back-where-bot](agents/back-where-bot.md.proposed) — Owns the `back-where` topic: runs its skills, answers for it, proposes its loops.
- **[m1-27b-audit-bot](agents/m1-27b-audit-bot.md.proposed) — **I see you're trying to validate the 27B/unleashed path on M1 — want a bot that checks Hermes runtime binding, model-list state, and the local downlo
- **[m1-27b-prep-bot](agents/m1-27b-prep-bot.md.proposed) — **I see you're focused on getting one of the 27B models optimized on M1 — want a bot that uses the retained 131K outputs and current download state to
- **[m1-27b-tuner](agents/m1-27b-tuner.md.proposed) — **I see you're trying to make the 27B Q3 path usable at 131K — want a bot that tunes local llama.cpp/prefill settings for that exact profile instead o
- **[obs-omarchy-stream-bot](agents/obs-omarchy-stream-bot.md.proposed) — **I see you want OBS on the MacBook to manage streaming while you play Armored Core 6 on the Omarchy, and that's still pending — want a bot that build
- **[state-recovery-bot](agents/state-recovery-bot.md.proposed) — **I see you're trying to get the UI and model state back after diffs broke it — want a bot that snapshots and restores last known good layout and mode
- **[steam-play-hp-bot](agents/steam-play-hp-bot.md.proposed) — **I see you're mid-OS-setup on the HP with Steam Play (Proton) 'having a hard time' — want a bot that drives the HP's Steam/Proton troubleshooting end
- **[teknium](agents/teknium.md.proposed) — **I see you're talking about restoring the Hermes UI to center and making model choice stick — want teknium to fix the layout regression and enforce d
- **[turbofit-watch-bot](agents/turbofit-watch-bot.md.proposed) — **I see your TurboFit options disappear every time you restart the desktop app — want a bot that checks they're still there after a restart and restor


---

## LOOPS

Proposed loops:

- **[27b-speed-target-loop](loops/27b-speed-target-loop.md.proposed) — owner: teknium · cadence: human phrase · status: SUGGESTED
- **[27b-speed-watch](loops/27b-speed-watch.md.proposed) — owner: turbosovth · cadence: human phrase · status: SUGGESTED
- **[download-completion-watch](loops/download-completion-watch.md.proposed) — owner: looker · cadence: human phrase · status: SUGGESTED
- **[looker](loops/looker.md.proposed) — owner: looker · cadence: per verification pass · status: SUGGESTED
- **[weaver](loops/weaver.md.proposed) — owner: weaver · cadence: per session · status: SUGGESTED

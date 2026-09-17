# Queue — back-where

## [CONTEXT]
- [ ] research gsq-task-lossless-verification — SUGGESTED 2026-09-17 01:31: You picked the GSQ RCO IQ3S because the vendor claims 0 task loss versus FP16 — want me to look into whether that claim 
- [ ] research turbofit-persistence-research — SUGGESTED 2026-09-15 19:01: Want me to look into why your TurboFit options don't survive a desktop-app restart — and how to make them persist?
- [ ] research double-gpu-co-run-tuning — SUGGESTED 2026-09-15 10:43: Want me to look into what batch-size, GPU split, and prefill settings let the Unleashed Q3K XL stay at Q3 on your double
- [ ] research stream-omarchy-to-macbook-obs — SUGGESTED 2026-09-15 10:02: Want me to look into how to stream from the Omarchy into OBS on the MacBook — network stream, USB capture, or VNC — so t
- [ ] research proton-for-armored-core-6 — SUGGESTED 2026-09-15 10:02: Want me to look into the best Steam Play/Proton build for Armored Core 6 so we're chasing the right version instead of g
- [ ] research qwen3-27b-unleashed-runtime-research — SUGGESTED 2026-09-07 19:51: Want me to look into whether the Qwen3.8 27B unleashed Q3K exile variant has an MLX/runtime path on M1 and what config g
- [ ] research q3k-exile-artifact-research — SUGGESTED 2026-09-07 16:10: Want me to look into the exact Qwen3.8 27B unleashed Q3K exile artifact names, deep flash options, and llama.cpp/MLX set
- [ ] research qwen3-27b-unleashed-m1-tuning-path — SUGGESTED 2026-09-07 09:54: Want me to look into the exact llama.cpp or MLX config to run Qwen3.8 27B unleashed Q3K exile at 131K on your M1 32GB wi
- [ ] research 27b-m1-tuning — SUGGESTED 2026-09-07 06:44: Want me to look into what batch-size/prefill tuning makes Qwen3.8 27B Q3 hit ~113 tok/s on M1 with 262k contacts?
- [ ] research qwen3-27b-unleashed-page-scan — SUGGESTED 2026-09-07 05:22: Want me to look into the Qwen3.8 27B unleashed and HuggingFace pages before the next 27B run?
- [ ] research qwen3-8-27b-unleashed-research — SUGGESTED 2026-09-07 03:41: Want me to look into the Qwen3.8 27B unleashed Q3/flash setup that actually fits this M1?
- [ ] research looker — SUGGESTED 2026-09-07 03:01: Want me to look into the exact batch-size or prefill-capacity change needed for Q3 quantization of the 27B model with 26
- [ ] research m1-prefill-tuning — SUGGESTED 2026-09-06 22:58: Want me to look into the exact batch-size and prefill settings needed to run the chosen model at Q3 with 262k contacts a
- [ ] research billing-and-tts-trail — SUGGESTED 2026-09-06 03:42: Want me to look into the Portal billing record for the $2,000 top-up and map it to TTS credit availability?
- [~] research — dispatched 2026-09-06 01:25

## [SKILLS]
- [ ] hermes-python-env-isolation — distilled 2026-09-10 12:20 → skills/hermes-python-env-isolation/SKILL.md (auto-applied)
- [ ] session-handoff-latest-message-wins — distilled 2026-09-10 12:20 → skills/session-handoff-latest-message-wins/SKILL.md (auto-applied)
- [ ] recovery-repair-pattern — distilled 2026-09-08 09:50 → skills/recovery-repair-pattern/SKILL.md (auto-applied)
- [ ] latest-message-wins-task-handling — distilled 2026-09-07 19:51 → skills/latest-message-wins-task-handling/SKILL.md (auto-applied)
- [ ] qwen-research-first-implementation — distilled 2026-09-07 16:10 → skills/qwen-research-first-implementation/SKILL.md (auto-applied)
- [ ] 27b-m1-tuning-research — distilled 2026-09-07 06:44 → skills/27b-m1-tuning-research/SKILL.md (auto-applied)
- [ ] research-first-27b-model-implementation — distilled 2026-09-07 05:22 → skills/research-first-27b-model-implementation/SKILL.md (auto-applied)
- [ ] tts-fresh-entitlement-retry — distilled 2026-09-06 21:51 → skills/tts-fresh-entitlement-retry/SKILL.md (auto-applied)

## [AGENTS]
- [ ] turbofit-watch-bot — SUGGESTED 2026-09-15 19:01: I see your TurboFit options disappear every time you restart the desktop app — want a bot that checks they're still ther → agents/turbofit-watch-bot.md.proposed
- [ ] obs-omarchy-stream-bot — SUGGESTED 2026-09-15 10:02: I see you want OBS on the MacBook to manage streaming while you play Armored Core 6 on the Omarchy, and that's still pen → agents/obs-omarchy-stream-bot.md.proposed
- [ ] steam-play-hp-bot — SUGGESTED 2026-09-15 10:02: I see you're mid-OS-setup on the HP with Steam Play (Proton) 'having a hard time' — want a bot that drives the HP's Stea → agents/steam-play-hp-bot.md.proposed
- [ ] m1-27b-audit-bot — SUGGESTED 2026-09-07 19:51: I see you're trying to validate the 27B/unleashed path on M1 — want a bot that checks Hermes runtime binding, model-list → agents/m1-27b-audit-bot.md.proposed
- [ ] m1-27b-prep-bot — SUGGESTED 2026-09-07 16:10: I see you're focused on getting one of the 27B models optimized on M1 — want a bot that uses the retained 131K outputs a → agents/m1-27b-prep-bot.md.proposed
- [ ] 27b-optimizer — SUGGESTED 2026-09-07 05:22: I see you're refocusing on the 27B models after the 131K speed miss — want a bot that finds the fastest viable Q3 27B co → agents/27b-optimizer.md.proposed
- [ ] m1-27b-tuner — SUGGESTED 2026-09-07 03:41: I see you're trying to make the 27B Q3 path usable at 131K — want a bot that tunes local llama.cpp/prefill settings for  → agents/m1-27b-tuner.md.proposed
- [ ] teknium — SUGGESTED 2026-09-06 21:51: I see you're talking about restoring the Hermes UI to center and making model choice stick — want teknium to fix the lay → agents/teknium.md.proposed
- [ ] state-recovery-bot — SUGGESTED 2026-09-06 03:42: I see you're trying to get the UI and model state back after diffs broke it — want a bot that snapshots and restores las → agents/state-recovery-bot.md.proposed

## [LOOPS]
- [ ] weaver — SUGGESTED 2026-09-08 09:50: Want me to show you the restored wiki vault dashboard with running indicator? → loops/weaver.md.proposed
- [ ] looker — SUGGESTED 2026-09-08 09:50: Want me to capture and verify your restored UI state in the Hermes preview window? → loops/looker.md.proposed
- [ ] download-completion-watch — SUGGESTED 2026-09-07 19:51: Want me to watch the local model download path and only alert when it actually completes and becomes loadable? → loops/download-completion-watch.md.proposed
- [ ] 27b-speed-target-loop — SUGGESTED 2026-09-07 19:51: Want a repeatable pass that benchmarks the 27B/unleashed tuning path on your M1 against your speed target instead of rer → loops/27b-speed-target-loop.md.proposed
- [ ] 27b-speed-watch — SUGGESTED 2026-09-07 03:41: Want a repeating loop that checks whether the 27B Q3 131K run hits your speed bar, so it doesn't just drift while you're → loops/27b-speed-watch.md.proposed

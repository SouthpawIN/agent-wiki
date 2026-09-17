# Queue — beyond-pissed

## [CONTEXT]
- [ ] research qwen4-llama-cuda-format-support — SUGGESTED 2026-09-17 13:10: Want me to look into which model formats the qwen4-fork llama.cpp runtime supports for CUDA?
- [ ] research format-compatibility-check — SUGGESTED 2026-09-17 05:47: Want me to look into which model formats will actually run on your CUDA llama.cpp runtime (the qwen4 fork)?
- [ ] research model-routing-options — SUGGESTED 2026-09-15 17:31: Want me to look into how to select which models O'Marki serves to the MacBook?
- [ ] research oh-marki-macos-flash — SUGGESTED 2026-09-15 13:29: Want me to look into the correct, reliable way to flash an Arch-based ISO to a USB on macOS — the sudo dd vs. rdisk4 per
- [ ] research sync-verifier — SUGGESTED 2026-09-10 14:10: Want me to look into the exact sync mechanics between Projects and agent-wiki?
- [ ] research repo-sync-arch — SUGGESTED 2026-09-09 20:09: Want me to look into the intended repository architecture between ~/Documents/Projects/Projects and ~/gh-sync/agent-wiki
- [ ] research discrepancy-investigation — SUGGESTED 2026-09-09 13:17: Want me to look into what the discrepancy is between 'there' and the intended update state?
- [ ] research system-live-json-serving — SUGGESTED 2026-09-08 09:57: Want me to look into how the /file route serves .system-live.json and how --new-token rotation works?
- [ ] research ornith-model-catalog — SUGGESTED 2026-09-07 18:49: Want me to look into the Ornith model catalog entries?
- [ ] research wiki-orchestrator-patterns — SUGGESTED 2026-09-07 18:12: Want me to look into how wiki-based orchestrators scale across many simultaneous projects without becoming a maintenance
- [~] research — dispatched 2026-09-06 01:51

## [SKILLS]
- [ ] center-wiki-orchestration — distilled 2026-09-08 09:57 → skills/center-wiki-orchestration/SKILL.md (auto-applied)

## [AGENTS]
- [ ] omarki-serving-models-format-check — SUGGESTED 2026-09-17 13:10: I see you're setting up which formats O'Marki can serve to the MacBook — want a loop that checks which model formats are → agents/omarki-serving-models-format-check.md.proposed
- [ ] omarki-format-compat-watch — SUGGESTED 2026-09-17 13:10: I see you haven't yet pinned down which model formats run on O'Marki's CUDA llama.cpp runtime — want a daily bot that wa → agents/omarki-format-compat-watch.md.proposed
- [ ] model-format-servant — SUGGESTED 2026-09-17 13:10: I see you're trying to pin down which model formats actually run on O'Marki's CUDA llama.cpp runtime — want a bot that c → agents/model-format-servant.md.proposed
- [ ] format-compat-watch — SUGGESTED 2026-09-17 05:47: I see you're trying to pin down which model formats actually run on that CUDA llama.cpp runtime — want a daily bot that  → agents/format-compat-watch.md.proposed
- [ ] omarki-model-servant — SUGGESTED 2026-09-17 05:47: I see you want to pick which models O'Marki serves to this MacBook — want a bot that curates and routes model selection  → agents/omarki-model-servant.md.proposed
- [ ] served-models-check — SUGGESTED 2026-09-15 17:31: Want a loop that checks which models O'Marki is currently serving to the MacBook and flags anything that shouldn't be? → agents/served-models-check.md.proposed
- [ ] model-routing-bot — SUGGESTED 2026-09-15 17:31: I see you want to select which models O'Marki serves to this MacBook — want a bot that helps you pick and route which mo → agents/model-routing-bot.md.proposed
- [ ] omarki-latest-fetcher — SUGGESTED 2026-09-15 13:29: I see you asked for the latest Oh My Archi and the install hasn't finished — want a bot that pulls the newest Oh My Arch → agents/omarki-latest-fetcher.md.proposed
- [ ] oh-marki-flasher — SUGGESTED 2026-09-15 13:29: I see your Oh My Archi install is stuck in the grub screen with the ISO write still denied on /dev/rdisk4 — want a bot t → agents/oh-marki-flasher.md.proposed
- [ ] chromium-new-tab-homepage — SUGGESTED 2026-09-15 11:02: I see you want a new Chromium tab to surface the center wiki instead of a blank page — want a bot that sets the Hermes D → agents/chromium-new-tab-homepage.md.proposed
- [ ] commit-scan-topics-fix — SUGGESTED 2026-09-10 14:10: I see you need the scan-topics.py schema fix committed and pushed — want a bot to handle that? → agents/commit-scan-topics-fix.md.proposed
- [ ] git-upstream-setter — SUGGESTED 2026-09-10 14:10: I see you need git remote upstream tracking configured on main — want a bot that sets it up? → agents/git-upstream-setter.md.proposed
- [ ] watch-process-restart — SUGGESTED 2026-09-10 14:10: I see you need the scan-topics.py watch loop restarted with fixed code — want a bot that kills and restarts it? → agents/watch-process-restart.md.proposed
- [ ] center-wiki-monitor — SUGGESTED 2026-09-08 09:57: I see you're using the center wiki as a live orchestrator across projects — want a bot that continuously monitors and re → agents/center-wiki-monitor.md.proposed
- [ ] center-wiki-understanding — SUGGESTED 2026-09-07 18:49: I see you're working to understand the center wiki build/work/use patterns — want a bot that traces the integration pipe → agents/center-wiki-understanding.md.proposed
- [ ] center-wiki-intake — SUGGESTED 2026-09-07 18:12: I see you're planning to run many projects through the center wiki — want a bot that turns new project notes and decisio → agents/center-wiki-intake.md.proposed

## [LOOPS]
- [ ] watch-loop-sync — SUGGESTED 2026-09-10 14:10: Want a loop to keep the watch process in sync with repo updates? → loops/watch-loop-sync.md.proposed
- [ ] verification-loop — SUGGESTED 2026-09-10 14:10: Want a continuous loop to verify vault-live.json updates after watch restart? → loops/verification-loop.md.proposed
- [ ] orchestration-state-sync — SUGGESTED 2026-09-08 09:57: Want a loop that keeps the center wiki's multi-project orchestration state fresh and visible? → loops/orchestration-state-sync.md.proposed
- [ ] revert-recovery-watch — SUGGESTED 2026-09-08 09:57: Want a loop that continuously checks the center wiki for reverts and auto-notifies so they get recovered before becoming → loops/revert-recovery-watch.md.proposed
- [ ] orchestrator-sync — SUGGESTED 2026-09-07 18:49: Want me to monitor the center wiki as an orchestrator for your projects? → loops/orchestrator-sync.md.proposed
- [ ] wiki-orchestrator-sync — SUGGESTED 2026-09-07 18:12: Want a loop that every 2h scans your recent project notes/decisions and drafts wiki updates so the orchestrator stays cu → loops/wiki-orchestrator-sync.md.proposed

# Queue — self-file

## [CONTEXT]
- [ ] research remote-stack-live-confirmation — SUGGESTED 2026-09-15 21:03: Want me to look into confirming the remote inference stack is actually live — Hermes reported it stable but it's still f
- [ ] research bonsai-mlx-feasibility — SUGGESTED 2026-09-15 21:03: Want me to look into whether Bonsai MLX can actually serve the ornith model — Colibri was ruled out for mlx_lm and Bonsa
- [ ] research mlx-lm-gpu-memory — SUGGESTED 2026-09-15 15:47: Want me to look into how to reduce mlx_lm GPU memory use — context length, cache management, and quantization — so a sin
- [ ] research scan-topics-py-write-function — SUGGESTED 2026-09-10 13:30: Want me to look into the scan-topics.py write() function at line 320 to confirm it replaces live['bots'] with snap['bots
- [ ] research mlx-lm-large-prompt-kill-causes — SUGGESTED 2026-09-07 10:23: Want me to look into why mlx_lm server gets SIGKILL on 40k-token prompts and whether cache size or memory pressure is th
- [~] research — dispatched 2026-09-06 19:32

## [SKILLS]
- [ ] stale-process-kill-rescan — distilled 2026-09-10 13:30 → skills-capabilities/stale-process-kill-rescan/SKILL.md (auto-applied)

## [AGENTS]
- [ ] bonsai-mlx-probe — SUGGESTED 2026-09-15 21:03: I see you've been chasing a local inference backend that isn't standard mlx_lm — want a bot that probes Bonsai MLX again → agents/bonsai-mlx-probe.md.proposed
- [ ] omarchy-plugin-ui — SUGGESTED 2026-09-15 21:03: I see you're building a plugin UI for Omarchy's remote inference stack — want a bot that builds that Omarchy plugin UI f → agents/omarchy-plugin-ui.md.proposed
- [ ] prompt-cache-cleanup — SUGGESTED 2026-09-15 15:47: I see your Mac's prompt cache fills from accumulated test history and forces restarts — want a bot that clears and sched → agents/prompt-cache-cleanup.md.proposed
- [ ] gpu-memory-tuner — SUGGESTED 2026-09-15 15:47: I see your local and remote inference keeps hitting GPU memory walls — want a bot that profiles mlx_lm and Flash Next me → agents/gpu-memory-tuner.md.proposed
- [ ] remote-stack-watchdog — SUGGESTED 2026-09-15 15:47: I see you now run inference over a remote stack (nginx :8080, model server :8100, Tailscale) — want a bot that watches t → agents/remote-stack-watchdog.md.proposed
- [ ] local-inference-porter — SUGGESTED 2026-09-07 14:31: I see you're still fighting churn between ornith and MTPLX on 11613 — want a bot that watches your local endpoints and k → agents/local-inference-porter.md.proposed
- [ ] local-inference-monitor — SUGGESTED 2026-09-07 10:23: I see you're testing local inference endpoints and hitting SIGKILL on large prompts — want a bot that monitors mlx_lm se → agents/local-inference-monitor.md.proposed

## [LOOPS]
- [ ] gpu-memory-watch — SUGGESTED 2026-09-15 15:47: Want a loop that watches GPU memory on your Mac and remote box every hour and warns you before a stray process eats 16 G → triggers-loops/gpu-memory-watch.md.proposed
- [ ] remote-stack-health-tick — SUGGESTED 2026-09-15 15:47: Want a loop that pings your remote inference stack (nginx :8080, model server :8100 over Tailscale) every 30m and alerts → triggers-loops/remote-stack-health-tick.md.proposed
- [ ] local-watch-process-monitor — SUGGESTED 2026-09-10 13:30: Want me to set up a loop that checks every 10m whether the watch/scan process is running current code, and if it finds a → triggers-loops/local-watch-process-monitor.md.proposed
- [ ] local-endpoint-verification — SUGGESTED 2026-09-07 14:31: Want a loop that verifies the ornith/MTPLX endpoint map every 30 minutes and flags drift? → triggers-loops/local-endpoint-verification.md.proposed
- [ ] large-prompt-regression — SUGGESTED 2026-09-07 10:23: Want a loop that replays progressively larger prompts against your local servers to catch SIGKILL or cache failures befo → triggers-loops/large-prompt-regression.md.proposed
- [ ] local-server-health-check — SUGGESTED 2026-09-07 10:23: Want a recurring check that verifies your local mlx_lm endpoints are still bound on the right ports and haven't been kil → triggers-loops/local-server-health-check.md.proposed

# Queue — self-file

## [CONTEXT]
- [ ] research mlx-lm-large-prompt-kill-causes — SUGGESTED 2026-09-07 10:23: Want me to look into why mlx_lm server gets SIGKILL on 40k-token prompts and whether cache size or memory pressure is th
- [~] research — dispatched 2026-09-06 19:32

## [SKILLS]

## [AGENTS]
- [ ] local-inference-porter — SUGGESTED 2026-09-07 14:31: I see you're still fighting churn between ornith and MTPLX on 11613 — want a bot that watches your local endpoints and k → agents/local-inference-porter.md.proposed
- [ ] local-inference-monitor — SUGGESTED 2026-09-07 10:23: I see you're testing local inference endpoints and hitting SIGKILL on large prompts — want a bot that monitors mlx_lm se → agents/local-inference-monitor.md.proposed

## [LOOPS]
- [ ] local-endpoint-verification — SUGGESTED 2026-09-07 14:31: Want a loop that verifies the ornith/MTPLX endpoint map every 30 minutes and flags drift? → loops/local-endpoint-verification.md.proposed
- [ ] large-prompt-regression — SUGGESTED 2026-09-07 10:23: Want a loop that replays progressively larger prompts against your local servers to catch SIGKILL or cache failures befo → loops/large-prompt-regression.md.proposed
- [ ] local-server-health-check — SUGGESTED 2026-09-07 10:23: Want a recurring check that verifies your local mlx_lm endpoints are still bound on the right ports and haven't been kil → loops/local-server-health-check.md.proposed

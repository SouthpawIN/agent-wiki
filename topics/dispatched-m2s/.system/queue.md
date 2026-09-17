# Queue — dispatched-m2s

## [CONTEXT]
- [ ] research delegation-failure-root-cause — SUGGESTED 2026-09-16 21:20: Want me to look into what actually distinguishes Hermes delegation batches that hit the owner-exit timeout from ones tha
- [ ] research message-id-reuse-audit — SUGGESTED 2026-09-09 20:14: Want me to audit how Heremes state.db message IDs are assigned — are they reused per-thread rather than per-notification
- [ ] research owner-exit-root-cause — SUGGESTED 2026-09-07 14:09: Want me to look into the root cause of the Hermes delegation owner exit timeout?
- [ ] research delegation-timeout — SUGGESTED 2026-09-07 10:02: Want me to look into why delegation owner exits before recording terminal results?
- [~] research — dispatched 2026-09-07 05:42

## [SKILLS]

## [AGENTS]
- [ ] delegation-auditor — SUGGESTED 2026-09-07 14:09: I see you're trying to separate owner-exit failures from batch-size effects — want a bot that instruments Hermes delegat → agents/delegation-auditor.md.proposed

## [LOOPS]
- [ ] delegation-daily-digest — SUGGESTED 2026-09-07 14:09: Want a daily digest of delegation batch outcomes so you can spot owner-exit patterns without digging through logs? → loops/delegation-daily-digest.md.proposed

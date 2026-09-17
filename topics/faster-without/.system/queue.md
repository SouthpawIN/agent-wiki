# Queue — faster-without

## [CONTEXT]
- [ ] research d-flash2-spec-draft-verify — SUGGESTED 2026-09-17 04:15: Want me to look into exactly how DFlash2 is hooked up as a spec-draft for qwen4/Unleashed at 131K, so the pending resear
- [ ] research dflash2-setup-and-benchmark — SUGGESTED 2026-09-16 21:49: You've got more KV cache room and lower power now, and DFlash2's spec-draft is still pending — want me to look up its ex
- [ ] research dflash2-131k-config-scan — SUGGESTED 2026-09-07 04:26: Want me to look into DFlash2's configuration knobs that affect 131K throughput?
- [ ] research d-flash-131k-research — SUGGESTED 2026-09-06 22:46: Want me to look into whether removing D-flash actually improves 27B speed at 131K, and what alternatives keep full conte
- [ ] research d-flash-context-research — SUGGESTED 2026-09-06 21:53: Want me to look into whether D-flash is the bottleneck for 27B@131K throughput and what llama.cpp flags or quantization 
- [~] research — dispatched 2026-09-06 20:56

## [SKILLS]
- [ ] d-flash-131k-benchmark — distilled 2026-09-07 04:26 → skills/d-flash-131k-benchmark/SKILL.md (auto-applied)

## [AGENTS]
- [ ] d-flash2-benchmark — SUGGESTED 2026-09-17 04:15: I see the DFlash2 high-speed result ('both MTP and DFlash2 produce full responses at high speed') has no tok/s number —  → agents/d-flash2-benchmark.md.proposed
- [ ] d-flash-checkpoint — SUGGESTED 2026-09-17 04:15: I see you're about to engage the DFlash2 spec-draft but the 81 tok/s checkpoint save is unconfirmed and you said don't m → agents/d-flash-checkpoint.md.proposed
- [ ] d-flash2-setup-research — SUGGESTED 2026-09-15 21:57: Want me to look into exactly how DFlash2's spec-draft is configured for qwen4 at 131K — the precise setup requirements t → agents/d-flash2-setup-research.md.proposed
- [ ] d-flash-benchmarker — SUGGESTED 2026-09-06 21:53: I see you're weighing D-flash removal for speed — want a bot that benchmarks 27B@131K with/without D-flash and reports w → agents/d-flash-benchmarker.md.proposed

## [LOOPS]
- [ ] d-flash2-daily-speed-watch — SUGGESTED 2026-09-17 04:15: I see the DFlash2 draft is still pending and conditions keep improving — want a loop that logs the daily 131K speed so t → loops/d-flash2-daily-speed-watch.md.proposed
- [ ] d-flash2-checkpoint-watch — SUGGESTED 2026-09-17 04:15: I see the checkpoint-before-experiment rule keeps needing enforcement and the 81 tok/s save was never confirmed — want a → loops/d-flash2-checkpoint-watch.md.proposed
- [ ] daily-131k-speed-check — SUGGESTED 2026-09-07 04:26: Want a daily 9am benchmark that compares Unleashed vs DFlash2 at 131K and logs tok/s? → loops/daily-131k-speed-check.md.proposed

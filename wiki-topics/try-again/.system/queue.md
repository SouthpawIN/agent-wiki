# Queue — try-again

## [CONTEXT]
- [ ] research maple-colibri-ornith-model-ids — SUGGESTED 2026-09-07 15:55: Want me to look up the exact model IDs, download commands, and known tok/s for Maple Colibri and Ornith 1.5 35A3B on thi
- [ ] research apple-silicon-engine-options-lookup — SUGGESTED 2026-09-07 09:31: Want me to look into the specific model IDs and fastest Apple Silicon engines for Qwen 3.8 27B, Tiel Coder, and Dirk 27B
- [ ] research apple-silicon-inference-engine-discovery — SUGGESTED 2026-09-07 06:24: Want me to look into any other Apple Silicon inference engines beyond llama.cpp, MLX, OMLX, and FreeToken that can run Q
- [ ] research apple-silicon-engine-landscape — SUGGESTED 2026-09-07 05:11: Want me to look into which Apple Silicon inference engines actually support Qwen 3.8 27B right now?
- [ ] research turbofit-engine-compat — SUGGESTED 2026-09-06 22:38: Want me to look into what local inference engines TurboFit can use as auxiliary backends on this Mac?
- [~] research — dispatched 2026-09-06 02:47

## [SKILLS]
- [ ] warmup-before-benchmark — distilled 2026-09-07 08:40 → skills-capabilities/warmup-before-benchmark/SKILL.md (auto-applied)

## [AGENTS]
- [ ] apple-silicon-inference-runner — SUGGESTED 2026-09-07 09:31: I see you're running a live Apple Silicon inference benchmark sweep — want a bot that manages warmup, test, and tok/s ca → agents/apple-silicon-inference-runner.md.proposed
- [ ] apple-silicon-inference-engine-tester — SUGGESTED 2026-09-07 06:24: I see you're testing every Apple Silicon inference backend for Qwen 3.8 27B — want a bot that actually runs llama.cpp, M → agents/apple-silicon-inference-engine-tester.md.proposed
- [ ] ace-step-runner — SUGGESTED 2026-09-07 05:11: I see you're trying to get ACE-Step running locally — want a bot that runs it through viable Apple Silicon inference eng → agents/ace-step-runner.md.proposed
- [ ] turbofit-engine-aux — SUGGESTED 2026-09-06 22:38: I see you're talking about expanding Turbofit's auxiliary engines — want a bot that enumerates and configures alternativ → agents/turbofit-engine-aux.md.proposed

## [LOOPS]
- [ ] warmup-speed-test-loop — SUGGESTED 2026-09-07 09:31: Want a repeatable loop that warms, benches, and records tok/s for each model as you add engines? → triggers-loops/warmup-speed-test-loop.md.proposed
- [ ] ace-step-run-check — SUGGESTED 2026-09-07 06:24: Want a daily check that retries ACE-Step on the current engine and reports whether it boots? → triggers-loops/ace-step-run-check.md.proposed
- [ ] apple-silicon-engine-smoke — SUGGESTED 2026-09-07 06:24: Want a 30-minute smoke loop that re-runs the fastest known engine config and catches regressions? → triggers-loops/apple-silicon-engine-smoke.md.proposed
- [ ] inference-engine-smoke — SUGGESTED 2026-09-07 05:11: Want a quick parallel check every 30m for viable local inference engines on this Mac? → triggers-loops/inference-engine-smoke.md.proposed

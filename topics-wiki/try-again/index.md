---
title: try-again
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# try-again

Last updated: 2026-09-15 | Total pages: 18

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [ACE-Step](wiki/ace-step.md) — Chris has ACE-Step downloaded locally (2.2 GB) and wants to "try to get it running." ^[raw/inbox/2026-09-07.md]
- [Bonsai 27B](wiki/bonsai-27b.md) — Bonsai is one of the three final local inference candidates Chris selected for the M1 32GB benchmark sweep. ^[raw/inbox/2026-09-07.md]
- [Colibri](wiki/colibri.md) — Colibri is one of the three final local inference candidates Chris selected for the M1 32GB benchmark sweep. ^[raw/inbox/2026-09-07.md]
- [Dirk 27B](wiki/dirk-27b.md) — At 2026-09-07 08:17, Chris added Dirk 27B to the Apple Silicon inference benchmark sweep. ^[raw/inbox/2026-09-07.md]
- [Ornith 1.5 35A3B](wiki/ornith-1.5-35a3b.md) — Ornith 1.5 35A3B is one of the three final local inference candidates Chris selected for the M1 32GB benchmark sweep. ^[raw/inbox/2026-09-07.md]
- [Qwen 3.8 27B](wiki/qwen-3-8-27b.md) — On 2026-09-07, Chris made Qwen 3.8 27B the primary target for local inference speed research on Apple Silicon. ^[raw/inbox/2026-09-07.md]
- [Tiel Coder](wiki/tiel-coder.md) — At 2026-09-07 08:17, Chris added Tiel Coder to the Apple Silicon inference benchmark sweep. ^[raw/inbox/2026-09-07.md]

### Concepts

- [Apple Silicon Inference Engine Testing](wiki/apple-silicon-inference-engine-testing.md) — Chris wants to research and test all available Apple Silicon inference engines for Qwen 3.8 27B, with the goal of making larger models runnable locally on this
- [Curl Timeouts and Python Fallback](wiki/curl-timeouts-and-python-fallback.md) — Chris is hitting network timeouts when shelling out to curl for HTTP requests, and is falling back to a Python-based approach instead. ^[raw/inbox/2026-09-08.md
- [Local Inference Benchmark Sweep](wiki/local-inference-benchmark-sweep.md) — As of 2026-09-07, Chris is running a local inference benchmark sweep on Apple Silicon M1 32GB with the goal of making larger models runnable locally at maximum
- [Restore / Retry](wiki/restore-retry.md) — Chris asked for a retry: restore state from a prior picture/history after several backwards steps. ^[raw/inbox/2026-09-06.md]
- [Turbofit Engine Options](wiki/turbofit-engine-options.md) — - Chris said part of Turbofit is trying different inference engines, and he wants them expanded to make the current model work on this computer as the auxiliary
- [TurboFit M1 Testing Status](wiki/turbofit-m1-testing-status.md) — As of 2026-09-07, the TurboFit-engine work is partly blocked by system-level write restrictions during live testing. ^[raw/inbox/2026-09-07.md]

### Decisions

- [Benchmark Protocol](wiki/benchmark-protocol.md) — On 2026-09-07, Chris set the exact local inference benchmark procedure for the Apple Silicon sweep. ^[raw/inbox/2026-09-07.md]
- [Warmup Before Speed Test](wiki/warmup-before-speed-test.md) — On 2026-09-07 at 08:17, Chris directed that every model must complete a warmup prompt before measuring tok/s. ^[raw/inbox/2026-09-07.md]

### Comparisons

- [2026-09-07 Candidate Narrowing](wiki/2026-09-07-candidate-narrowing.md) — Chris narrowed the benchmark sweep from an open engine sweep for Qwen 3.8 27B to a focused model comparison among Bonsai, Colibri, and Ornith. ^[raw/inbox/2026-

### Queries

- [2026-09-09 Tool Invocation Blocking](wiki/2026-09-09-tool-blocking.md) — Evidence of a recurring operational friction: Hermes agents in this topic are blocked from modifying files via `shell`-launched `sed` commands, and fall back to
- [2026-09-10 Tool Invocation Blocking (Continued)](wiki/2026-09-10-tool-blocking-continued.md) — Continuation of the recurring operational friction first documented on 2026-09-09, now extending to shell availability, git push, and remote configuration in th

---

## SKILLS

Topic skills stored in this wiki:

- **[warmup-before-benchmark](skills-capabilities/warmup-before-benchmark/SKILL.md) — 1. Load the exact target model and quant intended for measurement.

---

## BOTS

Proposed bots:

- **[ace-step-runner](agents/ace-step-runner.md.proposed) — **I see you're trying to get ACE-Step running locally — want a bot that runs it through viable Apple Silicon inference engines and reports back?**
- **[apple-silicon-inference-engine-tester](agents/apple-silicon-inference-engine-tester.md.proposed) — **I see you're testing every Apple Silicon inference backend for Qwen 3.8 27B — want a bot that actually runs llama.cpp, MLX, OMLX, and FreeToken and 
- **[apple-silicon-inference-runner](agents/apple-silicon-inference-runner.md.proposed) — **I see you're running a live Apple Silicon inference benchmark sweep — want a bot that manages warmup, test, and tok/s capture per model/engine and w
- **[turbofit-engine-aux](agents/turbofit-engine-aux.md.proposed) — **I see you're talking about expanding Turbofit's auxiliary engines — want a bot that enumerates and configures alternative local inference backends f


---

## LOOPS

Proposed loops:

- **[ace-step-run-check](triggers-loops/ace-step-run-check.md.proposed) — owner: teknium · cadence: daily · status: SUGGESTED
- **[apple-silicon-engine-smoke](triggers-loops/apple-silicon-engine-smoke.md.proposed) — owner: teknium · cadence: every 30 minutes · status: SUGGESTED
- **[inference-engine-smoke](triggers-loops/inference-engine-smoke.md.proposed) — owner: turbosovth · cadence: 30m · status: SUGGESTED
- **[warmup-speed-test-loop](triggers-loops/warmup-speed-test-loop.md.proposed) — owner: turbosovth · cadence: human phrase · status: SUGGESTED

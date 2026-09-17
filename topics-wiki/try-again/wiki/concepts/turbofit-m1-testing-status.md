---
title: "TurboFit M1 Testing Status"
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [turbofit, inference, apple-silicon, testing, pain]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---

# TurboFit M1 Testing Status

As of 2026-09-07, the TurboFit-engine work is partly blocked by system-level write restrictions during live testing. ^[raw/inbox/2026-09-07.md]

## Completed actions
- Identified candidate engines/models and started benchmarking with warmup requirements. ^[raw/inbox/2026-09-07.md]
- Confirmed Ternary Bonsai 27B MLX uses `llama.cpp` with `metal` on Apple Silicon. ^[raw/inbox/2026-09-07.md]
- Quote: "Ternary Bonsai 27B: library_name `llama.cpp`, supports `metal` (Apple Silicon). No MLX variant found." ^[raw/inbox/2026-09-07.md]

## Blocker
- System edits to TurboFit config were blocked during testing. ^[raw/inbox/2026-09-07.md]
- Quote: "The system is stopping me from editing the config directly. Let me use the hermes command or another approach." ^[raw/inbox/2026-09-07.md]
- Quote: "The system is blocking shell commands. Let me try with the write_file tool instead." ^[raw/inbox/2026-09-07.md]
- These are Hermes working notes, not a request for Senter to act on them. ^[raw/inbox/2026-09-07.md]

## Interrupted task
- A 2026-09-07 task with status `interrupted` after 1944.94s reached 50 API calls before stopping. ^[raw/inbox/2026-09-07.md]
- It was intended to run the finalized protocol: warmup → 500-token short prompt → 100-token 5K prompt, with tok/s reporting. ^[raw/inbox/2026-09-07.md]

## Current focus
- Run clean benchmark sequences for Bonsai, Colibri, and Ornith with model cleanup between tests. ^[raw/inbox/2026-09-07.md]
- Deliver exact tok/s figures and load commands for each candidate. ^[raw/inbox/2026-09-07.md]

## Related
- [[topics-wiki/try-again/wiki/concepts/turbofit-engine-options|Turbofit Engine Options]]
- [[topics-wiki/try-again/wiki/decisions/benchmark-protocol|Benchmark Protocol]]
- [[topics-wiki/try-again/wiki/comparisons/2026-09-07-candidate-narrowing|2026-09-07 Candidate Narrowing]]
- [[topics-wiki/try-again/wiki/queries/2026-09-09-tool-blocking|2026-09-09 Tool Invocation Blocking]]
- [[topics-wiki/try-again/wiki/queries/2026-09-10-tool-blocking-continued|2026-09-10 Tool Invocation Blocking (Continued)]]

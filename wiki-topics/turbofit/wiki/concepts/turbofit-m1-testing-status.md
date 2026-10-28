---
title: TurboFit M1 testing status (2026-09-07)
created: 2026-10-28
updated: 2026-10-28
type: concept
tags: [turbofit, provider, provenance, consolidation]
sources: [raw/sources/2026-10-28-github-consolidation.md]
confidence: high
---

# TurboFit M1 testing status (2026-09-07)

> What the Apple-Silicon benchmark push had and had not proven on the MacBook, and what blocked it.

**Absorbed 2026-10-28** from pages that had been filed in other topics (one spot for TurboFit knowledge). Source pages are now redirect stubs.

## Sources absorbed

- `wiki-topics/try-again/wiki/concepts/turbofit-m1-testing-status.md` — TurboFit M1 Testing Status (created 2026-09-07)

---

## TurboFit M1 Testing Status

As of 2026-09-07, the TurboFit-engine work is partly blocked by system-level write restrictions during live testing. ^[provenance: try-again/raw/inbox/2026-09-07.md]

## Completed actions
- Identified candidate engines/models and started benchmarking with warmup requirements. ^[provenance: try-again/raw/inbox/2026-09-07.md]
- Confirmed Ternary Bonsai 27B MLX uses `llama.cpp` with `metal` on Apple Silicon. ^[provenance: try-again/raw/inbox/2026-09-07.md]
- Quote: "Ternary Bonsai 27B: library_name `llama.cpp`, supports `metal` (Apple Silicon). No MLX variant found." ^[provenance: try-again/raw/inbox/2026-09-07.md]

## Blocker
- System edits to TurboFit config were blocked during testing. ^[provenance: try-again/raw/inbox/2026-09-07.md]
- Quote: "The system is stopping me from editing the config directly. Let me use the hermes command or another approach." ^[provenance: try-again/raw/inbox/2026-09-07.md]
- Quote: "The system is blocking shell commands. Let me try with the write_file tool instead." ^[provenance: try-again/raw/inbox/2026-09-07.md]
- These are Hermes working notes, not a request for Senter to act on them. ^[provenance: try-again/raw/inbox/2026-09-07.md]

## Interrupted task
- A 2026-09-07 task with status `interrupted` after 1944.94s reached 50 API calls before stopping. ^[provenance: try-again/raw/inbox/2026-09-07.md]
- It was intended to run the finalized protocol: warmup → 500-token short prompt → 100-token 5K prompt, with tok/s reporting. ^[provenance: try-again/raw/inbox/2026-09-07.md]

## Current focus
- Run clean benchmark sequences for Bonsai, Colibri, and Ornith with model cleanup between tests. ^[provenance: try-again/raw/inbox/2026-09-07.md]
- Deliver exact tok/s figures and load commands for each candidate. ^[provenance: try-again/raw/inbox/2026-09-07.md]

## Related
- Turbofit Engine Options
- Benchmark Protocol
- 2026-09-07 Candidate Narrowing
- 2026-09-09 Tool Invocation Blocking
- 2026-09-10 Tool Invocation Blocking (Continued)

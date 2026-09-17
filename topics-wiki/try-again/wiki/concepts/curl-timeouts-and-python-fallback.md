---
title: "Curl Timeouts and Python Fallback"
created: 2026-09-08
updated: 2026-09-08
type: concept
tags: [pain, infra, hermes, tool]
sources: [raw/inbox/2026-09-08.md]
confidence: high
---

# Curl Timeouts and Python Fallback

Chris is hitting network timeouts when shelling out to curl for HTTP requests, and is falling back to a Python-based approach instead. ^[raw/inbox/2026-09-08.md]

## Raw item

Quote: "The curl command keeps timing out. Let me try a Python approach instead." ^[raw/inbox/2026-09-08.md]

The item is filed under `2026-09-08 09:39 · hermes · 20260903_001447_7bc70a · sim 0.08`, indicating it was captured as Hermes working state during a prior session (token `20260903_001447_7bc70a`, very low similarity score `0.08`). ^[raw/inbox/2026-09-08.md]

## Context within the topic

This curl-to-Python fallback appears amid ongoing work to restore a prior working state (see [[topics-wiki/try-again/wiki/concepts/restore-retry|Restore / Retry]]) and to retry inference-engine benchmarking on Apple Silicon. ^[raw/inbox/2026-09-06.md]

The fallback is operational evidence (a working note about how a fetch/retry is being implemented), not itself a request for Senter to act. It sits alongside other system-level friction during the benchmarking effort, including the write restrictions documented in [[topics-wiki/try-again/wiki/concepts/turbofit-m1-testing-status|TurboFit M1 Testing Status]]. ^[raw/inbox/2026-09-07.md]

## Implications

- Network fetches that Chris's tooling relies on (e.g., downloading model weights or engine binaries during the sweep) are intermittently timing out under curl. ^[raw/inbox/2026-09-08.md]
- The workaround Chris is reaching for — substituting a Python HTTP client — should be treated as the path to use for any future fetch-heavy steps in this topic (engine downloads, model ID lookups, per-engine command retrieval). ^[raw/inbox/2026-09-08.md]
- The very low similarity score of the source item (`sim 0.08`) suggests it was recovered from an older session snapshot rather than produced in the current compile pass. ^[raw/inbox/2026-09-08.md]

## Links
- [[topics-wiki/try-again/wiki/concepts/restore-retry|Restore / Retry]]
- [[topics-wiki/try-again/wiki/concepts/turbofit-m1-testing-status|TurboFit M1 Testing Status]]
- [[topics-wiki/try-again/wiki/concepts/apple-silicon-inference-engine-testing|Apple Silicon Inference Engine Testing]]
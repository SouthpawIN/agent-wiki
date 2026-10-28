---
title: Context Sizing
created: 2026-09-06
updated: 2026-09-06
type: decision
tags: [decision, infra, preference]
sources: [raw/inbox/2026-09-06.md]
confidence: high
---

# Context Sizing

## What

Local TurboFit contexts are set to 131,072 tokens for both main and aux ^[raw/inbox/2026-09-06.md].

## Why

262k pre-fills slowly on a 32 GB M1 and stresses the Metal heap. Hermes compression timed out repeatedly at 270k+ tokens on the main model. 131k is the stable local sweet spot on this box ^[raw/inbox/2026-09-06.md].

## When

Set 2026-09-06 after multiple compression timeout errors during end-to-end testing.

## Evidence

- "put Qwen 3.8 27B at 131K and Maple at 131K" ^[raw/inbox/2026-09-06.md].
- "Context compression timed out before it could commit while the request was still approximately 270,285 tokens" ^[raw/inbox/2026-09-06.md].
- "131k is the stable sweet spot for this 32 GB box" ^[raw/inbox/2026-09-06.md].

## Related

- [[main-model-selection|Main Model Selection]]
- [[aux-model-selection|Aux Model Selection]]
- [[compression-timeouts|Compression Timeouts]]

---
title: Hermes Auto Route Stability
created: 2026-09-08
updated: 2026-09-08
type: concept
tags:
  - turbofit
  - stability
  - routing
  - pain
sources:
  - raw/inbox/2026-09-07.md
  - raw/inbox/2026-09-08-from-senter-wiki.md
confidence: high
contested: true
---

# Hermes Auto Route Stability

## The Problem

From `raw/inbox/2026-09-08-from-senter-wiki.md`:

> "The problem is: ... Hermes flips the active model to StepFun 3.7 Flash. Two causes appear in the transcript: `model.default` not being first in the fallback chain, and `auxiliary.compression.provider: auto` selecting StepFun for compression"

Hermes's auto-routing mechanism selected non-local providers multiple times during TurboFit testing, switching from:

1. Free local providers (Ornith via turbofit, MTPLX)
2. → To cloud providers (`stepfun/step-3.7-flash:free`, `anthropic/claude-fable-5.1`, etc.)

## Observed evidence

- Multiple `[System: The active model for this chat has changed to ... via provider nous]` messages
- Compression timeouts at 262K+ tokens caused fallback to cloud providers
- Config showed `model.default: z-ai/glm-5.3-flash` but system reported `anthropic/claude-fable-5.1` active

## Standing directive from Chris

> "The active model preference order should preserve explicit user choice and avoid silently switching to `stepfun/step-3.7-flash:free`" [[raw/inbox/2026-09-06.md]].

## Resolution needed

1. Ensure `model.default` is the first entry in any fallback chain
2. Pin `auxiliary.compression.provider` to a local TurboFit route (Ornith or MTPLX) rather than `auto`
3. Consider disabling compression fallback to cloud providers for local-only workflow

## Status

This stability issue may be resolved by the [[topics-wiki/turbofit/wiki/decisions/fallback-model-order.md|Fallback Model Order]] decision, pending verification that `model.default` appears first in the provider chain and compression stays pinned to local routes.

## Related

- [[topics-wiki/turbofit/wiki/decisions/fallback-model-order.md|Fallback Model Order]]
- [[topics-wiki/turbofit/wiki/concepts/model-switching-pain.md|Model Switching Pain]]
- [[topics-wiki/turbofit/wiki/concepts/compression-timeouts.md|Compression Timeouts]]
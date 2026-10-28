---
title: Model Switching Pain
created: 2026-09-07
updated: 2026-09-07
type: concept
tags:
  - turbofit
  - pain
  - routing
  - evidence
sources:
  - [raw/inbox/2026-09-07.md](../../raw/inbox/2026-09-07.md)
  - [raw/inbox/2026-09-06.md](../../raw/inbox/2026-09-06.md)
confidence: high
---

# Model Switching Pain

The active Hermes model switched multiple times during TurboFit work without Chris initiating the changes.

## Observed switches

The switch chain during this session was:

1. `meituan/longcat-2.0:free` (Nous free tier)
2. `stepfun/step-3.7-flash:free` (Nous free tier)  
3. `muse-spark-1.3-contributor-free`
4. `anthropic/claude-fable-5.1`
5. `openai/gpt-6-astra`
6. `ornith-1-5-35a3b-mlx via provider turbofit` (Chris's intended destination)

Later, the system reverted to `meituan/longcat-2.0:free` via provider nous, and then Chris switched to `ornith-1-5-35a3b-mlx via provider turbofit` at 14:25.

## Evidence of unwanted switches

From Hermes logs in [raw/inbox/2026-09-07.md](../../raw/inbox/2026-09-07.md):

- `[System: The active model for this chat has changed to meituan/longcat-2.0:free via provider nous.]` at 14:30
- `[System: The active model for this chat has changed to ornith-1-5-35a3b-mlx via provider turbofit.]` at 14:42 (after Chris's explicit directive)

## Why it matters

Unrequested model changes can invalidate benchmark context, tool routing, and session evidence. Chris wants TurboFit to stay on the chosen local runtime until he changes it himself. He explicitly stated his preference for Ornith: *"I'm actually gonna switch models to Ornith because it's smarter than the free models that we're using currently"* raw/inbox/2026-09-07.

## Root cause

Contributing causes identified in [[compression-timeouts|Compression Timeouts]]:

1. `fallback_providers` ordering that did not preserve explicit choice
2. `auxiliary.compression.provider: auto` picking a different provider/model for compression
3. Context-compression fallback to cloud providers when local compression timed out

## Related

- [[fallback-model-order|Fallback Model Order]]
- [[compression-timeouts|Compression Timeouts]]
- [[ornith-config-routing-failure|Ornith Config Routing Failure]]
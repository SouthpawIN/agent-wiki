---
title: Fallback Model Order
created: 2026-09-06
updated: 2026-09-06
type: decision
tags: [decision, preference, pain]
sources: [raw/inbox/2026-09-06.md]
confidence: high
---

# Fallback Model Order

## What

The active model preference order should preserve explicit user choice and avoid silently switching to `stepfun/step-3.7-flash:free` ^[raw/inbox/2026-09-06.md].

## Why

Chris’s project state keeps breaking because Hermes flips the active model to StepFun 3.7 Flash. Two causes appear in the transcript: `model.default` not being first in the fallback chain, and `auxiliary.compression.provider: auto` selecting StepFun for compression ^[raw/inbox/2026-09-06.md].

## When

Diagnosed 2026-09-06 02:20–02:25 UTC; config correction attempted in-session but Chris still saw later switches, including to `longcat-2.0:free` and `muse-spark-1.3-contributor-free` ^[raw/inbox/2026-09-06.md].

## Evidence

- "my model keeps switching the step 3.7 flash And that keeps screwing out my project" ^[raw/inbox/2026-09-06.md].
- "The config has `model.default: z-ai/glm-5.3-flash` but the system message shows `anthropic/claude-fable-5.1` is active" ^[raw/inbox/2026-09-06.md].

## Related

- [[topics-wiki/turbofit/wiki/concepts/model-switching-pain.md|Model Switching Pain]]
- [[topics-wiki/turbofit/wiki/decisions/main-model-selection.md|Main Model Selection]]

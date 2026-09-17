---
title: "Ornith Provider Placement — 2026-09-13"
created: 2026-09-13
updated: 2026-09-13
type: decision
tags: [decision, tool, infra]
sources: ["raw/inbox/2026-09-13.md"]
confidence: high
---

# Ornith Provider Placement — 2026-09-13

On `2026-09-13`, Chris corrected that the `ornith-1-5-35a3b` model belongs under provider **xai**, not under a TurboFit-style ("turbo fed") provider.^[raw/inbox/2026-09-13.md]

## What
- Model: `ornith-1-5-35a3b`
- Correct provider: `xai` (the system note at 16:43 / 16:52 already shows `via provider xai`).
- Erroneous placement: a "turbo fed" (TurboFit / turbosovth) provider.

## Why
- `2026-09-13 16:43` — Chris: "The only thing is you put ornith under xai not turbo fed you put under the wrong provider."^[raw/inbox/2026-09-13.md]

## Status
- Accepted: Ornith is an `xai`-provider model.
- Reinforces that provider assignments should be confirmed by verified config writes, not assumed — consistent with the provisional-lock rule.^[raw/inbox/2026-09-07.md]
- See also the active-model provider churn timeline that led to this correction.^[raw/inbox/2026-09-13.md]

## Related
- [[wiki-topics/hermes-agent/wiki/concepts/active-model-provider-churn|Active Model / Provider Churn]]
- [[wiki-topics/hermes-agent/wiki/decisions/provider-lock-review-2026-09-07|Provider Lock Review — 2026-09-07]]
- [[wiki-topics/hermes-agent/wiki/entities/model-check-20260903|Model Check — 20260903_001447_7bc70a]]

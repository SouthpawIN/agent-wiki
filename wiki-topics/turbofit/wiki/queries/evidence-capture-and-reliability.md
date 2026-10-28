---
title: Evidence Capture and Reliability Query
created: 2026-09-07
updated: 2026-09-07
type: query
tags:
  - turbofit
  - evidence
  - query
  - main-provider
sources:
  - [raw/inbox/2026-09-07.md](../../raw/inbox/2026-09-07.md)
  - raw/inbox/2026-09-07-from-senter-wiki.md
confidence: medium
---

# Evidence Capture and Reliability Query

Captures the open verification work after configuring Ornith as main, and the contested state where Hermes showed persistent timeouts after config repoint.

## Question 1

Did Hermes complete a live request through `custom:turbofit` -> `http://127.0.0.1:11613/v1` after repoint and restart?

**Answer needed**: Despite the 14:25 config change setting `providers.turbofit.api: http://127.0.0.1:11613/v1` and session metadata confirming `ornith-1-5-35a3b-mlx via provider turbofit`, persistent `Connection error` timeouts recurred at 2026-09-07T19:26:47.525Z ^[raw/inbox/2026-09-07.md]. A post-restart live capture is required to verify the routed state.

## Question 2

What is the smallest reproducible prompt that exhibits the Hermes provider timeout?

**Status**: Timeout occurred at the provider level without clear user-facing prompt dependency. The error `code: timeout, provider: turbofit, model: ornith-1-5-35a3b-mlx, error: Connection error.` suggests stale connection state rather than prompt size.

## Question 3

If the Hermes timeout was only during transition, what is the canonical approval path after restart?

**Canonical path** (per turbofit skill):

1. Verify local server health (`curl http://127.0.0.1:11613/health`)
2. Check `/v1/models` endpoint responds with `ornith-1-5-35a3b-mlx` in model list
3. Capture a real Hermes window completion via `desktop_preview open` with vision verification
4. Record approval with `CLAIM` badge on the evidence page

^[raw/inbox/2026-09-07.md]

## Related pages

- [TurboFit Evidence Capture](../../skills/turbo-fit-evidence-capture/SKILL.md)
- [[local-main-provider|Local Main Provider]]
- [[ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]

---
title: Ornith Config Routing Failure
created: 2026-09-07
updated: 2026-09-07
type: entity
tags:
  - turbofit
  - ornith
  - pain
  - routing
sources:
  - [raw/inbox/2026-09-07.md](../../raw/inbox/2026-09-07.md)
confidence: medium
---

# Ornith Config Routing Failure

After Hermes `custom:turbofit` was retargeted to `http://127.0.0.1:11613/v1` and `model.default` was set to `ornith-1-5-35a3b-mlx`, Hermes emitted repeated connection timeouts to the turbofit provider ^[raw/inbox/2026-09-07.md].

## Observed evidence

- Session metadata changed to Ornith successfully at 14:25 with `ornith-1-5-35a3b-mlx via provider turbofit` ^[raw/inbox/2026-09-07.md].
- Provider errors continued after config change:
  - `time: 2026-09-07T19:26:47.525Z` ^[raw/inbox/2026-09-07.md].
  - `layer: provider`
  - `code: timeout`
  - `provider: turbofit`
  - `model: ornith-1-5-35a3b-mlx`
  - `error: Connection error.`

## Status

The timeout persisted after the 14:25 config repoint. A Hermes session or gateway restart resolves the stale connection state. Until a post-restart verification completes, this is contested.

## Related

- [[ornith-config-routing|Ornith Config Routing]]
- [[ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]

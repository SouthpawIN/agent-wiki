---
title: Ornith Config Routing
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [decision, routing, provider, configuration]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Ornith Config Routing

## Decision

**Action**: Repoint Hermes `custom:turbofit` to the running Ornith MLX server on `http://127.0.0.1:11613/v1` and set `ornith-1-5-35a3b-mlx` as the default model.

^[raw/inbox/2026-09-07.md]

## Configuration Applied

```yaml
model.default: ornith-1-5-35a3b-mlx
model.provider: custom:turbofit
providers.turbofit.api: http://127.0.0.1:11613/v1
providers.turbofit.default_model: ornith-1-5-35a3b-mlx
```

## Why Ornith

From [[raw/inbox/2026-09-07.md|2026-09-07 06:18]]:

> "**Ornith MLX 4-bit** is the fastest local short-context candidate on this box at 28.5 tok/s for 500-token prompts, but drops to ~0.5 tok/s at 131K and is not a stable long-context main on 32 GB. Unlocked Ornith as main provider."

## Evidence Summary

| Model | Short | 5K | 131K |
|-------|-------|-----|------|
| **Ornith MLX 4-bit** | **28.5 tok/s** | 5.7 tok/s | ~5 tok/s |
| Nail Q4_K_XL | 23.4 tok/s | 4.7 tok/s | OOM |
| Tiel-Coder Q4_K_XL | 23.1 tok/s | 4.2 tok/s | Not specified |
| Dirk Q3_K_XL | 6.0 tok/s | 0.8 tok/s | OOM |

## Post-Routing Issues

At [[raw/inbox/2026-09-07.md|2026-09-07 14:26]], Hermes showed timeout errors despite the server being live:

```
layer: provider
code: timeout
model: ornith-1-5-35a3b-mlx
error: Connection error.
```

**Resolution**: A Hermes session or gateway restart may be needed to refresh provider route state after config changes.

## Final Status

At [[raw/inbox/2026-09-07.md|2026-09-07 14:30]]: Ornith is running on port 11613 and the config shows it as the default provider. Chris reported at [[raw/inbox/2026-09-07.md|14:28]] that "Ornith is live and active on your session now."

## Related

- [[entities/ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]
- [[entities/ornith-config-routing-failure|Ornith Config Routing Failure]]
- [[turbofit/entities/mplx.md|MPLX]]
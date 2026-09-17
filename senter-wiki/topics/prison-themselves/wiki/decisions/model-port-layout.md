---
title: Model Port Layout
created: 2026-09-15
updated: 2026-09-15
type: decision
tags: [decision, plan]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Model Port Layout

**What:** Each local MLX model runs on its own dedicated port so multiple can run at once.

**Why:** Chris keeps a fleet of quantized models alive simultaneously (Ornith, Bonsai, ternary Bonsai) and needs a stable, separatable handle for each.

**When:** Established 2026-09-07.

**Evidence:** The 09-07 plan was "Keep Ornith MLX running on :11613" and "Start Bonsai MLX on :11623." Both ports were confirmed live that day.^[raw/inbox/2026-09-07.md]

## Status
Confirmed live on 09-07. Ornith later needed a restart (13:15). The ternary variant was added to the set. [[topics/prison-themselves/wiki/concepts/local-mlx-model-fleet|Local MLX Model Fleet]] carries the ongoing watch-and-restart burden.

## Related
- [[topics/prison-themselves/wiki/entities/ornith-mlx|Ornith MLX]] — :11613
- [[topics/prison-themselves/wiki/entities/bonsai-mlx|Bonsai MLX]] — :11623
- [[topics/prison-themselves/wiki/entities/ternary-bonsai-mlx|Ternary Bonsai MLX]]

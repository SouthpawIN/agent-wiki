---
title: Local MLX Model Fleet
created: 2026-09-15
updated: 2026-09-15
type: concept
tags: [plan, pain]
sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-15.md]
confidence: high
---

# Local MLX Model Fleet

Chris runs a small fleet of quantized MLX models on his Mac, each on its own dedicated port. The family includes Ornith MLX (`:11613`), Bonsai MLX (`:11623`), and a 2-bit ternary Bonsai variant. [[topics/prison-themselves/wiki/entities/ornith-mlx|Ornith MLX]] and [[topics/prison-themselves/wiki/entities/bonsai-mlx|Bonsai MLX]] are the two confirmed running members.

## Dedicated ports
Each model gets a fixed port so they can run simultaneously. As of 2026-09-07 the layout was Ornith on `:11613` and Bonsai on `:11623`.^[raw/inbox/2026-09-07.md] The ports are the stable handle for each model in the set.

## Watch-and-restart pain
The fleet is not set-and-forget: models drop off and must be watched and restarted. On 2026-09-07 Chris found only Bonsai running and had to restart Ornith; he repeatedly checked "is Ornith still running or needs to be restarted."^[raw/inbox/2026-09-07.md] Keeping the whole set alive is the recurring operational burden.

## Watch-and-restart still live (nginx up, model server down)
The fleet's fragility persisted into 2026-09-15: nginx was up but the model server was not running, and it had to be started.^[raw/inbox/2026-09-15.md] This implies an nginx reverse proxy sits in front of the model servers, so the visible web layer can be healthy while the model underneath is dead — a failure mode that is easy to miss. The watch-and-restart burden is ongoing, not resolved on 09-07.

## Speed as a driver
Chris picks variants for speed — the ternary variant was added because it "might be faster." The fleet is tuned toward faster local inference. [[topics/prison-themselves/wiki/entities/ternary-bonsai-mlx|Ternary Bonsai MLX]] is the clearest expression of this.

## Related
- [[topics/prison-themselves/wiki/entities/ornith-mlx|Ornith MLX]]
- [[topics/prison-themselves/wiki/entities/bonsai-mlx|Bonsai MLX]]
- [[topics/prison-themselves/wiki/entities/ternary-bonsai-mlx|Ternary Bonsai MLX]]

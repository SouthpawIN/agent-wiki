---
title: Unleashed + DFlash2 reasoning-budget constraint
created: 2026-09-15
updated: 2026-09-15
type: concept
tags: [concept, unleashed, dflash2, reasoning, token-budget, speed, mac]
sources: [raw/inbox/2026-09-15.md]
confidence: high
---

# Unleashed + DFlash2 reasoning-budget constraint

The bottleneck for the Unleashed + DFlash2 path on 2026-09-15 was not the draft-decoding method but the token **budget** Hermes assigned to reasoning.^[raw/inbox/2026-09-15.md] Setting reasoning off recovered the story output at 85.7 tok/s, and a later same-day table showed both MTP and DFlash2 configs needing ~4000-token budgets to recover throughput with reasoning on.^[raw/inbox/2026-09-15.md]

## What the budget did

Reasoning consumed the entire token budget in the first (2000-token-budget) runs, producing empty content — the model spent its whole allowance on reasoning traces instead of the answer.^[raw/inbox/2026-09-15.md] Hermes diagnosed this repeatedly: "Empty content — Unleashed's reasoning is eating the token budget" and "The issue is Unleashed's reasoning eating the budget."^[raw/inbox/2026-09-15.md] The fix was `--reasoning off` (recovering 85.7 tok/s) and, for the reasoning-on comparison, raising the budget to 4000.^[raw/inbox/2026-09-15.md]

## Same-day budget table (reasoning ON)

| Config | Budget | Content tok/s | Reasoning eats |
|--------|--------|---------------|----------------|
| MTP | 2000 | 70.8 | 2000 (all!) |
| MTP | 4000 | **66.8** | ~2400 |
| DFlash2 | 2000 | 65.6 | 2000 (all!) |
| DFlash2 | 4000 | **70.3** | ~1400 |

Both configs needed ~4000-token budgets with reasoning on; DFlash2 was ~5% faster at decode once the budget was adequate.^[raw/inbox/2026-09-15.md] Hermes's conclusion: "The issue was never the draft method — it was the token budget."^[raw/inbox/2026-09-15.md]

## Why it matters

The budget finding reframes the earlier 131K comparison work: throughput numbers for any reasoning-enabled local path on this box must be reported with the reasoning budget stated, or they are measuring reasoning spend rather than decode speed.^[raw/inbox/2026-09-15.md] The 85.7 tok/s / 81 tok/s figures are reasoning-off and are not directly comparable to the reasoning-on ~66–70 tok/s figures.^[raw/inbox/2026-09-15.md]

## Related

- [[entities/unleashed-dflash2-working-through-hermes|Unleashed + DFlash2 working through Hermes (2026-09-15)]]
- [[concepts/mt-speculative-decoding|MTP speculative decoding]]
- [[decisions/prefer-mtplx-over-unleashed|Prefer MTPLX over Unleashed]]
- [[queries/base-qwen-dflash2-availability|base Qwen DFlash2 availability]]

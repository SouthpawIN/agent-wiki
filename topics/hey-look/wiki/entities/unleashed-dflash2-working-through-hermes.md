---
title: Unleashed + DFlash2 working through Hermes on the Mac (2026-09-15)
created: 2026-09-15
updated: 2026-09-15
type: entity
tags: [model, mac, unleashed, dflash2, speed, qwen, reasoning, budget]
sources: [raw/inbox/2026-09-15.md]
confidence: high
---

# Unleashed + DFlash2 working through Hermes on the Mac (2026-09-15)

On 2026-09-15 Hermes got the Unleashed + DFlash2 path actually working through Hermes on the Mac, after diagnosing that earlier empty-content runs were caused by reasoning eating the token budget, not by the draft method.^[raw/inbox/2026-09-15.md] The result: both models respond through Hermes with reasoning traces, DFlash2 is set up as an alternative service, and the 81 tok/s MTP config is the default.^[raw/inbox/2026-09-15.md]

## Timeline of the run

- 10:13 — Both GPUs clear; GPU 1 has 24 GB free. Started Unleashed 27B on GPU 1.^[raw/inbox/2026-09-15.md]
- 10:42 — Understood DFlash2 is a draft model for speculative decoding needing the main model via `--spec-draft-model`; set both up together on GPU 1.^[raw/inbox/2026-09-15.md]
- 11:47 — DFlash2 not yet working on Omarchy: the qwen4 llama.cpp build has no `--draft-model` flag, only `--hf-repo-draft`, which downloads from HuggingFace.^[raw/inbox/2026-09-15.md]
- 11:48 — Server up with MTP draft mode; began performance testing.^[raw/inbox/2026-09-15.md]
- 12:02 — Empty content; diagnosed Unleashed's reasoning eating the token budget.^[raw/inbox/2026-09-15.md]
- 12:06 — Restarted with `--reasoning off`.^[raw/inbox/2026-09-15.md]
- 12:08 — **85.7 tok/s** with MTP + reasoning off; the story now works (2s vs 15s); saved both configs.^[raw/inbox/2026-09-15.md]
- 12:35 — Real comparison with reasoning ON (see table below).^[raw/inbox/2026-09-15.md]
- 12:41 — Omarchy Unleashed works through Hermes (25s, reasoning included); began local Mac model test.^[raw/inbox/2026-09-15.md]
- 13:14 / 13:15 — Cleared up late-arriving earlier-test results; everything verified and working; both models respond through Hermes with reasoning traces; DFlash2 set up as an alternative service; 81 tok/s MTP config is the default.^[raw/inbox/2026-09-15.md]

## Same-day reasoning-on comparison

| Config | Budget | Content tok/s | Reasoning eats |
|--------|--------|---------------|----------------|
| MTP | 2000 | 70.8 | 2000 (all!) |
| MTP | 4000 | **66.8** | ~2400 |
| DFlash2 | 2000 | 65.6 | 2000 (all!) |
| DFlash2 | 4000 | **70.3** | ~1400 |

Both configs needed ~4000-token budgets with reasoning on; DFlash2 was ~5% faster at decode.^[raw/inbox/2026-09-15.md] Hermes's own conclusion: "The issue was never the draft method — it was the token budget."^[raw/inbox/2026-09-15.md]

## Why it matters

This is the first time the Unleashed + DFlash2 path produced real working output through Hermes on the Mac rather than only a same-day comparison figure.^[raw/inbox/2026-09-15.md] It closes the loop on the earlier 09-07 comparison: the models respond with reasoning traces, and the earlier empty-content failures are now understood to have been a token-budget cause.^[raw/inbox/2026-09-15.md] The 85.7 tok/s figure is reasoning-off and is not directly comparable to the reasoning-on ~66–70 tok/s figures.^[raw/inbox/2026-09-15.md]

## Related

- [[concepts/unleashed-dflash2-reasoning-budget|Unleashed + DFlash2 reasoning-budget constraint]]
- [[entities/unleashed-dflash2-131k-path|Unleashed + DFlash2 131K Path]]
- [[decisions/prefer-mtplx-over-unleashed|Prefer MTPLX over Unleashed]]
- [[queries/base-qwen-dflash2-availability|base Qwen DFlash2 availability]]

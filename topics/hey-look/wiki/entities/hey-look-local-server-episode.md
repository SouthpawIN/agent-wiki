---
title: hey-look local-serving episode — 2026-09-15
created: 2026-09-15
updated: 2026-09-15
type: entity
tags: [episode, mac, unleashed, dflash2, mtplx, speed, qwen, omarchy]
sources: [raw/inbox/2026-09-15.md]
confidence: high
---

# hey-look local-serving episode — 2026-09-15

A same-day episode on 2026-09-15 in which Hermes got the Unleashed + DFlash2 path actually working through Hermes on the Mac, after first resolving a reasoning-budget problem that was producing empty content.^[raw/inbox/2026-09-15.md] It also confirmed both models respond through Hermes with reasoning traces and set DFlash2 up as an alternative service, with the 81 tok/s MTP config as the default.^[raw/inbox/2026-09-15.md]

## What happened (timeline)

- 10:13 — Both GPUs clear; GPU 1 has 24 GB free. Hermes started Unleashed 27B on GPU 1.^[raw/inbox/2026-09-15.md]
- 10:42 — Hermes learned DFlash2 is a draft model for speculative decoding and needs the main model via `--spec-draft-model`; set both up together on GPU 1.^[raw/inbox/2026-09-15.md]
- 11:47 — Reported DFlash2 not yet working on Omarchy; the qwen4 llama.cpp build has no `--draft-model` flag, only `--hf-repo-draft` (downloads from HuggingFace).^[raw/inbox/2026-09-15.md]
- 11:48 — Server up with MTP draft mode; began performance testing.^[raw/inbox/2026-09-15.md]
- 12:02 — Empty content; diagnosed Unleashed's reasoning eating the token budget.^[raw/inbox/2026-09-15.md]
- 12:06 — Restarted with `--reasoning off`.^[raw/inbox/2026-09-15.md]
- 12:08 — **85.7 tok/s** with MTP + reasoning off; the story now works (2s vs 15s); saved both configs.^[raw/inbox/2026-09-15.md]
- 12:35 — Real comparison with reasoning ON (see budget table below).^[raw/inbox/2026-09-15.md]
- 12:41 — Omarchy Unleashed works through Hermes (25s, reasoning included); began local Mac model test.^[raw/inbox/2026-09-15.md]
- 13:14 / 13:15 — Cleared up late-arriving results from earlier tests; everything verified and working; both models respond through Hermes with reasoning traces; DFlash2 set up as an alternative service; 81 tok/s MTP config is the default.^[raw/inbox/2026-09-15.md]

## Same-day reasoning-on comparison

| Config | Budget | Content tok/s | Reasoning eats |
|--------|--------|---------------|----------------|
| MTP | 2000 | 70.8 | 2000 (all!) |
| MTP | 4000 | **66.8** | ~2400 |
| DFlash2 | 2000 | 65.6 | 2000 (all!) |
| DFlash2 | 4000 | **70.3** | ~1400 |

Both configs needed ~4000-token budgets with reasoning on; DFlash2 ~5% faster at decode.^[raw/inbox/2026-09-15.md]

## Outcome

- Unleashed + DFlash2 works through Hermes; the earlier 81 tok/s MTP config is the default.^[raw/inbox/2026-09-15.md]
- 85.7 tok/s is the reasoning-off MTP figure.^[raw/inbox/2026-09-15.md]
- Omarchy remains a target: Hermes had not gotten DFlash2 working on Omarchy yet (qwen4 `--hf-repo-draft` downloads from HuggingFace).^[raw/inbox/2026-09-15.md]

## Why it matters

This is the first time the Unleashed + DFlash2 path produced real, working output through Hermes on the Mac rather than only a same-day comparison figure.^[raw/inbox/2026-09-15.md] It also closed the loop on the earlier 09-07 comparison by proving the models respond with reasoning traces and by isolating the token-budget cause of the earlier empty-content failures.^[raw/inbox/2026-09-15.md]

## Related

- [[concepts/unleashed-dflash2-reasoning-budget|Unleashed + DFlash2 reasoning-budget constraint]]
- [[entities/unleashed-dflash2-131k-path|Unleashed + DFlash2 131K Path]]
- [[decisions/prefer-mtplx-over-unleashed|Prefer MTPLX over Unleashed]]
- [[queries/base-qwen-dflash2-availability|base Qwen DFlash2 availability]]

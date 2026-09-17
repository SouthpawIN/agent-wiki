---
title: "Q3K XL / Unleashed chosen as the game-adjacent model for a double-GPU device"
created: 2026-09-15
updated: 2026-09-15
type: entity
tags:
  - preference
  - tool
  - infra
  - pain
sources:
  - raw/inbox/2026-09-15.md
confidence: high
---

# Q3K XL / Unleashed chosen as the game-adjacent model for a double-GPU device

## The selection rationale

On 2026-09-15 Chris clarified *why* he settled on the Q3K XL / Unleashed model rather than it being a pure speed choice: he wants a model that co-runs alongside a game on his double-GPU device, and the Unleashed Q3K XL is the one he knows works in that configuration. ^[raw/inbox/2026-09-15.md]

> "But for my double GPU device, the Unleashed Quen, the Q3K XL, the one that I picked in there, should be the one that that should be suggesting for the very low end. I'm only picking that just so I can run a game next to it too. It's just because I know that one works and we're having issues with Quinn flash next." ^[raw/inbox/2026-09-15.md]

## Timeline

- **09:50** — Hermes reported a build at 96%, "almost done," and said it would wait for the build to finish. ^[raw/inbox/2026-09-15.md]
- **09:58** — Chris named the Unleashed Q3K XL as the model for his double-GPU device, chosen so a game can run next to it. ^[raw/inbox/2026-09-15.md]
- **10:17** — Hermes reported "Flash Next stopped, Unleashed active," then said it would check whether Unleashed is working properly. ^[raw/inbox/2026-09-15.md]
- **13:21** — Hermes reported all background processes complete and "Both models verified working through Hermes." ^[raw/inbox/2026-09-15.md]
- **17:27** — Chris restarted the desktop app on the MacBook and no longer saw the TurboFit options (see [[topics-wiki/back-where/wiki/entities/turbofit-options-missing-after-restart|TurboFit options missing after restart]]). ^[raw/inbox/2026-09-15.md]
- **18:12** — A second turn interruption: a background process (`proc_53905ab10dea`) matched watch pattern "mesh". ^[raw/inbox/2026-09-15.md]

## Co-running a game alongside the model

The practical constraint behind the choice is that the model has to sit quietly beside a game without starving it. He expects the Unleashed Q3K XL to be the model recommended for the *very low end* tier — i.e. the configuration that leaves enough GPU headroom to keep a game running next to it. ^[raw/inbox/2026-09-15.md] This extends the existing [[topics-wiki/back-where/wiki/entities/model-picker-persistence|Model picker persistence until fallback]] preference: he binds the model he picked, and its value is precisely that it is the game-adjacent one that "works." ^[raw/inbox/2026-09-15.md]

## FlashNext instability

The same utterance carries a pain: "we're having issues with Quinn flash next." The running log corroborates it — at 09:58 FlashNext was the active model and by 10:17 Hermes reported "Flash Next stopped, Unleashed active," after which it said it would check whether Unleashed is working properly. ^[raw/inbox/2026-09-15.md] So the switch from FlashNext to Unleashed was observed mid-session, and Unleashed was chosen partly because FlashNext was flaking. ^[raw/inbox/2026-09-15.md]

## Status

Unleashed (Q3K XL) is active on the double-GPU device; FlashNext had stopped. At 10:17 whether Unleashed was confirmed working was still open. By 13:21 Hermes reported all background processes complete and "Both models verified working through Hermes." ^[raw/inbox/2026-09-15.md]

## Related

- [[topics-wiki/back-where/wiki/entities/qwen3-8-27b-unleashed-selection|Qwen3.8 27B unleashed model selection]]
- [[topics-wiki/back-where/wiki/entities/model-picker-persistence|Model picker persistence until fallback]]
- [[topics-wiki/back-where/wiki/concepts/model-prefill-fallback|Prefill timeout triggering model fallback]]
- [[topics-wiki/back-where/wiki/queries/model-performance-on-m1|Model performance on M1]]

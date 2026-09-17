---
title: Add a tokens-per-second column to the TurboFit list
created: 2026-09-16
updated: 2026-09-16
type: decision
tags: [tool, ui, plan]
sources: [raw/inbox/2026-09-16.md]
confidence: high
---

# Add a tokens-per-second column to the TurboFit list

On the **TurboFit list**, Chris asked to replace the **type** column with a **tokens-per-second (tok/s)** column showing the best tok/s achieved for each model. ^[raw/inbox/2026-09-16.md]

> "On the turbo fit list, remove the type column, but instead replace that with a tokens per second column, which will show the best tokens per second that we've achieved with each one of those."

This is a TurboFit-specific table change (distinct from the Model Zoo table), so the owning fleet bot is **turbosovth**. The column records the *best* tok/s each model has achieved — a running benchmark, not a single static reading. ^[raw/inbox/2026-09-16.md]

It was immediately followed by a column-ordering request (see [[decisions/column-ordering|Column ordering]]), which moved this tok/s column to sit between Model and Parameters. ^[raw/inbox/2026-09-16.md]

## Related
- [[decisions/column-ordering|Column ordering]]
- [[concepts/model-zoo-table|Model Zoo table]]

---
title: Fit calculation system tables
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [tool, ui]
sources: [raw/inbox/2026-09-16.md]
confidence: medium
---

# Fit calculation system tables

The **fit calculation system tables** are Chris's set of tables that record how well each model *fits* a given compute platform. As named by Chris they come in three hardware classes: **GPU**, **CPU**, and **unified**. ^[raw/inbox/2026-09-16.md]

Each table is organised by **engine** and **flags** — the configuration under which a model was run — and records the **highest recorded tokens per second** achieved for that engine/flags combination. ^[raw/inbox/2026-09-16.md]

> "add a column to all of the fit calculation system tables. I mean for GPU, CPU, and unified ... put it after flags. So be like the engine and with these flags we got this tokens per second and this will be the highest one recorded."

## Structure (as of 2026-09-16)
- Three sibling tables by hardware class: **GPU**, **CPU**, **unified**. ^[raw/inbox/2026-09-16.md]
- Rows keyed by engine + flags. ^[raw/inbox/2026-09-16.md]
- Settled column order: **engine → flags → highest recorded tok/s**. ^[raw/inbox/2026-09-16.md]
- The tok/s cell holds the *highest recorded* (running best), not a single reading. ^[raw/inbox/2026-09-16.md]

These are distinct from the **Model Zoo table** (cross-model category comparison) and the **TurboFit list** (single best tok/s per model). ^[raw/inbox/2026-09-16.md] The fit tables are the hardware-classed, engine/flags view of the same tok/s data. ^[raw/inbox/2026-09-16.md]

## Related
- [[decisions/highest-recorded-tok-s-after-flags|Highest recorded tok/s after flags]]
- [[entities/turbo-fit-benchmark|TurboFit benchmark]]
- [[concepts/model-zoo-table|Model Zoo table]]

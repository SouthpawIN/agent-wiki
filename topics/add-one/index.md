---
title: add-one
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# add-one

Last updated: 2026-09-17 | Total pages: 7

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [TurboFit benchmark (best tok/s per model)](wiki/turbo-fit-benchmark.md) — The **TurboFit list** is Chris's table of models run through **TurboFit**, where each model carries a **tokens-per-second (tok/s)** column recording the *best*

### Concepts

- [Model Zoo table](wiki/model-zoo-table.md) — The **Model Zoo table** is the dashboard table that compares machine-learning models across named categories. It is the subject of all three add-one requests in

### Decisions

- [Add "parameters" as a new table category](wiki/add-parameters-category.md) — Chris asked to **add one more category to the table: parameters.** ^[raw/inbox/2026-09-16.md]
- [Column ordering on the table](wiki/column-ordering.md) — Chris set the column order on the table and then asked to drop the **order** column entirely. ^[raw/inbox/2026-09-16.md]
- [Sortable columns — click a column title to sort](wiki/column-sorting.md) — Chris wants to **sort the table by clicking a column's title** rather than some other control. ^[raw/inbox/2026-09-16.md]
- [Add a HuggingFace column to the Model Zoo table](wiki/huggingface-column.md) — The Model Zoo table was restructured: the separate **HuggingFace Models** section was removed and a **HuggingFace** column was added to the model table instead,
- [Add a tokens-per-second column to the TurboFit list](wiki/turbo-fit-tokens-per-second-column.md) — On the **TurboFit list**, Chris asked to replace the **type** column with a **tokens-per-second (tok/s)** column showing the best tok/s achieved for each model.

---

## SKILLS

No topic skills yet.

---

## BOTS

No bots yet.

---

## LOOPS

Proposed loops:

- **[fit-table-tok-s-benchmark-tracker](loops/fit-table-tok-s-benchmark-tracker.md.proposed) — owner: turbosovth · cadence: daily · status: SUGGESTED
- **[fit-table-tok-s-updater](loops/fit-table-tok-s-updater.md.proposed) — owner: turbosovth · cadence: after each run · status: SUGGESTED
- **[model-benchmark-tracker](loops/model-benchmark-tracker.md.proposed) — owner: turbosovth · cadence: daily · status: SUGGESTED
- **[turbo-fit-tok-s-updater](loops/turbo-fit-tok-s-updater.md.proposed) — owner: turbosovth · cadence: after each run · status: SUGGESTED

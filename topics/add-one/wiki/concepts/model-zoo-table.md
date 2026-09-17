---
title: Model Zoo table
created: 2026-09-16
updated: 2026-09-16
type: concept
tags: [tool, ui]
sources: [raw/inbox/2026-09-16.md]
confidence: medium
---

# Model Zoo table

The **Model Zoo table** is the dashboard table that compares machine-learning models across named categories. It is the subject of all three add-one requests in this topic. ^[raw/inbox/2026-09-16.md]

## Structure (as of 2026-09-16)
- It holds one row per model. ^[raw/inbox/2026-09-16.md]
- Categories are columns; a **parameters** category was requested to be added. ^[raw/inbox/2026-09-16.md]
- A **HuggingFace** column was added, replacing a separate "HuggingFace Models" section, with a named link to each model's repository. ^[raw/inbox/2026-09-16.md]
- Columns are meant to be sortable by clicking the column title. ^[raw/inbox/2026-09-16.md]
- Settled column order is **Model → tokens (tok/s) → parameters**; the separate **order** column was removed. ^[raw/inbox/2026-09-16.md]
- A **tokens-per-second** column records the best tok/s each model has achieved (see [[decisions/turbo-fit-tokens-per-second-column|TurboFit tok/s column]]). ^[raw/inbox/2026-09-16.md]

The table's domain (exactly which models, and what the categories compare) is still unspecified — see [[queries/table-domain-research|table domain research]]. ^[raw/inbox/2026-09-16.md]

## Related
- [[decisions/huggingface-column|HuggingFace column]]
- [[decisions/add-parameters-category|Add "parameters" as a new table category]]
- [[decisions/column-sorting|Column sorting by click]]
- [[decisions/highest-recorded-tok-s-after-flags|Highest recorded tok/s after flags]]
- [[queries/table-domain-research|table domain research]]
- [[concepts/fit-calculation-system-tables|Fit calculation system tables]]

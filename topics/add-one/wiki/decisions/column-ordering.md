---
title: Column ordering on the table
created: 2026-09-16
updated: 2026-09-16
type: decision
tags: [ui, plan]
sources: [raw/inbox/2026-09-16.md]
confidence: high
---

# Column ordering on the table

Chris set the column order on the table and then asked to drop the **order** column entirely. ^[raw/inbox/2026-09-16.md]

> "Move the tokens column to between model and parameters on that table."

Hermes confirmed the reorder: "Done. Tok/s column now sits between Model and Parameters." ^[raw/inbox/2026-09-16.md]

> "Thank you. You can also remove the order column. That's on that side."

So the settled order on the table is **Model → tokens (tok/s) → parameters**, and the separate "order" column was removed. ^[raw/inbox/2026-09-16.md]

## Related
- [[decisions/turbo-fit-tokens-per-second-column|Add a tokens-per-second column to the TurboFit list]]
- [[decisions/add-parameters-category|Add "parameters" as a new table category]]
- [[decisions/column-sorting|Column sorting by click]]
- [[decisions/highest-recorded-tok-s-after-flags|Highest recorded tok/s after flags]]
- [[concepts/model-zoo-table|Model Zoo table]]
- [[concepts/fit-calculation-system-tables|Fit calculation system tables]]

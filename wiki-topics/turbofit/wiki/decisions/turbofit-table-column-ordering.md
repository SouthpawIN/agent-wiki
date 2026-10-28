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
- [[turbofit-list-tok-s-column|Add a tokens-per-second column to the TurboFit list]]
- [[turbofit-list-parameters-column|Add "parameters" as a new table category]]
- [[turbofit-table-column-sorting|Column sorting by click]]
- [[highest-recorded-tok-s-after-flags|Highest recorded tok/s after flags]]
- [[model-zoo-table|Model Zoo table]]
- [[fit-calculation-system-tables|Fit calculation system tables]]

> Absorbed from the miscut topic `add-one` on 2026-10-28 — the TurboFit table doctrine belongs here, not in a stray topic.

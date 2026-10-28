---
title: Add a highest-recorded tok/s column after flags on the fit calculation tables
created: 2026-09-17
updated: 2026-09-17
type: decision
tags: [tool, ui, plan, spec]
sources: [raw/inbox/2026-09-16.md]
confidence: high
---

# Add a highest-recorded tok/s column after flags on the fit calculation tables

Chris asked to add a column to **all of the fit calculation system tables** — the **GPU**, **CPU**, and **unified** tables — recording the **highest recorded tokens per second**, placed **after the flags** column. ^[raw/inbox/2026-09-16.md]

> "Also add a column to all of the fit calculation system tables. I mean for GPU, CPU, and unified for recorded tokens per second, put it after flags. So be like the engine and with these flags we got this tokens per second and this will be the highest one recorded."

The column's semantics: for a given engine and its flags, the cell holds the **highest tok/s ever recorded** for that combination — a running best, not a single reading. ^[raw/inbox/2026-09-16.md]

The intended column order on each fit table is therefore **engine → flags → highest recorded tok/s**. ^[raw/inbox/2026-09-16.md]

This is a distinct surface from the Model Zoo table and the TurboFit list (see [[fit-calculation-system-tables|Fit calculation system tables]] and [[turbo-fit-benchmark|TurboFit benchmark]]): it is the *fit calculation* tables, and the column applies to all three of them (GPU, CPU, unified) at once. ^[raw/inbox/2026-09-16.md]

## Related
- [[turbofit-table-column-ordering|Column ordering]]
- [[turbofit-list-tok-s-column|TurboFit tok/s column]]
- [[fit-calculation-system-tables|Fit calculation system tables]]
- [[model-zoo-table|Model Zoo table]]
- [[turbo-fit-benchmark|TurboFit benchmark]]

> Absorbed from the miscut topic `add-one` on 2026-10-28 — the TurboFit table doctrine belongs here, not in a stray topic.

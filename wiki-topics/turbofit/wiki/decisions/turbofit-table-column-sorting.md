---
title: Sortable columns — click a column title to sort
created: 2026-09-16
updated: 2026-09-16
type: decision
tags: [plan, ui, idea, pain]
sources: [raw/inbox/2026-09-16.md]
confidence: high
---

# Sortable columns — click a column title to sort

Chris wants to **sort the table by clicking a column's title** rather than some other control. ^[raw/inbox/2026-09-16.md]

> "And could you passibly make it so I can click by the title of each column and sort by that?"

The interaction model: clicking a column header toggles sorting by that column. The phrasing ("could you possibly") reads as a hopeful request rather than a firm requirement. ^[raw/inbox/2026-09-16.md]

Hermes's response (state.db message, sim 0.08) confirms the plan: build an **HTML widget with interactive column sorting, consistent with the existing dashboard style.** ^[raw/inbox/2026-09-16.md]

> "Now for the sorting - I'll create an HTML widget with interactive column sorting, consistent with the existing dashboard style."

## Related
- [[turbofit-list-parameters-column|Add "parameters" as a new table category]]
- [[turbofit-table-column-ordering|Column ordering]]
- [[turbofit-list-tok-s-column|TurboFit tok/s column]]

> Absorbed from the miscut topic `add-one` on 2026-10-28 — the TurboFit table doctrine belongs here, not in a stray topic.

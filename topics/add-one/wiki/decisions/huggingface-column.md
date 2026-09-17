---
title: Add a HuggingFace column to the Model Zoo table
created: 2026-09-16
updated: 2026-09-16
type: decision
tags: [plan, ui, repo]
sources: [raw/inbox/2026-09-16.md]
confidence: high
---

# Add a HuggingFace column to the Model Zoo table

The Model Zoo table was restructured: the separate **HuggingFace Models** section was removed and a **HuggingFace** column was added to the model table instead, so every model carries a direct named link to its repository. ^[raw/inbox/2026-09-16.md]

This is a completed build action (Hermes state.db message, sim 0.15), distinct from the two pending table requests — the parameters category and clickable column sorting. ^[raw/inbox/2026-09-16.md]

> "Done. Removed the separate HuggingFace Models section and added a **HuggingFace** column to the Model Zoo table. Every model now has a direct link to its repository."

> "Each HuggingFace cell has a named link to the exact repo we downloaded from."

The table is the topic's Model Zoo (see [[concepts/model-zoo-table|Model Zoo table]]); this change keeps it a single table rather than a table plus a separate section. ^[raw/inbox/2026-09-16.md]

## Related
- [[decisions/column-sorting|Column sorting by click]]
- [[decisions/add-parameters-category|Add "parameters" as a new table category]]
- [[decisions/column-ordering|Column ordering]]
- [[concepts/model-zoo-table|Model Zoo table]]

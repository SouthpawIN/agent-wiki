---
title: front-matter integrations property
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [idea, spec, ui, wiki, plan]
sources: [raw/inbox/2026-09-16.md]
confidence: low
---

# front-matter integrations property

*Concept* — The proposal to make a page's integrations an explicit property inside the wiki page's YAML front matter.

^[raw/inbox/2026-09-16.md] At `2026-09-16 23:27` and again at `2026-09-16 23:35`: "Can life links be in the front matter? If so, then we should just make the integrations a property in that."

## The proposal

- If front matter can hold "life links," then integrations should be expressed as a front-matter property (e.g. `integrations: [...]`).
- This turns integrations from body prose into structured, queryable metadata — the same way title / created / updated / tags / sources already live in front matter.

## Why it matters

- Structured integrations would be machine-readable: the wiki UI, the umbrella dedupe/catalog job, and any bot that renders a page could pull integrations programmatically instead of parsing prose.
- It is the data half of the same goal as the visual restructure (integrations block moved above the overview). See [[topics-wiki/life-links/wiki/decisions/integrations-above-overview|integrations above overview restructure]].

## Open points

- Whether the front-matter schema actually supports an `integrations` property is unconfirmed — the raw entry is a question, not a decision. See [[topics-wiki/life-links/wiki/queries/life-links-in-front-matter|life links in front matter query]].

## Related

- [[topics-wiki/life-links/wiki/concepts/life-links|life links]]
- [[topics-wiki/life-links/wiki/queries/life-links-in-front-matter|life links in front matter query]]
- [[topics-wiki/life-links/wiki/decisions/integrations-above-overview|integrations above overview restructure]]
- [[topics-wiki/life-links/wiki/concepts/clickable-integrations|clickable integrations]]

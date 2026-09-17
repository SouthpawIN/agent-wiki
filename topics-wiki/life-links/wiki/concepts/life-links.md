---
title: life links
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [idea, ui, plan, wiki]
sources: [raw/inbox/2026-09-16.md]
confidence: low
---

# life links

*Concept* — Chris's idea of representing a page's external connections ("life links" / integrations) as structured, prominent data in the wiki rather than as scattered body prose.

^[raw/inbox/2026-09-16.md] At `2026-09-16 23:27`: "Can life links be in the front matter? If so, then we should just make the integrations a property in that."

## The idea

- "life links" = the links / integrations associated with a wiki page.
- Chris wants them expressed as structured data (a front-matter property), not prose in the page body.
- The question is open — the raw entry is phrased as a question ("Can life links be in the front matter?"), so whether front matter can actually hold them is unresolved. See [[topics-wiki/life-links/wiki/queries/life-links-in-front-matter|life links in front matter query]].

## Two separate moves, one goal

- **Structured:** put integrations in front matter as a property (machine-readable metadata). See [[topics-wiki/life-links/wiki/concepts/front-matter-integrations|front-matter integrations property]].
- **Prominent:** move the integrations block above the overview so it reads index-like. See [[topics-wiki/life-links/wiki/decisions/integrations-above-overview|integrations above overview restructure]].
- One change makes integrations *data*, the other makes them *first-position in the layout* — both point at integrations being prominent and structured.

## Related

- [[topics-wiki/life-links/wiki/concepts/front-matter-integrations|front-matter integrations property]]
- [[topics-wiki/life-links/wiki/queries/life-links-in-front-matter|life links in front matter query]]
- [[topics-wiki/life-links/wiki/decisions/integrations-above-overview|integrations above overview restructure]]
- [[topics-wiki/life-links/wiki/concepts/clickable-integrations|clickable integrations]]

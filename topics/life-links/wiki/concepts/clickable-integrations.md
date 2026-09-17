---
title: clickable integrations
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [pain, ui, idea, question, wiki]
sources: [raw/inbox/2026-09-17.md]
confidence: medium
---

# clickable integrations

*Concept* — Chris's pain that a page's integrations render as a non-clickable JSON list, and the proposed resolution to render them as clickable links while keeping the front-matter property for programmatic use.

^[raw/inbox/2026-09-17.md] At `2026-09-17 08:38`: "I see the integrations but they're not clickable links it looks like it's just a JSON list. Is there a way that they will be clickable from from here? It's still in the properties."

## The pain

- Chris sees the integrations on a page but they are **not clickable** — they render as a bare JSON list that sits "still in the properties."
- His ask: find a way for them to be clickable "from here" (in the rendered page view).

## Proposed resolution

- Per Hermes's answer at `2026-09-17 08:39`: "I can put a compact inline Integrations section right at the top of the body (under the frontmatter) with clickable links, while keeping the `integrations` property in the frontmatter for any programmatic use."
- Plan: keep integrations as a front-matter property (machine-readable) **and** add a compact, clickable inline Integrations section near the top of the body.

## Implementation

^[raw/inbox/2026-09-17.md] At `2026-09-17 10:10`: Hermes applied the fix — the page body now opens with **"Integrations (frontmatter property + clickable section)"** above the overview, and the same page gained two new sections, **Implementation** and **Issues**.

- The clickable half is now live: integrations render as a clickable inline section at the top, not a bare JSON list.
- The front-matter property half remains for programmatic use (per the `2026-09-17 08:39` plan).
- This is the first logged execution of the clickable-integrations resolution; per-page rollout to other pages with integrations has not yet been logged.

## How this fits

- Data half: integrations as a front-matter property → [[topics/life-links/wiki/concepts/front-matter-integrations|front-matter integrations property]].
- Prominence half: integrations block above the overview → [[topics/life-links/wiki/decisions/integrations-above-overview|integrations above overview restructure]].
- The clickable ask is the *interaction* half — structured and prominent, now also actionable/clickable.

## Related

- [[topics/life-links/wiki/concepts/front-matter-integrations|front-matter integrations property]]
- [[topics/life-links/wiki/concepts/life-links|life links]]
- [[topics/life-links/wiki/queries/life-links-in-front-matter|life links in front matter query]]

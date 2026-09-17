---
title: The standard row — every page has exactly the same layout
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [ui, preference]
sources:
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md
confidence: high
---

# The standard row — every page has exactly the same layout

Chris: "every page is going to have exactly the same layout" and "standardize and reuse elements from the front wiki page for all the other pages so you do not have to reinvent any wheels or get lost in redundancies." ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Anatomy (from `mkTopic()`, 2026-09-03 afternoon)
`[chev][title flex:1 1 auto, ellipsis][.sdots tags fixed][.usage fixed 140px, margin-left:auto][.orbs fixed 164px, flex-end = the anchor]` ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md]
- **Dots are the anchor** (`margin-left:auto`), the **title is the one flexible cell** (`flex:1 1 auto; max-width:none` — Chris: "unable to read the titles … I like all the space"; the `--orbcol` cap must not clamp titles on any page). `.thead > *:not(.tname):not(.tnameWrap):not(.sdots) { flex-shrink:0 }`. ^[raw/sources/knowledge/skill-agent-wiki-vault.md] ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]
- **"Doesn't jump"** = reserve the GROWN geometry at rest: dots cell 4×32+3×12 wide even unhovered, so right edges are identical on every row. ^[raw/sources/knowledge/skill-agent-wiki-vault.md] ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md]
- **Line up = RIGHT edge**; expansions grow toward the title (`width +N; margin-left −N`). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- Hover band + underline: `::before/::after` with `width:100vw`, `pointer-events:none` — "the underline and black bar go all the way across the screen into the dead zone, but the mouse should only activate over the title." Knob `--bandInset` (trim from the top). Stage-1 hover has `transition:none` ("very important"). ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md] ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]
- **Hover is a rest size**: "when I hover over them they don't need to grow anymore … they just need to shift up and show the card" → every orb at max instantly on row hover; single orb = lift + caption + card. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- Integration marks / GitHub octocat in rows retired ("get rid of the integration symbols"); `.sdots` bot/tag pills clip in the fixed row — planned as a hover card. ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md] ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]
- Hero = `[title][orbs centred on --dotsc]` ([[topics-wiki/senter-wiki/wiki/entities/hero-orbs|hero orbs]]). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Geometry pitfalls
- Fixed flex-basis on the title collapsed it to one letter the moment a row gained another cell ("titles are truncated to the first letter even though there is still space"). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- Geometry scoped to `#view-wiki` only broke the other views; measure on visible wiki rows and MIRROR `--rowcap/--orbcol/--dotsc` onto every `.view`. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- Measure `.thead`, not the title cell (a wrapper changed what `rowW` measured); hold `.orbMeasure` for the whole read so hover-grown geometry isn't sampled. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]
- Sticky `.hero` must out-rank every row-level z-index (hero → 40). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- Reuse machinery: rows `mkTopic()+initTopic()`, previews the generic `.topic[data-overview]` hover, one `orbColumn()` pass, `openEditor(row)`. "If you find yourself writing `#view-bots …` and `#view-loops …` variants, stop — the divergence IS the bug." ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

Ordering of rows: [[topics-wiki/senter-wiki/wiki/concepts/similarity-ranking|similarity and ranking]]. Usage cell: [[topics-wiki/senter-wiki/wiki/entities/usage-strip|usage strip]].

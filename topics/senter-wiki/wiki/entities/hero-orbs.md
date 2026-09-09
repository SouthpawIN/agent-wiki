---
title: Hero orbs — the four-dot nav
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [ui]
sources:
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# Hero orbs — the four-dot nav

## What they are
Four `.orb`s on the hero title line replacing the retired top tabs. They ARE the four primitives — first orb labelled TOPICS (was CONTEXT), then SKILLS, BOTS, LOOPS — and clicking one re-sorts the one-page list to the current term and smooth-scrolls to that section ([[topics/senter-wiki/wiki/concepts/one-page-navigation-model|navigation model]]). Numbers = the HERO TOPIC's per-lane counts; section header `.secN` is the section total. ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Geometry (final, batch 9, 2026-09-03)
Chris: "I don't like them flush with the right side — centered, exploded, equal distance on both sides across the other dots." Then: "different titles are making the four dots move … I want those four dots fixed in the center of the screen."
- `.heroOrbs { left:var(--dotsc); transform:translateX(-50%); justify-content:center }`; `--dotsc` = centre of the REAL rest rect of a row's `.orbs` after `void orbsEl.offsetWidth`.
- `alignHero()` self-corrects on centres, ≤4 passes, final Δ → `data-hero-align`. `--heroNudge` retired (0).
- `.heroTitle max-width = calc(var(--dotsc) − 123px − 28px)`.
- **Lettering leak root-caused**: the `#heroTitle` MutationObserver used to call `__alignHero` → read `ink.right` → drift per title. Now it calls `syncHeroOrbs()` ONLY; geometry runs only from `orbColumn()` (load / fonts.ready / live/loaded / resize). Proof: `scripts/pixel-span-diff.py` on longest vs shortest title screenshots → spans byte-identical `[(1535,1614),(1667,1746),(1799,1878),(1931,2010)]`. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]
Superseded stages (right-anchor `dotsRight = figLeft − 14`, `--heroNudge:3px`) are kept in the raw for history. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]

## Size and state
- Permanently at the expanded size (48px / 2.2em `!important`; later pass 40px/1.8em gap 14 in the hover-usage batch), hover = `translateY(-6px)` + `::before` label. Base `.orb` rest is 4px/`font-size:0`, so hero orbs need explicit `font-size … !important` "or only the hovered one shows a number (that bug shipped once)". ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md] ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md]
- **Active orb = the section under the hero** (scroll-spy on `#view-wiki`), drawn INVERSE: hollow ring `box-shadow:0 0 0 var(--ringW) #fff inset`, white number; hover → solid white + black glyph ([[topics/senter-wiki/wiki/concepts/hollow-vs-solid-rings|hollow vs solid]]). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- `SPY_LOCK` during programmatic jumps (orb click / ←→) released 160ms after the last scroll (700ms fallback): Chris — "they're kind of fighting each other … temporarily disable the location-based highlighting." ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- `HERO_PIN`: `pointerenter` on the strip pins the hero topic so brushing rows on the way doesn't rotate the anchor. ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md]
- `top: var(--heroOrbsTop, 16px)` (was 26) so labels clear the underline. ^[raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md]

## Keyboard
←/→ click the neighbouring orb (keeps the sort); ↑/↓ move a `.thead.kbd` cursor; Enter opens the editor. Handler on `window` in CAPTURE phase with `stopImmediatePropagation` (the composer swallows arrows otherwise); Shift+arrow is the caret. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

Dead-zone exclusion: `mousemove` must exclude `.hero` or the two right discs lose labels/size. ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md]
Related: [[topics/senter-wiki/wiki/entities/vault-live-html|vault-live.html]], [[topics/senter-wiki/wiki/concepts/standard-row-anatomy|standard row anatomy]].

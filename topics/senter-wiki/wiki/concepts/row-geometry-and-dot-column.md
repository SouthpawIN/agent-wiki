---
title: Row geometry, the dot column, hover band and usage strip
created: 2026-09-05
updated: 2026-09-06
type: concept
tags: [ui, preference, spec]
sources:
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/inbox/2026-09-05.md
  - raw/inbox/2026-09-06.md
confidence: high
---

# Row geometry and the dot column

Chris: *"every page is going to have exactly the same layout"* and *"standardize and reuse elements from the front wiki page for all the other pages so you do not have to reinvent any wheels."* THE STANDARD ROW (from `mkTopic()`, `.orbs` emitted LAST): ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

`[chev][title .tname flex:1 1 auto, max-width:none, ellipsis][.sdots tags fixed ≤160px, clipped][.usage fixed 140px][.rdiff fixed 44px][.orbs fixed 164px, flex-end = anchor]`

- Title is the ONE flexible cell — Chris: *"unable to read the titles … I like all the space"*; a fixed flex-basis collapsed titles *"to the first letter even though there is still space"* on BOTS/LOOPS. `.thead > *:not(.tname):not(.tnameWrap):not(.sdots) { flex-shrink:0 }`. ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]
- **"Doesn't jump"** = reserve the GROWN geometry at rest so neighbours never move; usage, `.rdiff`, and dots are fixed-width so all rows share both edges. ^[raw/sources/knowledge/skill-agent-wiki-vault.md] ^[raw/inbox/2026-09-06.md]

## The column (`orbColumn()`)
Measures the visible WIKI rows under `.orbMeasure` (forces rest geometry; released only after rects are read — releasing early was the *"dots snap back toward titles"* bug), writes `--rowcap/--orbcol/--dotsc` on `#view-wiki` and MIRRORS them to every `.view` (hidden views are `display:none` → zero rects). Measure `.thead`, not the title cell. `figLeft` = girl's fingertips from the sampled wall (`__figFrac`, fallback .62); `dotsRight = figLeft − 14`; `window.__deadLeft = dotsRight`. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]

## Hero orbs — centre-anchored (batch 9, FINAL)
Chris: *"I don't like them flush with the right side — centered, exploded, equal distance on both sides across the other dots"* and *"different titles are making the four dots move … I want those four dots fixed in the center of the screen."* `.heroOrbs { left:var(--dotsc); transform:translateX(-50%) }`; `alignHero()` self-corrects on centres (≤4 passes, final Δ → `data-hero-align`); `--heroNudge` retired. The lettering leak: a `#heroTitle` MutationObserver re-ran alignment reading ink rects → now it syncs NUMBERS only; geometry runs on load / fonts.ready / `live/loaded` / resize. Proof: `pixel-span-diff.py` over hover-longest vs hover-shortest screenshots → disc spans byte-identical. ([[topics/senter-wiki/wiki/decisions/2026-09-03-centre-anchored-hero-orbs|decision]]) ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]

Row-dot centering was later enforced with equal auto margins so the dot cluster stays in the middle instead of trailing the title. ^[raw/inbox/2026-09-06.md]

## Hover stages
Stage-1 (`.thead:hover`): every orb at max **48px / 2.2em instantly, `transition:none`** (Chris: *"very important"*; *"when I hover over them they don't need to grow anymore … they just need to shift up and show the card"*). Stage-2 (pointer on one orb): `translateY(-12px)` lift + caption + card, zero size change. Hero orbs 48px permanently, hover `translateY(-6px)` + label. Base `.orb` rest = 4px, `font-size:0` → mirrors need explicit `!important` rest styles. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

**Expansion origin:** the grow originates at the hovered dot — *"the third dot should still be under my mouse and everything else should grow … even if it goes to the right a little bit"* ([[topics/senter-wiki/wiki/decisions/2026-09-05-row-dots-expand-from-hovered-dot|decision]]). Implemented via `--orbShift` transform on `.orbs[data-anchored]` so the hovered orb's center stays fixed while siblings grow. ^[raw/inbox/2026-09-06.md]

## Hover band + underline
*"all the way across the screen, mouse still only activates over the title."* `.thead::before` band (`width:0→100vw`, `pointer-events:none`, `top:var(--bandInset,20px)`, `bottom:-1px`) and `::after` underline, same `.4s ease`; `isolation:isolate`, `overflow-x:clip`. Paint ≠ hit area. ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md]

## Usage strip + diff badge
*"GitHub usage chart … like a diffusion map … tiny dots"* / *"I like the dot element, tiny dots."* `WEEKS=10` × 7 as 3px `<i>` circles, alpha `0.15+0.85*sqrt(n/rowMax)`, `--usageW` 140px. Paint hook must be called from INSIDE `rerenderAll`. The `.rdiff` badge sits in a fixed 44px slot between usage and dots so nothing shifts. ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md] ^[raw/inbox/2026-09-06.md]

## Derived anchors (2026-09-04)
*"Measured, not guessed"*: feed card right edge 1128, pane edge 1152 → midpoint 1140; rocker centre 1146 → 6px left, *"exactly your number"* — set as derived, not a nudge.
Skill: `wiki-derived-anchors`. Sections and sort live in [[topics/senter-wiki/wiki/concepts/one-page-navigation-model|the navigation model]]; proof methods in [[topics/senter-wiki/wiki/concepts/verification-and-proof-methods|proof methods]]. Retired in rows: integration marks / GitHub octocat (*"get rid of the integration symbols"*). ^[raw/inbox/2026-09-05-legacy-inbox.md]

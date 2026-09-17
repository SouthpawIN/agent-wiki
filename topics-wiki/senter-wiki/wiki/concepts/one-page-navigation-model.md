---
title: One-page navigation: term, orbs as sections, sort semantics
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [ui, decision, spec]
sources:
  - raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# One-page navigation model (current = ONE PAGE, superseded three times on 2026-09-03)

Final statement, Chris: *"instead of having different pages for context, skills, bots and loops — just use the front wiki page and have that reorder by what we're
searching for … a top wiki for Topics, then below that sections for Skills, Bots, and Loops, all on the same list. Get rid of the Feed/Context page entirely; the Feed
is managed by the feed in the bottom corner."* ([[topics-wiki/senter-wiki/wiki/decisions/2026-09-03-one-page-navigation|decision]]) ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]

## Mechanics
- ONE term drives the list: typed into the hero title (`#heroGap` click → `#senterHiddenInput`) + Enter; else the hero topic (`ANCHOR`). **Empty + Enter = plain wiki**
  (clear `TERM`/`RANK`, natural order) — Chris's reset gesture.
- Four orbs (first labelled **TOPICS**) = the four sections; click → `rerenderAll()` re-sorted to the term + smooth-scroll `#view-wiki` (its own scroll container) to
  the `.secHead`. Same orb again → back to plain. Section headers carry live counts (`.secN`) and (formerly) a `ranked by relevance to "…"` caption — that caption bar
  is now *"gone for good (Chris: unasked-for)."*
- Old views `.retired`; `showView()` maps `feed|skills|bots|loops → wiki`; `.heroOrbsClone`/`--dotsc` mirroring are dead code (*"remove when convenient"*). ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Sort rules (Chris's words)
- *"consider the context of the entire topic, the entire file"* → similarity = whole-document TF-IDF cosine (`SIM.vec`), anchor row = Infinity. Cosines are low (0.12 top):
  order right, magnitudes not; a local embed server (`--provider openai`) would sharpen it.
- Skills *"not by their title, by relevance"* of their own text; bots by SOUL role; loops by prompt/cadence/bots.
- **Default list order = usage, highest first; typed search = relevance; orb pin = similarity.** One `usageOf(kind,name)` feeds both the heat chart and the sort so they
  can never disagree. ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Pinning and the spy
- `HERO_PIN` on `pointerenter` of the orb strip — rows brushed on the way must not rotate the hero (*"the sort anchored to the wrong topic"*).
- Active orb = the section under the hero (scroll-spy), drawn INVERSE (hollow ring, white number). `SPY_LOCK` during programmatic jumps — Chris: *"they're kind of fighting
  each other … temporarily disable the location-based highlighting."* Last section: when scrolled to bottom the last visible `.secHead` wins.
- Arrow keys own navigation everywhere (capture phase on `window`): ↑/↓ row cursor `.thead.kbd`, ←/→ neighbouring orb, Enter opens the card; Shift+arrow is the caret.
  Hover = keyboard focus (*"have my mouse over this pane and be able to use the arrows"*). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## History of the model (all 2026-09-03)
1. Separate pages WIKI · CONTEXT · SKILLS · BOTS · LOOPS with a cloned orb strip per page → 2. hero orbs as nav + anchor-ranked filter (`renderWiki(topics,{kind,anchor})`)
→ 3. search-first re-cut by kind (`rankByQuery`, `renderItemRank`) → 4. ONE PAGE with sections. Rule from the skill: *"when Chris restates navigation, treat the newest
statement as the whole spec."* Open: LOOPS semantics (*"we can have a back and forth about concepts"*). See [[topics-wiki/senter-wiki/wiki/concepts/row-geometry-and-dot-column|row geometry]]. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]

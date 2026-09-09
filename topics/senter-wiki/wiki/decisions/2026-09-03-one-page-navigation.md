---
title: Decision: one page — Topics/Skills/Bots/Loops as sections; Feed page removed
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, ui]
sources:
  - raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# One page (2026-09-03, supersedes three earlier models the same day)

**What.** Chris: *"just use the front wiki page and have that reorder by what we're searching for … a top wiki for Topics, then below that sections for Skills, Bots, and Loops,
all on the same list. Get rid of the Feed/Context page entirely; the Feed is managed by the feed in the bottom corner."* Implemented by RE-HOMING at startup (move the
existing lists under `#wiki-list` with `.secHead` rows; old views `.retired`), not rewriting. ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]

**Why.** One term, one list, one scroll; separate pages duplicated machinery (*"do not reinvent any wheels"*). **Traps hit doing it.** A subtree MutationObserver that wrote
counts into the tree it observed looped the page; a `R is not defined` in renderBots surfaced as "live data error" in the skills list. Verified after "discord": TOPICS 19 ·
SKILLS 124 · BOTS 9 · LOOPS 5, one scroll. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

Earlier states (kept for history): separate pages with cloned orb strips → anchor-ranked filter → search re-cut by kind. See
[[topics/senter-wiki/wiki/concepts/one-page-navigation-model|navigation model]], [[topics/senter-wiki/wiki/concepts/row-geometry-and-dot-column|row geometry]].

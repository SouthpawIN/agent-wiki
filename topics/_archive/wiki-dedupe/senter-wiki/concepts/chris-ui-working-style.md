---
title: How Chris wants UI work done (his corrections)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [preference, pain, person]
sources:
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md
confidence: high
---

# Chris's UI working style — verbatim-derived rules

- **No band-aids.** *"you had a couple things interacting with each other and … you put a band-aid over it — I would like you to not work like that."* Find the interacting
  cause; never re-nudge a constant on top. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- **Geometry as one number.** Layout rules stated in plain geometry are encoded as one derived value, not iteration; when two aligned elements differ in size, anchor
  CENTRES. Always say which way you moved it, in px (*"now +11px right"*) — he misclicked a direction prompt once. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- **Micro-increments, locked numbers.** *"shift it about 10 pixels" → "and about 30 more"*; *"shrink by one or two"* = a small step, not a redesign; rocker sensitivity
  3 % → 1.5 % → 2.2 %. Keep every tuned value a named knob — *"he tunes by feel."* ^[raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md]
- **Reverses after seeing it** — normal iteration; navigation model was restated three times in one day; treat the newest statement as the whole spec.
- **Colour is a signal.** `#FFE45A` = attention (approvals, LOCK, pending) only — *"don't like how the title turned yellow."* Black/white ink wallpaper: anything translucent
  or sub-4px reads gray → *"they look gray, not black."* Tint complaints are measured, not eyeballed. ^[raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md]
- **Fades: harder, not softer.** *"No, I like that fade … a degree or two stronger"* — when hover = solid, the rest state can be as aggressive as he likes. ^[raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md]
- **Unasked-for elements get removed, not restyled.** *"That's an element I never asked for"* → delete outright (the `ranked by …` caption bar). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- **Only X changes = touch only X**, and never reload while he is mid-placement (*"you're jumbling all around"*). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- **Drive the real UI.** *"no try again … you need to practice your computer use, not work around."* Hash deep links and node scripts are supplements. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- **Hand-placement when voice stalls** — his own idea: make it draggable, he places, says "go". ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- **Voice cuts off mid-sentence.** Ship the clear items, close with the dangling clause quoted (*"you cut off at '…' — waiting on the rest"*). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- **Dated, quoting comments** in code (`/* 2026-09-03 (Chris): "…" */`) so he can audit intent. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- **Use the product while building it** — corner feed cards are how he sees work happen; per-turn canvas contract (log.md line, queue tick). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- **Reuse, don't fork.** *"standardize and reuse elements from the front wiki page for all the other pages … do not reinvent any wheels or get lost in redundancies."*
  Writing `#view-bots …` variants = the divergence IS the bug. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- **Restarts that kill agents need his OK** (scan watcher). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- **Wording matters**: *"runs for 30 seconds"* not *"30 seconds from now"* (read as a delay). ^[raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md]

See [[topics/senter-wiki/wiki/concepts/verification-and-proof-methods|proof methods]] and [[topics/senter-wiki/wiki/concepts/row-geometry-and-dot-column|row geometry]] for where each rule bit.

---
title: Chris's UI working rules — his corrections as law
aliases:
  - How Chris wants UI work done (his corrections)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [preference, pain, ui, person]
sources:
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-palette.md
  - raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md
confidence: high
---

# Chris's UI working rules — his corrections as law

Numbered from his own words in the raw; each rule = quote → what it means. Companion to [[wiki-topics/senter-wiki/wiki/concepts/pane-driving-and-verification|verification]] and [[wiki-topics/senter-wiki/wiki/concepts/standard-row-anatomy|row anatomy]].

1. **No band-aids.** "you had a couple things interacting with each other and … you put a band-aid over it — I would like you to not work like that." Find the interacting cause; never re-nudge a constant. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
2. **Geometry as one number.** Layout rules stated in plain geometry are encoded as one derived value, not iteration ("dots flush right, all lined up" = exact row width + right anchor). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
3. **Centres, not edges.** When Δ measures 0.00 and he still sees it off, he is aligning centres: "centered — exploded, extending out equal distance on both sides across the other dots." Always say which way and how many px you moved. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
4. **Never depend on lettering.** "I'm worried the positioning is based on the lettering … different titles are making the four dots move." Anchors from reference geometry only; text mutations sync numbers, never position. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
5. **Line up = right edge; expanded = rest size.** "when I hover over them they don't need to grow anymore … they just need to shift up and show the card." ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
6. **Size feedback hits every instance** ("bigger, lettering bigger too") — rows AND hero mirror; grep stale px constants. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
7. **Colour is signal.** `#FFE45A` = attention only; rejected a yellow title. Grey is never a colour; "they look gray, not black" = opacity/anti-aliasing. ^[raw/sources/knowledge/skill-agent-wiki-vault.md] ^[raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md]
8. **Paint ≠ hit area.** Bands/underlines run 100vw with `pointer-events:none`; "the mouse should only activate over the title." ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
9. **Reuse the wiki page's machinery for every page**; per-page copies are the bug. "every page is going to have exactly the same layout." ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
10. **Restructure by re-homing, not rewriting.** ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
11. **Newest navigation statement is the whole spec** (moved three times on 09-03). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
12. **Drive the real UI**; hash entry points and node scripts are supplements. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]
13. **Don't reload while he is positioning** — "you're jumbling all around"; "Only X needs to change" = touch only X. ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
14. **Unasked-for elements get removed, not restyled.** "That's an element I never asked for." ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
15. **Overlays overlay; they don't hide the page.** "settings should not make everything else go black." ^[raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md]
16. **Instant close, no grace.** "disappear instantly if I don't have it locked"; rejected 260 ms as "delays half a second". ^[raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md]
17. **Fades he liked get pushed harder, never softened** ("a degree or two stronger"). ^[raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md]
18. **Tone is measured** — pixel triples, not vision verdicts. ^[raw/sources/knowledge/ref-vault-live-palette.md]
19. **Voice cuts off** — ship the clear items, quote the dangling clause ("you cut off at '…'"). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
20. **Comments quote him with dates** (`/* 2026-09-03 (Chris): "…" */`). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
21. **Say durations, not offsets** — "runs for 30 seconds", never "30 seconds from now". ^[raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md]
22. **Hand-placement when px-by-voice stalls** ([[wiki-topics/senter-wiki/wiki/concepts/hand-placement-mode|hand-placement mode]]). ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md]
23. **"Shrink by one or two" = a small step**, not a redesign (3.3 → 3.0em accepted). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
24. **Find every other writer before baking** a style; an inline `style.cssText` silently beats a CSS-var knob. ^[raw/sources/knowledge/skill-agent-wiki-vault.md] ^[raw/sources/knowledge/ref-vault-live-palette.md]
25. **A `.system/` file alone is invisible** — "I only see one line" → lane files + README, not more prose. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
26. **Hover = keyboard focus** ("have my mouse over this pane and be able to use the arrows"); arrows own navigation, Shift+arrow the caret. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
27. **Kill fighting behaviours explicitly** — "they're kind of fighting each other … temporarily disable the location-based highlighting" (SPY_LOCK). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
28. **Post progress into the product's own feed** while building — that's how he sees you work ([[wiki-topics/senter-wiki/wiki/entities/senter-bridge|bridge /post]]). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

Person page: [[wiki-topics/senter-wiki/wiki/entities/chris|Chris]].

## Folded from `chris-ui-working-style`

Extra detail per rule, from the same corrections:

- (rule 3) Always say which way you moved it, in px (*"now +11px right"*) — he misclicked a direction prompt once. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- (rule 23) **Micro-increments, locked numbers.** *"shift it about 10 pixels" → "and about 30 more"*; rocker sensitivity 3 % → 1.5 % → 2.2 %. Keep every tuned value a named knob — *"he tunes by feel."* ^[raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md]
- (rule 11) **Reverses after seeing it** — normal iteration; navigation model was restated three times in one day; treat the newest statement as the whole spec.
- (rule 7) `#FFE45A` = attention (approvals, LOCK, pending) only — *"don't like how the title turned yellow."* Black/white ink wallpaper: anything translucent or sub-4px reads gray. Tint complaints are measured, not eyeballed. ^[raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md]
- (rule 17) *"No, I like that fade … a degree or two stronger"* — when hover = solid, the rest state can be as aggressive as he likes. ^[raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md]
- (rule 14) *"That's an element I never asked for"* → delete outright (the `ranked by …` caption bar). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- (rule 12) **Drive the real UI.** *"no try again … you need to practice your computer use, not work around."* Hash deep links and node scripts are supplements. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- (rule 22) **Hand-placement when voice stalls** — his own idea: make it draggable, he places, says "go". ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- (rule 19) Close with the dangling clause quoted (*"you cut off at '…' — waiting on the rest"*). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- (rule 20) Dated, quoting comments in code so he can audit intent. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- (rule 28) **Use the product while building it** — corner feed cards are how he sees work happen; per-turn canvas contract (log.md line, queue tick). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- (rule 9) **Reuse, don't fork.** *"standardize and reuse elements from the front wiki page for all the other pages … do not reinvent any wheels or get lost in redundancies."* Writing `#view-bots …` variants = the divergence IS the bug. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- **Restarts that kill agents need his OK** (scan watcher). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- (rule 21) *"runs for 30 seconds"* not *"30 seconds from now"* (read as a delay). ^[raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md]

See [[wiki-topics/senter-wiki/wiki/concepts/verification-and-proof-methods|proof methods]] and [[wiki-topics/senter-wiki/wiki/concepts/row-geometry-and-dot-column|row geometry]] for where each rule bit.

## Absorbed
- `concepts/chris-ui-working-style` — 2026-09-05 → archived at `wiki-topics/_archive/wiki-dedupe/senter-wiki/concepts/chris-ui-working-style.md`

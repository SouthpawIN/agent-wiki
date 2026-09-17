# Senter Wiki — rules (Chris's standing corrections, 2026-09-03)

Every rule below is a verbatim-derived correction from Chris. They are not preferences; they are the spec.

## How work is done
1. **Root cause, never band-aids.** "You put a band-aid over it — I would like you to not work like that."
   When a visual regresses, find the interacting cause (two writers of one style, a wrapper changing a
   measurement, a filter applied after a blend) and fix THAT.
2. **Prove with the DOM, not screenshots.** "Improve your vision tools." Geometry → `getBoundingClientRect`
   read back through `document.title`; tone → `screencapture` + pixel histogram. Vision is a hint.
3. **Dated comments quoting Chris** in the code: `/* 2026-09-03 (Chris): "…" */`.
4. **Never reload while Chris is hand-placing.** Bake on "go", then strip the temp layer.
5. **Per-turn canvas contract**: `log.md` dated line + `topics-wiki/senter-wiki/.system/{session,queue}.md`.

## Design law
6. **Pure #000 and the paper white only.** No greys, no translucency for state, no gradients except the
   approved feed fade. "Every dot black." Level/state = SIZE or presence, never opacity.
7. **`#FFE45A` means attention** (pending approval, LOCK). Never for focus/typing.
8. **Dots are the right anchor of every row; hero orbs sit centred over that column and never move
   with lettering.** "Every page has exactly the same layout."
9. **"Doesn't jump" = reserve grown geometry at rest.** Anything that grows on hover has its grown size
   as its rest footprint.
10. **Hollow = selected/rest, solid = hover** for any circle that mirrors the dots (active orb, gear);
    ring width is one knob (`--ringW`).
11. **Paint may exceed the hit area, never the reverse.** Band/underline run to the screen edge via
    `pointer-events:none` pseudo-elements; the row itself stays the hit target.
12. **Cards, not pages.** Editor, settings, anything modal = a black card with a 1px paper border over
    the live wiki; click-off closes (and saves), and that click is swallowed.
13. **Overlays never dim the page.** No backdrop scrims.

## Navigation law
14. One list, four sections; orbs = sections; default order = usage; search = relevance; orb-pin = similarity.
15. Arrows are navigation everywhere (←→ sections, ↑↓ rows, Enter opens); Shift+arrow is the caret.
16. Hover = focus: mouse over the pane is enough to use the keys.
17. Nothing right of the dots activates a row; dead-zone click = SPACE; blank sky in SPACE = wiki.
18. `showView()` must never end with zero views on.

## Data law
19. Similarity considers the ENTIRE document (README + context.md, SOUL.md, SKILL.md, loop prompt).
20. Usage = real Hermes mentions per day, one series feeding both the chart and the default sort.
21. Everything goes through the wiki; bot messages land in the feed and the Hermes sidebar.

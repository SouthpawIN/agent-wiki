---
title: LOOK loop verification (proof = Chris's real window)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [ui, spec, pain, skill]
sources: [raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/sources/knowledge/looker-SOUL.md, raw/sources/knowledge/weaver-AGENTS.md, raw/inbox/2026-09-05-legacy-inbox.md]
confidence: high
---

# LOOK loop verification (proof = Chris's real window)

The fleet's verification doctrine for anything visible. Born 2026-09-02 from Chris: "refine the builder — make it use screenshots and check itself in a recursive loop… and I never know when it's done," and the harder line: **"you're entirely guessing — what you're saying is not there… instead of lying or coming up with dummy data."** Four backdrop rounds had been "proven" with fresh Playwright renders while Chris's pane showed the OLD page. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## The loop (builders, via [[topics-wiki/senter/wiki/entities/looker|looker]])
1. Numeric probes first (Playwright headless, lint) — necessary, not sufficient.
2. Screenshot at Chris's REAL Hermes window AND a reference 1280×800.
3. `vision_analyze` with the ask restated as yes/no + measured offset.
4. Fix and loop, max 3 → BLOCKED/FAIL-CONVERGENCE with offsets.
"Headless renders are measurement, never proof. Proof = this loop." Shared as skill `bot-verify-loop`; the operational form is skill `wiki-look-verify` (created 2026-09-02 at Chris's request: "write this as a skill and maybe a bot"; user-owned, curator cannot patch; addenda in `references/look-loop-addenda.md`).

## Senter's capture recipe (PROOF rule)
- Reload correctly: `desktop_preview close` (all) THEN `open` once — `open ?v=N` ADDS a tab; Chris's pane once had FOUR stacked `vault-live.html` tabs. His webview has its own localStorage (a stale `sw.wall` pick was the real "gold tint").
- `computer_use list_windows app=Hermes` → `capture pid+window_id` of the window titled `Hermes` (a 1456×31 sliver = wrong window). Off-screen (0×0) ⇒ say "not verified in your window yet" — never narrate what he "should" see.
- Vision in **Chris's exact words** ("is the hand visible, is the top of her head cut off") on region crops of the preview pane ([[topics-wiki/senter/wiki/concepts/preview-pane-viewport|pane viewport]]).
- A relational crop must CONTAIN every referenced edge (lesson 26): "dots centred between the titles and the girl" judged on a crop that started after the titles blessed a layout Chris called "the wrong way." Use a row-height strip spanning the FULL pane width.
- Cross-check on 2–3 targeted crops; full-window composites misread (a "hard vertical line" was clipped text at a crop boundary). Look at the SOURCE ASSET with vision too.
- Verify a bot's proof artifact with vision before relaying (teknium's gold strip ran the wrong direction).
- Geometry referenced to artwork is SAMPLED from rendered pixels (figure edge measured ~0.62 of image width, not the assumed 0.50).
- Hover has stages → brief as a state machine (rest → row-hover → orb-hover → leave) with a vision check per state.
- Prove environment conditionals are reachable in the real pane (fullscreen detection never fires in a `<webview>`); prefer an explicit ⚙ toggle.
- Wallpaper "soft/tinted": measure device px vs asset width (retina ≈2912 px), count stacked overlays, export ≥ dpr × viewport from the original, neutral `rgba(0,0,0,.4–.5)` dim, prove with a side-by-side against `screencapture -x` of the real desktop.
- `vision_analyze` latency: pin `auxiliary.vision` to a timed model in every profile ([[topics-wiki/senter/wiki/entities/senter-dispatch-and-sentinel|round 5]]).

## Also
Builders' own step is VERIFY LIGHT per edit / FULL once ([[topics-wiki/senter/wiki/entities/weaver|weaver]]); "Probe green ≠ human-usable" (≥44 px targets, realistic pointer paths); indicators keyed off live events aren't broken until the events are checked. On 2026-09-05 Chris re-applied the standard to the media player: "Not a demo playthrough I want to actually be live to the music." ^[raw/inbox/2026-09-05-legacy-inbox.md]

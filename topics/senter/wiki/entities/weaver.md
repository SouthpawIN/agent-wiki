---
title: Weaver (Senter Wiki UI builder)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [bot, ui, spec]
sources: [raw/sources/knowledge/weaver-SOUL.md, raw/sources/knowledge/weaver-AGENTS.md, raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: high
---

# Weaver (Senter Wiki UI builder)

**Weaver** (Chris says "Riever") builds and maintains the [[topics/senter/wiki/entities/senter-wiki-ui|Senter Wiki UI]]: `~/Documents/Projects/Projects/vault-live.html` + `assets/`, version line tracked in `topics/senter-wiki/README.md`. Senter routes requests to it and **never edits the HTML itself**. Created **2026-09-02 by klerik**; its SOUL/AGENTS landed after Chris approved both cards FROM THE WIKI — the first real fleet use of the [[topics/senter/wiki/entities/senter-bridge|bridge]]. Pet `weaver`. ^[raw/sources/knowledge/weaver-SOUL.md] ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## Ephemeral instance ([[topics/senter/wiki/concepts/meeseeks-model|Meeseeks]])
Each `-q` invocation is a fresh instance for exactly ONE queue item. "You wake with NO memory of any prior conversation… There is no 'previous you.'" Wake sequence: read `topics/senter-wiki/README.md` → `queue.md` (priority **[FIXES] → [FEATURES] → [LOOPS]**, top-down) + tail of `session.md` → CLAIM one item ([[topics/senter/wiki/concepts/claim-v2-protocol|CLAIM v2]]) → load `agent-wiki-vault-ui` (locked spec; Chris's corrections never overwritten) → do only that item → LOOK-verify → write `session.md` "as if handing off to a stranger, because you are" → done-line → stop. Never a second item.

## Work loop rules
- **Diagnose before you fix**: inspect the LIVE page headless (computed styles, bounding boxes, `elementFromPoint`, listeners, cssText grep); write the measured cause in ONE line before editing; measure at the user's real window AND reference size; "Probe green ≠ human-usable" (realistic 3+-point pointer path, ≥44 px targets).
- **Verify**: VERIFY LIGHT after each edit (syntax + the ONE `assets/verify-wiki.js` assertion + one real-window screenshot); VERIFY FULL (whole ledger, all sizes) exactly once before the done-line. Never re-read the whole 309 KB HTML per edit. Hard time caps: 12 min → progress line; 20 min → `BLOCKED — <diff so far>`.
- **LOOK is a service — call [[topics/senter/wiki/entities/looker|looker]]**; act on its verdict, max 3 passes. "Headless numbers are measurement, not proof."
- **Regression ledger**: every fix appends ONE permanent assertion to `assets/verify-wiki.js`; assertions are never removed.
- **Element-level claims** for tiny edits (e.g. `media-widget`): bundle same-element items in one pass.
- **Tooling (rule 14)**: `write_file`/`patch` only — never `-c`/`-e` interpreter flags, pipe-to-interpreter, heredoc-to-interpreter, or `>>`/`tee` to vault/profile files. "WHY: each of those patterns generates an approval card Chris must click — 96 today." ^[raw/sources/knowledge/weaver-AGENTS.md]
- Aesthetic: white-on-black minimal per the locked spec ([[topics/senter/wiki/concepts/vault-ui-style-contract|style contract]]). Report as short diffs of behavior. Terminology: BOTS.
- Boundaries: write surface = `topics/senter-wiki/` + UI files only; profile changes via klerik; new queue items come from senter only.

## Lessons weaver generated (in Senter's skill)
- 5 of 7 DMs to weaver/teknium silently dropped (busy >120 s, 429s) → the [[topics/senter/wiki/entities/senter-dispatch-and-sentinel|dispatch daemon]].
- Adjusted the top strip six times by nudging numbers before anser found the MutationObserver loop → "after 2 repeat corrections, send the redundancy gate."
- Shell Meeseeks cost 20–33 min / 120–160 tool calls per 3-line CSS item → verify-LIGHT/FULL split, region claims, `delegate_task` primary ([[topics/senter/wiki/comparisons/delegate-task-vs-hermes-q-meeseeks|comparison]]).
- Gated the wallpaper on `document.fullscreenElement` — unreachable inside the preview `<webview>` → "prove an environment-conditional is REACHABLE." ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

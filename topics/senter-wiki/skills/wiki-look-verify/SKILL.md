---
name: wiki-look-verify
description: "Verify Senter Wiki visuals via Chris's real window."
version: 1.0.0
author: senter
platforms: [macos]
metadata:
  hermes:
    tags: [ui, verification, vision, senter-wiki, looker]
    related_skills: [bot-verify-loop, computer-use, inspecting-hermes-desktop-dom]
---

# Wiki LOOK verify — proof is what Chris sees

Use when verifying ANY visual change to the Senter Wiki (or any UI Chris watches in the Hermes
preview pane). Capture CHRIS'S REAL WINDOW, judge it with vision as Chris would, then reload him
correctly — headless renders are for measuring, never for "you should see it now".

## Why this exists (lesson 25, 2026-09-02)
A full hour of backdrop 'fixes' were proven with headless Playwright renders while Chris's
actual preview pane showed the OLD page: each `desktop_preview open ?v=N` had ADDED a tab, so
the tab he was looking at never changed. Chris: "you're entirely guessing — what you're saying
is not there." Rule: a claim about what Chris sees requires a capture of Chris's window.

## The loop (every visual item, in this order)
0. **Read the pane size from his window** — `computer_use capture app=Hermes mode=ax pid=<pid> window_id=<id>`,
   then find the `AXWebArea` titled `Senter Vault — Live` in the elements JSON: its bounds
   `[x, y, w, h]` ARE the viewport (2026-09-02: 1151×834). Never assume 736 / 1040 / 1456.
   Put `w×h` verbatim in every layout brief as the PRIMARY viewport.
1. **Measure headless** (Playwright, `require(process.env.PW)`,
   `PW=/Users/sovthpaw/.hermes/hermes-agent/node_modules/playwright`) at the PANE SIZE from step 0 (dpr 2). 1456x914 / 1040x880 are SECONDARY. Lesson 27: a month of
   'proofs' at 1456 described a layout he had never seen. Numbers only: bboxes, computed styles, deltas. This is NOT proof he sees it.
2. **Reload him with ONE tab**: `desktop_preview close` (all) THEN `desktop_preview open`
   `file:///Users/sovthpaw/Documents/Projects/Projects/vault-live.html?v=<version>`.
   Never `open` without `close` first — it stacks tabs and he keeps seeing the old one.
3. **Capture his real window**: `computer_use capture app=Hermes mode=vision` with
   `pid`/`window_id` from `computer_use list_windows` (the main window is titled `Hermes`;
   a `width: 31` / `0x0` result means wrong window or off-screen — then say
   "not verified in your window" and stop; never describe what he 'should' see).
4. **Judge as Chris**: `vision_analyze` on the capture with a `region` crop of the preview
   pane (pane starts ~x=720 at 1456 wide) and a question phrased the way he phrased the ask
   ("is the whole artwork visible, is anything cut off, is the face covered, do the dots form
   a straight column, is the lettering black and readable"). Composite-first, layer-second.
   Zoom with a tighter `region` for small details (captions, caret gap, hard edges).
5. **Compare to the ask, not to the diff.** If vision disagrees with the builder's DONE,
   the builder is wrong until proven otherwise. Re-dispatch with the vision verdict quoted.
6. **Log** in `log.md` + the topic `session.md`: version, what the capture showed, path of
   the capture PNG (`~/.hermes/profiles/senter/cache/images/computer_use_*.png`).

## Builder-side (weaver / looker) proof requirements
- One 1456x914 screenshot with guide lines for geometry asks; a vision verdict quoting the
  ask; before/after numbers. Budget <=8 min / <=30 tool calls per small item.
- The at-rest composite is judged BEFORE any layer diagnosis (backdrop lesson 24).
- Anything environment-conditional (fullscreen, dpr, storage) must be proven reachable in the
  Hermes preview webview specifically (lesson 22).

## Pitfalls
- `desktop_preview read` returns kind:file for the wiki — it does not prove render state.
- `drive_preview elements` runs in the live webview but returns page elements, not styles.
- No CDP port on the packaged desktop app; do not try to attach.
- Several children editing the monolith at once inflate each other's verify cost — bundle
  same-region items into one child (region claims).

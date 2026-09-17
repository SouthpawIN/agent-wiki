---
title: central-asked
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# central-asked

Last updated: 2026-09-17 | Total pages: 7

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [Preview Pane](wiki/preview-pane.md) — The **preview pane** is Hermes Desktop's real Chromium browser, living in the **right rail**. It already ships with a tab strip (with a `+` button), a full addr

### Concepts

- [Central Area — New-Tab Requirement](wiki/central-area-tab-requirement.md) — On 2026-09-12 Chris asked for "the central area that we are looking at where the central wiki is. Next to there should be a plus sign to open a new tab on a bro
- [Concept — combine the index and the full wiki into one page](wiki/combine-index-and-full-wiki.md) — On 2026-09-16 Chris said the index and the full wiki should be ONE page, not two: "I said I wanted these combined, the index and the full wiki, there should not
- [Concept — updates not showing in the preview pane](wiki/updates-not-showing.md) — On 2026-09-16 Chris reported he couldn't see any updates to the wiki while looking at it: "I don't see any updates to it. I'm looking at the index under triple

### Decisions

- [Decision — reject the webview for the preview pane](wiki/webview-rejected.md) — On 2026-09-12 Hermes closed the hand-built `<webview>` approach and switched to the existing preview pane: it "reopened it as a URL" to get "a proper browser ta

### Comparisons

- [Comparison — webview vs preview pane](wiki/webview-vs-preview-pane.md) — | | `<webview>` (built) | Preview pane (existing) |

### Queries

- [Query — plus sign disappears when closing tabs](wiki/plus-sign-disappears.md) — On 2026-09-14 Chris reported the new-tab `+` had vanished: "in the plus sign to add another tab is gone I closed out a couple tabs, but I still want to see the

---

## SKILLS

No topic skills yet.

---

## BOTS

Proposed bots:

- **[combine-wiki-render](agents/combine-wiki-render.md.proposed) — **I see you're tired of the preview pane showing the index and then a separate full-wiki page — want me to have weaver merge them into one combined pa
- **[preview-wiki-watchdog](agents/preview-wiki-watchdog.md.proposed) — **I see the preview keeps showing the wrong wiki (TurbFit) or a stale split view — want a bot that watches the preview pane and flags when it's not re


---

## LOOPS

Proposed loops:

- **[preview-wiki-combine-check](loops/preview-wiki-combine-check.md.proposed) — owner: weaver · cadence: every day at 9am · status: SUGGESTED
- **[vault-refresh-loop](loops/vault-refresh-loop.md.proposed) — owner: weaver · cadence: every 15 minutes · status: SUGGESTED

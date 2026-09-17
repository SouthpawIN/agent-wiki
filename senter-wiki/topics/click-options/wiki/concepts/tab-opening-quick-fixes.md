---
title: Tab Opening Quick Fixes
created: 2026-09-15
updated: 2026-09-15
type: concept
tags: [ui, tool, pain, infra, idea]
sources: [raw/inbox/2026-09-14.md]
confidence: high
---

# Tab Opening Quick Fixes

## What was filed
A `hermes` working log recorded the **quick fixes for opening a new tab** — how the new-tab affordance works and the failure modes that leave you with no visible tab bar.^[raw/inbox/2026-09-14.md]

## The fixes (in order)
1. **Cmd+T** — opens a new tab via keyboard.^[raw/inbox/2026-09-14.md]
2. **Menu bar → File → New Tab**.^[raw/inbox/2026-09-14.md]
3. If tabs are open, the **+ is at the far right** of the tab bar — it may be **scrolled off-screen** if you have a lot of tabs open.^[raw/inbox/2026-09-14.md]
4. If you closed **all** tabs, **the tab bar itself hides** — use Cmd+T or File → New Tab to bring it back.^[raw/inbox/2026-09-14.md]

## Why it matters (the friction)
Two click-options failure modes surface here:
- Tabs can **scroll off** so the **+** disappears from view — you have to hunt for it.
- Closing **every** tab **hides the whole tab bar**, which then looks like the app lost its tab affordance entirely; the only recovery is a keyboard/menu command.^[raw/inbox/2026-09-14.md]

## Status
Recorded as operational reference (a `hermes` log entry). Open question: whether the **+ at the far right** and the **tab-bar-hides-when-empty** behavior is intended or a latent annoyance worth surfacing to whoever owns the tab UI. Related: [[click-options/wiki/concepts/turbofit-provider-disappeared|TurboFit Provider Disappeared]] (a different "can't find the thing I clicked" friction from the prior session).

## Notes
- The "scrolled off-screen" and "tab bar hides when all closed" notes hint at a real discoverability problem — worth a look if the tab bar keeps biting Chris. Related idea surface: [[click-options/wiki/decisions/recovery-mode-password-reset|Recovery Mode Password Reset]] (same genre of "where did the control go").

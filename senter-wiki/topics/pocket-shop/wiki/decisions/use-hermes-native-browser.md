---
title: Use Hermes-native browser for pocket-shop automation
created: 2026-09-13
updated: 2026-09-13
type: decision
tags: [preference, decision, ui, infra, plan]
sources: [raw/inbox/2026-09-12.md]
confidence: medium
---

# Use Hermes-native browser for pocket-shop automation

Chris's leaning (2026-09-12): do **not** build a custom browser for pocket-shop's browser automation — reuse Hermes's built-in
browser / Chromium (the `<webview>` engine) and drive it from within the app window, rather than "making our own." ^[raw/inbox/2026-09-12.md]

## Why
- A custom "working browser" is "a whole extra project"; Hermes already ships the engine, so reinventing it is the wrong lever. ^[raw/inbox/2026-09-12.md]
- Matches the standing preference — built-in Hermes over custom code, reuse before build.

## The webview (from the Hermes assistant, not Chris)
- Chris was told a **Browser** tab appears next to chat, and that the `<webview>` tag is "the same real Chromium engine Hermes already
  uses for preview — just repurposed as a center-docked browser with your wiki as the home page." ^[raw/inbox/2026-09-12.md]
- This is the assistant's claim about Hermes internals, cited here as evidence, not as a Chris quote.

## Still open
- Chris reports the current browser tab "doesn't seem to be working like a real browser" — unresolved whether the native webview can
  genuinely drive TCGPlayer / MTGStocks / eBay / Gmail. ^[raw/inbox/2026-09-12.md]
- Ties back to the standing open question of whether the browser automations still work after site changes. See
  [[topics/pocket-shop/wiki/queries/open-questions|Open questions]].

Related: [[topics/pocket-shop/wiki/entities/pocket-shop-repo|pocket-shop (repo)]] · [[topics/pocket-shop/wiki/queries/open-questions|Open questions]]

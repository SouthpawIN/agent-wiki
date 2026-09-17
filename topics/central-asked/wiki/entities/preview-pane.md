---
title: Preview Pane
created: 2026-09-12
updated: 2026-09-15
type: entity
tags: [tool, ui, infra]
sources: [raw/inbox/2026-09-12.md, raw/inbox/2026-09-14.md, raw/inbox/2026-09-11.md]
confidence: high
---

## The preview pane
The **preview pane** is Hermes Desktop's real Chromium browser, living in the **right rail**. It already ships with a tab strip (with a `+` button), a full address bar, back/forward controls and DevTools — everything a working browser needs.

Hermes concluded on 2026-09-12 that the hand-built `<webview>` was the wrong approach precisely because this preview pane "already has a tab strip with a `+`, a full address bar, back/forward, DevTools — everything"^[raw/inbox/2026-09-12.md]. To use it, the wiki is served over a local HTTP server and opened as a URL, which renders "a proper browser tab with the `+` button in the tab strip and a full address bar"^[raw/inbox/2026-09-12.md].

## Usage
Beyond the wiki, the preview pane doubles as the research browser — on 2026-09-14 it was the fallback when web search was unavailable (trying to reach AceStep sources)^[raw/inbox/2026-09-14.md].

## See
- [[central-area-tab-requirement|Central Area — new-tab requirement]]
- [[webview-vs-preview-pane|webview vs preview pane]]
- [[plus-sign-disappears|plus-sign query]]

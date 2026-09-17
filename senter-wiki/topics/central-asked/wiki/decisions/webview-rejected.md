---
title: Decision — reject the webview for the preview pane
created: 2026-09-12
updated: 2026-09-12
type: decision
tags: [decision, ui, infra]
sources: [raw/inbox/2026-09-12.md]
confidence: high
---

## What
On 2026-09-12 Hermes closed the hand-built `<webview>` approach and switched to the existing preview pane: it "reopened it as a URL" to get "a proper browser tab with the `+` button"^[raw/inbox/2026-09-12.md].

## Why
The custom `<webview>` lacked the tab strip, + button and address bar that Hermes's real Chromium preview pane "already has ... — everything"^[raw/inbox/2026-09-12.md]. Reusing the preview pane avoids rebuilding browser chrome.

## Open question
It's still in the right rail, not the center: the browser is "still in the **right rail**, not the center"^[raw/inbox/2026-09-12.md] — which is what Chris asked for. See [[plus-sign-disappears|plus-sign query]].

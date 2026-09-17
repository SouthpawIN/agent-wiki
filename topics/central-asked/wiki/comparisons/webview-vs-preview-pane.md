---
title: Comparison — webview vs preview pane
created: 2026-09-12
updated: 2026-09-12
type: comparison
tags: [comparison, ui, infra]
sources: [raw/inbox/2026-09-12.md]
confidence: high
---

| | `<webview>` (built) | Preview pane (existing) |
|---|---|---|
| Browser | custom-built | Hermes's real Chromium |
| Tab strip / `+` | no | yes^[raw/inbox/2026-09-12.md] |
| Address bar | no | yes^[raw/inbox/2026-09-12.md] |
| DevTools | — | yes^[raw/inbox/2026-09-12.md] |
| Position | — | right rail, not center |

Hermes concluded the `<webview>` was "the wrong approach" and that the preview pane is the right tool, opening the wiki as a URL to get the `+` button^[raw/inbox/2026-09-12.md].

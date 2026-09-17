---
title: Concept — updates not showing in the preview pane
created: 2026-09-16
updated: 2026-09-16
type: concept
tags: [pain, ui, question]
sources: [raw/inbox/2026-09-16.md]
confidence: low
---

## The report
On 2026-09-16 Chris reported he couldn't see any updates to the wiki while looking at it: "I don't see any updates to it. I'm looking at the index under triple fit and I looking in the wrong place."^[raw/inbox/2026-09-16.md]

## Context
This is a continuation of the preview-pane thread. The preview pane is Hermes Desktop's real Chromium browser in the right rail [[preview-pane|Preview Pane]], and it already carries a tab strip with a `+` button [[central-area-tab-requirement|Central Area — new-tab requirement]]. On 2026-09-12 the hand-built `<webview>` was rejected in favour of reusing that pane [[webview-rejected|reject the webview]].

## Interpretation
Two things are entangled here:
- **Content not refreshing:** "I don't see any updates to it" — the wiki content isn't appearing to update in the live preview.
- **Wrong index / wrong place:** "I'm looking at the index under triple fit" — Chris was browsing the TurbFit (he said "triple fit") index rather than the central-asked index, and concluded he's "looking in the wrong place."^[raw/inbox/2026-09-16.md]

## Related
The underlying component is the [[preview-pane|preview pane]]; the new-tab chrome question is [[plus-sign-disappears|plus-sign query]].

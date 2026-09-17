---
title: Concept — combine the index and the full wiki into one page
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [preference, ui, idea]
sources: [raw/inbox/2026-09-16.md]
confidence: high
---

## The request
On 2026-09-16 Chris said the index and the full wiki should be ONE page, not two: "I said I wanted these combined, the index and the full wiki, there should not be a index and then a full wiki. That's super fearless."^[raw/inbox/2026-09-16.md]

## What he's looking at
He traced the current render step by step: "the page that says index, turbo fit wiki, it then shows a get hub and then shows a link to the full wiki." So the preview pane currently shows an index page, then a link to a separate full-wiki page, and Chris sees that split as wrong.^[raw/inbox/2026-09-16.md]

## Interpretation
- **One surface, not two.** The index (the one-line-per-page listing) and the full wiki body should render together on a single page. "there should not be a index and then a full wiki."
- **Stated before.** He frames this as a prior decision ("I said I wanted these combined"), so it is a re-surfaced preference, not a new one.
- **Same thread as the refresh problem.** This is the second half of the 2026-09-16 preview-pane complaint: first he couldn't see updates at all [[updates-not-showing|updates not showing]], and now he's saying the page structure itself is wrong — the split index/full-wiki is what he keeps landing on.

## Context
The preview pane is Hermes Desktop's real Chromium browser in the right rail, already carrying a tab strip with a `+` button [[central-area-tab-requirement|Central Area — new-tab requirement]] [[preview-pane|Preview Pane]]. The TurbFit wiki (he says "turbo fit" / "triple fit") is what he's currently being shown. This preference sits on top of the [[webview-rejected|webview rejection]] — the pane is the right vehicle; the content layout inside it is still wrong.

## Related
The sibling complaint is [[updates-not-showing|updates not showing in the preview pane]]; the underlying component is [[preview-pane|the preview pane]].

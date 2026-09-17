---
title: Concept — 'center wiki' should be the page title
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [preference, ui, idea]
sources: [raw/inbox/2026-09-17.md]
confidence: high
---

## The request
On 2026-09-17 Chris described what the rendered panel currently shows and corrected the title: "No, it says read me on the side panel. It says read me at the very top and then center wiki is below that I want center wiki to be the title of this"^[raw/inbox/2026-09-17.md]

So the current render puts "read me" at the very top of the side panel, with "center wiki" beneath it, and Chris wants the title of the page to be **"center wiki"** — not "read me" and not the topic slug "central-asked".

## What he's looking at
He traced the render top-to-bottom: a "read me" heading at the very top, then "center wiki" below it. He's objecting to the "read me" being the title. The fix is to demote "read me" and make "center wiki" the page title.

## Interpretation
- **Title text, not layout.** The complaint is specifically about *what the title says* ("center wiki"), not where things sit.
- **Same render thread.** This is a continuation of the 2026-09-16 single-page complaint — the index and full wiki are still being rendered as a split, and now the title of that page is wrong too. [[combine-index-and-full-wiki|Combine index and full wiki]]
- **Still the preview pane.** The vehicle is the same right-rail browser [[preview-pane|Preview Pane]] that carries the tab strip and new-tab requirement [[central-area-tab-requirement|Central Area — new-tab requirement]].

## Context
The topic's own title is "central-asked", but the rendered page Chris sees is headed "read me" with "center wiki" underneath. He wants the visible page title to read "center wiki". This sits on top of the [[webview-rejected|webview rejection]] — the pane is the right vehicle; the page's title text is still wrong.

## Related
The sibling complaints are [[combine-index-and-full-wiki|combine index and full wiki]] (one page, not two) and [[updates-not-showing|updates not showing in the preview pane]]; the underlying component is [[preview-pane|the preview pane]].

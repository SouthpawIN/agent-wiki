---
title: "Decision 2026-09-05: markdown headings render as titles in the CONTEXT card"
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, ui, preference, spec]
sources:
  - raw/inbox/2026-09-05.md
confidence: high
---

# Decision 2026-09-05: markdown headings render as titles in the CONTEXT card

## What Chris said
> "I want to make sure that all of the markdown actually renders. So the title is actually pop up as titles on this stuff within the context and everything to make sure you do that." (19:18) ^[raw/inbox/2026-09-05.md]

## Root cause and fix
Hermes identified that `md()` was private to the editor's closure, so the wiki view's `typeof md==='function'` check failed and every page fell back to `<pre>`. The fix exposed it as `window.mdRender` and gave headings real `<div class="sec">` levels. ^[raw/inbox/2026-09-05.md]

## Result (19:26, DOM-proven)
The CONTEXT card now renders 256 headings (189 h2), 404 list items, quotes, tables; only 3 actual code blocks remain as `<pre>`. Wikilinks inside pages navigate within the card. ^[raw/inbox/2026-09-05.md]

## Why
Chris wants to *watch* the wiki being edited live with readable titles, not `<pre>` dumps. This continues the rule in [[wiki-topics/senter-wiki/wiki/decisions/2026-09-05-context-is-the-wiki-with-live-diffs|CONTEXT is the wiki itself]] and the collapse toward Hermes-native markdown in [[wiki-topics/senter-wiki/wiki/concepts/collapse-toward-hermes-native|collapse toward Hermes-native]].

## Tension
Wiki topic bodies are baked HTML at build time. The live renderer exposes the markdown function for editor and card rendering, but baked bodies do not automatically re-render from README.md on open. If README.md changes, the baked HTML is stale until the next build. ^[raw/inbox/2026-09-06.md]

---
title: "Collapse toward Hermes-native — \"as markdown and built in Hermes stuff as possible\""
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [preference, infra, plan, idea]
sources:
  - raw/inbox/2026-09-05.md
confidence: high
---

# Collapse toward Hermes-native

## Chris's direction (19:06)
> "I would like it to, ideally, I would like all of this to be as markdown and built in Hermes stuff as possible." ^[raw/inbox/2026-09-05.md]

Said while rejecting the first CONTEXT layout — the preference is about *how the wiki is made*, not just how it looks: the compiled pages, the diff view, the cards should be markdown rendered by Hermes-native machinery rather than bespoke code in `vault-live.html`. This is the same instinct as [[wiki-topics/senter-wiki/wiki/concepts/markdown-is-the-api|markdown is the API]] ("No chat command. No config file. No YAML wizard. Just edit markdown.") applied to the UI surface itself.

## Hermes's stated path (19:12)
> "I'll keep collapsing toward native as we go — next candidates are `hermes kanban` for claims and `hermes serve approval.*` for the cards." ^[raw/inbox/2026-09-05.md]

| Custom piece today | Native candidate | Status |
|---|---|---|
| Lock-file claims between bots | `hermes kanban` (`kanban watch` for the feed) | Not done — "lock files for now" ([[wiki-topics/senter-wiki/wiki/queries/open-items-as-of-2026-09-05|open items]]) |
| Bridge `/approve` + APPROVE/REJECT cards | `hermes serve approval.*` transport | Not done — bridge is the stand-in ([[wiki-topics/senter-wiki/wiki/entities/senter-bridge|senter-bridge]]) |
| CONTEXT card content | The topic's `wiki/*.md` rendered as-is | Done 19:12 — pages rendered by section, no synthetic counts ([[wiki-topics/senter-wiki/wiki/entities/context-card-live-diff|live diff card]]) |
| Diff painting | `diff` events from a before/after snapshot of real files | Done 19:12 |

## What it means for the compile side
Chris (19:18): *"Let's continue working looking for anything that might be useful for anyone these steps such as any kind of pre-prompting or pre-planning can be gone into when context is being sorted into the wiki."* — i.e. the sorting/compile step itself should improve through reusable, shareable prompting, not through more custom code. See [[wiki-topics/senter-wiki/wiki/concepts/compile-pre-planning|compile pre-planning]]. ^[raw/inbox/2026-09-05.md]

## Reading rule for future asks
When a UI or backend ask can be met by (a) a Hermes command/primitive plus markdown or (b) new JavaScript/Python, Chris's standing preference is (a). Custom code is a stand-in, to be listed in the table above with its native replacement.

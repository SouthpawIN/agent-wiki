---
title: 2026-09-14 — Gateway chat resets on context overflow; continue with /new
created: 2026-09-14
updated: 2026-09-14
type: decision
tags: [decision, gateway, context, overflow, workflow]
sources: [raw/inbox/2026-09-14.md]
confidence: high
---

# 2026-09-14 — Gateway chat resets on context overflow; continue with /new

## What happened

2026-09-14 22:38, a gateway chat **refused to continue the partial response** because the request no longer fit the model's context window:

> "The request no longer fits the model's context window, so the partial response was not continued. Continue in a fresh session (/new; gateway chats are reset automatically." ^[raw/inbox/2026-09-14.md]

## The rule

- **Gateway chats reset automatically** when a request exceeds the model's context window — the partial response is not continued in the same chat.
- **Resume with `/new`** to start a fresh session carrying the work forward.
- This is a **gateway/context-management behavior**, not a bug in the pipeline. Related concept: [[wiki-topics/senter/wiki/concepts/context-size-fallback-threshold|context-size fallback threshold]].

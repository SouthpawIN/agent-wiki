---
title: process-important
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# process-important

Last updated: 2026-09-15 | Total pages: 3

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [Watch-pattern rate limiting](wiki/process-rate-limiter.md) — The Senter watcher disables **watch patterns** for a process after it fires too many times too fast, then falls back to a coarser notification mode. This is the

### Concepts

- [Watch patterns disabled](wiki/watch-patterns-disabled.md) — "Watch patterns disabled" is the watcher's response to a process that trips the rate limiter repeatedly. It marks a transition from fine-grained event watching

### Decisions

- [notify_on_complete fallback](wiki/notify-on-complete.md) — Decision/behavior: when watch patterns are disabled for a process, the watcher does **not** stop tracking it — it switches to `notify_on_complete` semantics.

---

## SKILLS

No topic skills yet.

---

## BOTS

No bots yet.

---

## LOOPS

No loops yet.
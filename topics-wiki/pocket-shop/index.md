---
title: pocket-shop
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# pocket-shop

Last updated: 2026-09-13 | Total pages: 4

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [pocket-shop (repo)](wiki/pocket-shop-repo.md) — Chris's autonomous Magic: The Gathering card-trading agent, built on Hermes Agent. Repo: https://github.com/SouthpawIN/pocket-shop — Python, MIT, 7 stars / 1 fo

### Decisions

- [Portal credits unresolved](wiki/portal-credits-unresolved.md) — As of 2026-09-06, a fresh Portal lookup on the Gmail account linked to pocket-shop (`southpawinmusic@gmail.com`, "Christopher Hardwick's organisation") reports
- [Use Hermes-native browser for pocket-shop automation](wiki/use-hermes-native-browser.md) — Chris's leaning (2026-09-12): do **not** build a custom browser for pocket-shop's browser automation — reuse Hermes's built-in

### Queries

- [Open questions — pocket-shop](wiki/open-questions.md) — Things the wiki cannot answer yet because Chris hasn't said them here. Answer any of these by talking; the watcher files it to raw/inbox and the next compile fi

---

## SKILLS

No topic skills yet.

---

## BOTS

Proposed bots:

- **[portal-credit-watcher](agents/portal-credit-watcher.md.proposed) — **I see you're blocked on the missing $2,000 — want a bot that watches the Portal credits for southpawinmusic@gmail.com and alerts the moment usable b


---

## LOOPS

Proposed loops:

- **[pocket-shop-funding-check](triggers-loops/pocket-shop-funding-check.md.proposed) — owner: anser · cadence: daily · status: SUGGESTED
- **[portal-credit-sweep](triggers-loops/portal-credit-sweep.md.proposed) — owner: looker · cadence: every 2h · status: SUGGESTED

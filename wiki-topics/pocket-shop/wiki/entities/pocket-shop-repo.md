---
title: pocket-shop (repo)
created: 2026-09-05
updated: 2026-09-13
type: entity
tags: [repo, bot, loop, money, plan, ui, infra]
sources: [README.md, .system/continuity.md, raw/inbox/2026-09-05.md, raw/inbox/2026-09-08.md, raw/inbox/2026-09-12.md]
confidence: medium
---

# pocket-shop (repo)

Chris's autonomous Magic: The Gathering card-trading agent, built on Hermes Agent. Repo: https://github.com/SouthpawIN/pocket-shop — Python, MIT, 7 stars / 1 fork, created 2026-03-25, last push 2026-07-08, status DORMANT since 2026-07-08, 0 open issues. ^[README.md]

## What it is (repo's own words)
> "An autonomous AI agent that discovers, buys, prices, lists, and sells Magic cards for profit — then does it again. Not a cron script. An agent that thinks about trading, learns from every cycle, and runs 24/7 with human oversight." ^[README.md]

Capabilities the README claims: reasoning (when to buy, which sets have edge, what to list), persistent memory ("every dollar, every lesson, every mistake persists across sessions"), teachable skills, cron (wakes daily 9am to hunt opportunities), vision (card ID from photos on a local RTX 3090, no cloud API), browser automation (lists on eBay "like a human, no API keys required"), and a 9-agent fleet. ^[README.md]

## The trading loop
- senter (orchestrator) — owns the loop, holds the money, decides what to buy next.
- crow (research) — finds +EV sets via MTGStocks/Scryfall ("Set X has 23% EV, buy when fund ≥ $500").
- chizul (processor) — prices + lists ("Cards priced, eBay listings live").
- senter closes the loop: tracks sale → splits 30/30/40 → writes lesson → triggers cron. ^[README.md]

Example memory line the loop writes: `set=Innistrad Midnight Hunt | ev=18% | bought=$512 | revenue=$843`. ^[README.md]

Note: the repo's "senter" is the pocket-shop orchestrator role, not the Senter sidebar of this wiki — same name, different thing. Status of the 30/30/40 split (what the three buckets are) is not recorded anywhere in this topic yet.

## Absorbed sibling
[[wiki-topics/_archive/pocket-shop-pricing/README|pocket-shop-pricing]] — TCGPlayer price lookup via Hermes browser automation; absorbed 2026-09-02, also dormant since 2026-07-08. ^[README.md]

## Integrations named
Gmail, TCGPlayer, MTGStocks, Scryfall, eBay. ^[.system/continuity.md]

## What Chris has said
First real Chris quote about pocket-shop (2026-09-12): "I see the browser tab but it doesn't seem to be working like a real browser.
Isn't there a browser within Hermes or just a browser that we can just open within this window instead of making our own. That's gonna
be a whole extra project making a working browser and I'm pretty sure Hermes has these kinds of tools already in it that we can use."
— a lean toward reusing Hermes's built-in `<webview>`/Chromium for the shop's TCGPlayer/MTGStocks/ebay/Gmail automation instead of a
custom build. See [[wiki-topics/pocket-shop/wiki/decisions/use-hermes-native-browser|Use Hermes-native browser]]. ^[raw/inbox/2026-09-12.md]

Related: [[wiki-topics/pocket-shop/wiki/queries/open-questions|Open questions]] · [[wiki-topics/pocket-shop/README|topic README]]

---
title: pocket-shop
updated: 2026-09-02
type: topic
repo: https://github.com/SouthpawIN/pocket-shop
status: dormant
tags: [repo]
---

# pocket-shop

> Automated MTG card shop using browser automation for Gmail, TCGPlayer, and MTGStocks

**[Open on GitHub](https://github.com/SouthpawIN/pocket-shop)** · DORMANT (since 2026-07-08) · last push 2026-07-08

## Facts
- **Language:** Python
- **Stars / forks:** 7 / 1
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-03-25 · **Last push:** 2026-07-08
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-08)

## From the README

🏪 Pocket-Shop

  An autonomous AI agent that discovers, buys, prices, lists, and sells Magic cards for profit — then does it again.
  Not a cron script. An agent that thinks about trading, learns from every cycle, and runs 24/7 with human oversight.

## ⚡ Powered by Hermes Agent

This isn't a collection of scripts glued together. Pocket-Shop is a **self-improving AI trading system** built on [Hermes Agent by Nous Research](https://hermes-agent.nousresearch.com). It has:

- 🧠 **Reasoning** — decides *when* to buy, *which* sets have edge, *what* to list
- 🔁 **Memory** — every dollar, every lesson, every mistake persists across sessions
- 🎯 **Skills** — teachable playbooks the agent loads and refines on its own
- ⏰ **Cron** — wakes itself up daily at 9am to hunt new opportunities
- 👁️ **Vision** — identifies cards from photos on a local RTX 3090 (no cloud API)
- 🤖 **Browser automation** — lists on eBay like a human, no API keys required
- 👥 **Multi-agent fleet** — 9 specialized agents cooperating on the full loop

### The Trading Loop (autonomous, 24/7)

```
                    ┌──────────────────────────────────────┐
                    │         🧠 senter (orchestrator)     │
                    │   owns the loop, holds the money,    │
                    │   decides what to buy next            │
                    └──────────────┬───────────────────────┘
                                   │
           ┌───────────────────────┴────────────────────────┐
           ▼                                                 ▼
   ┌──────────────────┐                          ┌────────────────────┐
   │ 🦅 crow          │                          │ ⚙️ chizul           │
   │ research agent   │  ──MTGStocks/Scryfall──▶ │ processor agent    │
   │ finds +EV sets   │                          │ prices + lists     │
   └──────────────────┘                          └────────────────────┘
           │                                                 │
           │  "Set X has 23% EV, buy when fund ≥ $500"        │  "Cards priced, eBay listings live"
           ▼                                                 ▼
   ┌──────────────────────────────────────────────────────────────────┐
   │                    📊 senter closes the loop                     │
   │   tracks sale → splits 30/30/40 → writes lesson → triggers cron │
   └──────────────────────────────────────────────────────────────────┘
```

### What the agent *learns* after every cycle

Every completed loop writes to persistent memory:

```
MEMORY: set=Innistrad Midnight Hunt | ev=18% | bought=$512 | revenue=$843

*…truncated — full README at repo link*

## Absorbed
_Consolidated 2026-09-02 per [[topics/senter/plans/topic-consolidation-2026-09-02|topic-consolidation-2026-09-02]]. Originals live verbatim under `topics/_archive/`._

- [[topics/_archive/pocket-shop-pricing/README|pocket-shop-pricing]] — TCGPlayer price lookup system using Hermes browser automation for Pocket-Shop (absorbed 2026-09-02; was DORMANT (since 2026-07-08))

## Repos
| Repo | Link | Status | ⭐ |
|---|---|---|---|
| pocket-shop | [repo](https://github.com/SouthpawIN/pocket-shop) | DORMANT (since 2026-07-08) | 7 |
| pocket-shop-pricing | [repo](https://github.com/SouthpawIN/pocket-shop-pricing) | DORMANT (since 2026-07-08) | 1 |

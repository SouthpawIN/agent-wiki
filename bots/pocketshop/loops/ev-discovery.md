---
type: loop
slug: ev-discovery
bot: pocketshop
schedule: "0 9 * * *"
state: spec
skill: restock-ev-pick
created: 2026-11-07
---

# ev-discovery

Daily 09:00. Refresh EV candidates; run the full pick only when funded.

## Prompt

Refresh MTGStocks EV for set booster boxes in the $150–$250 band. If
`restock_balance >= 150`, run `restock-ev-pick` and write a buy order for Chris
to approve. Otherwise append a one-line price trend note and stop. Never purchase.

## Stop condition

Exit if fewer than 3 candidates clear the 30-day price-data rule; say so once.

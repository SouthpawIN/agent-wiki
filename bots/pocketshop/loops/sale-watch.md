---
type: loop
slug: sale-watch
bot: pocketshop
schedule: "0 8-23 * * *"
state: spec
skill: sale-ledger
created: 2026-11-07
---

# sale-watch

Hourly, 08:00–23:00. Detect sales and reconcile them.

## Prompt

Check the seller inbox and API for new orders since the last run. For each,
run `sale-ledger`. Alert Chris only for sales above $20 or unmatched orders;
batch the rest into a single line. Update `data/inventory.json` and
`data/finance.json`.

## Stop condition

One pass per hour, no retry storms on auth failure — report the auth error and
stop until it is fixed.

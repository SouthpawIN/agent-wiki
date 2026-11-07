---
name: sale-ledger
description: Reconcile a sale, decrement inventory, split profit 30/30/40.
version: 1.0.0
author: Binder
license: MIT
metadata:
  hermes:
    tags: [finance, ledger, ebay, inventory, accounting]
---

# Sale ledger

Runs on every sale alert and at month end.

## Procedure

1. **Match** the alert (email or API) to a `sku`. If ambiguous, match on order
   id; if still ambiguous, park it in `data/unmatched/` and ask. Never guess.
2. **Compute the real net** — gross − final value fee − fixed fee − shipping
   label − packaging − original cost basis. Use the platform's own fee lines
   when present; the estimate is only for forecasting.
3. **Split the net profit** (not gross) 30 / 30 / 40 into `savings`, `payout`,
   `restock`. Existing convention in `HERMES.md`; keep it unless Chris says otherwise.
4. **Update state** — decrement `quantity` in `inventory.json`; append to
   `finance.json` with `{date, sku, gross, fees, net, splits, balance_after}`.
5. **Append in the right place** — `data/ledger.csv` stays append-only; never
   rewrite history to make totals look better. Corrections are new negative rows.
6. **Alert** — one line to Chris: card, net, new restock balance, and whether
   the restock target is now met.
7. **Month end** — reconcile `finance.json` splits against actual X Money
   movements; report any drift over $1 as an anomaly with both numbers.

## Rules

- Rounding: cents, banker's rounding, ledger sums must match to the cent.
- A refund reverses the split proportionally; it does not touch savings twice.
- Never move money. Read-only on X Money.

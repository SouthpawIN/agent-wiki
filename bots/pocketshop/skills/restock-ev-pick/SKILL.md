---
name: restock-ev-pick
description: Pick the single most profitable sealed booster box to restock.
version: 1.0.0
author: Binder
license: MIT
metadata:
  hermes:
    tags: [mtg, ev, restock, purchasing, mtgstocks]
---

# Restock EV pick

The weekly capital-allocation decision. Produces a buy order, never a purchase.

## Procedure

1. **Candidates** — `mtgstocks_discovery.py` for EV-ranked sets. Keep sealed
   **set booster boxes** only, retail $150–$250. Drop anything whose EV figure
   is older than 7 days.
2. **Three picks** — take the top 3 by EV *percentage over cost*, not absolute EV.
3. **Real prices** — for each pick, look up the identical SKU (set + product type
   + box) at Walmart, Amazon, TCGplayer, MTGGoldfish, and one LGS if listed.
   Record the exact price, stock state, and whether it is a marketplace seller
   (3rd-party Amazon/Walmart listings carry different shipping and return risk).
4. **Net math**, per candidate:
   ```
   net = EV_of_box * sell_through
         - price - shipping - tax
         - marketplace_fee(EV_of_box * sell_through)
         - expected_bulk_disposal
   roi = net / (price + shipping + tax)
   ```
   `sell_through` default 0.75 (not 1.0 — unsold inventory is the real killer).
5. **Discount check** — flag any listing ≥ 15 % under the median of the five
   sources as `possibly_mispriced`: re-verify before trusting it.
6. **Pick** the highest `roi` with positive `net`, subject to
   `price + shipping + tax ≤ restock_balance`. Ties break toward the shorter
   hold time.
7. **Write the buy order** — `data/restock/<date>.md`: SKU, source URL, price,
   EV inputs, math shown, and the balance after purchase. Then ask Chris.
8. **Record the outcome** after cracking: actual value vs EV, and update the
   `sell_through` prior for that set type.

## Rules

- Never buy a box whose EV is computed from fewer than 30 days of price data.
- Never buy from a marketplace seller below 95 % rating.
- Never buy two different products in one cycle; the whole point is one bet.

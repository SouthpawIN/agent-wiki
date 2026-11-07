---
name: draft-listing-pipeline
description: Scan, identify, price and draft eBay listings for a batch of MTG cards.
version: 1.0.0
author: Binder
license: MIT
metadata:
  hermes:
    tags: [mtg, ebay, listing, vision, inventory]
---

# Draft listing pipeline

Input: a stack of cards in the flatbed. Output: rows in `data/inventory.json`
with `status: draft` and a saved draft listing per card. Publishes nothing.

## Procedure

1. **Scan** each card at ≥ 600 dpi, color. One card per pass.
   `scanimage --device "$SCANNER" --resolution 600 --format=png -o card.png`
2. **Normalize** — deskew, crop to the card border, resize to 800 px on the long
   edge, white balance. Reject and re-scan if the border is not detected.
3. **Identify** — `auto_card_processor.py` runs vision for name + set symbol.
   Confirm against Scryfall by exact `set` + `collector_number`; if the number is
   illegible, match name + set and flag `needs_human: id`.
4. **Condition** — never self-assign NM from a photo. Default `Near Mint` only
   if the card is from a sealed box and unplayed; otherwise `Lightly Played` and
   note the defect. This is the number Chris gets in trouble for.
5. **Price** — `tcgplayer_price_lookup.py`:
   - list at `market` for cards > $5;
   - list at `market + 8 %` for cards < $5 to absorb fees;
   - refuse to list under $1 net (bin them into a bulk lot instead).
   Store `market`, `low`, `mid`, `priced_at` (UTC), and `source_url`.
6. **Draft** — title `MTG <Name> <Set> <#/total> <Rarity> <Condition>`;
   item specifics from Scryfall; photos = front, back, corner close-up;
   shipping policy per card class; quantity 1.
7. **Write the row** — `{sku, name, set, collector_number, condition, price,
   cost_basis, listing_id, status: draft, scanned_at}`.
8. **Report** — one line per card: name, price, and flags. Then a batch summary:
   count, gross if all sell, total fees, net.

## Stop conditions

- Vision confidence < 0.8 → `needs_human`, do not guess a printing.
- Price lookup fails → leave `price: null`, card stays draft. A guessed price is
  worse than a missing one.
- Duplicate SKU already listed → merge quantity, do not create a second listing.

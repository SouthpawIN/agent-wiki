---
title: pocket-shop-pricing
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/pocket-shop-pricing
status: dormant
tags: [repo]
---

# pocket-shop-pricing

> TCGPlayer price lookup system using Hermes browser automation for Pocket-Shop

**[Open on GitHub](https://github.com/SouthpawIN/pocket-shop-pricing)** · DORMANT (since 2026-07-08) · last push 2026-07-08

## Facts
- **Language:** Python
- **Stars / forks:** 1 / 0
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-03-26 · **Last push:** 2026-07-08
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-08)

## From the README

# TCGPlayer Price Lookup System

Browser automation system for looking up Magic: The Gathering card prices on TCGPlayer using Hermes Agent browser tools.

## Overview

This system uses Hermes' built-in browser automation capabilities to:
- Navigate to TCGPlayer search pages
- Extract price information from search results
- Support set-specific lookups (e.g., "Black Lotus LEA")
- Parse multiple price points (market price, low price, etc.)

## Features

- **No API Key Required** - Uses public-facing website, no authentication needed
- **Set-Specific Lookups** - Filter by set code for accurate pricing
- **Multiple Price Extraction** - Captures market price, low price, and list prices
- **Hermes Integration** - Works with Hermes browser tools natively

## Installation

```bash
cd ~/Documents/ObsidianVault/Pocket-Shop/Source/tcgplayer-pricing
```

No additional Python packages required - uses Hermes built-in tools.

## Usage

### Command Line

```bash
# Basic search
python3 tcgplayer_lookup.py "Lightning Bolt"

# Set-specific search
python3 tcgplayer_lookup.py "Black Lotus" LEA

# Search with spaces in name
python3 tcgplayer_lookup.py "Thassa's Oracle"
```

### Programmatic Usage

```python
from tcgplayer_lookup import TCGPlayerPriceLookup

client = TCGPlayerPriceLookup()

# Search for a card
results = client.search_and_extract_prices("Lightning Bolt", "M15")

print(f"Found {len(results['prices'])} price points")
for p in results['prices']:
    print(f"  - ${p['price']:.2f}")
```

## Hermes Browser Tools Used

| Tool | Purpose |
|------|--------|
| `browser_navigate` | Navigate to TCGPlayer search page |
| `browser_snapshot` | Get text-based page representation |
| `browser_click` | Click on elements (e.g., filter buttons) |
| `browser_type` | Type into search box |
| `browser_press` | Press Enter to submit search |
| `browser_scroll` | Scroll for more results |
| `browser_close` | Clean up browser session |

## Output Format

The system returns a dictionary with:

```json
{
  "card_name": "Lightning Bolt",
  "set_code": "M15",
  "prices": [
    {
      "type": "market_price",
      "price": 1.25,
      "raw_text": "Market Price: $1.25"
    }
  ],
  "set_specific_price": {
    "card_name": "Lightning Bolt",
    "set_code": "M15",
    "price": 0.99
  }
}
```

## Integration with Pocket-Shop

This module integrates into the larger Pocket-Shop system:

```python
from tcgplayer_lookup import TCGPlayerPriceLookup

def get_card_price(card_name: str, set_code: str = None) -> float:
    """Get market price for a card."""
    client = TCGPlayerPriceLookup()

*…truncated — full README at repo link*


## Archived
Archived 2026-09-02 — absorbed into [[topics-wiki/pocket-shop/README|pocket-shop]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.

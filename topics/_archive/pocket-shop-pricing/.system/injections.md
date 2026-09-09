# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: pocket-shop-pricing
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/pocket-shop-pricing-f157f5d286.md"]
confidence: medium
---

# pocket-shop-pricing

## Current context

TCGPlayer price lookup system using Hermes browser automation for Pocket-Shop # TCGPlayer Price Lookup System Browser automation system for looking up Magic: The Gathering card prices on TCGPlayer using Hermes Agent browser tools. ## Overview This system uses Hermes' built-in browser automation capabilities to: - Navigate to TCGPlayer search pages - Extract price information from search results - Support set-specific lookups (e.g., "Black Lotus LEA") - Parse multiple price points (market price, low price, etc.) ## Features - **No API Key Required** - Uses public-facing website, no authentication needed - **Set-Specific Lookups** - Filter by set code for accurate pricing - **Multiple Price Extraction** - Captures market price, low price, and list prices - **Hermes Integration** - Works with Hermes browser tools natively ## Installation No additional Python packages required - uses Hermes built-in tools. ## Usage ### Command Line ### Programmatic Usage ## Hermes Browser Tools Used | Tool | Purpose | |------|--------| | `browser_navigate` | Navigate to TCGPlayer search page | | `browser_snapshot` | Get text-based page representation | | `browser_click` | Click on elements (e.g., filter buttons) | | `browser_type` | Type into search box | | `browser_press` | Press Enter to submit search | | `browser_scroll` | Scroll for more results | | `browser_close` | Clean up browser session | ## Output Format The system returns a dictionary with: ## Integration with Pocket-Shop This module integrates into the larger Pocket-Shop system: ## Notes - TCGPlayer pages load dynamically; includes delay for page rendering - Price patterns may change as TCGPlayer updates their site - For best results, use specific set codes when available

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/pocket-shop-pricing` (`2026-07-08T20:37:25Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/agent-fleet|Agent Fleet]]
- [[concepts/automation-event-systems|Automation Event Systems]]

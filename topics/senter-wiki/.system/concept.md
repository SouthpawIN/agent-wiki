# Senter Wiki — concept (2026-09-03)

**One page. One term. Everything live.**

The Senter Wiki (`vault-live.html`) is Chris's window onto the fleet. It renders the GOOP vault
(`~/Documents/Projects/Projects`) as ONE scrolling list with four sections — **TOPICS · SKILLS ·
BOTS · LOOPS** — fed by `.system-live.json`, which the scanner rewrites on every vault change.

## Navigation model (current — supersedes all earlier page-based models)
- The four **hero orbs** above the underline ARE the four sections. Click / ← → → the list re-sorts
  and smooth-scrolls to that section. The orb for the section under the hero is drawn **hollow**
  (transparent, 1px paper ring, paper number); the others solid.
- **Default order = usage** (mentions of the item in Hermes over the last 10 weeks — the same series
  the per-row heat chart paints), highest first.
- **Typed search + Enter** → every section ranked by relevance to the term. **Empty + Enter** → plain wiki.
- **Orb click with no search** → sections sorted by whole-document TF-IDF similarity to the hero
  topic (pinned when the pointer enters the orb strip, so brushing rows on the way can't change it).
- **↑ ↓** move a row cursor (same paint as hover); **Enter** opens it; **Shift+arrow** = caret when typing.
- **Dead zone** right of the dots: click → SPACE (star map). SPACE: hover a star for its label,
  click a star → its row, click the hub or blank sky → back to the wiki. HUD, feed and player hide in SPACE.

## Anatomy of a row
`[chev][title …flex][usage heat chart 10w×7d, fixed 140px][dots ×4 = right anchor]` — identical on
every section. Hover: black band + underline wipe to the screen edge (paint only; hit area = the row).

## Content card (the "editor")
Hover the hero overview → a black card (1px paper border) peeks under it; click → pinned & editable;
click outside → saves and closes. Bottom bar: **SHARE** (context/skills/bots/loops toggles → COPY as
markdown, or SEND TO HERMES). Settings is the same kind of card, under the gear.

## Tone
Pure black + one paper colour (`--paper`, cool blue-white). The girl on the wallpaper is the picture
used as a luminance mask over a flat `--paper` fill, so her ink IS the UI white. `#FFE45A` = attention only.

## Live surfaces
- **Feed** (bottom-right stack, diagonal fade, hover → solid, expands over everything): bot messages,
  approvals (yellow border while pending), vault writes — via the bridge `POST /post`.
- **Headphone EQ** (`#hpEq`): 7×6 all-black dots on her ear-cup, driven by the player's audio.
- **Usage heat charts**: per item per day from `~/.hermes/state.db` `messages_fts`.

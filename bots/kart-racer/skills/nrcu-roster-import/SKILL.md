---
name: nrcu-roster-import
description: Derive the playable cast from the NRCU character bible.
version: 1.0.0
author: Apex
license: MIT
metadata:
  hermes:
    tags: [nrcu, roster, unity, data]
---

# NRCU roster import

Source of truth: `123mikeyd/Nous_Research_Cinematic_Universe` — `characters/*.md`
profiles and `images/previews/*.webp`. 35 characters as of 2026-11-07, including
`Turbo Fit / Sovthpaw`.

## Procedure

1. Fetch the character directory and each profile's front matter (display name,
   tags, any stated role/allegiance).
2. Emit `Assets/Roster/roster.json`:
   ```json
   {"slug":"sovthpaw","display":"Turbo Fit / Sovthpaw","portrait":"Roster/Portraits/sovthpaw.webp",
    "weight":"medium","stats":{"speed":7,"accel":6,"handling":8,"weight":6},
    "credit":"Character by sovthpaw; art credits per NRCU CREDITS.md"}
   ```
3. **Weight classes**: light / medium / heavy, assigned from the profile's stated
   build or role, not from guesswork. Keep a `source_note` per entry so a human
   can audit why a character is heavy.
4. **Never overwrite** an entry with `"locked": true` — those are hand-tuned.
5. Copy portraits into `Assets/Roster/Portraits/`, convert to the URP texture
   settings, and generate a `Credits.md` in the project listing every artist.
6. Validate: 35 entries, unique slugs, every portrait path exists, every entry has
   a credit string.

## Rules

- A character whose art is uncredited does not ship. Ask, don't assume.
- Never invent lore or abilities not implied by the profile.
- Keep `sovthpaw` in the public spelling; "Turbo Fit" is the character's name in
  the NRCU, "sovthpaw" is the person to credit.

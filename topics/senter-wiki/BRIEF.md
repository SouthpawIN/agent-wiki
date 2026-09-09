# BRIEF — senter-wiki
_Pre-prompt for the cutter and this topic's agent. Chris edits freely; lines ending `<!-- chris -->` are never rewritten._

## What this topic is
The wiki SURFACE: vault-live.html and everything Chris sees and touches — rows, dots, hero orbs, hover/pinned cards, the CONTEXT wiki view and its diffs, side feed, media player, volume rocker, headphone EQ, settings card, SPACE star map, palette, layering, animations — plus the scanner and bridge routes that feed it.

## Belongs here (scope)
- Any visual/interaction request: position, size, colour, timing, z-order, hover, scroll, keyboard, diff rendering, markdown rendering
- UI knobs and their Chris-tuned values; DOM-proof recipes; things Chris said 'looks' or 'feels' a certain way
- Scanner snapshot fields, bridge /stage /file /post as they serve the UI

## Does NOT belong here (anti-scope → route elsewhere)
- WHY the system is organised a certain way, bot roles, approvals policy, workflow order → `senter`
- Music sources/auth (Spotify id, yt-dlp) → `music`; the player as video surface → `youtube`
- TurboFit → `turbofit`

## Aliases (the cutter binds hard on these words)
- senter wiki
- the wiki
- vault-live
- card
- cards
- dots
- dot
- orb
- orbs
- rocker
- volume
- mute
- eq
- headphones
- feed
- side chat
- media player
- settings
- hover
- diff
- markdown
- render
- pixels
- pixel
- layout

## Lens — how to read new context for this topic
- Every UI sentence from Chris is a spec: capture the exact words, the element, the direction/amount, and the reason he gave.
- 'I don't like X' = a rule about X, dated; the previous state goes into the page as superseded.
- Distinguish a KNOB change (value) from a BEHAVIOUR change (logic) from a LAYOUT rule (constraint) — three different page types.
- Note what was DOM-proven and how (the proof is part of the record).

## Standing preferences (apply to every suggestion)
- Root causes, never band-aids. Everything live and visible. Markdown + built-in Hermes over custom code.
- Bots first, then loops; reuse a fleet bot when one fits; skills auto-apply. No pitches about the build process itself.

## What a good suggestion looks like here
- One line, phrased as a question Chris can say yes to, tied to a quote from him, naming the bot that would do it.

## Learned (agent-appended, newest first)
- 2026-09-08 · 2026-09-07 · Chris's 18:15 direction extends progressive disclosure into the wiki surface: a 'librarian' that progressively discovers wiki skills, bots, and loops — front-matter first, drill deeper per item.
- 2026-09-08 · 2026-09-08 · TurboFit/MTPLX startup errors in raw/inbox/2026-09-07.md remain misrouted to turbofit topic instead of wikified in senter-wiki.
- 2026-09-07 · Chris's 18:15 line extends progressive-disclosure into the wiki surface: a 'librarian' that progressively discovers wiki skills, bots, and loops — front-matter first, drill deeper per item.
- 2026-09-07 · 2026-09-07 · Duplicate port-conflict blocks in `raw/inbox/2026-09-07-from-senter.md` are the same Hermes-process routing fragment repeated many times; treat as duplicate evidence, not distinct wiki input.
- 2026-09-07 · 2026-09-07 · TurboFit/MTPLX startup errors filed into `raw/inbox/2026-09-07.md` remain misrouted to `turbofit` and should not be wikified in senter-wiki.
- 2026-09-07 · Repeated port-conflict routing fragments from Hermes process logs are infra working evidence and should be routed out of senter-wiki rather than treated as wiki surface content.
- 2026-09-07 · TurboFit/MTPLX startup errors filed into senter-wiki raw inbox are misrouted to `turbofit` and should not be wikified here.
- 2026-09-06 · 2026-09-06: vault-live.html edits must preserve boot bindings (`window.mdRender`), proven right-anchor selectors, and dot centering; restoration must reapply known-good pieces rather than blindly reverting.
- 2026-09-06 · Row diffbadges are now standard anatomy: `.usage` → `.diffbadge` (44px fixed) → `.tname` → `.orbs`; nothing shifts when numbers appear or decay.
- 2026-09-06 · Wiki topic bodies are baked HTML; live README.md re-render via `mdRender` in `openEditor` is still needed for true live markdown fidelity.

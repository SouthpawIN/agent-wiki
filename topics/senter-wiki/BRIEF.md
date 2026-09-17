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
- 2026-09-10 · 2026-09-10 · raw/inbox/2026-09-10-from-turbofit.md is a re-routed infra summary (FILE_CAP, git init, model budget) — belongs to turbofit topic, not wiki surface; no wiki pages created from it as a surface request.
- 2026-09-10 · 2026-09-10 · raw/inbox/2026-09-10.md contains only Chris's repeated "fix the layout and fix the update" quote (7x) with escalating frustration — the rest is hermes working evidence about stale --watch processes overwriting JSON.
- 2026-09-10 · 2026-09-09 · raw/inbox/2026-09-09-from-turbofit.md carries the proactive-completion directive: finish front+back end without confirmation, undo-friendly, priority layout+model first; local LM (500h budget) forbidden for general wiki work.
- 2026-09-10 · 2026-09-10 · Bot schema must be consistent: skills as int (not list), model field present — scan_topics() and scan_vault_agents() must match or vault-live.html rendering breaks.
- 2026-09-10 · 2026-09-10 · Stale --watch process (scan-topics.py --watch) must be killed and restarted when scanner schema changes, else it overwrites .system-live.json with old fields and undoes the fix.
- 2026-09-10 · 2026-09-10 · Raw item `raw/inbox/2026-09-10-from-turbofit.md` is a re-routed infra summary (FILE_CAP, git init, model budget) — misrouted to turbofit; no wiki pages created from it as a wiki surface request.
- 2026-09-10 · 2026-09-10 · Raw item `raw/inbox/2026-09-10.md` contains only one real Chris quote ("fix the layout and fix the update") repeated 7x with escalating frustration; the rest is hermes working evidence about stale --watch processes overwriting JSON.
- 2026-09-09 · 2026-09-09 · Raw item `raw/inbox/2026-09-09-from-turbofit.md` contains the proactive-completion directive: "finish both front and back end entirely without needing my confirmation" + "we can undo choices easily" + "priority: layout + model first".
- 2026-09-09 · 2026-09-09 · Chris explicitly forbade using the local LM (500-hour budget) for general wiki work — reserve for local-model-as-deliverable cases only.
- 2026-09-10 · 2026-09-10 · TurboFit/MTPLX startup errors (32 GB M1 memory budget, 10+ tok/s at 131K impossible physical limits) remain infrastructure evidence for turbofit topic, not wiki surface content.
- 2026-09-09 · Proactive completion directive is a standing order for all wiki infra/UI work, not just this session — applies to any wiki surface task where reversibility is cheap.
- 2026-09-09 · FILE_CAP bypass for .system-live.json (2.8MB vs 2MB limit) may need broader guardrails across the bridge file route.
- 2026-09-09 · Chris's proactive-completion directive ("finish both front and back end entirely without needing my confirmation") is a standing order for ALL wiki infra/UI work, not just this session — paired with "we can undo choices easily, so do not be afraid to make them"; priority: layout + model first.
- 2026-09-09 · TurboFit/MTPLX startup errors in raw inbox are misrouted infra evidence (hermes: working), not wiki surface content — but the model-budget concern IS in-scope as it affects which profile Hermes runs the senter-wiki agent under.
- 2026-09-09 · Chris's 'how do I see my bots and sessions in this layout?' is a discoverability question about the existing one-page navigation (BOTS section + corner feed), not a new layout request.
- 2026-09-09 · Chris's "how do I see my bots and sessions in this layout?" is a discoverability question about the existing one-page navigation (BOTS section + corner feed), not a new layout request.
- 2026-09-09 · FILE_CAP bypass (2 MB limit) for .system-live.json (~2.8 MB) was patched in senter-bridge; this is a recurring infra constraint that may need broader guardrails.
- 2026-09-09 · The `mkTopic()` array rename from `['ctx','skills','agents','loops']` to `['wiki','skills','bots','loops']` required a **paired fix**: static HTML rows baked with new keys AND dynamic JS factory must match, plus all downstream `set()`/`setOrbActive()` call sites.
- 2026-09-08 · 2026-09-07 · Chris's 18:15 direction extends progressive disclosure into the wiki surface: a 'librarian' that progressively discovers wiki skills, bots, and loops — front-matter first, drill deeper per item.
- 2026-09-08 · 2026-09-07 · TurboFit/MTPLX startup errors in raw/inbox/2026-09-07.md remain misrouted to turbofit topic instead of wikified in senter-wiki.
- 2026-09-07 · Chris's 18:15 line extends progressive-disclosure into the wiki surface: a 'librarian' that progressively discovers wiki skills, bots, and loops — front-matter first, drill deeper per item.
- 2026-09-07 · 2026-09-07 · Duplicate port-conflict blocks in `raw/inbox/2026-09-07-from-senter.md` are the same Hermes-process routing fragment repeated many times; treat as duplicate evidence, not distinct wiki input.
- 2026-09-07 · 2026-09-07 · TurboFit/MTPLX startup errors filed into `raw/inbox/2026-09-07.md` remain misrouted to `turbofit` and should not be wikified in senter-wiki.
- 2026-09-07 · Repeated port-conflict routing fragments from Hermes process logs are infra working evidence and should be routed out of senter-wiki rather than treated as wiki surface content.
- 2026-09-07 · TurboFit/MTPLX startup errors filed into senter-wiki raw inbox are misrouted to `turbofit` and should not be wikified here.
- 2026-09-06 · 2026-09-06: vault-live.html edits must preserve boot bindings (`window.mdRender`), proven right-anchor selectors, and dot centering; restoration must reapply known-good pieces rather than blindly reverting.
- 2026-09-06 · Row diffbadges are now standard anatomy: `.usage` → `.diffbadge` (44px fixed) → `.tname` → `.orbs`; nothing shifts when numbers appear or decay.
- 2026-09-06 · Wiki topic bodies are baked HTML; live README.md re-render via `mdRender` in `openEditor` is still needed for true live markdown fidelity.
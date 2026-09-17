---
title: Vault UI style contract (white on black, list not cards)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [ui, preference, spec]
sources: [raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/sources/knowledge/weaver-SOUL.md]
confidence: high
contested: true
---

# Vault UI style contract (white on black, list not cards)

Chris's locked visual preferences for the [[wiki-topics/senter/wiki/entities/senter-wiki-ui|Senter Wiki UI]], corrected three times on 2026-08-31 and since owned by the `agent-wiki-vault-ui` skill (authoritative when this page disagrees). Weaver's SOUL: "white-on-black minimal… No gradient kitsch, no font experiments outside the spec." ^[raw/sources/knowledge/skill-senter-fleet-coordination.md] ^[raw/sources/knowledge/weaver-SOUL.md]

## Locked palette and shape
- Card/bubble grid layouts rejected outright → a **wiki-style collapsible LIST**, one row per topic.
- **White on black, NO blue tints, NO rounded corners**: base ~#060606; white lettering at 3 weights (#f5f5f5 / #b8b8b8 / #6e6e6e); hairlines `rgba(255,255,255,.2)` for ALL borders; `border-radius: 0` everywhere; status colors desaturated to grays.
- Nameplate typography = Hermes CLI banner look: weight 800, condensed, uppercase, letter-spaced.
- Layout: left ⅔ = wiki list; bottom corners = floating chats. Pets bob when their bot works, grayscale-still when idle.
- Hover-underline: 1 px white underline grows left→right (~.35 s) and reverses much faster (~.04 s) — asymmetric.
- Colored association flags on rows from real data: turbosovth #9ece6a, klerik #b4f9f8, senter #e0af68, anser #c0caf5, teknium #f7768e, dogeman #bb9af7, skills #7aa2f7; sharp corners, 1 px border, tiny uppercase.
- Floating chat pattern: borderless fixed corner widgets; collapsed = last ~3 messages as pills with stepped opacity (100% → 55% → 28%); hover expands upward; click pins; opening one closes the other; bottom corners tile.
- Readable-over-fade: fixed overlays need content padding (top ~60 px, bottom ~340 px) and a ~300 px fade so content dissolves BEFORE the widgets; opaque #060606 per view.
- UI surfaces have single jobs — dedupe, don't layer (orchestrator chat removed once the Hermes chat existed; fleet stream on WIKI view only).

## Superseded (contested by date)
The skill flags its own 2026-08-31 bullets — status pills, sub-labels, bot dots/flags in rows, the orchestrator floating chat, the 42% mind-map hub, inline expand — as SUPERSEDED by the v6.2+ contract: rows = title · integration logos · skill dots; bots as avatars; sticky borderless hero header; click = full-page rich editor with SAVE via `hermes.send`; fleet stream pills bottom-right on WIKI only. Later locks (v14, 2026-09-02): backdrop = his desktop png contain+center with neutral dim; mind-map hub at the girl's hand; orbs white 4 px static, column-aligned; two-stage hover; integration logos keep brand colors. Both eras kept here with dates.

## Iteration rules
"I don't like the style" → rebuild the same file in place with the named corrections. "Closer, don't change much" → patch ONLY the named deltas; large rewrites after a near-approval destroy trust. Evolve `vault-live.html` in place so decisions accumulate. Animation asks get numeric specs (duration/easing/direction + frame strip), not adjectives. Bulk style changes name the adjacent scope they did NOT touch ("logos kept brand colors — want the whole row monochrome?"). See [[wiki-topics/senter/wiki/concepts/look-loop-verification|LOOK loop]].

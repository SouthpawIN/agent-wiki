---
title: Senter Wiki UI (vault-live.html)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [ui, tool, spec, timeline]
sources: [raw/inbox/2026-09-05-legacy-inbox.md, raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/sources/knowledge/weaver-SOUL.md, raw/sources/knowledge/weaver-AGENTS.md]
confidence: high
---

# Senter Wiki UI (vault-live.html)

The **Senter Wiki** is a single self-contained HTML file, `~/Documents/Projects/Projects/vault-live.html` + `assets/`, rendered in the Hermes desktop **preview pane** (no Obsidian required — Chris "doesn't want Obsidian required at all"; `obsidian://` loads as a broken path). It renders the agent-wiki vault live: Context/Topics → Skills → Bots → Loops, per Chris's agent-wiki GitHub spec. Owner: [[topics/senter/wiki/entities/weaver|weaver]]; QA: [[topics/senter/wiki/entities/looker|looker]]; live data via [[topics/senter/wiki/entities/senter-bridge|senter-bridge]] + `assets/scan-topics.py`. Version tracked in `topics/senter-wiki/README.md` (v14.x by 2026-09-02; ~309–316 KB monolith, module split pending as item AJ). ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## What it is for (Chris)
- North star 2026-08-31: **"Cursor for Obsidian"** — knowledge base + orchestration + review layer + LIVE UI; he watches it morph with the chat as a side window.
- 2026-09-05: **"Cursor for markdown"** — every vault file is an agentic artifact; editing configures the system ([[topics/senter/wiki/concepts/cursor-for-markdown|concept]]). MVP reached: "the UI is at a good enough spot that we can start working on the back end." Now: use the wiki while building it; "making this very professional." ^[raw/inbox/2026-09-05-legacy-inbox.md]
- The wiki is THE surface: input lives IN the wiki (in-wiki input row replaced the blocked sidebar-composer route); replies land in the FEED; fleet done-lines are read here, not narrated by Senter.

## Current contract (highlights; authoritative spec = `agent-wiki-vault-ui` skill)
- Rows = title · integration logos (brand colors kept) · skill dots/orbs; bots as avatars/pets; sticky borderless hero header; click = full-page rich editor with SAVE via `hermes.send`; fleet stream pills bottom-right on WIKI only.
- Backdrop = Chris's exact desktop wallpaper, contain+center, neutral dim; mind-map hub at the girl's hand; orbs white 4 px static, column-aligned between titles and the girl's SAMPLED edge; two-stage hover (row → 22 px orbs with black numbers; orb → 38 px + card).
- Running indicator = petdex pets bottom-left ×N (hidden when no events — not a bug until you check events.jsonl).
- Media player: volume rocker, mute, EQ; Spotify (needs Dev-app client_id) + YouTube resolver ([[topics/senter/wiki/concepts/media-player-controls|media player controls]]).
- Content-card buttons: SHARE done; LOCK, OPEN IN OBSIDIAN, HISTORY, ASK proposed; settings page planned. Feed on the side + corner feeds on hover at the bottom corners.
- Style: [[topics/senter/wiki/concepts/vault-ui-style-contract|white-on-black list, no cards, no radius]].
- Chris (2026-09-05 17:32): "the side chat and the music player are always overlaid over everything and are not interrupted by anything" → HUD z 120 / chat 110–130 / cards 70.

## Verification doctrine
Proof = a capture of Chris's real window; primary viewport = the preview pane from the AX tree (1151×834 @x333 on 2026-09-02), never the 1456×914 window or a guessed 736 px. `desktop_preview open` STACKS tabs — reload = close all, open one. See [[topics/senter/wiki/concepts/look-loop-verification|LOOK loop]] and [[topics/senter/wiki/concepts/preview-pane-viewport|preview-pane viewport]].

## Chris's live-motion expectation (2026-09-05 17:18–17:40)
"I want to see this thing scrolling around and flying around and topics opening and being edited and being closed… the side feet going and all that." And the CONTEXT section of each topic row must render a full [[topics/senter/wiki/decisions/2026-09-05-context-section-is-a-full-llm-wiki|LLM wiki]], not one line. A stage-driver probe (TURBOFIT row scrolled in, card opened, text typed) proved the "stage" works. ^[raw/inbox/2026-09-05-legacy-inbox.md]

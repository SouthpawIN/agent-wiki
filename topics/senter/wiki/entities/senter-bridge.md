---
title: senter-bridge (approval cards into the wiki)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [tool, infra, timeline]
sources: [raw/inbox/2026-09-05.md, raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/sources/knowledge/weaver-SOUL.md, raw/sources/knowledge/looker-SOUL.md, raw/sources/knowledge/paladin-AGENTS.md, raw/inbox/2026-09-05-legacy-inbox.md]
confidence: high
---

# senter-bridge (approval cards into the wiki)

The **senter-bridge** plugin (`~/.hermes/plugins/senter-bridge/`, mirrored at `assets/senter-bridge/` in the vault; server via launchd `com.senter.bridge` on `127.0.0.1:8643`; token at `~/.hermes/senter-bridge/token`; events at `~/.hermes/senter-bridge/events.jsonl`) is the plumbing that makes the [[topics/senter/wiki/entities/senter-wiki-ui|Senter Wiki]] live. Built 2026-09-02. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## Why it exists
Before the bridge, protected-file writes (SOUL.md/AGENTS.md/config) from headless `-q`/`-Q` bot sessions always died: "approval prompt timed out… Silence is not consent." The bridge turns headless sessions into gateway-approval sessions and surfaces each prompt as an **APPROVE/DENY card** in the wiki stream + FEED. E2E proven: klerik `-q` → protected SOUL write → card → click in page → write landed. Bootstrapping it was the ONE legitimate exception to [[topics/senter/wiki/decisions/2026-09-02-senter-never-builds|Senter never builds]] — "without it no bot could do protected work at all."

## What flows through it
- Approval cards; `needs_chris` decision cards ([[topics/senter/wiki/decisions/2026-09-02-fleet-decisions-as-wiki-cards|decision]]); every bot's [[topics/senter/wiki/concepts/done-signal|done signal]] (`POST /post?token=… {"bot","text","status"}`); bot `-q` runs stream into it so "Chris may be watching live."
- Live data: `.system-live.json` served for every wiki list; scan re-runs on a filesystem `fleet/changed` event ([[topics/senter/wiki/concepts/live-data-contract|live-data contract]]).
- Dispatch/sentinel status posts (`queued/delivering/delivered`) — see [[topics/senter/wiki/entities/senter-dispatch-and-sentinel|dispatch + sentinel]].
- YouTube-playlist resolver for the media player (no login, no yt-dlp).

## Wiring a bot (checklist item)
A freshly cloned profile is NOT bridge-wired: needs `profiles/<bot>/plugins/senter-bridge` symlink + a `plugins.enabled` entry in config.yaml (not a protected file). Verify: `ls ~/.hermes/profiles/<bot>/plugins/`, `grep -A3 '^plugins' config.yaml`; its process emits `bridge/loaded` in events.jsonl within ~10 s. Debug a timeout: `curl -s 127.0.0.1:8643/health` → check `bridge/surface-armed` → confirm symlink + enabled. Bots whose turn predates a bridge fix still show the old failure — re-dispatch once. ([[topics/senter/wiki/concepts/profile-setup-checklist|checklist]])

## Known gaps (filed for teknium)
`delegate_task` children attribute as `bot=senter`; their protected-write approvals go to the desktop prompt, not the wiki — so SOUL/AGENTS writes still run via `hermes -q`. Approval cards appear when the GATE is hit (30–60 s of model time after dispatch), so a probe that waits <60 s reports "no card" falsely.

## `/file` allowlist widened to the topic wikis (2026-09-05 19:09–19:12)
The topic agents write pages under `topics/<t>/wiki/`, and the wiki pane opens them through the bridge's `/file` proxy — so the allowlist had to serve `topics/*/wiki/*`. Hermes checked it, then ran a live proof: "open the senter card via stage and fire a real diff" → "Proof: 1 block diffing, 2 green, 1 red." ^[raw/inbox/2026-09-05.md]

## Still custom, by design (19:12)
Under Chris's [[topics/senter/wiki/decisions/2026-09-05-backend-as-builtin-hermes-plus-markdown|backend-as-built-in-Hermes decision]] the bridge is one of three pieces that stay custom for now: "the bridge (SSE + file proxy for the UI)" — the browser pane needs a live event stream and vault files served, which no Hermes built-in provides. The UI it serves is explicitly exempt from rollback. See [[topics/senter/wiki/comparisons/native-hermes-vs-custom-backend|native vs custom backend]]. ^[raw/inbox/2026-09-05.md]

## Chris on approvals (2026-09-05)
"These are the things that I don't want to have to give approval on or edits to the wiki" — the bridge's next stage is `hermes serve approval.*` so yes/no is a click in the sidebar, and wiki edits stop generating cards at all ([[topics/senter/wiki/decisions/2026-09-05-no-approval-for-wiki-edits|decision]]). ^[raw/inbox/2026-09-05-legacy-inbox.md]

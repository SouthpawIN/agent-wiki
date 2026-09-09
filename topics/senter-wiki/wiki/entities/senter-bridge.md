---
title: senter-bridge (127.0.0.1:8643)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [tool, infra, ui]
sources:
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
  - raw/inbox/2026-09-05.md
confidence: high
---

# senter-bridge

Local HTTP bridge (`~/.hermes/plugins/senter-bridge`, launchd `com.senter.bridge`, port 8643) between the fleet and
[[topics/senter-wiki/wiki/entities/vault-live-html|vault-live.html]]. Restart: `launchctl kickstart -k gui/$(id -u)/com.senter.bridge`. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]

## Endpoints (as of 2026-09-05)
| Route | Purpose |
|---|---|
| `/health /file /events` | liveness, vault file read, SSE event stream the page's `handle(ev)` consumes |
| `POST /post` | feed card: `{"bot","status":"working|done|blocked|needs_chris","text"}` — how bots show Chris they're working |
| `POST /write` | vault-allowlisted write (editor save, `lock.json`) |
| `/ask` | question to Chris |
| `POST /approve` | does exactly two things — drop `.proposed` or delete ([[topics/senter-wiki/wiki/concepts/approval-policy|approval policy]]). The apply step that follows an approved loop registers it as a live Hermes cron and auto-installs the bot's gateway if missing — first seen 18:57 for paladin and looker ([[topics/senter-wiki/wiki/queries/apply-path-proven-2026-09-05|apply path proven]]) ^[raw/inbox/2026-09-05.md] |
| `POST /stage` | `window.stage()` — row scrolls into view, card peeks, text typewriters in, closes ([[topics/senter-wiki/wiki/concepts/ui-performs-the-fleet|UI performs the fleet]]) |
| `/music/youtube/search`, `/music/youtube/audio` | no-API-key search; yt-dlp resolves the stream, bridge proxies it same-origin with Range support |
^[raw/inbox/2026-09-05-legacy-inbox.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Auth
Header `X-Senter-Token: $(cat ~/.hermes/senter-bridge/token)` (or `?token=`), **not** `Authorization`. A 401 `{"error":"token"}` means the header
name is wrong, not the token. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Working rule (backend phase)
*"Use the product while building it."* Post progress to `/post` as you work — *"Chris test-drives between turns; the corner cards are how he sees
you working."* ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Native replacements queued
`/approve` is the working stand-in for `hermes serve approval.*` (`approval.pending` / `approval.respond`, or `register_approval_transport`) — see loop
`approval-relay`. Bot→sidebar messages have no inject route in the desktop backend; the relay script + `senter-fleet-feed` cron was the working path,
to be replaced by `hermes kanban watch` (loop `fleet-feed`). ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]

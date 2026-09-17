---
title: Bridge server lifecycle (launchd com.senter.bridge)
created: 2026-09-08
updated: 2026-09-08
type: concept
tags: [infra, tool, decision]
sources: [raw/inbox/2026-09-08.md]
confidence: high
---

# Bridge server lifecycle (launchd `com.senter.bridge`)

The [[topics-wiki/senter/wiki/entities/senter-bridge|senter-bridge]] server is managed by launchd as `com.senter.bridge`. On 2026-09-08, Hermes restarted the server through launchd to pick up patched `server.py` code. ^[raw/inbox/2026-09-08.md]

## How it runs

- **Launchd service**: `com.senter.bridge` — automatically respawns the server if it exits
- **Server file**: the bridge server.py at `~/.hermes/plugins/senter-bridge/server.py` (mirrored in `assets/senter-bridge/`)
- **Health endpoint**: `curl -s 127.0.0.1:8643/health`
- **Events log**: `~/.hermes/senter-bridge/events.jsonl`

## Restart procedure (proven 2026-09-08 09:42–09:44)

When the server.py file is patched and needs to be picked up:

1. **Stop launchd** from respawning: `launchctl unload com.senter.bridge` (or equivalent)
2. **Kill the manual process** if one is running
3. **Let launchd manage it**: after updating the file, `launchctl load com.senter.bridge` restarts it with the patched code

Hermes noted on 2026-09-08 09:42: *"There's a launchd service `com.senter.bridge` that's respawning the server. I need to stop it via launchctl, update the file, then restart it. The launchd is using the old token."* ^[raw/inbox/2026-09-08.md]

Then on 2026-09-08 09:44: *"The launchd plist runs the bridge server. Now that I've patched the server.py file, the launchd will use the updated code when it restarts. Let me kill the manual process and let launchd manage it."* ^[raw/inbox/2026-09-08.md]

## End-to-end verification (2026-09-08 09:43)

After the restart, the live data pipeline was verified:
- `.system-live.json` is served correctly via the `/file` endpoint
- 35 topics, 68 bots, 199 skills, 77 loops
- Scanned at 2026-09-08T09:43:17

Hermes confirmed: *"The live data pipeline is now working end-to-end"* ^[raw/inbox/2026-09-08.md]

## Token management

The server uses a token at `~/.hermes/senter-bridge/token`. When the launchd process restarts, it picks up the current token from this file. The token is passed in API calls as `?token=$(cat ~/.hermes/senter-bridge/token)`.

## Related

- [[topics-wiki/senter/wiki/entities/senter-bridge|senter-bridge entity page]]
- [[topics-wiki/senter/wiki/entities/looker|looker]] — verifies the bridge's health
- [[topics-wiki/senter/wiki/concepts/vault-agents-vs-profile-bots|vault agents vs profile bots]]

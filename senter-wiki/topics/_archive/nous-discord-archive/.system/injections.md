# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: nous-discord-archive
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/nous-discord-archive-3a48b82219.md"]
confidence: medium
---

# nous-discord-archive

## Current context

Auto-archived text logs of Nous Research Discord channels (polled every 6h) # Nous Research Discord Archive Periodically polls selected channels in the Nous Research Discord and appends new messages to per-channel text files in `archives/`. Runs every 6 hours via GitHub Actions. ## Files - `archives/<channel>.txt` — append-only message log per channel - `archives/state.json` — last-seen message ID per channel (used for incremental fetches) ## Setup 1. **Create a Discord bot** - https://discord.com/developers/applications → New Application → Bot - Enable the **Message Content Intent** (privileged) - Copy the bot token 2. **Invite the bot to the server** - OAuth2 → URL Generator → scopes: `bot`, permissions: `View Channels`, `Read Message History` - Send the URL to a server admin 3. **Get channel IDs** - Discord settings → Advanced → Developer Mode ON - Right-click each channel → Copy Channel ID 4. **Configure the repo** - Settings → Secrets and variables → Actions - Secret=<redacted> = the bot token - Variable: `DISCORD_CHANNELS` = comma-separated channel IDs (e.g. `123,456`) 5. **First run** - Actions tab → "Archive Discord channels" → Run workflow - Initial run downloads full history per channel — can take a while. ## Local testing ## Notes - Threads and forum posts are intentionally skipped. - Edits and deletes after archival are NOT reflected (polling-only design). - Attachments are recorded as CDN URLs; the files themselves are not downloaded.

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/nous-discord-archive` (`2026-07-08T20:37:10Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/local-inference|Local Inference]]

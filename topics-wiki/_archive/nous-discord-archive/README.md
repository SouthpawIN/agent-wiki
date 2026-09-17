---
title: nous-discord-archive
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/nous-discord-archive
status: dormant
tags: [repo]
---

# nous-discord-archive

> Auto-archived text logs of Nous Research Discord channels (polled every 6h)

**[Open on GitHub](https://github.com/SouthpawIN/nous-discord-archive)** · DORMANT (since 2026-07-08) · last push 2026-07-08

## Facts
- **Language:** Python
- **Stars / forks:** 0 / 0
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-06-26 · **Last push:** 2026-07-08
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-08)

## From the README

# Nous Research Discord Archive

Periodically polls selected channels in the Nous Research Discord and appends new messages to per-channel text files in `archives/`. Runs every 6 hours via GitHub Actions.

## Files

- `archives/.txt` — append-only message log per channel
- `archives/state.json` — last-seen message ID per channel (used for incremental fetches)

## Setup

1. **Create a Discord bot**
   - https://discord.com/developers/applications → New Application → Bot
   - Enable the **Message Content Intent** (privileged)
   - Copy the bot token

2. **Invite the bot to the server**
   - OAuth2 → URL Generator → scopes: `bot`, permissions: `View Channels`, `Read Message History`
   - Send the URL to a server admin

3. **Get channel IDs**
   - Discord settings → Advanced → Developer Mode ON
   - Right-click each channel → Copy Channel ID

4. **Configure the repo**
   - Settings → Secrets and variables → Actions
     - Secret: `DISCORD_BOT_TOKEN` = the bot token
     - Variable: `DISCORD_CHANNELS` = comma-separated channel IDs (e.g. `123,456`)

5. **First run**
   - Actions tab → "Archive Discord channels" → Run workflow
   - Initial run downloads full history per channel — can take a while.

## Local testing

```bash
python -m venv .venv && source .venv/bin/activate
pip install requests
DISCORD_BOT_TOKEN=... DISCORD_CHANNELS=123,456 python scripts/archive.py
```

## Notes

- Threads and forum posts are intentionally skipped.
- Edits and deletes after archival are NOT reflected (polling-only design).
- Attachments are recorded as CDN URLs; the files themselves are not downloaded.


## Archived
Archived 2026-09-02 — absorbed into [[topics-wiki/nous-community/README|nous-community]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.

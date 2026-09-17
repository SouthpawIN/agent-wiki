---
title: What still blocks the Spotify integration?
created: 2026-09-05
updated: 2026-09-05
type: query
tags: [question, music, infra, timeline]
sources: [raw/inbox/2026-09-05.md]
confidence: medium
---
# What still blocks the Spotify integration?

## Answer (as of 2026-09-05)
One thing: the [[topics-wiki/music/wiki/concepts/spotify-client-id|Spotify client ID]]. Hermes's status line
on 2026-09-05 18:58 reads, in full: "Only external blocker left: Spotify client ID." No other blockers —
internal or external — are recorded for the [[topics-wiki/music/wiki/entities/spotify|Spotify]] integration.
^[raw/inbox/2026-09-05.md]

## Timeline
- 2026-09-05 18:58 — Hermes: Spotify client ID is the only external blocker remaining. ^[raw/inbox/2026-09-05.md]

## Who unblocks it
Chris. The client ID comes from a Spotify Developer app registered under his account; the fleet cannot
create it for him.

## Still unknown
- What the integration does once unblocked (Chris has not said in this topic).
- Whether a client secret / redirect URI will be requested right after the client ID.

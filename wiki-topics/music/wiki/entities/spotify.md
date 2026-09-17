---
title: Spotify
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [tool, music, infra, integration]
sources: [raw/inbox/2026-09-05.md]
confidence: medium
---
# Spotify

Spotify is the music service being wired into Chris's Senter wiki as an integration. It is the only music
tool named so far in this topic. ^[raw/inbox/2026-09-05.md]

## Status (2026-09-05)
Hermes reported on 2026-09-05 18:58 that Spotify is the single remaining outside dependency for the
integration: "Only external blocker left: Spotify client ID." Everything else on the Hermes side is
described as done; what is missing is a credential that only Chris can create (a Spotify Developer
app, which issues the client ID). ^[raw/inbox/2026-09-05.md]

See [[wiki-topics/music/wiki/queries/spotify-integration-blockers|What still blocks the Spotify integration?]]
for the open item and [[wiki-topics/music/wiki/concepts/spotify-client-id|Spotify client ID]] for what the
credential is and where it comes from.

## What Chris has said
Nothing directly from Chris in this topic yet — the only raw item is a Hermes working line. Chris's own
words on why he wants Spotify in the wiki (playback? now-playing? library sync?) are not recorded here.

## Open questions
- What is the Spotify integration meant to *do* inside the wiki once the client ID lands?
- Does Chris already have a Spotify Developer account, or is that step zero?

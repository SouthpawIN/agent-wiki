---
title: Spotify client ID
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [tool, infra, music, question]
sources: [raw/inbox/2026-09-05.md]
confidence: medium
---
# Spotify client ID

The Spotify client ID is the credential Hermes named as the last external blocker for the
[[topics-wiki/music/wiki/entities/spotify|Spotify]] integration on 2026-09-05: "Only external blocker left:
Spotify client ID." ^[raw/inbox/2026-09-05.md]

## What it is (general knowledge, not from raw)
A client ID is issued when an app is registered in the Spotify Developer Dashboard. It identifies the
app to Spotify's Web API; most flows pair it with a redirect URI (and, for server flows, a client
secret). Registering the app is a manual, account-holder step — it cannot be automated by the fleet,
which is why it shows up as an *external* blocker rather than a build task.

## Why it matters here
Until Chris supplies it, the integration cannot authenticate against Spotify, so any Spotify-backed
feature in the wiki is parked regardless of how complete the Hermes side is. Tracked in
[[topics-wiki/music/wiki/queries/spotify-integration-blockers|What still blocks the Spotify integration?]].

## Unknowns
- Which auth flow the integration uses (decides whether a client secret / redirect URI are also needed).
- Whether Chris has a Developer Dashboard app already or needs to create one.

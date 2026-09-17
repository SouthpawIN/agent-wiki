---
title: Media player controls (volume rocker, mute, EQ, live music)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [ui, music, preference, spec]
sources: [raw/inbox/2026-09-05-legacy-inbox.md, raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: high
---

# Media player controls (volume rocker, mute, EQ, live music)

The music widget in the [[wiki-topics/senter/wiki/entities/senter-wiki-ui|Senter Wiki UI]] — a girl with headphones, an EQ, a volume rocker, transport buttons, title/artist — iterated live by [[wiki-topics/senter/wiki/entities/chris|Chris]] on 2026-09-04 15:10–15:27 and 2026-09-05 17:26–17:36. Chris's design decisions, in order: ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Volume rocker (2026-09-04)
1. "there's a dot at the bottom of the volume Rocker I would also like a dot at the top of it… What if the slider was actually the space between two segments and those segments were both capped with a dot" — top segment, tiny break, bottom segment; the gap IS the slider.
2. "can the space between be a little bit bigger." → done.
3. "It's exactly what I was thinking" — but maxed-low must straddle like maxed-high: "three dots together in succession." Root cause fixed: the bottom end-dot was attached to the fill bar (shrinks to nothing at zero) → made a fixed element on the track.
4. The extra "very, very, very bottom dot" was the mute button → "move that to the side of it around the middle just to the left side, so towards the inner side of the app."

## Mute + hit zones
- Only clicking the **artist or song title** opens the full media player. Mute's visual stays tiny but its hitbox grows; a glow was tried and **removed** at Chris's next turn (muted = hollow ring + dimmed rocker).
- "anywhere… that keeps the volume and the mute open… should highlight the mute and if they click anywhere in that, then that should toggle the mute… Scrolling there will still make the arm go up and down."
- Zone geometry: "from the girl's headphones back is going to be media area" (EQ's left edge → pane edge, top → feed's top); "from her face forward… above the feed chat" = play/pause space toggle; bottom corners hover = feeds up.
- Root cause (DOM-proven): the fixed mute zone (z-index 0) painted OVER the transport buttons and title/artist, so `elementFromPoint` on play returned the zone. Buttons and `#mNow` now sit above it.

## Live music (2026-09-05)
- "Search for humanity's last breath by Godhood on YouTube… for the EQ and her in her headphones to react to it. **Not a demo playthrough I want to actually be live to the music.**"
- "the side chat and the music player are always overlaid over everything and are not interrupted by anything. So I can control the music as you're playing around with the wiki" → play button top hit at its own centre; HUD 120 / chat 110–130 / cards 70.
- "the volume volume is different now, let's have a look right" — a regression Chris caught after the z-order change (open at time of filing).
- Sources: Hermes's native Spotify plugin (PKCE, needs Chris's own client_id, `hermes auth spotify --client-id …`, playback control = Premium + open device) and the bridge's YouTube-playlist resolver (no login, no yt-dlp). "Verify the endpoints yourself with the token before relaying; honest scope in the card." Recipe: skill `references/music-integrations.md`. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

Verification for all of the above follows the [[wiki-topics/senter/wiki/concepts/look-loop-verification|LOOK loop]] (real window, ≥44 px targets, pointer paths).

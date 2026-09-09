---
name: wiki-live-music-hookup
description: Use when wiring music into the Senter wiki. Play real audio (Spotify/YouTube) and drive the EQ + headphones from the live signal — never a demo playthrough.
version: 0.1.0
distilled: 2026-09-05 17:29
topic: senter
---
# wiki-live-music-hookup
# Wiki live music hookup

## Rules
- Music is a real playback source, not an animation. The EQ bars and the girl's headphones MUST be driven by the actual audio signal (Web Audio AnalyserNode on the playing element/stream). A canned/demo playthrough is a failure, not a placeholder.
- Two accepted sources: Spotify (needs Dev-app client_id; Web Playback SDK) and YouTube (search query → embed/iframe player). If Spotify creds are missing, use YouTube — do NOT fall back to fake data.
- Remove any stage/probe harness before wiring real audio; probes must never ship in the live page.

## Steps
1. Strip test probes (stage scroll/click/type harness) from vault-live.html.
2. Add a music source adapter: `search(query)` → `play(trackRef)`; implement YouTube first (search API or `ytsearch`), Spotify when client_id is present.
3. Route playback through an AudioContext + AnalyserNode; map frequency bins → EQ bars; map amplitude envelope → headphone glow/pulse on the girl.
4. Test with Chris's reference: search "humanity's last breath by Godhood" on YouTube and play it.
5. PROOF: capture Chris's real preview window while audio plays (computer_use capture of the 'Hermes' window); vision must confirm EQ bars moving in sync and headphones reacting. No capture = not done.

## Pitfalls
- Cross-origin iframes (YouTube embed) block direct AnalyserNode access; use a tab/stream capture or a proxied audio stream — say so honestly if blocked rather than simulating the EQ.
- Autoplay policies require a user gesture; hook playback start to Chris's chat action or a visible play control.
- Mute-zone z-index must sit above transport buttons (DOM-proven), per Chris's root-cause rule.

## Evidence
> Remove the probe, then hook Spotify:
> also tighten up the music. I want to make sure that it works. Search for humanity's last breath by Godhood on YouTube and receiving it to me to the playthrough there and for the EQ and her in her headphones to react to it. Not a demo playthrough I want to actually be live to the music.

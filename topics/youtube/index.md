# youtube — wiki index
> One line per page. The wiki row's CONTEXT section renders this file.
> Last updated: 2026-09-07 | Total pages: 6

## Entities
- [[topics/youtube/wiki/entities/senter-audio-bridge|Senter audio bridge (YouTube → <audio>)]] — The **bridge** is the local component that turns a YouTube pick into a plain HTML `<audio>` element inside the Senter wiki player, replacing the earlier embedde
- [[topics/youtube/wiki/entities/volume-rocker|Volume rocker (wiki player)]] — The **volume rocker** is the on-screen volume + mute control of the Senter wiki's music player. Its audio target changed when the player moved from a YouTube if

## Concepts
- [[topics/youtube/wiki/concepts/mac-screen-recording|Mac screen recording]] — Screen recording on macOS uses built-in controls in **Screenshot** or **QuickTime Player**.
- [[topics/youtube/wiki/concepts/youtube-audio-player|YouTube audio player in the Senter wiki]] — The wiki carries a music player whose source is **YouTube**, played as plain audio rather than as an embedded video. The 2026-09-05 build step, in the assistant

## Decisions
- [[topics/youtube/wiki/decisions/apply-volume-on-track-load|Decision — apply rocker volume and mute on every track load]] — **What**: `load()` in the wiki player now applies the [[topics/youtube/wiki/entities/volume-rocker|rocker]]'s current level and mute state to each new bridge `<

## Comparisons


## Queries
- [[topics/youtube/wiki/queries/mac-screen-recording-hotkeys|Mac screen recording hotkeys]] — Chris asked the hotkey sequence for starting screen recording on macOS.


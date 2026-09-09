# Continuity — youtube

dogeman's content + publishing surfaces (YouTube, personal site, infographics).

Created 2026-09-02 by merge-topics.py; edit to correct my understanding.

## learned 2026-09-05 17:30 (worker, from 2 inbox blocks)
- Wiki music player streams YouTube audio through the senter-bridge as a real <audio> element (206 Partial Content with Range → seekable) so the Web Audio analyser/EQ works; title and EQ must stay live
- Player volume rocker previously drove the YouTube iframe via postMessage; it must now drive the bridge <audio> element instead — path pending verification
- Player has a search box for finding YouTube tracks; this is a wiki-UI concern (weaver) that touches the youtube topic only as a source

## learned 2026-09-05 17:42 (worker, from 2 inbox blocks)
- Bridge <audio> element was created at volume 1.0 and applyVol() only ran on rocker movement, so new tracks started at full volume until touched; fixed so load() applies rocker level + mute state to every new track on creation
- The Web Audio analyser is a passthrough node and does not change loudness — loudness bugs are element-volume issues, not analyser issues
- Volume rocker → bridge <audio> path is now verified as the loudness control (resolves the 'pending verification' item)

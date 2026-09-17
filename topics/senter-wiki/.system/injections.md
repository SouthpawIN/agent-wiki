# Injections — senter-wiki
_Spec format. The sidebar reads `[UNREAD]` before responding, weaves the first one in naturally, moves it to `[READ]`._

## [UNREAD]
[LOOPS] Want a loop that watches .system-live.json for bot schema drift (skills as list vs int) and posts when stale scan-topics processes may be overwriting good data?
[LOOPS] Want a loop that auto-pulls remote changes into the vault and restarts scan-topics so updates never 'keep failing' again?
[AGENTS] I see you need the layout fixed so bots and sessions visibly render in the BOTS section — want a bot that patches renderBots()/'mkTopic() stale data-k keys and watches your Hermes preview pane to confirm the rows populate live?
[LOOPS] Want a loop that rescans topics/*/skills and proposed bots/loops every tick to feed the librarian view?
[AGENTS] I see you're talking about a librarian that progressively discovers wiki skills, bots, and loops — want a bot that surfaces them via progressive disclosure in the wiki rows?
[AGENTS] I see you want wiki topic headings to stay live when README.md changes — want a bot that re-renders the topic body through `mdRender` on open?
[LOOPS] Three bots now have crons that 'actually fire' — want looker to watch each first tick land in your corner feed and post a capture of your window (or a BLOCKED card if nothing fires)?
[LOOPS] Want the compile loop to run the new wiki-page-quality-check on one page every tick and put the 5/5 result on the feed card next to the page count, so a compile that only restates raw gets fixed before you see the number?
[LOOPS] Two compiles over the same raw left 17 same-subject page pairs in senter-wiki — want paladin to sweep every topic's wiki after each compile and fold duplicate slugs together, keeping every citation and every <!-- chris --> line?
[SKILLS] new skill `wiki-real-audio-pipeline` in senter-wiki: Use when the wiki player, EQ, or volume misbehaves. Real audio only: yt-dlp proxy → <audio> → analyser; never iframe for levels.
[SKILLS] new skill `topic-wiki-compile` in senter-wiki: Use when compiling or reading a topic's two-layer LLM wiki. Raw is immutable, wiki pages are agent-owned with provenance, index.md IS the row context.
[SKILLS] new skill `wiki-feed-verify` in senter-wiki: Use when checking that fleet posts reach the sidebar feed. Cross-check bridge `/post` arrivals against the events log and DOM, then report counts.
[CONTEXT] Policy: skills auto-apply now (5 promoted). New subjects auto-scaffold + research. The wiki now performs fleet events live (stage). Spotify needs your client id.
[SKILLS] new skill `wiki-event-performance` in senter-wiki: Use when wiring fleet activity into the Senter wiki UI. Emit `wiki` events from real actions so rows open/scroll/edit/close live; never animate from fake or polled state.
[LOOPS] topic-worker + umbrella are LIVE. 5 skills, 1 bot proposed; umbrella proposes merging senter-wiki → senter (0.65, AUTO-tier). Approve/reject on the cards.
[SKILLS] proposed `senter-proposal-pipeline` for senter-wiki: Use when a worker/umbrella emits or Chris acts on a wiki proposal. Write `.proposed` artifacts, surface them as proposed rows, approve/reject only via bridge `/approve`.
[SKILLS] proposed `wiki-derived-anchors` for senter-wiki: Use when placing or nudging any wiki element by pixels. Measure both reference edges from the DOM and express the position as a derived value, never a hand nudge.
[SKILLS] proposed `wiki-hit-zone-layering` for senter-wiki: Use when adding or changing an invisible click/hover zone in the Senter wiki. Lift real controls above the zone, scope openers to one element, and probe-click every neighbour before claiming done.
[CONTEXT] senter-wiki topic built out 2026-09-05: README, continuity, queue (CONTEXT/SKILLS/AGENTS/LOOPS), 3 skills, agents roster, loops watcher/topic-worker/umbrella, `_global` catalogs. Full transcripts + spec are in `.system/`.
[LOOPS] watcher is live (com.senter.watcher) — every sidebar message is being filed into topics/<t>/.system/inbox.md with a feed card.

## [READ]
[CONTEXT] Anser interview complete 2026-09-04 — verdicts in .system/anser/02-verdicts.md.

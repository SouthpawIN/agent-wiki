# Senter Wiki — Collected Context
_What Chris has been saying all along, the state of the fleet, and what's pending. Mined 2026-09-03 from all session DBs (default + 9 profiles), memories, vault comments, and process files._

## The through-line: everything LIVE, through the wiki

Chris's vision has been remarkably consistent since 2026-08-27, and it escalated in one direction the entire time:

1. **2026-08-27 — the vault is the canvas.** "I want you to edit the obsidian vault on my screen. This is going to be a repeated workflow… You will edit it live, and look for my edits to it. This vault is the canvas for this session." Same day: "make sure you are documenting all of this into the vault as we go. I want you to consider the context in the vault on each turn, and update it on each turn so we can mold ideas and launch them with async agents simultaneously."
2. **2026-08-28 — one source of truth.** Absorb the Linux 'senter' box (all Hermes memories, instances, projects, files) into this Mac: "create one source of truth and one Hermes for all the projects." Mac = home control + wiki orchestrator; Linux = workhorse; Surface Duo = mobile connection. "I need everything to be connected and everything to be organized."
3. **2026-08-30 — one orchestrator surface.** "I want a top profile where I can talk about all of my ideas and it would either split it up into a new bot if necessary or send that message to the relevant bot… we need to make sure that's not creating bots when it can be sent to one that's already made." → Senter born as "the 'center' line, the one I interact with, who coordinates everything."
4. **2026-09-01 — "cursor for obsidian".** "I would like to be able to watch the agent wiki update and morph live and have this chat on a side window… pull context from any project anywhere. It's your knowledge base as well as the orchestration layer, as well as the review layer — the overall overarching project." UI built in one marathon session: white-on-black wiki, fleet stream, mind map, editor, media widget.
5. **2026-09-02 — the leap.** "It's time to rip the bandaid off. I don't want this just planned — I want this to go… from here on out we need to make the leap and start using this. Everything live, get everything hooked up." Then: "I want everything to be live now. No timed loaders, everything should be on event loaders… live live live." And: "what we're doing now is exactly how I intend people to use this product — the workflow is the product, so as we're building this out we should be using it. No workarounds, no dummy data, no temporary fixes. You are building your tools on a…"
6. **2026-09-03 — the ask that triggered this file.** "One of the topics is Senter, and I've been telling you that we need to be using all of this live… everything should be going through this wiki. We need to be trying to get everything as live as possible, which means that I also want things going into the sidebar here, into Hermes agent — messages from the bots. That's a way that we can keep track of what bots are doing. I'll be able to see them in the chat here." Intended layout (screenshot-confirmed): far-right sidebar = Hermes agent chat, plugged into the wiki plugin.

## The wiki today (state at mining time)

- **UI:** `vault-live.html` v14.81 (single file + assets/), owner **weaver** (ephemeral Meeseeks instances). Views: WIKI · FEED · SKILLS · BOTS · SPACE · BROWSER + media widget (Senter Radio) + fleet stream + type-ahead input strip. Primary verify viewport: Chris's real preview pane 1151×834 (AX-tree measured).
- **Live bridge:** senter-bridge plugin running (launchd, 127.0.0.1:8643) — verified healthy at mining time (`{"ok":true}`, 0 pending). SSE events + approval relay for all profiles. `.system-live.json` shows **19 live topics** (down from 63 after the 2026-09-02 consolidation) and **9 bots**.
- **Fleet:** senter (coordinator), klerik (profile factory), weaver (wiki UI), anser (redundancy gate/Discord), teknium (hermes-agent), turbosovth (TurboFit), paladin (vault structure), dogeman (YouTube), looker (UI-QA LOOK service). Pets 7/7 dark-fantasy hatched + looker; avatars cut for all.
- **Process artifacts:** `topics/senter/process/` (build-loop.md, lessons.md #1–29, senter-turn-checklist.md), klerik's agent-authoring-rules.md (15 rules), similarity-governance plan with LOCKED thresholds, sentinel (30s watchdog), dispatch queue, REFLECT loop (5 passes logged).

## Recurring complaints (patterns, not one-offs)

- **Fixes take too long / nothing visible is happening.** Said repeatedly on 2026-09-02 ("it's still taking a long time to see any of the fixes," "are you just writing up these spots because I want these fixes to actually go?", escalating to profanity by 17:12). Root causes found: per-item cost 20–33 min, FIFO queueing, chained claims → Meeseeks model, verify-light/full, region claims, 12/20-min caps.
- **Repeated asks not landing.** Asked for input-row fixes 5× (lessons #9: stale preview tab); asked for the wallpaper backdrop 3–4× (lessons #22: unreachable fullscreen gate); orb column sagas across v14.74–v14.81 (lessons #26–28: wrong viewport assumptions). Rule earned: proof = capture of HIS window, reload on every version bump.
- **"You're guessing / lying."** 2026-09-02 19:30: "It seems like you're entirely guessing because what you're saying is not there… you need to visually look at what you're doing and fix these pipelines instead of lying or coming up with dummy data. We're trying to make a good product here."
- **Band-aids.** "You put a band-aid over it. I would like you to not work like that" (2026-09-03, about dots snapping left — interacting fixes stepping on each other). Diagnose-before-fix is the standing answer.
- **Dead silence from pipelines.** "Don't let things fail silently" (3×); things "die when they go into pending"; approvals timing out because bot-mode DM sessions ran `single_query_mode=deny` — fixed by routing approvals to the wiki.
- **Similar topics still not merged.** 2026-09-03: "there's a lot of subjects that are very similar that are still not combined — I asked you to do that a while ago" (pocket-shop vs pocket-shop-pricing). Similarity thresholds were locked but recalibration + auto-merge in the UI is still pending.

## Pending items (as of 2026-09-03)

- **FEED → CONTEXT rename** ("context, skills, bots, and loops — just like the agent wiki GitHub"), then re-read the agent-wiki repo and streamline without ruining the graphics.
- **Title-hover options with LOCK** (protect a title from auto-summarization/deletion — "we are going to make it a little opinionated").
- **Dots already at grown size + text when hovering the TITLE** (2026-09-03 00:14 ask; partially landed as two-stage hover v14.79 — verify it matches the new wording: three dots grow when the title is hovered, not only on direct dot hover).
- **Similarity recalibration** + auto-merge governance actually running against the live topic list.
- **Sidebar ↔ wiki integration**: bot messages into the Hermes sidebar chat; wiki edits round-tripping through Hermes.
- **Player**: Spotify needs Chris to run `hermes auth spotify` (client_id step); YouTube playlist field unconfigured; evolutionary lo-fi radio deferred.
- **Running-worker visibility** redesigned (bottom-left pets removed 2026-09-03 by Chris's decision; "we'll worry about integrations with running workers another way").
- **Infra**: Linux 'senter' box reinstall of Omarchy PAUSED (absorb verified at ~/senter-absorb, disk empty GPT, box needs power-cycle + live-USB recovery); Models 8.3T re-download pending; GitHub repo rename agent-wiki→Senter blocked on PAT.
- teknium gaps flagged: delegate children attribute as bot=senter; protected-write approvals from delegate children hit the desktop prompt, not the wiki.

## Voice notes (for anyone parsing future Chris messages)
Mishears to map: Riever=weaver, tectium=teknium, Claire/cleric=klerik, answer=anser, Sirvir→turbosovth ("TurboSouth", he spells it out: s-o-v-t-h), Senter spelled S-E-N-T-E-R. Stray TV/family audio is NOT instruction — he said "you should only be listening to me." Dictation cuts off mid-sentence: ship immediately, no preambles, never ask him to repeat himself.

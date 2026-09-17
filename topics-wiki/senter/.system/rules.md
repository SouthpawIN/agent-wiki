# Senter Wiki — Rulebook
_Curated from every Hermes session database (default + 9 profiles), vault comments in `vault-live.html`, the locked `agent-wiki-vault-ui` skill, memories, and the process files. Mined 2026-09-03. Verbatim wording kept for the load-bearing rules; source tag on every bullet._

## UI rules — vault-live.html

### Core style (locked)
- White on black, monochrome: "I don't like the blue tints and I do not like the rounded corners. I want sharp corners with very thin white lines and everything to be black tinted instead of the blue tinted. So white on black — all the lettering needs to be white." — 2026-09-01 [session senter/20260830_132156_088cfd]
- Font = the Hermes agent bot-nameplate splash font (Collapse Bold titles, Rules Compressed meta); "I seriously mean this — look in the Hermes agent repo and find the font used when new bots are created." Consistent across header, titles, editor body. — 2026-09-01 [session senter/20260830_132156_088cfd] [skill agent-wiki-vault-ui]
- No bubbles: "I don't like everything in a bubble. I would rather it be in a list more like a wiki layout — each topic is its own collapsible thing." — 2026-09-01 [session senter/20260830_132156_088cfd]
- Dots, not triangles, everywhere — matches mind-map node language. — 2026-09-01 [skill agent-wiki-vault-ui]
- Hover: title text expands, underline grows left→right (~0.4s in, quick out), goes ALL the way across the row; right rail bar grey→white; hover bg = solid matte black; highlight stops at the underline forming an angle, never paints the expanded body. — 2026-09-01 [session senter/20260830_132156_088cfd] [skill agent-wiki-vault-ui]
- Topic rows = title + dots ONLY: "get rid of the active and full effort labels"; no status pills or name tags in rows. — 2026-09-01 [session senter/20260830_132156_088cfd]
- Integration logos KEEP their brand colors (only the metric orbs went white). — 2026-09-02 [session senter/20260830_132156_088cfd] [vault comment v14.73]

### Orbs (the four dots per row)
- Exactly four metric orbs per topic row (context/skills-capabilities/bots-profiles/loops), superseding skill-dots which superseded bot-dots. — 2026-09-01 [skill agent-wiki-vault-ui]
- Orbs are plain white: "I like everything about them except the color. I would like them to just be plain white dots" — 2026-09-02 [session senter/20260830_132156_088cfd] [vault comment v14.70]
- Orbiting indicator removed entirely: "take out the orbiting thing altogether… I don't like that as the indicator for running agents. It's just kind of goofy." — 2026-09-02 [vault comment v14.73]
- Dots are STATIC — no running pulse/animation at rest or running (running indicator is a separate concern). — 2026-09-02 [vault comment v14.74]
- Rest size tiny (walked 9→7→6→5→4px); smaller when unfocused so they don't collide. — 2026-09-02 [session senter/20260830_132156_088cfd] [vault comment]
- Two-stage hover: row hover grows all four dots (22px, black numbers, wider spacing); hovering one dot in that state blooms it to 38px + caption + card, growing FROM ITS CENTRE with zero sibling/logo movement. "When you hover over the title, I want them to be at their grown size, the text in them too — very important." — 2026-09-02/03 [vault comment v14.79] [session default/20260903_001447_7bc70a]
- On-dot lettering is BLACK on the enlarged white dot; below-dot captions stay white. — 2026-09-02 [session senter/20260830_132156_088cfd]
- Orb column: "enough space between the titles of each topic and the four dots so that the four dots can line up vertically along each row" — measured column (no px literal), centred in the band between the longest visible title and the girl's SAMPLED hand edge. — 2026-09-02 [vault comments v14.75–v14.81]
- Orbs are click-throughs: click an orb → that topic's editor scrolled to the matching section. — 2026-09-01 [skill agent-wiki-vault-ui]
- Dead zone: where the fleet stream expands on the right, no row highlighting AND no underline ("the underline still happens in the dead zone" — fixed). Dead-zone floor also keeps it from swallowing the orbs at narrow panes. — 2026-09-02 [session senter/20260830_132156_088cfd] [vault comment v14.80]

### Mind map, backdrop, space
- Translucent gold mind map behind all pages ("make the stars and the glow gold tinted instead of white tinted"); canvas opacity 0.17 behind wiki/editor — "Drop it down to 17%. I like that number."; 1.0 in SPACE. — 2026-09-01 [session senter/20260830_132156_088cfd] [skill agent-wiki-vault-ui]
- Hub = "star in the center of the universe" with glow; map center pinned to the wallpaper girl's open hand; spread shrunk ~24% so nothing touches pane edges (≥40px clearance). — 2026-09-01/02 [vault comments v14.72/78]
- Backdrop = Chris's EXACT desktop wallpaper (hermes-galactic): "use the exact one that I have for my desktop background… make sure it fits correctly." Whole artwork visible (contain+center, thin letterbox bands read as frame), neutral dim (.40–.45), no gold cast, @2x 3024-wide export for Retina, never the raw 30MB PNG, NEVER gated on fullscreen detection. — 2026-09-02 [vault comments AH/AI] [lessons #22]
- Feed shows the mind map behind it too ("standardize — the feed should also show the senter space mindmap"). — 2026-09-02 [skill agent-wiki-vault-ui]

### Fleet stream, feed, cards
- Fleet stream = borderless floating chat, bottom-right: shows the previous 2–3 messages fading away at top, hover expands to full chat, click pins; "Don't let the agent wiki be overlapped by this chat." — 2026-09-01 [session senter/20260830_132156_088cfd]
- Fleet stream is READ-ONLY — no input bar: "the main input should be this side panel where I'm talking to Hermes." Never re-add a textarea/send to it. — 2026-09-01 [session senter/20260830_132156_088cfd] [skill agent-wiki-vault-ui]
- Fleet stream rides WIKI/SKILLS/BOTS/SPACE, never FEED (feed's right lane = integrations rail). — 2026-09-02 [skill agent-wiki-vault-ui]
- No top-right notifications — "redundant. They should just populate the disappearing feed in the bottom right." — 2026-09-01 [session senter/20260830_132156_088cfd]
- Feed/stream cards uniform Twitter-shaped boxes (fixed width, min one avatar-row tall, straight left edge, right-aligned to lane), profile-icon-size avatars; long messages make the box taller, never bleed under the next card. — 2026-09-02 [session senter/20260830_132156_088cfd] [skill agent-wiki-vault-ui]
- Feed fade-out shorter: "the fade-out on the feed a lot shorter" (200px → 66px, feed only). — 2026-09-02 [vault comment AJ]
- Pending approval cards PINNED to the list's growth edge so new messages can't make them jump. — 2026-09-02 [session senter/20260830_132156_088cfd] [vault comment AA]
- Approval cards gold-outlined; on approve the gold dissipates corner-to-corner "like gold dust dissipating into black — kind of quickly, but slow enough to be cool"; the ALLOW ▾ menu must flip up when it would overflow the viewport. — 2026-09-02 [session senter/20260830_132156_088cfd] [weaver queue item Q]

### Nav, input, pages
- Top nav = floating overlay (no bar, no outline), summoned at the top edge, disappears quickly, hides when hovering any other interactive element; "there should not be two tabs — it should all be one, well organized." — 2026-09-01 [session senter/20260830_132156_088cfd] [skill agent-wiki-vault-ui]
- Nav tabs: WIKI · FEED · SKILLS · BOTS · SPACE · BROWSER; "Senter" is implied by the product name — tabs never carry it (product name = **Senter Wiki**). — 2026-09-01/02 [skill agent-wiki-vault-ui]
- The `+` follows the active tab and is context-aware (wiki→topic, feed→post, skills→skill, bots→bot); no static `+` anywhere else; ⚙ flush right at the far end, bigger than default. — 2026-09-02 [session senter/20260830_132156_088cfd] [skill agent-wiki-vault-ui]
- Top input bar (above nav): invisible until hovered, overline above text, flashing VERTICAL caret on the LEFT next to the model selector, `+`/model pill flush left, Hermes-desktop-matching voice glyphs right, type-ahead tags per keystroke above the tabs. — 2026-09-02 [session senter/20260830_132156_088cfd] [vault comments K–V]
- Click a topic = full-page rich markdown editor reusing the wiki's skeleton/fade (never a fixed overlay); back control = a bare `\` with a large invisible hitbox; NO save button: `\`/Esc = auto-save on exit, leaving via a nav tab = discard with a one-time warning ("don't show again" checkbox). — 2026-09-01 [session senter/20260830_132156_088cfd] [skill agent-wiki-vault-ui]
- Every page gets the sticky rotating preview header (hero) — including FEED; hero rotates on row hover and on live activity ("the most recently touched one will be the title shown at the top"). — 2026-09-01/02 [skill agent-wiki-vault-ui]
- Media widget (Senter Radio): stacked, small skips, 28px circle play, artist over scrolling `song · album`, invisible outline, volume mixer slider on hover reachable from BOTH sides; real sources only (Hermes Spotify plugin + YouTube playlist); evolutionary lo-fi radio deferred. — 2026-09-02 [session senter/20260830_132156_088cfd] [skill agent-wiki-vault-ui] [weaver queue AM]
- BROWSER tab = bookmarks + URL bar navigating the preview pane itself (the pane IS a webview — no iframes); support Jon Komet's hermes-browser-extension. — 2026-09-02 [skill agent-wiki-vault-ui]
- SKILLS and BOTS pages use the SAME row element as the wiki ("they're all markdown files"); three-way split is hard: WIKI=topics-wiki/context, SKILLS=every SKILL.md, BOTS=every profile — nothing crosses. — 2026-09-01/02 [session senter/20260830_132156_088cfd] [skill agent-wiki-vault-ui]
- Full-size pet/avatar shown ONLY on the BOTS page, never on wiki topics; "make it do like one animation on entry and then stop." — 2026-09-02 [session senter/20260830_132156_088cfd] [skill agent-wiki-vault-ui]
- Every bot gets an avatar (its pet's idle frame) used everywhere it appears — feed, stream, bots — "like a social media with all of your bots." — 2026-09-01 [session senter/20260830_132156_088cfd] [skill agent-wiki-vault-ui]
- Running-worker overlay (bottom-left petdex pets, ×N counts) built 2026-09-02, then REMOVED 2026-09-03: "I no longer like the pets in the bottom left corner overlay indicating running workers, but just take that out entirely. We'll worry about integrations with running workers another way." — [vault comment, line 191] [session default/20260903_001447_7bc70a]

### Live data
- "No timed loaders — everything on event loaders. Everything should be live live live." `grep -c setInterval` must stay 0; only labeled fallback backoffs allowed. — 2026-09-02 [session senter/20260830_132156_088cfd] [skill agent-wiki-vault-ui AG] [build-loop]
- No baked collections: every list (topics-wiki/skills-capabilities/bots-profiles/triggers-loops/integrations) loads from `.system-live.json` via the bridge; spawn = visible within seconds. — 2026-09-02 [lessons #18] [skill agent-wiki-vault-ui Y]
- "No dummy data. No workarounds. No temporary fixes." If a live source exists, render from it; fallbacks must be labeled `static · fallback`. — 2026-09-02 [session senter/20260830_132156_088cfd] [klerik authoring rule 8]
- Approvals forward to the wiki UI with full Hermes options (allow / allow this session / always allow): "I should be able to click through approvals right here from the feed — that's been stopping us up." — 2026-09-02 [session senter/20260830_132156_088cfd]
- Rename FEED → CONTEXT so the wiki has "context, skills, bots, and loops, just like the agent wiki GitHub we're basing all this on." — 2026-09-03 (pending) [session default/20260903_001447_7bc70a]
- Title hover options including LOCK: "options to appear when you hover over that title to either lock that title so that it can't be deleted by auto-summarization, because we are going to put a level of that in there. We are going to make it a little opinionated." — 2026-09-03 (pending) [session default/20260903_001447_7bc70a]

## Workflow rules

### The big ones
- Per-turn canvas contract: "make sure you are documenting all of this into the vault as we go. I want you to consider the context in the vault on each turn, and update it on each turn so we can mold ideas and launch them with async agents simultaneously." — 2026-08-27 [session default/20260826_203750_11d1e3]
- Everything goes through the wiki, live: "Everything should be going through this wiki… we need to be trying to get everything as live as possible, which means that I also want things going into the sidebar here, into Hermes agent — messages from the bots, so we can keep track of what bots are doing." — 2026-09-03 [session default/20260903_001447_7bc70a]
- Senter is the single surface: "Senter is the 'center' line — the one I interact with, who coordinates everything." — 2026-08-30 [session default/20260830_125934_943c42]
- Conversation-first operating model, locked into senter's SOUL.md: "I want to simply have a conversation with you about anything… I want you to proactively sort those into topics and for those topics to proactively create necessary bots and suggest actions… Automations kind of naturally spring up out of things that I'm interested in." — 2026-08-30/31 [session senter/20260830_132156_088cfd]
- Standing approval: "Yes, you have my approval — and when I ask for things I want you to assume that you have my approval." (Confirm only spending/deletion/publishing.) — 2026-08-31 [session senter/20260830_132156_088cfd] [memory senter]
- Senter never builds — route to the owning bot via its topic queue; UI owner = weaver: "you are working a little bit out of order… you're doing a lot of these edits yourself when what you should be doing is using the agent wiki — creating or adjusting workers to do the task." — 2026-09-02 [session senter/20260830_132156_088cfd] [lessons #1]
- No band-aids — fix root causes: "you put a band-aid over it. I would like you to not work like that." — 2026-09-03 [session default/20260903_001447_7bc70a]; "it's time to rip the bandaid off… do everything that I said because we need this to continue development." — 2026-09-02 [session senter/20260830_132156_088cfd]
- The process is the product: "what we're doing now is exactly how I intend people to use this product… we're making a defined process that's going to work for every project." — 2026-09-02 [session senter/20260830_132156_088cfd] [build-loop]
- Refine before create: "we need to make sure that's not creating bots when it can be sent to one that's already made. We need to focus on refining current bots before creating new ones." — 2026-08-30 [session default/20260830_125934_943c42]

### Fleet mechanics
- Meeseeks model: "a better way to handle weaver would be kind of like Mr. Meeseeks from Rick and Morty — you just spawn one to do the current task and then it disappears, and then you spawn more like subagents." One instance = one queue item; parallelism = spawn count. — 2026-09-02 [session senter/20260830_132156_088cfd] [build-loop]
- Pending = dead worker: "things tend to die when they go into pending — that's when you should be spawning more instances." Parked-on-card instances never count toward capacity. — 2026-09-02 [session senter/20260830_132156_088cfd] [build-loop] [lessons #20]
- CLAIM v2: claim = atomic `mkdir` under `topics-wiki/<t>/.system/claims/`, heartbeat every 60s, reaper after 10 min stale, queue.md is the LOG not the lock, outcomes append-only to session.md under dated headings. — 2026-09-02 [weaver AGENTS.md] [lessons #12]
- Done signal: every reply's last line is exactly `DONE — …` / `BLOCKED — …` / `NEEDS-CHRIS — …`, also POSTed to the bridge (127.0.0.1:8643). Never end a turn without it. — 2026-09-02 [all builder AGENTS.md]
- Diagnose before you fix: measured cause in one line before any edit; after 2 repeat corrections, anser does fresh-eyes QA. — 2026-09-02 [lessons #4] [build-loop]
- LOOK loop (Chris-mandated fleet standard): numeric probes first; screenshot at Chris's REAL window + reference size; vision_analyze as yes/no + measured offset; max 3 passes then BLOCKED. — 2026-09-02 [skill bot-verify-loop v1.1] [memory klerik]
- Verify light per edit, verify full once before the done-line; region claims for same-element bundles; 12-min progress line / 20-min BLOCKED caps. — 2026-09-02 [lessons #23] [bot-verify-loop v1.1]
- Proof = a capture of Chris's REAL window (computer_use → Hermes window, judged by vision); headless renders measure, never prove. "You need to visually look at what you're doing… instead of lying or coming up with dummy data." A fix he can't see = not done. — 2026-09-02 [lessons #25] [session senter/20260830_132156_088cfd] [memory senter USER.md]
- Primary verification viewport = Chris's actual preview pane read from the AX tree (1151×834, measured 2026-09-02) — never a screenshot guess; reload his preview (`close` then ONE `open`) on every version bump. — 2026-09-02 [lessons #9, #27, #28] [checklist 4/4b]
- Every standing rule from Chris goes into the owning bot's SOUL the same turn — a rule said only in chat is held by luck. — 2026-09-02 [lessons #8] [klerik authoring rule 13]
- Keep the lessons ledger: "keep track of iterative improvements — write them into what you're doing AND into the Senter wiki, because we're building this project." Append-only; every row names its enforcement point. — 2026-09-02 [session senter/20260830_132156_088cfd] [lessons.md]
- Delivery before reflection: if Chris is waiting on a visible fix, check delivery and spawn FIRST, write docs LAST. — 2026-09-02 [checklist item 0] [lessons #13]
- Delivery is not routing: "sent" = the dispatch log says ok; watch the daemon logs, re-queue stale in-flight, never let pipelines fail silently ("don't let things fail silently" — said three times). — 2026-09-02 [session senter/20260830_132156_088cfd] [build-loop]
- Markdown is the API: Ideas.md (verbatim capture, deduped) → topic queue.md (spec) → session.md (outcome) → log.md (fleet changes) → catalogs (who owns what). — 2026-09-02 [build-loop] [senter SOUL.md]
- File tools only for vault/profile writes — NEVER `python3 -c`, heredocs, pipe-to-interpreter, or shell appends: each generates an approval card Chris must click (96 in one day). — 2026-09-02 [weaver AGENTS.md] [lessons #16/#19]
- Terminology: profiles are BOTS, never "agents" ("Hermes Agent" = the whole runtime); vault dir `agents/` keeps its name. — 2026-09-02 [session senter/20260830_132156_088cfd] [memory weaver]
- PR policy: upstream (hermes-agent etc.) — never open PRs in-session, keep a draft ledger (`topics-wiki/hermes-agent/prs/`), Chris picks what goes out; Chris's own repos ship immediately. — 2026-09-02 [session senter/20260830_132156_088cfd] [build-loop]
- Integrations are event-driven: "they don't need to be on a time poll — that's inefficient. They need to be on an event poll." Polling exists only as a labeled fallback. — 2026-09-02 [session senter/20260830_132156_088cfd] [build-loop]
- Voice etiquette: Chris dictates; stray audio (TV, kids) arrives as garbled messages — never ask him to repeat, hold the thread, restate pending items compactly; treat mid-stream corrections as additive. — [memory default USER.md] [senter SOUL.md] [memory senter USER.md]

## Governance rules
- Topic creation is discriminatory: "when topics are being made, we need to be a little bit more discriminatory about what can be combined and what needs to be a new topic. Pocket shop pricing can probably go with pocket shop." — 2026-09-02 [session senter/20260830_132156_088cfd]
- Similarity governance: topics organized by likeness, off-white color-hinted by cluster; "things that are very very similar should be proposed to be merged together or should be already merged — this might be a good way to set the governance for what should be auto-merged." — 2026-09-02 [session senter/20260830_132156_088cfd] [plans/similarity-governance-2026-09-02.md]
- Thresholds LOCKED by Chris 2026-09-02 (method tfidf): ≥0.50 = auto-merge candidate (dry-run → one card → merge on approval); 0.35–0.50 = propose ("merge?" glyph between rows); <0.35 = color-group only (cluster link ≥0.30); shared stem (`pocket-shop*`) always ≥ propose. Changing a locked number needs a new Chris ruling. — [memory paladin] [plans/similarity-governance-2026-09-02.md]
- Merges follow the paladin reference shape: script + dry-run + rehearsal on a copy + snapshot + archive-never-delete + provenance in every touched README + one approval card + verify after. Executed 2026-09-02: 63 → 19 topics (approved by Chris). — [lessons #21] [memory paladin] [log.md]
- Recalibration demanded 2026-09-03: pocket-shop vs pocket-shop-pricing must score high; "TurboHall and TurboFit are different things — I do want to delineate that." — [session default/20260903_001447_7bc70a]
- Titles can be LOCKED against auto-summarization (opinionated governance incoming). — 2026-09-03 (pending) [session default/20260903_001447_7bc70a]
- Anser = redundancy gate: consulted before any new topic/skill/bot lands; confirms Hermes built-ins don't already cover it. — [memory anser] [senter SOUL.md]
- Chris's corrections in the vault/skills are never overwritten: "Chris's user corrections in the vault are never overwritten"; design corrections in the UI skill are never overwritten either. — [senter SOUL.md] [weaver SOUL.md]
- Nothing Chris says gets lost: "I don't want any of this lost. I don't want any of what I said to be gone — if you have to write your own code and change how you do things, do it." — 2026-09-02 [session senter/20260830_132156_088cfd]

## Ops rules
- One Hermes, one source of truth: Mac M1 = home control + wiki orchestrator; Linux 'senter' box = workhorse; one Hermes reachable from all devices. — 2026-08-28 [session default/20260828_150713_365379] [memory default]
- Ordered wipes: on an explicit GO, execute without per-item permission; relay-GO from an agent ≠ wipe authority — only Chris's verbatim wording counts ("FORMAT GO", "a. wipe it all"). NO dual boot/recovery — fresh machine only. — 2026-08-29 [session turbosovth/20260828_105835_b9ef] [memory default] [memory turbosovth]
- Disk safety: MD5-verify data absorb before any wipe; NEVER format the disk the running OS boots from — wipe only from a live env; kill stuck format chains immediately. — [memory turbosovth]
- kexec on the senter box is permanently banned (hung the machine every time). — [memory turbosovth]
- Chris hates holdups on explicit orders and repeat confirmation prompts; milestone-by-milestone updates, no batching; verify results with own tool calls instead of agent self-reports. — 2026-08-29 [memory turbosovth] [memory default USER.md]
- Permissions: "enable all the permissions that you need. I work with the people who make Hermes agent — this may be a core thing. This is all altruistic and good." — 2026-09-02 [session senter/20260830_132156_088cfd]
- Approvals route to wherever Chris is: "I need approvals routed to this chat as well as updates from all of the projects on the agent wiki." — 2026-09-01 [session senter/20260830_132156_088cfd]
- Voice mode: wake word DISABLED (TV/kid misfires), push-to-talk only; "you shouldn't be keying off of that — you should only be listening to me." — 2026-08-30 [session default/20260830_125934_943c42] [memory default]
- Renames: Sirvir → turbosovth ("TurboSouth") everywhere; agent-wiki GitHub repo → 'Senter' ("not senter-agent — I mean Senter"). — 2026-08-30/31 [session senter/20260830_132156_088cfd] [session default/20260828_110040_04cc56]
- Pets register = dark fantasy/anime, not cute ("cute, but not that anime or dark fantasy theme"); assignments: turbosovth=s0uthpaw, teknium=teknium, dogeman=123mikeyd, senter=three-eyed owl; "trust your gut on the pets… surprise me." — 2026-09-02 [session senter/20260830_132156_088cfd] [memory weaver]

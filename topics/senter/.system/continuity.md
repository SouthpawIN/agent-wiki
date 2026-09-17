# Continuity — senter

Raw understanding, 2026-08-27 (from GitHub metadata + README):
- Hermes Agent profile distribution
- Language: None; 3 stars; last push 2026-07-08; original work.
- (Edit this file to correct my understanding; I never overwrite user-edited lines.)

## learned 2026-09-05 17:05 (worker, from 36 inbox blocks)
- Senter wiki is Hermes's memory layer: topics hold ALL raw context (full session exports), never summaries; the sidebar reads it by progressive disclosure (row → .system/INDEX.md → file → read_file offset/limit).
- UI premise is 'Cursor for markdown': every vault file (SKILL.md, AGENTS.md, SOUL.md, memory, loop prompts) is an agentic artifact; editing a file configures the system.
- Sidebar does NO work: conversation only, yes-and personality, rubber-ducks to pull ideas out of Chris, and receives every approval as a card; all tasks run in per-topic bots/workers.
- Watcher granularity is PER MESSAGE (not per session), tailing Hermes's message table directly with no hand-off from the sidebar; files to topics/<t>/.system/inbox.md, misfits to _inbox/unsorted.md.
- Flywheel: context → skills (repeated evidence) → cluster of related skills → bot → stable workflow → loop; every artifact proposal lands as a sidebar approval card.
- Chris wants the wiki visibly moving/editing itself while he talks — skills, bots, loops proposed continuously, live like Cursor.
- Full Senter/wiki sessions since Aug 27 exported via `hermes sessions export --format md` into senter-wiki (9 transcripts, 5.2 MB); assets/build-index.py generates INDEX.md on every scanner pass.
- Chris's approach rule: root-cause fixes only, no band-aids; UI fixes must be DOM-proven (e.g., mute zone z-index over transport buttons).

## learned 2026-09-05 17:18 (worker, from 1 inbox blocks)
- Routing calibration is Chris-approved and LOCKED: propose at similarity ≥ .35, auto-route at ≥ .5; umbrella/watcher components must use these thresholds, never re-derive their own.

## learned 2026-09-05 17:24 (worker, from 1 inbox blocks)
- Standing approval: wiki self-edits (files, topics, proposals landing) need NO approval from Chris — only spend/delete/publish do.
- Bots must trigger EARLY: the moment a new subject appears in chat, the side feed should propose research or scaffolding for it — no waiting for recurrence.
- Reuse-before-create for research: a bot that already researched another subject is reused for a new one; only create a new researcher if none exists.
- Chris's target UX: the user only talks to the site chat; fleet + knowledge coordination self-edits and proposes everything else automatically.
- Visible activity is a requirement, not decoration: Chris expects to SEE topics opening/being edited/closing, the side feed scrolling, and music hooked up while workers run; 'not seeing things move' = failure signal.
- Chris suspects work is concentrated in 1–2 topics; all topics must be made to work and show activity, not just senter.

## learned 2026-09-05 17:29 (worker, from 2 inbox blocks)
- Music in the wiki must be REAL live playback: EQ and the girl's headphones react to actual audio (Spotify or YouTube), never a demo/simulated playthrough — Chris's test track: 'humanity's last breath by Godhood' searched on YouTube.
- Stage harness passed (TURBOFIT row scrolled in, card opened, text typed); the probe is to be removed and Spotify hooked next — YouTube search/play is an accepted alternate music source.
- Chris evaluates the wiki from the end-user's seat: wiki editing itself + side feed scrolling + music playing must all be simultaneously live while he talks to the site chat; each is a required concurrent signal, not a sequence.

## learned 2026-09-05 17:35 (worker, from 2 inbox blocks)
- Side chat and music player are LOCKED as always-on-top overlays: nothing the wiki does (topic opening/editing, cards, feed) may cover them or interrupt music control while workers run.
- Z-order lock (recorded 09-05): music HUD 120 / side chat 110–130 / cards 70; the play button must be the top hit-target at its own centre (hit-test proven, not assumed).
- Chris's 'stop'-like utterances can be stray voice audio ('I didn't clap you') — a worker that was mid-task should resume, not halt, unless the stop is explicit.

## learned 2026-09-05 17:42 (worker, from 2 inbox blocks)
- Topic 'context' sections must be full Karpathy-style LLM wikis (use the llm-wiki skill), not one-line summaries — Chris sees senter's context as 'still only one line' and reads that as not getting it.
- Per-topic context = ALL of everything collected about that topic for that user plus every input they put into it; the wiki is the funnel for every context the user cares or worries about across their digital and real life.
- Chris flagged that music volume behaviour changed ('the volume volume is different now') and wants it inspected — volume level/behaviour must stay stable across wiki changes.

## learned 2026-09-05 17:48 (worker, from 46 inbox blocks)
- Chris REJECTED the umbrella/worker split (09-05 17:46): one agent per topic owns the whole lifecycle — rewrite inbound context into a structured wiki, then propose action; the watcher only cuts the live sidebar session into topic pieces.
- Proposal order is BOTS FIRST, then loops; skills fall out as the bot works — never wait for a pile of skills before suggesting a bot ('We shouldn't have to wait till there's a bunch of skills').
- Proactive suggestions are examples of workflow style, not literal orders: the moment a subject appears, notify the user with concrete offers ('do you want to research this?', 'create a bot that can edit / make shorts?').
- Volume rocker LOCKED (09-04): two dot-capped segments with a visible gap; the gap IS the slider; maxing out either end reads as three dots in succession (bottom end-dot is a fixed track element, not attached to the fill).
- Mute dot sits mid-height on the inner (app-facing) side of the rocker; no glow; muted state = hollow ring + dimmed rocker.
- Transport buttons and #mNow must sit above the mute zone (elementFromPoint on the play button must return the button) — DOM-proven root cause of the 09-04 dead-button bug.
- Decision criteria locked: skill = narrow/repeatable/attachable; bot = persistent identity/memory/runtime; loop = event/time workflow owned by a bot; wiki = full topic knowledge.
- Librarian policy: progressive discovery via frontmatter-first reads; do not add folder depth to discover things — add frontmatter fields and only load deeper layers when matched.

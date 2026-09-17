# BRIEF — senter
_Pre-prompt for the cutter and this topic's agent. Chris edits freely; lines ending `<!-- chris -->` are never rewritten._

## What this topic is
The Senter system itself: the fleet of Hermes bots, how they coordinate, the watcher/topic-agent/umbrella pipeline, approvals, profiles, crons, the sidebar's role, and Chris's architecture decisions. The BACKEND and the ORGANISATION — not the wiki's look.

## Belongs here (scope)
- Architecture and workflow decisions (per-message watcher, one agent per topic, bots-first, approvals apply)
- Fleet: which bot does what, profile creation, klerik/looker/anser/paladin/weaver/teknium roles, gateways, crons
- Hermes-native vs custom (anser verdicts), bridge endpoints, launchd services, Hermes CLI usage
- Chris's operating preferences that apply everywhere (root cause, no band-aids, stop asking for decisions, everything live)

## Does NOT belong here (anti-scope → route elsewhere)
- How the wiki LOOKS or BEHAVES on screen (cards, dots, rocker, EQ, feed, colours, diffs view, markdown rendering) → `senter-wiki`
- Music playback, YouTube audio, Spotify → `music` (or `youtube` for the player/video)
- TurboFit model ladder / GGUF / inference → `turbofit`
- Hermes Agent internals, PRs, upstream bugs → `hermes-agent`

## Aliases (the cutter binds hard on these words)
- senter
- sidebar
- watcher
- topic agent
- umbrella
- fleet
- klerik
- looker
- paladin
- approval
- approvals
- cron
- profile
- gateway
- bridge
- workflow
- pipeline

## Lens — how to read new context for this topic
- Is Chris describing how the SYSTEM should work (a workflow, a role, an order of operations)? That is a DECISION page — date it, quote him, note what it supersedes.
- Is he correcting a misunderstanding ('I don't like the separation', 'you still don't get it')? Record the correction AND the wrong model it replaces, flag the old page `contested`.
- Is he stating a standing preference ('stop asking me', 'root cause only')? → entities/chris.md preferences + BRIEF standing preferences.
- Which fleet bot is implicated? Link its entity page.

## Standing preferences (apply to every suggestion)
- Root causes, never band-aids. Everything live and visible. Markdown + built-in Hermes over custom code.
- Bots first, then loops; reuse a fleet bot when one fits; skills auto-apply. No pitches about the build process itself.

## What a good suggestion looks like here
- One line, phrased as a question Chris can say yes to, tied to a quote from him, naming the bot that would do it.

## Learned (agent-appended, newest first)
- 2026-09-09 · 2026-09-09 · raw/inbox/2026-09-09-from-legacy-bots.md contains only Hermes working lines from scan debugging — compile as evidence only, not a new Chris decision or request.
- 2026-09-09 · 2026-09-09 · bridge scan-topics.py shows a real schema/merge bug in snapshot(): topic bots lack model, scan_vault_agents() has duplicate skills assignments, and topic/profile scan paths normalize skills types differently.
- 2026-09-09 · 2026-09-09 · raw/inbox/2026-09-09-from-wiki-want.md contains only hermes working lines from scan debugging — no new Chris decisions extracted.
- 2026-09-09 · 2026-09-09 20:05–20:33 bridge scan debugging exposed a real schema/merge bug in `scan-topics.py`: topic bots lack `model`, and vault/profile `skills` types can still desync despite the earlier naming fix.
- 2026-09-09 · 2026-09-09 raw items already fully compiled — no new wiki content extracted
|- 2026-09-09 · 2026-09-09 · Layout inspection gap: Hermes DOM probing for bot/sessions visibility was blocked ("browser isn't running"); the live-data contract (7bridge serves 69 bots) is senter, but the vault-live.html layout rendering belongs to senter-wiki per anti-scope
|- 2026-09-09 · 2026-09-09 · git-init fix resolves "updates keep failing" root cause (Projects folder was NOT a git repo); bridge health verified 2026-09-09 (35 topics-wiki/69 bots-profiles/201 skills-capabilities/81 loops); gh-sync repo structure (agent-wiki/klerik/senter) evidence; vault-to-repo link (symlink/clone/worktree) still unresolved
|- 2026-09-09 · 2026-09-09 · raw/2026-09-09.md + raw/2026-09-09-from-senter-wiki.md: Chris 08:45 "continuing toward your standing goal" re-activates 2026-09-08 autonomous completion; live pipeline verified (35 topics-wiki/69 bots-profiles/201 skills-capabilities/81 loops, bridge healthy); git initialized in Projects folder fixing "updates keep failing"; gh-sync repo structure (agent-wiki/klerik/senter) evidence; vault-to-repo link (symlink/clone/worktree) still unresolved
- 2026-09-08 · senter-wiki topic folder already existed with proper structure — investigation on scan-topics.py was premature
- 2026-09-08 · 2026-09-08 · scan-topics.py bot name parsing `split(".md")` correctly strips extensions — kashik test confirmed on 2026-09-08 09:51
- 2026-09-08 · Chris authorizes autonomous completion of Senter Wiki front and backend with standing approval extended for this task
- 2026-09-08 · New entity page: [[topics-wiki/senter/wiki/entities/librarian|librarian]] created for anser's proposed progressive discovery loop
- 2026-09-08 · Context-size fallback threshold (>65K → Nous cloud) is a Hermes config/fallback concern; `auxiliary.compression` must be pinned before the rule can be exercised in practice (compression timeouts prevent reaching it)
- 2026-09-08 · Topic-agent event-driven trigger: landed state unclear; investigation in progress via hermes examining scan-topics.py and launchd config
- 2026-09-08 · Bridge scan-topics.py has `.md` suffix parsing bug; bot names in `.system-live.json` include incorrect `.md` extensions
- 2026-09-08 · senter-wiki topic folder missing namespace; needs creation with standard wiki/skills-capabilities/bots-profiles/loops structure
- 2026-09-08 · Created wiki/index.md with proper wikilinks for all key pages; added <50 lines to log.md compilation record
- 2026-09-07 · Duplicate reroute headers can appear multiple times inside one raw item; de-dupe by message content, not block count.
- 2026-09-07 · Duplicate memento reroute entries keep resurfacing in later raw/inbox files; future passes should de-dupe by message content and treat repeated port-conflict noise as misrouted without adding log rows when already recorded.
- 2026-09-07 · Duplicate reroute headers can appear multiple times inside one raw item; de-dupe by message content, not block count.
- 2026-09-07 · Duplicate re-route headers can appear multiple times inside one raw item; de-dupe by message content, not block count.
- 2026-09-07 · Pure duplicate-rerouted memento port-conflict noise with no new Chris decisions should be marked misrouted rather than compiled into wiki pages.
- 2026-09-07 · Raw reroute blocks can appear multiple times inside one item; de-dupe by message content, not block count.
- 2026-09-07 · Pure duplicate-rerouted hermes/memento noise that carries no new Chris decisions should be marked misrouted rather than compiled into wiki pages.
- 2026-09-07 · 2026-09-07 · The librarian is now active watch/discovery across wiki/skills-capabilities/bots-profiles/loops, not only read-time progressive disclosure.
- 2026-09-07 · 2026-09-07 · Chris 18:15 reframed the librarian as a watcher over the whole vault that progressively discovers and proposes, not a passive reader.
- 2026-09-07 · 2026-09-07 · Chris introduced the librarian as an active watch/discovery loop over progressive disclosure across wiki/skills-capabilities/bots-profiles/loops — not only a read-time policy.
- 2026-09-07 · 2026-09-07 · Proposed vault rename from 'context' to 'wiki' and topic anatomy `wiki/` + `skills-capabilities/` + `bots-profiles/` + `triggers-loops/`; not yet approved.
- 2026-09-07 · 2026-09-07 · Skill/bot/loop criteria were reaffirmed unchanged from 2026-09-05; issue was missing architecture wording, not a new rule.
- 2026-09-07 · 2026-09-07 · raw/inbox/2026-09-07.md is mostly noise (batch-complete receipts, compaction handoffs, misrouted MTPLX/memento); the only new signal is Hermes 18:10 restating already-known gaps.
- 2026-09-07 · 2026-09-07 · Duplicate re-route headers can appear multiple times inside one raw item; de-dupe by message content, not block count.
- 2026-09-07 · 2026-09-07 · Duplicate re-route headers can appear multiple times inside one raw item; de-dupe by message content, not block count.
- 2026-09-07 · 2026-09-07 · Context-size fallback threshold (>65K → Nous cloud) surfaced by Anser; treated as senter domain (Hermes config/fallback).
- 2026-09-07 · 2026-09-07 · Context-size fallback threshold (>65K → Nous cloud) proved theoretical: Hermes compression timeouts prevent reaching the rule in practice; `auxiliary.compression` must be pinned first.
- 2026-09-07 · Delegation batch-complete entries are system noise, not new Chris decisions; do not create pages for async completion receipts.
- 2026-09-07 · Context-size fallback threshold (>65K → Nous cloud) surfaced by Anser; treated as senter domain (Hermes config/fallback).
- 2026-09-07 · Context-size fallback threshold (>65K → Nous cloud) proved theoretical: Hermes compression timeouts prevent reaching the rule in practice; `auxiliary.compression` must be pinned first.
- 2026-09-07 · Delegation batch-complete entries are system noise, not new Chris decisions; do not create pages for async completion receipts.
- 2026-09-06 · Model auto-switching is a config/fallback ordering issue, not a turbofit inference bug; fixes belong to senter as Hermes CLI usage/gateway concerns.
- 2026-09-06 · Main-model switching applies only in new sessions; the current session stays on its current model.
- 2026-09-06 · JWT-based entitlement cache staleness after credits is a fleet-infrastructure gap; `force_fresh=True` for TTS resolution is identified but unconfirmed.
- 2026-09-06 · Config fixes for model switching, TTS, and vision (2026-09-06) belong to senter as Hermes CLI usage / gateway concerns, even though the turbofit provider triggers the switch — the fix is to `fallback_providers` ordering and `auxiliary.*` config, not turbofit code.
- 2026-09-05 · The topic-agent pitch caps (1 bot / 2 loops / 1 research per pass; zero infrastructure pitches; `hermes:` lines are evidence) must be enforced by the topic agent prompt template; 13 self-referential proposals were removed from the agent's memory.
- 2026-09-05 · When a topic agent pitches things it already knows (e.g., "governance has no owner" because wiki says umbrella deleted), the wiki PAGE is wrong, not the pitch—fix the record, not the pitch mechanism.
- 2026-09-05 · The watcher IS the cutter, not a separate worker: it cuts messages by subject using TF-IDF and files the pieces to topics. The topic agent picks up the cut pieces and rewrites them into wiki.
- 2026-09-05 · Topic agent should fire on new inbox writes (EVENT-DRIVEN), but the 5-min timer remains; the WatchPaths mechanism only syncs when the watcher scaffolds a new topic, not when the topic agent should run.

## Standing preferences
- Root causes, never band-aids. Everything live and visible. Markdown + built-in Hermes over custom code.
- Bots first, then loops; reuse a fleet bot when one fits; skills auto-apply. No pitches about the build process itself.
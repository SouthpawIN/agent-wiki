# Queue

## [SKILLS]
- [ ] librarian-cross-topic-discovery — distilled 2026-09-07 20:00 → skills-capabilities/librarian-cross-topic-discovery/SKILL.md (auto-applied)
- [ ] librarian-progressive-discovery — distilled 2026-09-07 18:21 → skills-capabilities/librarian-progressive-discovery/SKILL.md (auto-applied)
- [ ] hermes-runtime-config-fixes — distilled 2026-09-06 22:54 → skills-capabilities/hermes-runtime-config-fixes/SKILL.md (auto-applied)
- [ ] hermes-native-first-backend — distilled 2026-09-05 19:17 → skills-capabilities/hermes-native-first-backend/SKILL.md (auto-applied)
- [ ] wiki-fix-the-record-not-the-pitch — distilled 2026-09-05 18:58 → skills-capabilities/wiki-fix-the-record-not-the-pitch/SKILL.md (auto-applied)
- [ ] preempt-decision-test — distilled 2026-09-05 18:25 → skills-capabilities/preempt-decision-test/SKILL.md (auto-applied)
- [ ] chris-examples-are-illustrations — distilled 2026-09-05 18:06 → skills-capabilities/chris-examples-are-illustrations/SKILL.md (auto-applied)
- [ ] topic-agent-bot-first — distilled 2026-09-05 17:48 → skills-capabilities/topic-agent-bot-first/SKILL.md (auto-applied; edit or delete freely)
- [ ] wiki-media-hud-hitzones — distilled 2026-09-05 17:48 → skills-capabilities/wiki-media-hud-hitzones/SKILL.md (auto-applied; edit or delete freely)
- [ ] topic-context-llm-wiki — distilled 2026-09-05 17:42 → skills-capabilities/topic-context-llm-wiki/SKILL.md (auto-applied; edit or delete freely)
- [ ] wiki-overlay-z-order — distilled 2026-09-05 17:35 → skills-capabilities/wiki-overlay-z-order/SKILL.md (auto-applied; edit or delete freely)
- [ ] wiki-live-music-hookup — distilled 2026-09-05 17:29 → skills-capabilities/wiki-live-music-hookup/SKILL.md (auto-applied; edit or delete freely)
- [ ] wiki-live-activity-visibility — distilled 2026-09-05 17:24 → skills-capabilities/wiki-live-activity-visibility/SKILL.md (auto-applied; edit or delete freely)
- [ ] new-subject-early-trigger — distilled 2026-09-05 17:24 → skills-capabilities/new-subject-early-trigger/SKILL.md (auto-applied; edit or delete freely)
- [ ] topic-flywheel-gepa — PROPOSED 2026-09-05 17:05 → skills-capabilities/topic-flywheel-gepa/SKILL.md.proposed (approve: drop .proposed)
- [ ] watcher-per-message-filing — PROPOSED 2026-09-05 17:05 → skills-capabilities/watcher-per-message-filing/SKILL.md.proposed (approve: drop .proposed)
- [ ] sidebar-rubber-duck — PROPOSED 2026-09-05 17:05 → skills-capabilities/sidebar-rubber-duck/SKILL.md.proposed (approve: drop .proposed)
- [ ] *(empty)*
## [AGENTS]
- [ ] scan-topics-schema-fixer — SUGGESTED 2026-09-09 20:38: I see the live snapshot still has schema holes — want a builder bot to normalize `scan-topics.py` so every bot object ha → agents/scan-topics-schema-fixer.md.proposed
- [ ] librarian — SUGGESTED 2026-09-07 20:00: I see you're talking about a vault-wide discovery layer — want a bot that progressively surfaces the right wiki/skill/bo → agents/librarian.md.proposed
- [ ] vault-librarian — SUGGESTED 2026-09-07 18:21: I see you're talking about watching the whole vault and progressively surfacing wiki/skills-capabilities/bots-profiles/loops — want a bot that → agents/vault-librarian.md.proposed
- [ ] project-topic-scaffolder — SUGGESTED 2026-09-07 18:16: I see you want the watcher/topic-agent wired as an orchestrator over your actual projects — want a bot that scaffolds pr → agents/project-topic-scaffolder.md.proposed
- [ ] context-fallback-pin — SUGGESTED 2026-09-07 00:56: I see you're setting a 65K context fallback to Nous cloud — want a bot that scans every profile and pins this rule in co → agents/context-fallback-pin.md.proposed
- [ ] hermes-runtime-guard — SUGGESTED 2026-09-06 22:54: I see you're hitting Hermes runtime config landmines — want a bot that watches model-picker stickiness, TTS gateway fres → agents/hermes-runtime-guard.md.proposed
- [ ] sidebar-soul-rewrite — SUGGESTED 2026-09-05 18:06: I see the senter SOUL still says coordinator/delegator while you want a sidebar that does no work and rubber-ducks you — → agents/sidebar-soul-rewrite.md.proposed
- [x] **merge-topics (2026-09-02, from senter via klerik) — Execute the topic consolidation in `topics-wiki/senter/plans/topic-consolidation-2026-09-02.md` as a script `assets/merge-topics.py`.**
  - GATE: ONLY after anser's `## Anser audit` section in that plan file signs off on the merge table. If the audit section is absent or unsigned, report NEEDS-CHRIS and stop.
  - Build the script with a DRY-RUN mode that posts a diff summary to the bridge (POST http://127.0.0.1:8643/post, token in ~/.hermes/senter-bridge/token, bot "paladin").
  - Chris approves the RUN once — it is destructive-adjacent: originals go to `topics-wiki/_archive/<name>/`, never deleted; merged READMEs get `## Absorbed` + `## Repos`; `.system/` contents move into the target's session.md under dated headings; `[[wikilinks]]` rewritten across the vault; `index.md` + `catalogs/` regenerated.
  - Follow `## Working a topic queue` claim protocol; outcomes → `.system/session.md`.
- [x] **topic-similarity (2026-09-02, from senter) — Build `assets/topic-similarity.py` per `topics-wiki/senter/plans/similarity-governance-2026-09-02.md`: embed every topic, pairwise cosine, cluster, write `.system-live.json`.similarity; propose thresholds as needs_chris card with real top-20 pairs.**
## [LOOPS]
- [ ] snapshot-schema-audit — SUGGESTED 2026-09-09 20:38: Want a 30-minute fleet audit that re-runs the live snapshot and cards any `.md` suffixes, missing `model`, or non-int `s → triggers-loops/snapshot-schema-audit.md.proposed
- [ ] librarian-discovery — SUGGESTED 2026-09-07 20:00: Want a repeating discovery sweep that checks for duplicate, stale, or missing wiki/skill/bot/loop artifacts and surfaces → triggers-loops/librarian-discovery.md.proposed
- [ ] context-to-wiki-rename-sweep — SUGGESTED 2026-09-07 18:21: Want a loop that watches for 'context' references in vault docs and prepares rename proposals by topic? → triggers-loops/context-to-wiki-rename-sweep.md.proposed
- [ ] new-topic-activation — SUGGESTED 2026-09-07 18:16: Want a loop that watches for new project topic folders and primes the watcher/topic-agent so filings start immediately i → triggers-loops/new-topic-activation.md.proposed
- [ ] model-fallback-sticky-audit — SUGGESTED 2026-09-06 23:03: I see you just fixed model/TTS/vision session-boundary config — want a loop that audits fallback_providers and auxiliary → triggers-loops/model-fallback-sticky-audit.md.proposed
- [ ] hermes-config-drift-audit — SUGGESTED 2026-09-06 22:54: Want a loop that catches Hermes config drift before it silently switches models or breaks TTS? → triggers-loops/hermes-config-drift-audit.md.proposed
- [ ] record-vs-reality-audit — SUGGESTED 2026-09-05 18:58: The wiki just told its own agent a launchd job was deleted when it was still running — want looker to check every infra  → triggers-loops/record-vs-reality-audit.md.proposed
- [ ] topic-governance-rehome — SUGGESTED 2026-09-05 18:53: Topic merge/split governance has had no owner since the umbrella script was deleted at 17:53 — want paladin to run it on → triggers-loops/topic-governance-rehome.md.proposed
- [x] completion-sweep — SUGGESTED 2026-09-05 18:25: You said 'look for things that aren't complete yet and complete them' — want klerik to sweep every topic's Open items /  → triggers-loops/completion-sweep.md.proposed — superseded 2026-09-05 (build-process chatter or already done)
- [ ] topic-agent-on-inbox-write — SUGGESTED 2026-09-05 18:06: topic-agent.py runs on a 5-minute timer, which is exactly the 'timed loader' you banned — want teknium to make it fire t → triggers-loops/topic-agent-on-inbox-write.md.proposed
- [ ] topic-governance — SUGGESTED 2026-09-05 18:06: The umbrella that did topic merge/split and skill dedupe vanished when we collapsed to one agent per topic — want paladi → triggers-loops/topic-governance.md.proposed
- [ ] *(empty)*
CLAIM merge-topics paladin 2026-09-02T22:00:24Z
NEEDS-CHRIS merge-topics paladin 2026-09-02T22:07:50Z — dry-run posted; awaiting approval + aichess/veiled ruling
CLAIM topic-similarity paladin 2026-09-02T23:11:43Z
DONE merge-topics paladin 2026-09-02T23:37:11Z
DONE topic-similarity paladin 2026-09-02T23:37:11Z

## 2026-09-03 — live-session steering items (from Chris, default-profile chat)
- [x] [PLUGINS] Remove the bottom-left pets overlay (#runInd) entirely — running-worker signal TBD. DONE (vault-live.html edited directly).
- [x] [PLUGINS] Orbs at grown size + numbers INSTANTLY on title hover. DONE.
- [x] [PLUGINS] Fix dots snapping left on hover-off — root cause, no band-aid. DONE (orbColumn measurement pass).
- [x] [PLUGINS] WIKI rows live from .system-live.json (baked rows retired to offline fallback). DONE.
- [x] [PLUGINS] Title hover → LOCK option protecting a topic from auto-merge/summarization (persisted + honored server-side). DONE (bridge /write + similarity/merge guards).
- [x] [LOOPS] Bot messages visible in the Hermes desktop chat sidebar. DONE (cron senter-fleet-feed, every 2m, relay script).
- [x] Similarity recalibration: name-containment pairs must score HIGH (pocket-shop/pocket-shop-pricing), distinct families stay apart (turbohaul vs turbofit). DONE.
- [ ] [PLUGINS] Chris: "there's going to be one more thing" — await spec.
- [ ] Verify live-rows + lock pill + instant orbs in Chris's real pane (headless browser unavailable; preview pane is the target surface).

## 2026-09-03 — batch 2 (from Chris, live)
- [x] [PLUGINS] Dots a little further left → then superseded: "closer to the middle, almost touching the girl's fingers" — centred on the title↔fingers band (−5px nudge applied then reverted per correction).
- [x] [PLUGINS] Integrations BETWEEN dots and titles; dots = end of the hover zone; beyond dots = dead space; ONLY dead-zone activation = click opens SPACE. SPACE removed from nav (LOOPS in its place). DONE.
- [x] [PLUGINS] Expand-to-right → expand-to-LEFT (more room between dots). DONE.
- [x] [PLUGINS] Buttons off the input bar — caret = whole-app search (multi-candidate overlay / single-candidate auto-jump). DONE.
- [x] [LOOPS] scan-topics watcher made durable (launchd com.senter.scanwatch) — the live snapshot never goes stale again. DONE.

## [CONTEXT]
- [ ] research hermes-snapshot-schema-upstream — SUGGESTED 2026-09-09 21:34: Want me to look into whether Hermes Agent already has a planned path for unified live-snapshot bot schema merging, so we
- [ ] research system-live-source-audit — SUGGESTED 2026-09-09 21:16: Want me to look into which .system-live.json the Hermes Desktop UI actually reads?
- [ ] research snapshot-stale-cache-research — SUGGESTED 2026-09-09 20:38: Want me to look into why `senter-wiki-readme-live` still shows `skills=[]` after a patch — is the bridge serving a stale
- [ ] research verify-event-driven-trigger — SUGGESTED 2026-09-08 13:25: Want me to look into the topic-agent trigger path?
- [ ] research verify-live-preview — SUGGESTED 2026-09-08 08:58: Want me to look into the live preview state for the UI elements (background image, Q-in-headphones, dot alignment)?
- [ ] research wiki-to-project-bridge-research — SUGGESTED 2026-09-07 20:00: Want me to look into the minimal set of explicit bridges needed for the center wiki to use the agent-wiki GitHub repo as
- [ ] research topic-anatomy-migration-plan — SUGGESTED 2026-09-07 18:21: Want me to look into what renaming and restructuring to `wiki/` + `skills-capabilities/` + `bots-profiles/` + `triggers-loops/` would touch in watcher,
- [ ] research project-topic-inventory — SUGGESTED 2026-09-07 18:16: Want me to look into what project topics already exist in the vault and which active projects don't have a matching sent
- [ ] research context-size-fallback-research — SUGGESTED 2026-09-07 00:56: Want me to look into whether Hermes config supports context-size-based provider selection natively?
- [ ] research hermes-profile-config-inheritance — SUGGESTED 2026-09-06 23:03: Want me to look into Hermes profile config inheritance for fallback_providers and auxiliary.*?
- [ ] research hermes-upstream-freshness-fix — SUGGESTED 2026-09-06 22:54: Want me to look into whether Nous Research has already upstreamed a `force_fresh` fix for TTS gateway entitlement cachin
- [ ] research hermes-per-message-hook — SUGGESTED 2026-09-05 19:17: Want me to look into whether Hermes already exposes (or has a PR in flight for) a per-message plugin hook, so the watche
- [ ] research verify-apply-paths-and-watchpaths-landed — SUGGESTED 2026-09-05 18:58: Want me to verify that the two 18:18 completions actually landed — com.senter.topic-agent runs on WatchPaths (not a 5-mi
- [ ] research cut-accuracy-audit — SUGGESTED 2026-09-05 18:06: Want me to look into how often the watcher mis-cuts your messages — the shorts example landed in youtube, but nothing me

## [2026-09-05 18:33] closed today
- [x] watcher per message → cutter · [x] topic agent (wiki+pitches) · [x] approve applies (cron/bot/research) · [x] sidebar SOUL on senter · [x] music live · [x] layers
- [ ] kanban claims (lock files suffice for now) · [ ] Spotify id · [ ] desktop sidebar → senter profile

---
- [ ] [WIKI] Row diff badges (.rdiff): fixed-width slot between usage and dots; clamp bloom to slot; empty slot reserves space.
- [ ] [WIKI] Edits silent on row: diffs update card in-place or post to feed; no auto-open editor on wiki diff.

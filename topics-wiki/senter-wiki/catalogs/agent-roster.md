---
title: Agent Roster
updated: 2026-08-27
type: catalog
---

# Agent Roster

Named agent profiles across the fleet.

| Agent | Repo | Notes |
|---|---|---|
| klerik | [[topics-wiki/senter/klerik-profile|profile]] | Hermes Agent meta-profile for reviewing and correcting other agent profiles |
| anser | [[topics-wiki/anser/README|repo]] | Hermes Agent tech support moderator for the Nous Research Discord |
| frieza | [[topics-wiki/legacy-bots-profiles/README|repo]] | Galactic Emperor of Discord — server admin agent for Hermes Agent |
| crow | [[topics-wiki/crow/README|repo]] | Crow — deep research agent for Hermes Agent. Produces lore via web search, extraction, and llm-wiki structure. |
| kashik | [[topics-wiki/kashik/README|repo]] | Silent historian and librarian — watches agent activity and maintains per-agent llm-wiki documentation |
| veiled | [[topics-wiki/music/README|repo]] | Veiled — cosmic prose lyricist & song forge Hermes Agent profile |
| llmc | [[topics-wiki/music/README|repo]] | LLMC — LLM + MC. Your lyric and song companion. Hermes Agent profile. |
| jestur | [[topics-wiki/nous-community/README|repo]] | Creative studio gremlin Discord DM companion for Hermes Agent |
| test-bot | [[topics-wiki/hermes-agent/README|repo]] | Creative operations bot — Discord DM companion for image, music, and video generation |
| senter | [[topics-wiki/senter/README|repo]] | Hermes Agent profile distribution |
| chizul | [[topics-wiki/legacy-bots-profiles/README|repo]] | Hermes Agent profile distribution |
| nous-girl | [[topics-wiki/nous-community/README|repo]] | Hermes Agent profile distribution |
| nous-girl-agent | [[topics-wiki/nous-community/README|repo]] | Nous Girl agent + OmniStep Evolution Radio plugin — curated local model pet, multimodal by default, voice + music from the model |
| Senter-archive | [[topics-wiki/senter/README|repo]] | A lightweight, skill-aware AI agent that uses RAG-based capability discovery. |


## Pets (Senter Wiki avatars)
senter=senter-owl · turbosovth=s0uthpaw · teknium=teknium · dogeman=123mikeyd · klerik=klerik-stitcher · anser=anser-warden · paladin=paladin-warden. Regenerate: `assets/hatch-pet.py --bot <bot> --slug <slug> "<concept>"`.

## Terminology (locked 2026-09-02)
**Bots** = the individual Hermes profiles we create (senter, turbosovth, klerik, anser, teknium, dogeman, paladin). **Hermes Agent** = the whole runtime they live in. Say *bots*, not *agents*, in all UI, docs, and chat. The vault directory `topics-wiki/<name>/agents/` keeps its name for GOOP-spec compatibility; it holds bots.

| weaver | Senter Wiki UI builder — owns vault-live.html + assets/, works topics-wiki/senter-wiki/.system/queue.md top-down ([FIXES]→[FEATURES]→[LOOPS]); verifies headless before reporting | pet: weaver | spawned 2026-09-02 by klerik |
| paladin | Repo + vault structure standards: topic merges, renames, index/catalog regen, wikilink rewrites — scripted, dry-run first, nothing deleted. Home topics-wiki/senter. Model claude-fable-5.1 | pet: paladin-warden | spawned 2026-09-02 by klerik, smoke-verified by senter |
| fleet-orchestrator | Kanban board orchestrator — triages, decomposes, dispatches, ticks, and routes cards across the fleet; never builds. Home topics-wiki/senter. Model claude-fable-5.1 | no pet yet | spawned 2026-09-05 by senter/klerik, smoke turn emitted bridge/loaded |

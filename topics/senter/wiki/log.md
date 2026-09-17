# Senter Topic Wiki Log

## [2026-09-09] compile | raw/inbox/2026-09-09.md

**Created pages:**
- wiki/concepts/vault-repo-mapping.md — observed three repos in gh-sync (agent-wiki, klerik, senter); relationship to vault working directory unresolved
- wiki/queries/vault-repo-link-status.md — query to verify whether ~/Documents/Projects/Projects is a git repo, symlink, or separate path

**Key findings:**
- raw/2026-09-09.md contains only hermes: working lines (no Chris requests); filed as evidence
- Vault-to-repo mapping (gh-sync → agent-wiki/klerik/senter) is an infrastructure concern; the working directory's git link status was investigated but not resolved
- No new Chris decisions or corrections in this item

**Misrouted:** none (all content belongs to senter per vault/repo/git aliases)

---

## [2026-09-08] compile | raw/inbox/2026-09-07.md, raw/inbox/2026-09-08.md, raw/inbox/2026-09-08-from-hermes-agent.md, raw/inbox/2026-09-08-from-kashik.md

**Created pages:**
- wiki/decisions/2026-09-08-autonomous-completion-standing-approval-extended.md — Chris's re-authorization for autonomous completion
- wiki/concepts/vault-agents-vs-profile-bots.md — distinction between proposed vault specs and live profile bots
- wiki/concepts/bridge-server-restart-via-launchd.md — launchd restart procedure for bridge server
- wiki/entities/turbosovth.md — moved from other-fleet-bots.md (bot entity page)
- wiki/entities/dogeman.md — moved from other-fleet-bots.md (bot entity page)

**Updated pages:**
- wiki/entities/senter.md — added extended standing approval, fleet roster, related pages
- wiki/entities/anser.md — confirmed librarian proposal and looker delivery
- wiki/decisions/2026-09-08-complete-senter-wiki-autonomously.md — fixed miswikilinks to correct pages
- wiki/decisions/2026-09-08-senter-wiki-bot-topic-folder-missing.md — status: creation in progress per 09:00-09:56 investigation
- wiki/decisions/2026-09-08-bridge-scan-topics-bot-name-parsing.md — clarified confusion in original analysis; `split(".md")` correctly strips simple extensions
- wiki/queries/event-driven-trigger-gaps-2026-09-08.md — added 09:22-09:56 investigation findings
- wiki/queries/senter-timeline.md — added 2026-09-08 open items

**Misrouted (anti-scope → other topics):**
- raw/inbox/2026-09-07.md MTPLX warmup/memory-guard → turbofit
- raw/inbox/2026-09-07-from-turbofit.md → turbofit
- raw/inbox/2026-09-07-from-hermes-agent.md (context compaction timeouts) → hermes-agent
- raw/inbox/2026-09-08.md (kashik `.split(".md")` test) → senter-wiki (already in scope for senter per scan-topics.py analysis)
- Various async delegation batch-complete receipts → background process noise
- Duplicate reroute headers from memento/hermes → misrouted noise

**Key findings:**
- Bridge server restarted via launchd with patched code; live data pipeline verified 09:43
- Topic-agent trigger path investigation ongoing (09:22-09:56)
- senter-wiki-bot topic folder needs creation with standard wiki/skills/bots/loops structure
- Vault agents in `topics/*/agents/` are proposed specs, not live bots; live bots are in `~/.hermes/profiles/`

## [2026-09-07] compile | raw/inbox/2026-09-07-from-memento.md
Result: no wiki pages created. Item is duplicate-rerouted memento/hermes noise with no new Chris decision; filed as misrouted instead.

## [2026-09-07] compile | raw/inbox/2026-09-07-from-senter-wiki.md
Result: no wiki pages created. Item is pure duplicate-rerouted hermes noise with no new Chris decision; filed as misrouted instead.
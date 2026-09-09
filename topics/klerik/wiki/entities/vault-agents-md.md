---
title: Vault AGENTS.md — behaviour rules for any Hermes running in the vault dir (drafted 18:47, written 18:50, 2026-09-05)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [spec, infra, bot, decision, question]
sources: [raw/inbox/2026-09-05.md]
confidence: medium
contested: true
---
# Vault AGENTS.md

**What it is.** A proposed `AGENTS.md` at the vault root (`~/Documents/Projects/Projects/AGENTS.md`) — "behaviour rules for any Hermes in this dir" ^[raw/inbox/2026-09-05.md]. Hermes reads an `AGENTS.md` from the working directory as project-level instructions, so this one file would bind every profile whose workdir is the vault: the topic agents, the senter-bridge apply steps, and klerik's drain loop (its cron job's workdir is exactly `/Users/sovthpaw/Documents/Projects/Projects`). It does not exist on disk at 18:48.

**State.** Drafted, not written: "blocked as a protected file — I have the text ready." ^[raw/inbox/2026-09-05.md] Listed at 18:47 as the second of three items "Blocked on you (one click each, not a decision)" ([[topics/klerik/wiki/queries/what-is-blocked-on-chris|What is blocked on Chris?]]). The draft text itself is not in the raw; the wiki does not remember its contents.

**Relation to the 18:31 "leave AGENTS.md alone" ack (contested).** Sixteen minutes before this item was listed, the session wrote "Noted — I'll leave AGENTS.md alone." ^[raw/inbox/2026-09-05.md] The earlier compile could not tell which AGENTS.md (default profile's vs klerik's). This item adds a third, and now most likely, reading: the session tried to create the vault `AGENTS.md`, the protected-file prompt appeared, Chris declined or deferred it, and the session acknowledged. If so, "blocked … I have the text ready" at 18:47 is the same file re-offered, and Chris has already once said no (or not now). All three readings are kept in [[topics/klerik/wiki/decisions/2026-09-05-leave-agents-md-alone|Leave AGENTS.md alone]]; this page marks the third as most probable but unconfirmed — the ask was never filed, only the ack.

**Why klerik should care.** klerik's authoring lane is profile files; a vault-root AGENTS.md is a *project* file and outside that lane — it belongs to paladin (vault structure) if anyone. But its content would govern what klerik's drain loop may do when it ticks in the vault, so klerik's rules ([[topics/klerik/wiki/entities/klerik|klerik]]) and this file must not contradict each other. Until it exists, the drain loop runs under klerik's own SOUL/AGENTS only.

**Open questions.** (1) Does Chris want this file at all — was 18:31 a "no" or a "not now"? (2) If yes, what is in the draft — it should be captured into a topic (`raw/sources/`) before it is written, so the wiki remembers it. (3) Should the one-click ask be a wiki card rather than a CLI prompt, consistent with "decisions to him as wiki cards"?

**Update 19:07 — WRITTEN.** `~/Documents/Projects/Projects/AGENTS.md` exists: 2284 b, mtime 2026-09-05 18:50, opening "# Senter vault — how Hermes behaves here (loaded automatically when cwd is the vault) … Read `topics/senter/.system/architecture.md` once per session." The 18:47 "blocked as a protected file — I have the text ready" ^[raw/inbox/2026-09-05.md] was cleared within three minutes of the stand-up; the 18:58 close-out does not mention it, consistent with it no longer being open. This is the file klerik's drain loop inherits when its workdir is the vault. Cleared list: [[topics/klerik/wiki/queries/what-is-blocked-on-chris|What is blocked on Chris?]]; the 18:31 veto reading in [[topics/klerik/wiki/decisions/2026-09-05-leave-agents-md-alone|Leave AGENTS.md alone]] — if the veto referred to this file, it was overridden by the nod at 18:50; if to another, it still stands. `contested: true` remains.

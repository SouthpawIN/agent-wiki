# Hermes Built-In Self-Reflection & Self-Knowledge Machinery — Audit

Date: 2026-09-01 16:22 CDT
Prepared by: Anser (@anser)
For: Senter (@senter) — first-mission deliverable

---

## 0. Config boot verification (per your handoff)

- config.yaml now parses clean. `model.base_url: null`, `model.default: deepseek/deepseek-v4-pro`, `model.provider: nous`. The 33 `***` placeholders are gone — every `base_url`/`api_key` under `auxiliary.*` is now `null`.
- Corrupt backup confirmed on disk: `config.yaml.corrupt.20260831-174322.bak` (18,038 bytes vs the 18,071-byte clean file).
- My live runtime reports `deepseek/deepseek-v4-pro / nous` — the profile is booting on the intended model.
- Credential note for you: the profile dir `~/.hermes/profiles/anser/` has **no `.env` and no `auth.json`** — only `.env.EXAMPLE` (197 B) and an empty `auth.lock`. The real secrets live at the parent `~/.hermes/.env` (24,792 B) and `~/.hermes/auth.json` (10,471 B). This session is authenticated, so the Nous OAuth pool is being resolved from the shared home — but if you want per-profile secret isolation, that symlink/copy still needs wiring. Flagging as you asked, not blocking: it works today.

---

## 1. Audit scope

"Self-reflection / self-knowledge machinery" = anything that lets an agent (or its runtime) (a) hold durable knowledge about itself, the user, or its history, (b) improve itself over time, or (c) verify its own work. Hermes ships these in distinct layers with different persistence, retrieval, and lifespan semantics. Each section: what it covers / what it doesn't / does the proposed **agent-wiki vault** overlap it.

---

## 2. Per-mechanism verdicts

### 2.1 Memory (the `memory` tool)

**Covers:** Two flat text stores — `user` (who the user is: name, preferences, style) and `memory` (agent's own notes: environment facts, conventions, tool quirks, lessons). Injected into every turn. Hard char budget (config: `memory_char_limit: 2200`, `user_char_limit: 1375`). Batched atomic writes; on overflow the agent must consolidate in the same batch. Background "flush" via the `flush_memories` auxiliary model (kimi-k2.6) and a periodic `nudge_interval: 10` reminder.

**Doesn't cover:** Structure. It's a flat list of declarative sentences with no interlinking, no taxonomy, no schema, no query language (you can't ask "what do I know about X" — you get everything, always, verbatim). It can't hold a rich self-model (capability maps, decision trees, relationships between facts). Enforced-tiny by design, so it self-prunes to high-signal one-liners.

**Agent-wiki vault overlap:** Partial, on the *declarative fact* axis only. The vault would be a superset of memory's intent (structured, interlinked, queryable self-facts), but memory's unique property — auto-injected into every turn — is not something a file-tree vault provides. A vault does not replace memory; it would *export* its distilled conclusions into memory as one-liners.

### 2.2 Skills + self-improvement (skill_manage / skill_view)

**Covers:** Procedural memory — reusable how-to workflows (`SKILL.md` + references/templates/scripts). The agent creates and patches its own skills after hard tasks; new sessions auto-load them. This is Hermes's primary "learning" loop.

**Doesn't cover:** Declarative self-knowledge ("who am I", "what have I decided", "what do I currently believe"). Skills answer "how do I do X", not "what do I know / who am I". A skill is a procedure, not a self-model.

**Curator (skill lifecycle) — worth calling out separately:** Background subsystem that tracks per-skill usage (`.usage.json` sidecar: use_count/view_count/patch_count/last_activity), marks idle agent-created skills stale, archives (never deletes) them, and can consolidate overlaps. It is Hermes's *automated* self-improvement hygiene. It only touches skills with `created_by: agent`; bundled/hub skills are off-limits; pinned skills exempt.

**Agent-wiki vault overlap:** Low. Different axis (procedural vs declarative). But the **Curator pattern is the template** the vault would need — a lifecycle manager that tracks what's stale, archives, consolidates, and never hard-deletes. The vault has no equivalent today.

### 2.3 Session search (`session_search`)

**Covers:** Episodic recall. FTS5 over the canonical `state.db`; query (ranked discovery + temporal sort), scroll (window around an anchor message), and full read of a past session. This is "what did we do about X" — raw conversation history.

**Doesn't cover:** Distillation. It returns *raw messages*, not synthesized conclusions. It's the agent's memory of *events*, not its memory of *lessons*. Searching is keyword/FTS, not semantic or structured. It also requires the agent to think to search — nothing from it is auto-injected.

**Agent-wiki vault overlap:** Complementary, not duplicative. Session search is the raw episodic layer; the vault would be the distilled declarative layer *built from* it (e.g. "decision log" pages that compress many sessions into one page). The vault's value is precisely that it is the synthesis session-search can't give you.

### 2.4 AGENTS.md / project context files / SOUL.md

**Covers:** Static instruction injection. `AGENTS.md`/`agents.md` (cwd-only), `.hermes.md`/`HERMES.md` (parent-walk to git root), `CLAUDE.md`, `.cursorrules` — one loaded per session, capped 20k chars, threat-pattern scanned. `SOUL.md` (in `$HERMES_HOME`) is identity/persona and always loaded.

**Doesn't cover:** Growth. These are authored files, not self-accumulating knowledge. An agent doesn't append to its own AGENTS.md as it learns — it's a fixed operating contract, not a growing self-model. No history, no versioning of beliefs, no interlinking.

**Agent-wiki vault overlap:** Low-medium. The vault *feels* similar (markdown files an agent reads), but AGENTS.md/SOUL.md are *authoritative fixed inputs* while the vault is *self-accumulating state*. Key design rule that falls out: the vault must live **outside** the context-file discovery path so it never gets injected verbatim (it would blow the 20k cap and pollute every turn) — it must be *queried on demand* like a skill or via search_files.

### 2.5 Verification hooks

**Covers:** Output-quality guardrails, layered in the runtime and the system prompt:
- **Behavioral constitution** (system prompt): `<verification>` (correctness/grounding/formatting/safety/completion), `<external_state_verification>` (re-read the target after any external write — "a successful tool call is not a successful task"), `<mandatory_tool_use>` (never answer from memory what a tool can check), "Finishing the job" (deliver a working artifact, not a description).
- **`display.file_mutation_verifier: true`** — confirms on-disk hashes after file writes (backed by `verification_evidence.db`, present in the profile dir at 32,768 B).
- **`tool_loop_guardrails`** — detects exact-failure / same-tool-failure / idempotent-no-progress loops; warns then optionally hard-stops.
- **`checkpoints`** — periodic session snapshots (max 50, auto-prune) enabling resume/rollback.
- **Context compression** — the agent self-summarizes long history instead of truncating, preserving continuity of its own reasoning.

**Doesn't cover:** *Persistent* self-knowledge. These are transient, per-run checks. They verify *work product*, not *identity/beliefs*. They generate evidence (verification_evidence.db) but don't aggregate it into anything durable the agent can introspect later.

**Agent-wiki vault overlap:** None directly — verification is about truth of *actions*, the vault is about truth of *self*. But note: a vault would *need* these hooks (its pages are only as trustworthy as the verification that produced them). The vault could even ingest verification evidence as provenance.

### 2.6 Cron continuity

**Covers:** Recurring-task state. `continuity: true` injects a job's own previous output each run (dedupe / incremental progress); `context_from: [job_id]` chains one job's output into another; `monitor` is a change-detector gate (cheap deterministic pre-check that skips the agent run when nothing changed). This gives *autonomous, unattended* agents a memory that survives between runs.

**Doesn't cover:** Cross-job / cross-agent self-knowledge. Continuity is scoped per-job (a single recurring task's "where I left off"), not a shared self-model for the whole fleet. A scout that learns "this feed changes at 9am" holds that only inside its own job's continuity buffer.

**Agent-wiki vault overlap:** Adjacent but distinct. Cron continuity is *operational* continuity for one task; the vault would be *shared* declarative knowledge for the whole fleet. The vault is arguably what several cron jobs should *write into* so lessons cross-pollinate instead of living in isolated continuity buffers.

### 2.7 "Anything we missed" — additional mechanisms not on your list

- **Skills list / available_skills snapshot** — every session starts with a self-inventory of what the agent can do (name + description of every installed skill). This is *capability self-awareness*, auto-injected. But it's one-line-per-skill, not a capability *model*.
- **Curator** — already covered in 2.2; it's the automated self-improvement hygiene layer, easy to overlook because it runs in the background.
- **Context compression** — self-summarization of the agent's own reasoning history (covered in 2.5).
- **`flush_memories` + memory nudge** — background distillation of the live session into durable memory (covered in 2.1).
- **`profile_describer` auxiliary model** — an aux-model that generates descriptions of profiles (used by the dashboard/roster). A tiny piece of "the system describing itself".
- **Bot-mode roster + `message_agent`** — the agent knows its teammates (names + roles) and can message them. *Fleet self-awareness*, but the roster lives in the system prompt / profile files, not in a queryable store.
- **Self-improving suggestion engine (sovth-config)** — in this profile's AGENTS.md: on every tech-support question, check `SouthpawIN/sovth-config` for a matching profile/skill; gap → brainstorm (nous-girl) → review (klerik) → publish. This is a *human/fleet-authored* improvement loop, not an automated store.
- **Context-length cache (`context_length_cache.yaml`)** — runtime caches per-model context windows; infrastructure self-knowledge.
- **`verification_evidence.db`** — durable evidence store backing the file-mutation verifier (covered in 2.5).

---

## 3. Gap analysis — what self-knowledge has NO home today

Mapping the axes: **episodic (events) / procedural (how-to) / declarative (facts-about-self) / verification (is-it-true) / operational (recurring-state)** against the mechanisms:

| Axis | Mechanism | Structured? | Queryable? | Auto-injected? |
|---|---|---|---|---|
| Episodic (what happened) | session_search | No (FTS) | Yes (FTS) | No |
| Procedural (how to) | skills | Yes (SKILL.md) | Yes (skill_view) | On load |
| Declarative (facts) | memory | No (flat) | No | **Yes (every turn)** |
| Declarative (identity) | SOUL.md | Semi | No | Yes (static) |
| Verification (true?) | hooks + evidence DB | Partial | No | No |
| Operational (recurring) | cron continuity | No | Per-job only | Per-job only |

**The real gap is the declarative self-model.** There is no place where the agent holds a *structured, interlinked, queryable* description of: its own capabilities (beyond one-line skill blurbs), its accumulated decisions and their rationale, lessons learned, its relationships to teammates/tools, and contradictions/uncertainties it has flagged. Today that knowledge is either (a) squeezed into 2,200 chars of flat memory, (b) lost in raw session transcripts, or (c) scattered across per-job continuity buffers and human-authored AGENTS.md.

That is exactly what an agent-wiki vault would house, and nothing currently occupies that slot.

---

## 4. Verdict — does the agent-wiki vault fill a real gap or duplicate?

**Fills a real gap — if (and only if) it is scoped as the *declarative self-model layer*.**

- **It is NOT a duplicate of memory** — memory is flat, tiny, auto-injected; the vault is structured, unbounded, on-demand. They compose: vault → distilled one-liners → memory.
- **It is NOT a duplicate of skills** — skills are procedures; the vault is self-description/decision/lesson pages. The vault *references* skills ("capability: see skill X") but doesn't replace them.
- **It is NOT a duplicate of session_search** — search is raw episodic recall; the vault is the synthesized declarative layer built *from* those episodes.
- **It is NOT a duplicate of AGENTS.md/SOUL.md** — those are fixed authored contracts; the vault is self-accumulating state, and must be kept *out* of the context-file injection path.
- **It IS a reuse opportunity, not a new plumbing project** — the `llm-wiki` skill (Karpathy wiki pattern) already ships the exact substrate: SCHEMA.md (conventions/taxonomy), index.md (catalog), log.md (append-only action log), entity/concept pages with frontmatter, wikilinks, lint (orphans/broken links/contradictions/staleness), and an "orient first" resume protocol. Point that machinery at a *self-knowledge domain* instead of external research, and the vault is 80% built.

**Concrete recommendation:**
1. Scope the vault to declarative self-knowledge: capability inventory, decision log (with rationale), lessons-learned taxonomy, teammate/tool relationships, open-questions/contradictions.
2. Reuse `llm-wiki`'s three-layer structure (SCHEMA/index/log) as the substrate; give it its own `SCHEMA.md` defining self-knowledge conventions.
3. Add a **curator-style lifecycle** (like the skills curator): usage tracking, staleness, archive-never-delete, optional consolidation — because the vault will otherwise rot the same way unmanaged wikis do.
4. **Do not** inject the vault verbatim into the system prompt; make it query-on-demand (search_files / skill_view style), and flush its one-line conclusions into `memory` so the always-loaded layer stays current.
5. Give cron jobs a place to *write* shared lessons (today their continuity buffers are siloed) — the vault is the natural shared sink.

**Bottom line:** the vault is the missing *declarative self-model* layer. Hermes covers episodic (search), procedural (skills), flat-fact (memory), and verification (hooks) self-knowledge well; it has no home for a structured, growing, queryable account of what the agent *is* and what it has *decided*. Build that, don't re-plumb what already exists.

---
name: agent-wiki-vault
description: Use when working in the user's agent-wiki Obsidian vault.
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [obsidian, agent-wiki, goop, workflow, hermes]
metadata:
  hermes:
    tags: [obsidian, agent-wiki, goop, workflow, hermes]
    related_skills: [obsidian]
---

# Agent-Wiki Vault Workflow

## When to use

- The user references "the vault", "the canvas", Obsidian vault edits, or agent-wiki.
- Starting a session that touches `~/Documents/Projects/Projects`.
- Spawning async agents whose briefs live in a topic's `.system/session.md`.

The user runs an Obsidian vault as the **session canvas**, structured per their
[agent-wiki](https://github.com/SouthpawIN/agent-wiki) spec (GOOP). The vault is not just
documentation — it is the coordination layer between the user, the agent, and async agents.

## Vault path

Resolve at session start: check the memory entry, else
`~/Library/Application Support/obsidian/obsidian.json` (`vaults.*.path`), else
`~/Documents/Projects/Projects`.

## Per-turn contract (user-mandated)

1. **Read first**: `topics-wiki/<active-topic>/.system/session.md` — live state: verified steps,
   in-flight work, fix list, and the async-agent launchpad.
2. **Update every turn**: session.md (state changes) + `.system/queue.md` (new fixes/ideas)
   + `log.md` (dated one-liner). Stale canvas = broken workflow; the user checks this.
3. **Ideas verbatim**: user ideas land in `Ideas.md` quoted verbatim, then triaged with a
   framing paragraph and a status line.

## Structure (GOOP)

- `index.md` — entry; `catalogs/` (fleet-dashboard, topic-index, agent-roster, skill-registry,
  loop-registry); mirrored into `topics-wiki/_global/.system/`.
- `topics-wiki/<topic>/` — one per repo/project: `README.md` (human dashboard: facts + README
  extract), `.system/` (continuity.md, session.md, queue.md, injections.md), `skills-capabilities/`,
  `agents/`, `triggers-loops/`.
- User edits ARE the steering wheel: user corrections to continuity.md are never overwritten;
  queue items `[SKILLS]/[AGENTS]/[LOOPS]/[PLUGINS]` typed by the user are actionable work.

## Async-agent launchpad

session.md carries lettered agent briefs (A, B, C…). Each brief: goal, inputs, blockers.
Launch pattern: user says "launch B and D" → delegate_task with the session doc content as
context (children see nothing of this conversation). Keep briefs self-contained.

## Layout for live watching

User likes watching vault edits live with the Hermes HUD docked at the bottom of the screen.
- Position via osascript System Events (needs Accessibility grant; ask user to click Allow).
  Obsidian top (0,25 → 1512x600), Hermes HUD bottom (0,640 → 1512x230) on a 1512x894 pt display.
- Pitfall: cua-driver focus_app/window matching misses Electron apps (Obsidian) after
  AppleScript positioning — drive positioning through `osascript` System Events instead.
- Never click macOS permission dialogs; hand them to the user.

## Pitfalls

- Web-scraped GitHub repo lists undercount; the API (`/users/<u>/repos?per_page=100`)
  returns more. Pull via API, READMEs via raw.githubusercontent (not rate-limited).
- Deep vault builds: write a Python builder script (write_file + terminal), not dozens of
  write_file calls. Verify with a walk + spot-read one topic.
- Read `references/remote-absorption-ssh.md` before any SSH-based consolidation (surveying or
  pulling Hermes data from another machine — pty password pattern, scp-vs-base64 transfer
  gotchas, async du recipe, consent gate for passwords shared in chat).

## Fleet consolidation (multi-machine absorption, validated 2026-08-28 senter→Mac)

When the user asks to absorb another machine's Hermes/files into the vault as "one source of
truth", the working shape is:

1. **Topic per effort** (`topics-wiki/<host>-consolidation/`): README.md = the survey (fleet table,
   what lives where, redundancy clusters, phase plan); `.system/session.md` = live state +
   lettered agent briefs; `.system/queue.md` = steering items (password rotation, dirty
   worktrees, cron fate). The survey IS the absorption artifact.
2. **Redundancy clusters** are the deliverable the user cares most about — enumerate dupe
   variants (e.g. repo vs repo-local vs repo-upstream vs scratch variants), record last-commit
   dates + sizes + non-git status, and propose MERGE/KEEP/DELETE per cluster for user approval.
   Never delete anything during survey.
3. **Order of pull**: memories + skills + config first (small, high value), then sessions
   manifest (index before content), then project docs. Multi-TB model weights are documented
   via their registry file (e.g. MODEL-REGISTRY.md), never pulled wholesale.
4. **Dedup execution policy varies by user mandate** — default is propose-then-approve, but on
   2026-08-28 Chris overrode it mid-run: "act without my permission … I can recover whatever
   you delete, important stuff is on GitHub." When the user grants blanket deletion authority,
   execute the matrix autonomously in recoverable form: MERGE = `cp -Rn donor/. keeper/.merged-<donor>/`
   then `mv` donor aside; ARCHIVE = plain `mv` into `_archive_<date>/`; DELETE only tiny assets;
   write a MANIFEST.md in the archive dir mapping every move. Big `cp -Rn` merges (500M+) exceed
   foreground SSH timeouts — run detached remotely with a sentinel file (`echo DONE > /tmp/status`),
   then poll.
5. **Destructive phases (wipe/reinstall) need explicit user go-ahead per phase** — a survey
   that surfaced dirty worktrees, live cron jobs, and disk-capacity data feeds that decision;
   don't start it unasked. (Exception: a mid-run blanket mandate like "act without my
   permission" transfers approval authority for that phase — see item 4.)
   `~/.hermes/config.yaml` outright (security-sensitive path); `hermes config set providers.<name>.api <url>`
   etc. works and takes nested dotted keys. Back up config first (`cp config.yaml config.yaml.bak.<tag>`).
   Switching a provider to a remote gateway = set `api` + `default_model` + per-model
   `models.<key>.model`, then verify with `hermes config get providers.<name>` + curl the gateway.

## Repo rename / fleet consolidation into Senter (2026-08-29, validated)

The GitHub org was consolidated: `agent-wiki` + `klerik` + `senter` → one repo **Senter**
(user directive: "this should combine senter, agent wiki, and klerik … replace all with
Senter"). The vault-side procedure that worked:

1. `git mv`-style topic rename: `topics-wiki/agent-wiki` → `topics-wiki/senter` (mv the dir). If a
   same-named topic already exists (old senter), archive its README as
   `fleet-orchestrator-profile.md` inside the merged topic before overwriting; same for
   klerik → `klerik-profile.md`.
2. Preserve the old topic's `.system/` under `.system/archive/<old-name>-old/` — never
   delete continuity/queue history.
3. Repoint catalogs with targeted replaces: `[[topics-wiki/klerik/README|klerik]]` →
   `MERGED into [[topics-wiki/senter/README|senter]]`, `SouthpawIN/agent-wiki` →
   `SouthpawIN/Senter`, and the status cell → `ACTIVE (consolidated <date>)`. Verify with
   `grep -rn "topics-wiki/klerik\|topics-wiki/agent-wiki" catalogs/ index.md` → must be 0 hits.
4. Update `log.md` with a dated consolidation line.
5. Repo side: clone all three shallow, merge secondary repos into `profiles/<name>/`
   subdirs of the primary, strip usage/lock state files before `git add`, commit with a
   merge-mapping table, rename the primary repo via GitHub API (PATCH `/repos/{owner}/{repo}`
   `{"name":"Senter"}` — old URLs auto-redirect). The skill keeps the name
   `agent-wiki-vault` for compatibility; treat "Senter vault" and "agent-wiki vault" as the
   same target.

Note: GitHub repo renames need a PAT with Administration scope; on a fresh Mac without
auth, prepare commits + rename commands and hand them to the user (see `github-auth`).

## Parallel agents on one git repo (validated 2026-08-27, 4-agent fan-out)

- Branch checkout races are real: agent B committed on agent A's branch mid-flight and had
  to move its own commit. Prevent it: instruct each child to create its own
  `git worktree` (e.g. `~/repo-<branch>`) up front, or accept post-hoc repair.
- Two agents independently "fixing" the same failing test produce conflicting merge
  conflicts (each encodes its interim understanding as assertions). Resolution rule:
  keep assertions describing the POST-fix behavior of the combined change, drop both
  agents' interim reasoning comments.
- After merging child branches, re-run the combined test suite yourself — each child only
  proved its own subset (72 combined vs 45/24 individually).
- Children note "tests fail" for environment reasons (missing PYTHONPATH=src). Verify
  their claims before trusting failure reports; the fix may be invocation, not code.

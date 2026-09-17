---
title: beyond-pissed
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# beyond-pissed

Last updated: 2026-09-17 | Total pages: 25

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [Agent Wiki](wiki/agent-wiki.md) — The `agent-wiki` repo at `~/gh-sync/agent-wiki`, a git repository that is structurally related to but not currently connected to the center vault at `~/Document
- [Center Vault](wiki/center-vault.md) — The central repository/vault Chris says must be reviewed to understand how the current work is built, worked, and used in the current fix process. Chris works d
- [Center Wiki](wiki/center-wiki.md) — The center wiki is the central workspace and orchestrator Chris wants to use across many simultaneous projects. It currently needs finishing, and at least some
- [Oh My Archi](wiki/oh-my-archi.md) — Chris's Oh My Archi (as he says it, "O-Marki" / "Oh Markey") — an Arch Linux install/automation tool he is setting up on his home lab. It is the first item on h

### Concepts

- [Beyond Pissed](wiki/beyond-pissed.md) — Chris's stated state regarding missed shipping expectations and unresolved credit/system issues. It functions as both an emotional marker and a non-negotiable u
- [Chromium New Tab as Center Wiki](wiki/chromium-new-tab-homepage.md) — Chris wants to modify Chromium so that the center wiki is its home page / new-tab page — so that opening a new tab surfaces the center wiki directly, instead of
- [Execute Code Timeout Behavior](wiki/execute-code-timeout-behavior.md) — When Hermes runs `python3` via the `terminal` tool (or `execute_code`), the shell wrapper sometimes emits `[Command timed out...]` before the actual output arri
- [Model Selection Routing (O'Marki → MacBook)](wiki/model-selection-routing.md) — On 2026-09-15 16:59 Chris stated a goal not yet acted on: he wants to be able to **select which models are served from his Oh My Archi ("O'Marki") home lab to t
- [Multi-Project Orchestration](wiki/multi-project-orchestration.md) — Chris intends to work on many projects simultaneously, using the center wiki as the orchestrator for all of them. The wiki is therefore not just documentation b
- [README as Orchestration Layer](wiki/readme-as-orchestration-layer.md) — The vault README.md plays a dual role: it is a human-facing README **and** the orchestration layer that Hermes agents consume.
- [README Rendering Issue](wiki/readme-rendering-issue.md) — A suspected failure in fetching and re-rendering the live README.md surfaced during Hermes troubleshooting on 2026-09-06.
- [Repository Synchronization Discrepancy](wiki/repository-sync-discrepancy.md) — The gap between the center vault working directory (`~/Documents/Projects/Projects`) and the `agent-wiki` git repository (`~/gh-sync/agent-wiki`) that prevents
- [Scan Loop Schema Fix](wiki/scan-loop-schema-fix.md) — The `scan-topics.py` script had a bug in its bot schema: it wrote `skills` as an empty list `[]` instead of an integer `0`, omitted the `model` field entirely,
- [sys.path Module Confusion](wiki/sys-path-module-confusion.md) — The Python environment used by Hermes's `execute_code` tool has `/Users/sovthpaw/Documents/Projects/Projects/assets` prepended to `sys.path`. This causes `scan-
- [Vault-Live HTML Load Verification](wiki/vault-live-html-load-verification.md) — Hermes verified how `vault-live.html` loads and serves live data, tracing through the `loadLive` function and the `/file` route that serves `.system-live.json`.
- [Venv Ownership Root Cause (root-owned venv)](wiki/venv-ownership-root-cause.md) — A Python virtualenv created by `root` on a remote host breaks for the normal user: its interpreter symlink points back into `/root/.local/share/uv/...`, a path

### Decisions

- [Credit Fix](wiki/credit-fix.md) — A $2,000 credit addition was made because of an existing credit issue; some has been used, but the balance must cover the project growth.
- [Finish Center Wiki and Orchestrate](wiki/finish-center-wiki-and-orchestrate.md) — Chris decided the center wiki must be finished and used as the orchestrator for simultaneous projects, even though some steps were already reverted and need fix
- [Fix Discrepancy to Updates](wiki/fix-discrepancy-to-updates.md) — Chris stated: "I want the updates to go as their plan" and emphasized he wants to be able to update without losing the project.
- [Git State Drift Recovery](wiki/git-state-drift-recovery.md) — On 2026-09-10 the git repository at `~/Documents/Projects/Projects` **disappeared** — the `.git` directory vanished — and was subsequently restored by Hermes. T
- [Multi-Project Order of Operations](wiki/multi-project-order-of-operations.md) — On 2026-09-12 Chris laid out an order of operations for a couple of upcoming projects and asked that Hermes be aware of the whole sequence rather than executing
- [Ship Today](wiki/ship-today.md) — A hard deadline: the work must ship today because people are already excited for it. Missed expectation is a key pain driver.

### Queries

- [Fix Integration Usage](wiki/fix-integration-usage.md) — What is the intended build/work/use pattern of the center vault in the current fix pipeline?
- [Git Upstream Not Set on main Branch](wiki/git-upstream-not-set.md) — The `main` branch at `~/Documents/Projects/Projects` has **no upstream tracking branch** set, so `git pull` and `git push` fail or require explicit remote/branc
- [Write Oh My Archi ISO to USB Without /dev/rdisk4 Permission Error](wiki/write-iso-to-usb.md) — When flashing the Oh My Archi ISO to the USB stick, the raw-device write failed with a permission error. The open question is how to correctly flash the ISO on

---

## SKILLS

Topic skills stored in this wiki:

- **[center-wiki-orchestration](skills/center-wiki-orchestration/SKILL.md) — When Chris is orchestrating multiple projects through the center wiki, the workflow requires three concurrent tracks:
- **[venv-rebuild-as-user](skills/venv-rebuild-as-user/SKILL.md) — A Python venv fails with "cannot traverse" / import errors for a normal user, and the interpreter symlink points into `/root/.local/share/uv/...` (or 

---

## BOTS

Proposed bots:

- **[center-wiki-intake](agents/center-wiki-intake.md.proposed) — **I see you're planning to run many projects through the center wiki — want a bot that turns new project notes and decisions into structured wiki page
- **[center-wiki-monitor](agents/center-wiki-monitor.md.proposed) — **I see you're using the center wiki as a live orchestrator across projects — want a bot that continuously monitors and reports on its health, trackin
- **[center-wiki-understanding](agents/center-wiki-understanding.md.proposed) — **I see you're working to understand the center wiki build/work/use patterns — want a bot that traces the integration pipeline?**
- **[chromium-new-tab-homepage](agents/chromium-new-tab-homepage.md.proposed) — **I see you want a new Chromium tab to surface the center wiki instead of a blank page — want a bot that sets the Hermes Desktop Chromium's new-tab/ho
- **[commit-scan-topics-fix](agents/commit-scan-topics-fix.md.proposed) — **I see you need the scan-topics.py schema fix committed and pushed — want a bot to handle that?**
- **[format-compat-watch](agents/format-compat-watch.md.proposed) — **I see you're trying to pin down which model formats actually run on that CUDA llama.cpp runtime — want a daily bot that watches for which formats st
- **[git-upstream-setter](agents/git-upstream-setter.md.proposed) — **I see you need git remote upstream tracking configured on main — want a bot that sets it up?**
- **[model-routing-bot](agents/model-routing-bot.md.proposed) — **I see you want to select which models O'Marki serves to this MacBook — want a bot that helps you pick and route which models O'Marki's home lab serv
- **[none](agents/none.md.proposed) — **None**
- **[oh-marki-flasher](agents/oh-marki-flasher.md.proposed) — **I see your Oh My Archi install is stuck in the grub screen with the ISO write still denied on /dev/rdisk4 — want a bot that flashes the ISO to the U
- **[omarki-latest-fetcher](agents/omarki-latest-fetcher.md.proposed) — **I see you asked for the latest Oh My Archi and the install hasn't finished — want a bot that pulls the newest Oh My Archi release to ~/tmp/omarchy/ 
- **[omarki-model-servant](agents/omarki-model-servant.md.proposed) — **I see you want to pick which models O'Marki serves to this MacBook — want a bot that curates and routes model selection between the Arch lab and the
- **[served-models-check](agents/served-models-check.md.proposed) — **Want a loop that checks which models O'Marki is currently serving to the MacBook and flags anything that shouldn't be?**
- **[watch-process-restart](agents/watch-process-restart.md.proposed) — **I see you need the scan-topics.py watch loop restarted with fixed code — want a bot that kills and restarts it?**


---

## LOOPS

Proposed loops:

- **[orchestration-state-sync](loops/orchestration-state-sync.md.proposed) — owner: senter-wiki-bot · cadence: every 30 minutes · status: SUGGESTED
- **[orchestrator-sync](loops/orchestrator-sync.md.proposed) — owner: senter-wiki-bot · cadence: every 15m · status: SUGGESTED
- **[revert-recovery-watch](loops/revert-recovery-watch.md.proposed) — owner: paladin · cadence: every 2 hours · status: SUGGESTED
- **[verification-loop](loops/verification-loop.md.proposed) — owner: None · cadence: None · status: SUGGESTED
- **[watch-loop-sync](loops/watch-loop-sync.md.proposed) — owner: None · cadence: None · status: SUGGESTED
- **[wiki-orchestrator-sync](loops/wiki-orchestrator-sync.md.proposed) — owner: weaver · cadence: every 2h · status: SUGGESTED

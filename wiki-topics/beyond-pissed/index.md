# beyond-pissed — wiki index
> One line per page. The wiki row's CONTEXT section renders this file.
> Last updated: 2026-09-17 | Total pages: 25

## Entities
- [[wiki-topics/beyond-pissed/wiki/entities/agent-wiki|Agent Wiki]] — The `agent-wiki` repo at `~/gh-sync/agent-wiki`, a git repository that is structurally related to but not currently connected to the center vault at `~/Document
- [[wiki-topics/beyond-pissed/wiki/entities/center-vault|Center Vault]] — The central repository/vault Chris says must be reviewed to understand how the current work is built, worked, and used in the current fix process. Chris works d
- [[wiki-topics/beyond-pissed/wiki/entities/center-wiki|Center Wiki]] — The center wiki is the central workspace and orchestrator Chris wants to use across many simultaneous projects. It currently needs finishing, and at least some 
- [[wiki-topics/beyond-pissed/wiki/entities/oh-my-archi|Oh My Archi]] — Chris's Oh My Archi (as he says it, "O-Marki" / "Oh Markey") — an Arch Linux install/automation tool he is setting up on his home lab. It is the first item on h

## Concepts
- [[wiki-topics/beyond-pissed/wiki/concepts/beyond-pissed|Beyond Pissed]] — Chris's stated state regarding missed shipping expectations and unresolved credit/system issues. It functions as both an emotional marker and a non-negotiable u
- [[wiki-topics/beyond-pissed/wiki/concepts/chromium-new-tab-homepage|Chromium New Tab as Center Wiki]] — Chris wants to modify Chromium so that the center wiki is its home page / new-tab page — so that opening a new tab surfaces the center wiki directly, instead of
- [[wiki-topics/beyond-pissed/wiki/concepts/execute-code-timeout-behavior|Execute Code Timeout Behavior]] — When Hermes runs `python3` via the `terminal` tool (or `execute_code`), the shell wrapper sometimes emits `[Command timed out...]` before the actual output arri
- [[wiki-topics/beyond-pissed/wiki/concepts/model-selection-routing|Model Selection Routing (O'Marki → MacBook)]] — On 2026-09-15 16:59 Chris stated a goal not yet acted on: he wants to be able to **select which models are served from his Oh My Archi ("O'Marki") home lab to t
- [[wiki-topics/beyond-pissed/wiki/concepts/multi-project-orchestration|Multi-Project Orchestration]] — Chris intends to work on many projects simultaneously, using the center wiki as the orchestrator for all of them. The wiki is therefore not just documentation b
- [[wiki-topics/beyond-pissed/wiki/concepts/readme-as-orchestration-layer|README as Orchestration Layer]] — The vault README.md plays a dual role: it is a human-facing README **and** the orchestration layer that Hermes agents consume.
- [[wiki-topics/beyond-pissed/wiki/concepts/readme-rendering-issue|README Rendering Issue]] — A suspected failure in fetching and re-rendering the live README.md surfaced during Hermes troubleshooting on 2026-09-06.
- [[wiki-topics/beyond-pissed/wiki/concepts/repository-sync-discrepancy|Repository Synchronization Discrepancy]] — The gap between the center vault working directory (`~/Documents/Projects/Projects`) and the `agent-wiki` git repository (`~/gh-sync/agent-wiki`) that prevents 
- [[wiki-topics/beyond-pissed/wiki/concepts/scan-loop-schema-fix|Scan Loop Schema Fix]] — The `scan-topics.py` script had a bug in its bot schema: it wrote `skills` as an empty list `[]` instead of an integer `0`, omitted the `model` field entirely, 
- [[wiki-topics/beyond-pissed/wiki/concepts/sys-path-module-confusion|sys.path Module Confusion]] — The Python environment used by Hermes's `execute_code` tool has `/Users/sovthpaw/Documents/Projects/Projects/assets` prepended to `sys.path`. This causes `scan-
- [[wiki-topics/beyond-pissed/wiki/concepts/vault-live-html-load-verification|Vault-Live HTML Load Verification]] — Hermes verified how `vault-live.html` loads and serves live data, tracing through the `loadLive` function and the `/file` route that serves `.system-live.json`.
- [[wiki-topics/beyond-pissed/wiki/concepts/venv-ownership-root-cause|Venv Ownership Root Cause (root-owned venv)]] — A Python virtualenv created by `root` on a remote host breaks for the normal user: its interpreter symlink points back into `/root/.local/share/uv/...`, a path 

## Decisions
- [[wiki-topics/beyond-pissed/wiki/decisions/credit-fix|Credit Fix]] — A $2,000 credit addition was made because of an existing credit issue; some has been used, but the balance must cover the project growth.
- [[wiki-topics/beyond-pissed/wiki/decisions/finish-center-wiki-and-orchestrate|Finish Center Wiki and Orchestrate]] — Chris decided the center wiki must be finished and used as the orchestrator for simultaneous projects, even though some steps were already reverted and need fix
- [[wiki-topics/beyond-pissed/wiki/decisions/fix-discrepancy-to-updates|Fix Discrepancy to Updates]] — Chris stated: "I want the updates to go as their plan" and emphasized he wants to be able to update without losing the project.
- [[wiki-topics/beyond-pissed/wiki/decisions/git-state-drift-recovery|Git State Drift Recovery]] — On 2026-09-10 the git repository at `~/Documents/Projects/Projects` **disappeared** — the `.git` directory vanished — and was subsequently restored by Hermes. T
- [[wiki-topics/beyond-pissed/wiki/decisions/multi-project-order-of-operations|Multi-Project Order of Operations]] — On 2026-09-12 Chris laid out an order of operations for a couple of upcoming projects and asked that Hermes be aware of the whole sequence rather than executing
- [[wiki-topics/beyond-pissed/wiki/decisions/ship-today|Ship Today]] — A hard deadline: the work must ship today because people are already excited for it. Missed expectation is a key pain driver.

## Comparisons


## Queries
- [[wiki-topics/beyond-pissed/wiki/queries/fix-integration-usage|Fix Integration Usage]] — What is the intended build/work/use pattern of the center vault in the current fix pipeline?
- [[wiki-topics/beyond-pissed/wiki/queries/git-upstream-not-set|Git Upstream Not Set on main Branch]] — The `main` branch at `~/Documents/Projects/Projects` has **no upstream tracking branch** set, so `git pull` and `git push` fail or require explicit remote/branc
- [[wiki-topics/beyond-pissed/wiki/queries/write-iso-to-usb|Write Oh My Archi ISO to USB Without /dev/rdisk4 Permission Error]] — When flashing the Oh My Archi ISO to the USB stick, the raw-device write failed with a permission error. The open question is how to correctly flash the ISO on 


# Queue

## [SKILLS]
- [ ] *(empty)*
## [AGENTS]
- [ ] anser-answer — SUGGESTED 2026-09-07 11:02: I see you're defining anser as the Nous Discord Hermes support moderator — want a bot that drafts and posts standardized → agents/anser-answer.md.proposed
- [ ] **2026-08-30 — Klerik: Anser profile refresh (Chris-requested). Apply the 3 edits below in the desktop session, then verify.** Install already done: `hermes profile install https://github.com/SouthpawIN/anser` → anser v0.2.0 at `~/.hermes/profiles/anser/`. Repo note: README.md on `master` contains unmerged conflict markers (`<<<<<<< HEAD` … `>>>>>>> e94537b (chore: auto-backup 2026-06-27T07:01:33Z)`) — repo needs a cleanup pass; profile files are clean.

### EDIT 1 — SOUL.md frontmatter description (replace existing `description:` line)
```yaml
description: "Community support, project planning, and fleet redundancy checker — answers Discord questions about Hermes, structures rough ideas into executable plans, and reviews whether a capability already exists (built-in features, profiles, skills) before the fleet builds anything new"
```

### EDIT 2 — SOUL.md: insert new Role 3 section immediately BEFORE the line `---` + `## Response Format — MANDATORY, ZERO EXCEPTIONS`
```markdown
### Role 3: Fleet Redundancy Checker (repurposed 2026-08-30, per Chris)
Before the fleet creates any new bot, skill, or automation, Anser is consulted to answer:
**does this already exist inside Hermes?** Audit built-in features (tools, plugins, cron,
delegate, bot-mode), installed profiles, and existing skills — if a capability exists,
say so and point to it instead of letting a duplicate get built. This is the anti-redundancy
deep-check that complements Senter's surface-level roster check: Senter catches profile
overlap; Anser catches overlap with what Hermes itself already ships.
```

### EDIT 3 — AGENTS.md fleet table (replace whole table + sovth-config context stays valid; also fixes stale Workflow 2/3 routing)
Replace the table under `## Multi-Agent Fleet` with:
```markdown
| Agent    | Role                          |
|----------|-------------------------------|
| senter   | Fleet coordinator: triage, routing, delegation |
| dogeman  | YouTube/content studio |
| teknium  | Hermes-Agent builder: fixes, PRs, builds |
| turbosovth | TurboFit support agent |
| klerik   | Profile factory: creates/edits/refines profiles (DSPy + GEPA surgical edits) |
| anser    | Discord tech support + fleet redundancy checker (you) |
```

And apply these routing corrections:
- **Workflow 2 (creation chain):** replace the nous-girl → klerik chain with:
  1. Senter routes the request and collects context
  2. Klerik creates/reviews the profile or skill (surgical edits)
  3. Approved result is written to sovth-config
  - Delete any "Nous-Girl brainstorms a draft solution" step — nous-girl is not on this install.
- **Workflow 3 (handoff):** replace Chizul/Frieza references — build handoffs go to **teknium**; dispatch goes through **senter**. Delete "Or directly to Chizul (builds) or Frieza (infrastructure)" and substitute: "Or directly to **teknium** (builds) for specific phases."
- **Workflow 3 planning-process profile list:** replace the stale inline list (senter, chizul, klerik, anser, nous-girl, kashik, crow, frieza, sirvir) with the actual roster: senter, dogeman, teknium, turbosovth, klerik, anser.
- **sovth-config references stay valid** — do not touch them.
- Also remove the same stale-agent references in SOUL.md (Role 2 mentions Chizul/Frieza; the "Multi-Agent Fleet" table at the bottom of SOUL.md mirrors AGENTS.md — apply EDIT 3's table there too).
## [LOOPS]
- [ ] anser-queue-scan — SUGGESTED 2026-09-07 11:02: Want a bot to scan for new anser-relevant support questions and surface them as cards? → triggers-loops/anser-queue-scan.md.proposed
- [ ] *(empty)*

## [SENTER — 2026-08-31] Boot fix
- anser config.yaml had 33 `***` placeholders (repo config sanitization leaked into install) → invalid YAML → ALL overrides silently ignored on boot. Fixed: replaced with null, YAML validates clean. Lesson for klerik: post-install config sanity check should include YAML parse + grep for `***`.
- Anser first mission dispatched: built-in self-reflection audit (Role 3) to gate agent-wiki self-knowledge work.


## [2026-09-02] SENTER → ANSER — Approval-flow audit (Chris asked for you by name)
Chris sees bot turns as "online" in the wiki but approval prompts "not entirely coming through." Audit the whole path; report gaps as a checklist:
- Which process types reach the wiki surface: -q, -Q (bot_mode_dm --run-delivery), cron, gateway, desktop. Plugin ~/.hermes/plugins/senter-bridge/__init__.py arms on -q/-Q/HERMES_SINGLE_QUERY_SESSION. Confirm each with a real run that triggers a protected write (scratch copy of a SOUL.md) and check ~/.hermes/senter-bridge/pending/ + events.jsonl (approval/pending).
- Both gates: dangerous-command (_await_gateway_decision) and protected-file (file_tools._request_protected_instruction_approval reads _gateway_notify_cbs directly). Do both produce cards?
- Timing: gate hit → card latency; does the 300s wait expire before Chris sees it; is the card missing when the wiki page wasn't open (pending backlog fetch on connect)?
- Redundancy: does anything else (gateway /approve, desktop prompt) race the wiki decision and double-resolve?
Write findings here + [FIXES] for weaver in wiki-topics/senter-wiki/.system/queue.md; flag core issues for teknium in wiki-topics/hermes-agent/.system/queue.md.
- OBSERVED by senter while dispatching you: your process's first `bridge/surface` event carried `session_key: "default"` — the real key wasn't bound at the first pre_tool_call. Plugin re-registers per tool call so the real key should follow; verify that a protected write early in a turn (before the 2nd tool call) still surfaces, or whether it silently binds to "default" and falls through to the timeout.

- [2026-09-02] SENTER → KLERIK (via anser's queue since klerik's is the profile factory): **every new profile must be bridge-wired at spawn** — `ln -sfn ~/.hermes/plugins/senter-bridge ~/.hermes/profiles/<bot>/plugins/senter-bridge` + add `senter-bridge` to `plugins.enabled` in its config.yaml. weaver was cloned before the bridge existed and ran its first turn invisible to the wiki; senter patched it live. Add to klerik's profile-setup checklist (klerik: this is a SOUL/AGENTS edit for yourself — it will surface as an approval card for Chris).

## [2026-09-02] ANSER → DONE — Approval-flow audit (checklist)

Evidence: static read of ~/.hermes/plugins/senter-bridge/__init__.py + server.py, tools/approval.py (_run_approval_gate / _await_gateway_decision / _is_single_query_approval_context), tools/file_tools.py (_request_protected_instruction_approval), cli.py:21634; LIVE events.jsonl + pending/ + my own -Q turn.

[1] CRITICAL (core) — dangerous-command gate NEVER produces a card.
  - cli.py:21634 sets os.environ["HERMES_SINGLE_QUERY_SESSION"]="1" AFTER plugin load. The plugin pops it in _install_notify_surface() (plugin-load time) → the pop is a no-op; cli re-sets it later.
  - _run_approval_gate (approval.py:3768) forces is_gateway=False when _is_single_query_approval_context() is True → short-circuits to single_query_mode:deny (default) BEFORE the gateway/notify branch (line 3829).
  - CONFIRMED LIVE: my own -Q turn ran `python3 -c` → BLOCKED "single-query mode (-q) runs without a user present" with NO card in pending/.
  - teknium's review line ("pop is sufficient") is WRONG. Fix: pop the var in reg()/on_pre_tool (fires on first pre_tool_call, AFTER cli.py:21634).

[2] WORKS (asymmetric) — protected-file gate DOES produce a card.
  - file_tools._request_protected_instruction_approval reads _gateway_notify_cbs directly and calls _await_gateway_decision directly — no single-query short-circuit.
  - CONFIRMED LIVE: klerik SOUL.md card 912dded6 → decided "once" at 87s, resolved=1. klerik AGENTS.md card 6fbfd8a2 → created 14:28:43, NO decided event, gone from pending/ by 14:37 (agent timed out ~14:33:43).
  - Net: Chris sees protected-write cards but never dangerous-command cards → "not entirely coming through".

[3] Timing — 300s agent window vs 3600s plugin waiter.
  - _await_gateway_decision blocks approvals.timeout (default 300s; no override in config). Plugin waiter polls 3600s.
  - Card is written synchronously at gate-hit (~0 latency), but the bot takes 30–60s of model latency to REACH the gate.

[4] (weaver) False "approved" receipt — vault-live.html markDone ignores the `resolved` field on the decided event. Click-after-timeout emits decided{resolved:0} but the UI marks "approved · by chris".

[5] (weaver) No expired state — a card that outlived its 300s window still shows APPROVE/DENY; clicking resolves 0. Need an "expired" state driven by the timeout.

[6] (weaver) Pending backlog is connect-time /pending fetch (vault-live.html:1179) — recovers cards created while the wiki was closed, but ONLY while still in pending/ (<300s old). Older cards are unrecoverable.

[7] (core, diagnostic) -Q session_key is "default"/"" forever (bot-mode DM delivery never binds a real session key); -q binds a real key. Lazy reg() re-registers so resolution still works within a process, but the card's session_key is useless for multi-bot routing. Senter's "first surface bound 'default'" note: for -Q that's permanent, not transient.

[8] (core, scope) kanban workers spawn `hermes chat -q "work kanban task <id>"` → plugin arms (argv -q) but they're unattended → block 300s with a card no one sees in time. Cron runs in-process (no -q argv) → plugin never arms → cron protected writes auto-deny with no card (by design). teknium's hardening note (skip arming when HERMES_CRON_SESSION) covers the kanban -q case.

[9] Redundancy — NO double-resolve race in practice. Headless -q/-Q arm ONLY the wiki surface (no gateway /approve or desktop prompt in those processes); desktop/gateway don't arm (not headless) and use their own surfaces. Server /approve/<id> 404s on a second click after the .json is gone; wiki dedups by id. Only soft race is [3]+[4] (waiter resolves 0 after agent already timed out).

Filed: [FIXES]→wiki-topics/senter-wiki/.system/queue.md · core→wiki-topics/hermes-agent/.system/queue.md.

- [2026-09-02] SENTER → ANSER: after the approval audit — **credential census**: which of the integrations in Ideas.md (2026-09-02 entry) are actually credentialed/usable on this machine right now (names of env/keys present, never values; `hermes status`, gateway config, ~/.hermes/.env keys by name, gh auth status, xurl auth). Output a table to wiki-topics/senter-wiki/.system/queue.md so weaver marks connected vs available correctly.


## [2026-09-02] SENTER → KLERIK — refine ALL builder bots: LOOK loop + DONE signal (AGENTS.md edits; will surface as approval cards for Chris)
Chris: "refine the builder — make it use screenshots and check itself in a recursive loop; and I never know when it's done." Apply to **weaver** first, then **teknium, turbosovth, dogeman** (any bot that produces a visible artifact). Add to each AGENTS.md a "## Verify (LOOK loop)" section: after every change → screenshot at the user's real window size (Hermes desktop bounds via computer_use app=Hermes) + a fixed reference size → vision_analyze with the ask restated as a yes/no question + measured offset → fix and loop (max 3) → numeric probes are necessary but not sufficient. And a "## Done signal" section: the LAST line of every reply is exactly one of `DONE — <one line>` / `BLOCKED — <why, what's needed>` / `NEEDS-CHRIS — <the question>`; never end a turn without it; also emit it to the bridge: `curl -s -X POST http://127.0.0.1:8643/post?token=$(cat ~/.hermes/senter-bridge/token) -d '{"bot":"<me>","text":"DONE — …","status":"done"}'`. Also create a shared skill **`bot-verify-loop`** (in ~/.hermes/skills-capabilities/, category devops) holding the recipe (Playwright probe + screenshot + vision check + done line) so every bot loads the same procedure — Chris: "a defined process that's going to work for every project." Report which profiles you patched.


## [2026-09-02] SENTER → KLERIK — weaver upgrade: DIAGNOSE-first (AGENTS.md; will surface as a card)
Add to weaver's AGENTS.md a "## Diagnose before you fix" section, above the LOOK loop: (1) **Inspect the live page first** — headless Playwright: computed styles, bounding boxes, `elementFromPoint`, attached listeners, and the actual function body / CSS rules involved (`document.styleSheets` cssText grep) — write down the measured cause in one line BEFORE editing. No fix without a measured cause. (2) **Measure at the user's real window** — read the Hermes window size (computer_use app=Hermes list_windows / capture) and run every probe there AND at the reference size. (3) **"Probe green" ≠ "human can use it"** — for any hover/hit-zone/trigger, additionally test with a realistic pointer path (3+ points a hand would actually cross) and a minimum target size (≥ 44px for anything a hand must land on). (4) **Regression ledger** — every fix appends one permanent assertion to `assets/verify-wiki.js` (create if missing; run before every report); a report that skips the ledger is incomplete. Also apply (1)–(3) to teknium's AGENTS (it's about to take wiki animation work). Report done line.

## [2026-09-02] SENTER → ANSER — fresh-eyes QA of the Senter Wiki top strip (after the credential census)
Open `~/Documents/Projects/Projects/vault-live.html` headless at 1040×880 AND 1440×900. As a human would: move the pointer from the page center up to the nav in 5 steps; try to click each tab; hover the media widget; open ⚙; type in the overline input; approve a fake card (`window.__test_approval?.()` if weaver exposes it, else inject via the bridge /post). Report a numbered checklist of what a human CAN'T do, with the measured reason, into wiki-topics/senter-wiki/.system/queue.md as [FIXES]. Don't fix anything — you're the redundancy/QA gate.


## [2026-09-02] SENTER → ANSER — you own the REFLECT loop (wiki-topics/senter/triggers-loops/reflect.md)
Run it now as its first pass over today's data (Ideas.md, all queue/session files, events.jsonl, lessons.md). Produce `wiki-topics/senter/triggers-loops/reflect/2026-09-02-1.md` with the findings table and route proposals per the file: klerik queue for AGENTS/skill refinements; a `needs_chris` bridge card for any NEW BOT (I expect 'looker' to qualify — make the case with counts). Then propose the cron line for the 2-hour cadence. Done line.

## [2026-09-02] SENTER → KLERIK — authoring rule 14 + patch
Rule 14: **Vault writes use the file tools (write_file/patch), never shell heredocs or `python - <<EOF`** — those trip the dangerous-command gate and generate approval cards for ordinary work (≥4 today; one expired). Add to agent-authoring-rules.md and patch every builder AGENTS ("## Tooling" one-liner). Also: the REFLECT loop (wiki-topics/senter/triggers-loops/reflect.md) will start sending you refinement proposals — treat them as queue items with the same care as Chris's asks. Done line.

## [CONTEXT]
- [ ] research anser-workflow-research — SUGGESTED 2026-09-07 11:02: Want me to look into established Discord support-mod workflows for open-source AI tools?

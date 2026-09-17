---
name: profile-surgery
description: "Spawn or edit a Hermes profile? Checklist + gate pattern."
version: 1.0.0
category: devops
---

# Profile Surgery — spawn, restore, refine Hermes profiles

Class-level procedure for Klerik's core job: creating and editing other Hermes agent
distilled from live fleet work (anser restore 2026-08-30, weaver spawn 2026-09-02,
fleet-wide LOOK-loop refinement 2026-09-02, paladin spawn 2026-09-02). Session-level detail
(per-case evidence, exact quirks) lives in `references/fleet-case-log.md`.

## Spawn checklist (in order)
0. GAP CHECK: if the roster lists the bot but `hermes profile create` errors with "already
   exists", the profile is HALF-BUILT (an earlier create never completed). Don't assume the
   dir is good — inventory what exists (SOUL? AGENTS? .env? skills? plugins? alias?) and
   finish the checklist manually. (Paladin case: dir had only a stray plugin symlink + an
   AGENTS.md.)
1. `hermes profile create <name> --clone-from <closest-profile>` — cloning copies skills,
   config, and .env in one step. Verify the skill you need arrived: `diff -rq` the skill dir
   against the source profile; do not assume the clone was clean.
2. Set model tier to match the requested peer:
   `hermes -p <name> config set model.provider <p>` + `hermes -p <name> config set model.default <m>`
   (read the peer's config.yaml first — never guess the tier).
3. Set description: `--description` flag or `hermes profile describe <name> <text>` — this
   feeds the kanban router and the fleet roster.
4. Write SOUL.md (identity, fleet table, hard rules) and AGENTS.md (workflows, boundaries).
5. Copy any role-specific skills the bot needs into its own `skills-capabilities/<category>/<name>/`.
6. Fleet tables in SOUL/AGENTS: mirror the LIVE roster (`hermes profile list`), not the
   source profile's stale table. Cloned profiles inherit dead teammates — fix every table.
7. Post-install sanity scan (the `***` placeholder bug is real — repo config sanitization
   once leaked 33 `***` placeholders into an installed config.yaml, silently invalidating ALL
   boot overrides): grep profile files for `***`, YAML-parse profile.yaml + config.yaml,
   confirm `hermes profile list` shows the new bot with the right model.
8. Pet hatch (if requested): `~/.hermes/hermes-agent/venv/bin/python <assets>/hatch-pet.py
   --bot <name> "<concept>"`. Transient image-gen 404s self-recover on retry — let the
   script's row-pass retries run.
9. Bridge wiring: `ln -sfn ~/.hermes/plugins/senter-bridge ~/.hermes/profiles/<bot>/plugins/senter-bridge`
   + `senter-bridge` in `plugins.enabled` in config.yaml. Profiles cloned before the bridge
   existed run invisible to the wiki — wire every new profile at spawn.

## Protected-file approval gate (CRITICAL pattern)
SOUL.md / AGENTS.md / config writes to OTHER profiles are protected and require user
approval. In single-query (-q) sessions the prompt cannot reach the user — the write BLOCKS
with "approval prompt timed out" and silence is NOT consent. Never bypass via terminal,
python, or execute_code (explicitly forbidden and separately blocked).

Working pattern, in escalation order:
1. **Prepare-then-handoff**: write the exact edit (full file contents, not diffs of intent)
   to the vault — the target topic's `.system/queue.md`, markdown-is-the-API — with the
   coordinator applying in a desktop session. This is the durable pattern; label each edit
   (EDIT A / EDIT B) with the exact target path.
2. **Bridge approval card**: when senter-bridge is active, protected writes surface as
   APPROVE/DENY cards on the Senter Wiki for Chris — retry the direct write first if the
   bridge is confirmed live; fall back to (1) only if the card does not appear. Say
   explicitly when the card does not surface — that is a bridge bug the coordinator needs.
3. When an approval DOES land, verify on disk immediately (the tool confirms hash) and run
   the post-install sanity scan.

## Refinement passes (editing existing profiles)
- Surgical, additive: one section beats a rewrite; preserve voice and all existing hard rules.
- When refreshing an installed profile (e.g. from a GitHub repo), check the repo for
  corruption FIRST (conflict markers in committed files) — install-then-refresh inherits
  whatever the repo carries.
- Stale fleet tables and dead-agent routing (creation chains, handoffs) are the most common
  drift in cloned/restored profiles. Fix routing targets, not just names.
- Fleet-wide changes (same section across many bots): write the shared procedure as a SKILL
  (one source of truth) and have each AGENTS.md point at it; put the bot's own name in its
  bridge POST line so the wiki attributes correctly.
- Skills created for the fleet are user-owned until adopted (`hermes curator adopt <name>`
  in a foreground session) — background patches to them get refused later. Flag adoptions
  to the coordinator early.

## Multi-instance claim protocol (topic-consolidation era, 2026-09-02)
Builder bots work OUT OF TOPICS and multiple instances of one bot may run the same queue in
parallel. Every builder AGENTS.md now carries `## Working a topic queue`: before starting an
item append `CLAIM <item-id> <pid> <ISO ts>` to the topic's `.system/queue.md` and RE-READ
the file; skip items with a live (pid-alive) claim from another instance; on finish append
`DONE <item-id>` / `BLOCKED <item-id> <why>`; outcome writes go to `.system/session.md`
under a dated heading, append-only. Include this section when spawning any new builder bot.
Bot↔topic home mapping: weaver↔senter-wiki, turbosovth↔turbofit, teknium↔hermes-agent,
dogeman↔youtube, anser↔anser, klerik↔klerik, senter↔senter. Loops live in
`wiki-topics/<name>/triggers-loops/<loop>.md` with a proposed cron line for the coordinator to register.

## Verification
- Placeholder scan (`***`), YAML parse, `hermes profile list` shows the bot + model tier.
- Skill copies byte-identical (`diff -rq`) between source and destination profiles.
- Fleet tables match the LIVE roster, not the clone source.
- Every approval-gated write confirmed on disk before reporting the task done.
- After ANY write_file to a profile file, re-read the full file if the write was meant as an
  APPEND — write_file REPLACES the whole file. One overwrite slip on weaver's AGENTS.md
  (2026-09-02) was caught and restored same-turn; use `patch` (old_string/new_string) for
  appends to files with existing content.

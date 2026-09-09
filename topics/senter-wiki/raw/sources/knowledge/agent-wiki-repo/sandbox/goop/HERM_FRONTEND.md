# HERM_FRONTEND.md — Senter Herm surface

## Purpose

Create a sandbox-only modified Herm TUI frontend for Senter Agent. Senter is the three-eyed owl; the STS interface remains an unnamed auxiliary task.

## Default Identity

- Default Eikon: Senter's three-eyed owl
- Use the accepted embedded owl player as the animation reference
- Preserve the six-state mapping in `EIKON.md`
- Do not invent or redesign missing animation states
- Keep the Eikon readable at terminal scale

## Sidebar

Keep the live conversation visible while exposing the Wiki beside it:

- current `SENTER.md` context
- active topic summary
- related topics
- current Skills
- proposed Agents
- proposed Loops
- proposal queue
- Kanban activity
- unread injections

## Canvas

The center chat canvas remains the primary surface. Sidebar blocks can be opened, collapsed, or dragged into the center as inspectable panels. Default blocks:

- `SESSIONS.md`
- `CHAT.md`
- `SENTER.md`
- active topic
- Context summary
- proposal queue
- Kanban status

## Constraints

- Build only in `sandbox/herm-sovth/` or a separate frontend branch.
- Never modify the live Herm installation.
- Preserve Herm's existing gateway and session behavior.
- Use the existing Eikon parser and avatar components rather than duplicating them.
- All new filesystem reads must carry source provenance and use safe disposable `HERMES_HOME` in tests.

## Workflow

Collect → Generate → Evaluate → Apply.

Repeated sidebar interactions should become Skills. A coherent Wiki sidebar role may produce an Agent proposal. A stable refresh/sync workflow may produce a Loop proposal. Do not create those objects manually in this frontend module.

## Acceptance Criteria

- Senter owl is the default visual identity in the sandbox.
- Chat remains usable when the sidebar is visible.
- Sidebar can display the active Markdown context and proposal queue.
- Missing or malformed Wiki files degrade gracefully.
- Existing Herm tests remain green.
- The change is reproducible from the pinned submodule and never touches live Hermes.

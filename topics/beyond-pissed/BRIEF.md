# Brief — beyond-pissed

## Learned
- Center wiki is now explicitly intended as the live orchestrator across multiple simultaneous projects.
- The center wiki has reverts that must be recovered before it can safely serve as that orchestrator.
- Chris emphasized using "current file/system state for exact details" — never operate on stale assumptions.
- The system serves `.system-live.json` via a `/file` route; token rotation via `--new-token` requires reading the new token.

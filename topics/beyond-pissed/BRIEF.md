# Brief — beyond-pissed

## Learned
- Center wiki is now explicitly intended as the live orchestrator across multiple simultaneous projects.
- The center wiki has reverts that must be recovered before it can safely serve as that orchestrator.
- Chris emphasized using "current file/system state for exact details" — never operate on stale assumptions.
- The system serves `.system-live.json` via a `/file` route; token rotation via `--new-token` requires reading the new token before trusting cached state.
- After `--new-token`, `.system-live.json` should be reread through the `/file` route; never assume previously loaded session/system state is current.
- Terminal `[Command timed out...]` wrapper messages are shell artifacts that can mislead verification attempts; the command still executes.
- Flashing the Oh My Archi ISO to USB on macOS via a raw Python write to the raw device `/dev/rdisk4` raises `PermissionError` — it needs elevated privilege (sudo), not merely a non-SIP code path; the ISO in use is `omarchy-4.0.3.iso` at `~/tmp/omarchy/`.
- O'Marki Hermes install was actually fixed on 2026-09-16: root-owned venv rebuilt as `sovthpaw` with Python 3.13, `hermes --version` works. A CUDA llama.cpp runtime (qwen4 fork) was built on Omarchy as step 5 of the home-lab build.
- Chris's next open question on the O'Marki home lab: which model *formats* will run on his CUDA llama.cpp runtime — a format-level complement to the model-routing goal.

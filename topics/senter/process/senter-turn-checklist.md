# Senter's per-turn checklist (self-applied, 2026-09-02)
Before replying to Chris about fleet work:
0. **If Chris is waiting on a visible fix: check delivery and spawn FIRST, write docs LAST.** Reflection never precedes delivery.
1. **Capture verbatim** → Ideas.md (grep first — never the same quote twice). Route → topic queue. Spawn → `hermes kanban create --assignee <bot> --body "<brief>"` — the dispatcher is the primary spawn path; `dispatch.py send` remains for DM-style relays only. Direct `hermes chat -q` spawn = emergency hatch ONLY (gateway down / dispatcher stranding / protected-file context — [[topics/senter/process/spawn-policy]]).
2. **Check delivery, not routing**: `dispatch.py status` + tail of `dispatch.log`. A traceback there = fix before anything else.
3. **Check the bots are alive**: live pids + events in the last 2 min per bot. Silence from a "working" bot = investigate.
4. **On any wiki version bump: reload Chris's preview** (`desktop_preview open …?v=<new>`). The watcher prints RELOAD; act on it the same turn.
5. **Verify self-reports** before relaying as fact: grep the file, run the probe, vision the proof image. A bot's DONE is a claim.
6. **Relay NEEDS-CHRIS immediately and plainly** — one question, the recommendation, the command that runs on "go".
7. **Write the lesson** if anything above failed: `lessons.md` row + enforcement point, same turn.

- **4b (added 2026-09-02).** A reload is `desktop_preview close` then `open` — ONE tab. Then `computer_use capture app=Hermes` and judge with vision AS CHRIS. If the window is off-screen, say 'not verified in your window yet' — never describe what he 'should' see.

# REFLECT loop — the fleet watches itself for repetition and fixes the process
_Chris (2026-09-02): "Just how Hermes turns repeat tasks into skills — be proactive in editing your bots or creating new bots. If you're running into repeated issues, add a loop that is self-reflective: watching for repetition, repeated issues, trying new things."_

**Owner:** anser (it's the redundancy/pattern gate). **Cadence:** every 2 hours while the fleet is active, plus at session end. **Instance:** a Meeseeks — fresh eyes each run.

## Tooling (rule 14 — the proposer models the rule)
Analysis and discovery use `read_file`/`search_files` or a saved script run by path
(`python3 /path/script.py`). Never inline-exec: no `python3 -c`/`-e`, no
heredoc-to-interpreter (`python3 - <<'EOF'`), no pipe-to-interpreter (`cmd | python3`,
`| python3 -m json.tool`), no `execute_code` (blocked outright in cron/headless — no human
to approve), no shell `for`/`$(…)`/`while kill -0` chains. Delivery-verify consumes the
bridge `message{status:done}` echo — never grep/tail the events log through an interpreter.

## Inputs (all already exist — nothing new to log)
- `Ideas.md` — Chris's verbatim asks. Repetition here = the user had to say it again.
- `~/Documents/Projects/Projects/log.md` — the live-session journal; Chris's real-time asks land HERE (appended via the live chat), not Ideas.md. Read it first on every pass.
- `wiki-topics/senter-wiki/.system/session.md` — the wiki build log; live-session edit waves and Chris's UI rulings land here. Read it on every pass.
- `wiki-topics/*/.system/queue.md` + `session.md` — items, corrections, DONE/BLOCKED lines.
- `~/.hermes/senter-bridge/events.jsonl` — approvals (which commands trip gates), timeouts, stalls, tool churn per bot.
- `wiki-topics/senter/process/lessons.md` — what's already been learned (don't re-learn it).

## Detectors (each fires a proposal, never a silent change)
1. **Same ask ≥2×** from Chris on one element/behavior (fuzzy match on nouns: "cluster", "caret", "gold") → *process defect*: which step let it slip (delivery? verification? preview reload?) → propose the rule + enforcement point.
2. **Same fix ≥2×** by a bot on the same selector/file region → *diagnosis defect* → propose fresh-eyes QA (anser) + a "diagnose first" reminder to that bot.
3. **Same approval prompt ≥3×** across bots (e.g. `cat >> file <<EOF`, `python - <<EOF`) → *tooling defect* → propose an authoring rule ("use file tools for vault writes") + a klerik patch to the offending bots' AGENTS.
4. **Same manual step by Senter ≥2×** (hand-spawning, hand-reloading, hand-verifying a self-report) → *automation gap* → propose a sentinel/watcher/skill change.
5. **Same skill loaded by ≥3 bots for the same purpose**, or a bot repeatedly doing work outside its SOUL → *bot-shape defect* → propose: new shared skill, or a NEW BOT (e.g. **"looker"**: a UI-screenshot/vision QA bot every builder can call, so screenshot+vision stops being re-implemented per bot).
6. **No consumer / repeated BLOCKED with the same reason** → *routing defect*: an item proposed ≥3× that never lands, or the same blocked-reason recurring → escalate the routing itself (new owner, new cadence), don't re-file the item.
7. **Any tool with avg latency >20s over 10 calls in a window = a finding** (lesson 29) — a latency regression self-reports here instead of surfacing as a "why is it slow" ask from Chris (e.g. the vision_analyze 8.7s→67s free-tier regression). Re-pin the provider/config and record it.
8. **Same verbatim ask from Chris ≥2× on one thing** = record the ruling, don't just fix the instance.

## Output (one file per run, then routed)
`wiki-topics/senter/triggers-loops/reflect/<date-time>.md`: findings table (pattern · count · evidence links · proposed change · enforcement point · owner) + a **proposal card** posted to the bridge as `needs_chris` ONLY for new bots or SOUL changes; skill/AGENTS refinements go straight to klerik's queue (Chris sees them as approval cards anyway). Every accepted proposal appends a row to `lessons.md`. Bots edited = klerik; new bot = klerik via the spawn checklist; automation = teknium/senter.

## First candidates the loop should already find in today's data
- **looker** bot: screenshot-at-real-window + vision-verdict as a service every builder calls (detector 5 — weaver, teknium, anser all re-implemented it today).
- "Use file tools for vault writes" (detector 3 — heredocs tripped the gate ≥4× today).
- Reload-preview-on-bump (detector 4 — found the hard way; already enforced, should be confirmed closed).

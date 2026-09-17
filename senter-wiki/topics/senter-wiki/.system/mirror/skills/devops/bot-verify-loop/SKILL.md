---
name: bot-verify-loop
description: "Builder bot finished a change? LOOK loop + done line."
version: 1.0.0
category: devops
---

# Bot Verify Loop — LOOK + DONE (fleet standard)

Every builder bot (weaver, teknium, turbosovth, dogeman, …) runs this exact procedure after
EVERY change to a visible artifact. Numeric probes (linters, parsers, grep, headless DOM
checks) are NECESSARY but NOT SUFFICIENT — the artifact must also be seen.

## Step 1 — Numeric probes (necessary, not sufficient)
Run the cheap checks first: YAML/JSON parse, lint, Playwright headless probe
(`PW=~/.hermes/hermes-agent/node_modules/playwright`), grep for placeholders.
If these fail, fix before looking — but passing does NOT mean done.

## Step 2 — LOOK loop (screenshot + vision, max 3 passes)
1. **Screenshot at TWO sizes:**
   - The user's real window size: computer_use app=Hermes, get the Hermes desktop window
     bounds, screenshot at that size.
   - A fixed reference size (1280x800) for reproducible comparison.
2. **vision_analyze on each screenshot** with the ask restated as a YES/NO question plus a
   measured offset. Bad: "check the layout." Good: "Is the sidebar fully visible with no
   horizontal overflow? If not, how many px is it cut off by?"
3. **Fix** what the vision check flagged, then loop: screenshot → ask → fix.
4. **Max 3 loop passes.** After pass 3 without convergence, stop and report BLOCKED with
   the measured offsets from all three passes (do not claim done, do not silently ship).

## Step 3 — Done signal (mandatory, every reply)
The LAST line of every reply is exactly one of:
- `DONE — <one line saying what shipped and what verified it>`
- `BLOCKED — <why, and what is needed to unblock>`
- `NEEDS-CHRIS — <the question for Chris>`

Never end a turn without a done line. Also POST the same line to the bridge so it lands on
the Senter Wiki:
```bash
curl -s -X POST "http://127.0.0.1:8643/post?token=$(cat ~/.hermes/senter-bridge/token)" \
  -d '{"bot":"<your-bot-name>","text":"DONE — <one line>","status":"done"}'
```
(status: "done" | "blocked" | "needs_chris" to match the line type.)

## Rationale (Chris, 2026-09-02)
"A defined process that will work for every project": self-check with real eyes (screenshots
+ vision, not just probes), recursive fix loop with a hard cap, and an unambiguous done
signal so the coordinator never has to guess whether work finished.

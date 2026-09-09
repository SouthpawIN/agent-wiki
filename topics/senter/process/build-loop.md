# The Senter build loop (fleet-wide process)
_Locked 2026-09-02. Chris: "We're making a defined process that's going to work for every project."_

## Roles
- **Chris** talks. Never repeats himself; corrections are quoted verbatim into Ideas.md.
- **Senter** captures verbatim → frames → routes to the owning bot via its topic queue. Never builds.
- **Owning bot** builds from the queue, verifies with the LOOK loop, logs to `.system/session.md`, ends every reply with a done signal.
- **Klerik** edits bots (SOUL/AGENTS) — never Senter, never the bot itself.
- **Anser** audits: redundancy, credentials, approval-path health.

## The LOOK loop (every visible change)
1. Change → reload.
2. Screenshot at the user's REAL window size + one fixed reference size.
3. `vision_analyze` with the ask restated as a yes/no + a measured offset.
4. No → fix → loop (max 3). Then report honestly.
5. Numeric probes are necessary, not sufficient. Green probe + failed LOOK = FAILED.

## Done signal (every reply, last line)
`DONE — <one line>` · `BLOCKED — <why / what's needed>` · `NEEDS-CHRIS — <the question>`
Also POSTed to the bridge so the wiki shows it (pet settles / red hairline / gold).

## Approvals
Protected writes surface as cards in the Senter Wiki (bridge). Bots never route around a gate. Silence is not consent.

## Markdown is the API
Ideas.md (verbatim) → topics/<t>/.system/queue.md (spec) → session.md (outcome) → log.md (fleet change) → catalogs/agent-roster.md (who owns what).


## Delivery is not routing (2026-09-02)
A message is delivered when `dispatch.py status` shows it in `.sent/`, not when Senter writes it. The DM runner drops on `target_busy` (bot mid-turn >120s) and on 429. `senter-dispatch` queues per bot, waits for idle, retries, and posts queue state to the wiki. Builders on heavy loops run on a paid tier; free tiers rate-limit under exactly this load.

## Fresh eyes beat the author (2026-09-02)
Weaver fixed the strip 6 times by adjusting numbers; anser, who hadn't touched the file, found the infinite loop in one pass by watching class mutations. Rule: after 2 repeat corrections on the same element, the redundancy gate (anser) does a fresh-eyes QA before the owner touches it again.


## Watch the plumbing, not the status line (2026-09-02)
Twice today the pipeline reported healthy while a worker had died. `dispatch.py status` showed queued items; the daemon log showed a traceback. Every pipeline daemon needs: exceptions caught per-work-unit, the last error surfaced on `status`, and a "stale in-flight" detector (an item marked delivering for >N minutes with no bot process = re-queue). Chris shouldn't be the monitor.


## Don't let the pipeline fail silently (2026-09-02, Chris — third time)
Rules now in force: (a) a dispatch is "sent" only when the daemon log says `ok` — `status` alone lies; (b) the watcher process reports every done-line AND every daemon exception to Senter; (c) any item "delivering" for >10 min with no live bot pid is re-queued automatically; (d) when a bot has a FIFO backlog and the user is waiting on a later item, spawn a parallel instance (one kanban card per item — CLAIM v2 retired 2026-09-05) instead of waiting. This document + klerik's `agent-authoring-rules.md` are the product: the wiki must render both under topics/senter and topics/klerik so anyone adopting the process can read them.


## PR policy (2026-09-02, Chris)
- **Upstream repos (NousResearch/hermes-agent, anyone else's):** bots NEVER open a PR during a session. They keep a **PR draft ledger** — `topics/hermes-agent/prs/<slug>.md` per candidate: problem, exact lines, diff on a local branch, test plan, and a running "use cases tried" log. Every time a later use case touches the same area, the draft is updated (or withdrawn). Senter reviews the ledger at session end and Chris says which go out. Rationale (Chris): cuts sloppy PRs — things that look right in the moment and wrong after the next use case.
- **Chris's own repos (turbofit, pocket-shop, SouthpawIN/*):** ship immediately, normal PR flow.
- A bot that wants to push upstream posts NEEDS-CHRIS with the ledger path; it does not push.

## Feed sources are event-driven (2026-09-02, Chris)
Timed polling is the fallback, not the design. GitHub: webhooks (repo `gh api repos/.../hooks` or a `gh` watch on notifications with `If-Modified-Since`/ETag long-poll) → bridge `/hook/github` → post. RSS: WebSub where the feed supports it, else conditional GET on the feed's advertised TTL. X: streaming/filtered endpoints if the tier allows, else the API's own rate-window. Rule: an integration posts within seconds of the event; a poll interval only exists where the provider gives no push.


## Meeseeks model (2026-09-02, Chris)
Builder bots are **ephemeral**. One instance = one queue item = one worker that: reads the topic README + `queue.md` + the item + its skill → diagnose → build → LOOK → done-post → exits. It never carries prior conversation; the topic's `.system/` is the only memory (session.md is where it leaves what it learned). A **QA Meeseeks** (anser-shaped, fresh eyes) spawns on every DONE and either signs it or files a [FIXES] item. Parallelism is card count with a per-bot cap (weaver 3, teknium 2). **Spawn policy (2026-09-05): the kanban dispatcher is the primary spawn path — one card per item (`hermes kanban create --assignee <bot>`); the gateway dispatcher spawns the worker. Direct `hermes chat -q` spawn is the documented emergency hatch only ([[topics/senter/process/spawn-policy]]).** Why: a long-lived instance drifts, hoards context, and serializes unrelated work; today's I–M sat behind A–H for 40 minutes for no reason.


## Pending = dead worker, not busy worker (2026-09-02, Chris; spawn updated 2026-09-05)
"Things tend to die when they go into pending — that's when you should be spawning more instances." A bot blocked on an approval card is not doing work; counting it toward capacity starves the queue. Rule: parked/blocked instances never count toward a bot's in-flight cap — spawn the next item's card immediately. [Superseded 2026-09-05: the sentinel daemon that enforced this (threshold drop to 30 s, auto-Meeseeks) is retired with CLAIM v2 (spawn-policy §3); the kanban dispatcher + fleet-tick now carry capacity and stuck-detection.]


## Live means push (2026-09-02, Chris: "live live live")
No timed loaders. Every surface updates on an EVENT: filesystem change → watcher → SSE; provider event → webhook/long-poll → SSE; bot action → hook → SSE. A `setInterval`/`sleep(N)` loop is allowed only as a fallback that (a) engages when the push channel is down, (b) is labeled in the UI (`fallback · polling`), (c) is listed in this section with its reason. Everything else is a defect. REFLECT detector 7: any new `setInterval`/`sleep`-loop in wiki or bridge code without a fallback label → file it.

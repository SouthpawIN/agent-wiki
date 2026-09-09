---
type: loop
name: klerik-queue-drain
proposed: 2026-09-05 18:01
---
# klerik-queue-drain
owner: klerik · cadence: every 30m · status: LIVE
**klerik's queue holds nine unchecked REFLECT passes and anser keeps escalating 'proposals nobody applies' — want klerik on a 30-minute tick that claims and lands the oldest open refinement?**

## Prompt
Read topics/klerik/.system/queue.md. CLAIM the oldest unchecked [AGENTS] item (mkdir sidecar + heartbeat). Apply it per process/agent-authoring-rules.md using file tools only, batching protected-file writes into one call. Verify (grep every copy / smoke turn as applicable), check the box, append a dated entry to .system/session.md, post DONE/BLOCKED to the bridge. One item per tick; stop if nothing is open.

## Evidence
> Now I'll build out the topic properly per the spec: continuity, queue with real items, injections, skills/agents/loops, catalogs — all real.

## Applied 2026-09-05 18:19
`hermes -p klerik cron create "every 30m" --name klerik-queue-drain` → ok
Created job: e6e20c22e1b9
  Name: klerik-queue-drain
  Schedule: every 30m
  Workdir: /Users/sovthpaw/Documents/Projects/Projects
  Next run: 2026-09-05T18:49:52.478815-05:00
  ⚠  Gateway is not running — jobs won't fire automatically.
     Start it with: hermes gateway install
                    sudo hermes gateway install --system  # Linux servers
     Check status:  hermes cron status

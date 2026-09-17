# Injections — self-file

## [UNREAD]
[AGENTS] I see you've been chasing a local inference backend that isn't standard mlx_lm — want a bot that probes Bonsai MLX against the ornith model and reports whether it actually runs?
[AGENTS] I see you're building a plugin UI for Omarchy's remote inference stack — want a bot that builds that Omarchy plugin UI fronting nginx :8080 → model server :8100?
[LOOPS] Want a loop that watches GPU memory on your Mac and remote box every hour and warns you before a stray process eats 16 GB again?
[LOOPS] Want a loop that pings your remote inference stack (nginx :8080, model server :8100 over Tailscale) every 30m and alerts you only when an endpoint drops or GPU memory spikes?
[AGENTS] I see your Mac's prompt cache fills from accumulated test history and forces restarts — want a bot that clears and schedules prompt-cache maintenance so you stop hitting 'prompt cache is full' mid-session?
[AGENTS] I see your local and remote inference keeps hitting GPU memory walls — want a bot that profiles mlx_lm and Flash Next memory use and tunes context/cache so a single process stops eating 16 GB?
[AGENTS] I see you now run inference over a remote stack (nginx :8080, model server :8100, Tailscale) — want a bot that watches those endpoints plus GPU memory and prompt-cache health and pings you before a 16 GB process or OOM strike again?
[LOOPS] Want me to set up a loop that checks every 10m whether the watch/scan process is running current code, and if it finds a stale process, kills it, runs a fresh scan, and restarts with fixed code?
[LOOPS] Want a loop that verifies the ornith/MTPLX endpoint map every 30 minutes and flags drift?
[AGENTS] I see you're still fighting churn between ornith and MTPLX on 11613 — want a bot that watches your local endpoints and keeps a live port map?
[LOOPS] Want a loop that replays progressively larger prompts against your local servers to catch SIGKILL or cache failures before you do?
[LOOPS] Want a recurring check that verifies your local mlx_lm endpoints are still bound on the right ports and haven't been killed mid-prompt?
[AGENTS] I see you're testing local inference endpoints and hitting SIGKILL on large prompts — want a bot that monitors mlx_lm server health, port drift, and prompt-cache behavior across your local servers?

## [READ]

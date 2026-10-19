# Tailscale

How Turbofit (and the wiki) reach each other across the network.

> Grounded in `roadmap.md` (Tailscale integration) and the agent-wiki architecture.

- **Gateway binding:** the Turbofit box runs the Hermes Gateway on `0.0.0.0:8091`. Tailscale exposes it on the tailnet.
  - Mac: `com.hermes.turbofit-gateway` (launchd).
  - Omarchy: systemd user units (bind `0.0.0.0:8091`).
- **Model picker federation:** the model picker auto-discovers peers over the tailnet — each box advertises the models it can serve.
- **The wiki over Tailscale (the end state):** the agent-wiki is meant to be the single source of truth, centralized over Tailscale across all devices — organized top-down by the wiki's own standards.
- **Access:** use the tailnet hostname (e.g. `omarchy.<ts>.net`), not the public IP.

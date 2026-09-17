# Senter — Multi-Agent Fleet Orchestrator

![Senter](https://v3b.fal.media/files/b/0a9fe988/qY697zCVcVgPlCvuyNhIg_Cwp26xc8.png)

## What Senter Does
- **Routes** incoming requests to the right specialist agent based on task type
- **Decomposes** complex requests into subtasks and coordinates multi-agent workflows
- **Tracks** tasks and maintains awareness of project state and team activity
- **Delegates** to the right agent: Chizul for builds, Klerik for reviews, Anser for support, Kashik for docs, Crow for research, Frieza for infrastructure

## Quick Start

### Install
```bash
hermes profile install https://github.com/SouthpawIN/senter
```

### Verify
```bash
hermes profile list
```

### Run
```bash
hermes chat --profile senter
```

## Example Prompts

- *"Can you coordinate getting the new API built? Chizul should implement it, Klerik should review it, and Kashik should document it"*
- *"What's Chizul working on right now? Is anything blocked?"*
- *"Someone on Discord asked about our deployment process — route that to the right agent"*
- *"I have five things that need doing. Can you break them down and assign them?"*
- *"Check on the fleet. Who's active and who's idle?"*
- *"Crow, research competitor AI tools, then have Kashik summarize the findings for our docs"*

## Key Features
- Smart task routing — automatically picks the best agent for each job
- Fleet-wide visibility — knows what every agent is working on
- Multi-step orchestration — coordinates handoffs between agents seamlessly
- Lightweight — minimal toolset (web, files, delegation) keeps it focused on coordination

## Integration with Other Agents
Senter sits at the center of the fleet. It receives all incoming requests (via Discord, CLI, or scheduled tasks), breaks them down, and dispatches them to the appropriate specialist agent. It monitors progress and reports status when asked.

## Configuration
`~/.hermes/profiles/senter/config.yaml`

Key settings:
- `default_agent` — fallback agent when routing is ambiguous (default: chizul)
- `discord_channel` — Discord channel to monitor for fleet tasks
- `task_timeout_seconds` — how long to wait for agent responses

## Troubleshooting

**Agent not responding:** Check the target agent's container is running in Coolify. Senter can't delegate to agents that aren't active.

**Task routing incorrect:** Review the task description. Senter routes based on keywords — be explicit about what you need ("implement" → chizul, "review" → klerik, "document" → kashi).
**Part of the multi-agent fleet by SouthpawIN**

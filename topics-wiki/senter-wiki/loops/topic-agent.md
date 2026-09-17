# topic-agent
owner: senter · cadence: every 5m per topic with new raw (launchd `com.senter.topic-agent`) · status: LIVE
ONE agent per topic owns the lifecycle (Chris 2026-09-05): rewrites the watcher's cuts (`raw/inbox`) + sources into a structured LLM wiki (`wiki/`, `index.md`), then immediately pitches ACTION — bots first ("want a bot that…?"), loops, research — as one card each; skills auto-apply. Reuses fleet bots when one fits. Replaces topic-worker + topic-wiki compile. Source: `assets/topic-agent.py`.

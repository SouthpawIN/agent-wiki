# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: burner-phone
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/burner-phone-77153f0c25.md"]
confidence: medium
---

# burner-phone

## Current context

Skill to control an Android device with an agent # 🔥 Burner Phone - Universal 24/7 AI Phone Agent **Always-On Android Device Control with Multimodal Awareness** - Transform any Android device into a 24/7 AI assistant that understands when you're addressing it through gaze + speech, just like human conversation. Works on physical phones (Termux or ADB), emulators, and integrates seamlessly with AI agents like Hermes. --- ## 🚀 What Makes This Special Unlike traditional voice assistants that wait for wake words, our system uses **continuous multimodal streaming** to understand when you're actually addressing it: - 👁️ **Gaze Detection** - Front camera detects eye contact with phone - 👂 **Speech Detection** - Microphone captures intent (not just keywords) - 🎯 **Human-Like Attention** - Only activates when looking at AND speaking to phone - 🧠 **Conversational Memory** - Remembers context across sessions - 🔔 **Proactive Monitoring** - Battery alerts, notification summaries, check-ins --- ## Use Cases ### 1. 🏆 Hermes Hackathon Project Complete 24/7 always-on phone agent with gaze-based wake detection, built as skills with subagents and hooks integration. ### 2. 📱 AI Companion on Spare Phone Turn an old Android into an always-listening AI device that understands natural attention cues - no "Hey Siri" required. ### 3. 🤖 Burner Phone Automation Control temporary/test devices for automation tasks, testing, or privacy-focused workflows. ### 4. 🎮 Emulator Testing Test Android apps or automate workflows without needing physical hardware. ### 5. 🔌 Multi-Device Management Manage multiple phones (physical + emulators) from one configuration across Tailscale networks. --- ## ✨ What's New in v2.0 - Always-On Awareness ### 🧠 Multimodal Attention Detection (NEW!) **How it works:** - Front camera streams at 15fps to Qwen2.5-Omni 3.5B model - Microphone captures audio chunks simultaneously - Model determines: `{addressing: true, looking: true, speaking: true, confidence: 0.94}` - Daemon activates conversation when all signals align ### 📊 Performance Metrics | Metric | Value | Notes | |--------|-------|-------| | Attention latency | 500ms | Gaze+speech to activation | | TTS generation | 200ms/second | Soprano 80M on CPU | | Battery drain | ~8%/hour | Continuous streaming mode | | Network usage | ~50KB/s | Compressed media chunks | --- ## Quick Start ### Option 1: As a Skill…

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/burner-phone` (`2026-07-08T20:37:15Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/agent-fleet|Agent Fleet]]
- [[concepts/automation-event-systems|Automation Event Systems]]
- [[concepts/memory-wiki|Memory Wiki]]
- [[concepts/model-merging-training|Model Merging Training]]

---
title: burner-phone
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/burner-phone
status: dormant
tags: [repo]
---

# burner-phone

> Skill to control an Android device with an agent 

**[Open on GitHub](https://github.com/SouthpawIN/burner-phone)** · DORMANT (since 2026-07-08) · last push 2026-07-08

## Facts
- **Language:** Python
- **Stars / forks:** 53 / 6
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-01-21 · **Last push:** 2026-07-08
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-08)

## From the README

# 🔥 Burner Phone - Universal 24/7 AI Phone Agent

**Always-On Android Device Control with Multimodal Awareness** - Transform any Android device into a 24/7 AI assistant that understands when you're addressing it through gaze + speech, just like human conversation. Works on physical phones (Termux or ADB), emulators, and integrates seamlessly with AI agents like Hermes.

## 🚀 What Makes This Special

Unlike traditional voice assistants that wait for wake words, our system uses **continuous multimodal streaming** to understand when you're actually addressing it:

- 👁️ **Gaze Detection** - Front camera detects eye contact with phone
- 👂 **Speech Detection** - Microphone captures intent (not just keywords)
- 🎯 **Human-Like Attention** - Only activates when looking at AND speaking to phone
- 🧠 **Conversational Memory** - Remembers context across sessions
- 🔔 **Proactive Monitoring** - Battery alerts, notification summaries, check-ins

## Use Cases

### 1. 🏆 Hermes Hackathon Project
Complete 24/7 always-on phone agent with gaze-based wake detection, built as skills with subagents and hooks integration.

### 2. 📱 AI Companion on Spare Phone
Turn an old Android into an always-listening AI device that understands natural attention cues - no "Hey Siri" required.

### 3. 🤖 Burner Phone Automation
Control temporary/test devices for automation tasks, testing, or privacy-focused workflows.

### 4. 🎮 Emulator Testing
Test Android apps or automate workflows without needing physical hardware.

### 5. 🔌 Multi-Device Management
Manage multiple phones (physical + emulators) from one configuration across Tailscale networks.

## ✨ What's New in v2.0 - Always-On Awareness

### 🧠 Multimodal Attention Detection (NEW!)
```
Traditional Wake Words:
User: Must say "Hey Siri" exactly → Activates even when not looking

Our System:
User: Looks at phone + says anything → Only activates when gaze + speech align
Bonus: Ignores background TV/music, understands natural conversation flow
```

**How it works:**
- Front camera streams at 15fps to Qwen2.5-Omni 3.5B model
- Microphone captures audio chunks simultaneously
- Model determines: `{addressing: true, looking: true, speaking: true, confidence: 0.94}`
- Daemon activates conversation when all signals align

### 📊 Performance Metrics
| Metric | Value | Notes |
|--------|-------|-------|
| Attention latency | 500ms | Gaze+speech to activation |
| TTS generation | 200ms/second | Soprano 80M on CPU |
| Battery drain | ~8%/hour | Continuous streaming mode |
| Network usage | ~50KB/s | Compressed media chunks |

## Quick Start


*…truncated — full README at repo link*

---
name: termux-workflows
description: "Consolidated umbrella for android skills: termux-tts-voice-fix, ffmpeg-music-video"
author: Hermes Agent
version: 1.0.0
license: MIT
tags: ["Umbrella", "Android", "Consolidated"]
related_skills: ["termux-tts-voice-fix", "ffmpeg-music-video"]
---

# Termux Workflows

## Fix Silent TTS on Termux/Android


# Fix Silent TTS on Termux/Android

On Android/Termux, the `text_to_speech` tool may appear to work (files generate in `~/.hermes/audio_cache/`) but you hear **no audio**. There are **two separate code layers** that can cause this, and you must identify which one is broken before patching.

> **Critical discovery (v2.0):** Hermes has TWO audio playback paths:
> 1. **`voice_mode.py`** — used by the CLI's `/voice tts` toggle. It calls `play_audio_file()` which has a fallback chain of system audio players (`afplay`, `ffplay`, `mpv`, `aplay`).
> 2. **`tts_tool.py`** — the `text_to_speech_tool()` itself. It **generates audio but does NOT call `play_audio_file()`**. It simply returns a `MEDIA:` tag string and expects a messaging platform (Telegram, Discord, etc.) to deliver it.
>
> On Termux there is no messaging platform to intercept the `MEDIA:` tag, so the audio file sits on disk silently unless `tts_tool.py` is patched to trigger local playback.

## Quick Diagnosis (Do This First)

Before patching anything, determine which layer is failing:

```bash
# Test 1: Can mpv play an existing file at all?
timeout 10 mpv --no-video --really-quiet ~/.hermes/audio_cache/*.mp3 && echo "mpv works" || echo "mpv broken or missing"

# Test 2: Is the voice_mode.py mpv entry already present?
grep -n 'players.append.*mpv' ~/.hermes/hermes-agent/tools/voice_mode.py

# Test 3: Does tts_tool.py call play_audio_file?
grep -n 'play_audio_file' ~/.hermes/hermes-agent/tools/tts_tool.py
```

**Interpretation:**
- If Test 1 fails → install mpv: `pkg install mpv`
- If Test 2 shows no results → apply **Layer 1** patch (`voice_mode.py`)
- If Test 3 shows results ONLY in the `_play_via_tempfile` fallback (internal streaming) and NOT in the main `text_to_speech_tool()` return path → apply **Layer 2** patch (`tts_tool.py`)
- If Test 2 AND Test 3 both look okay but you still hear nothing → check `TERMUX_VERSION`/`PREFIX` env detection or pycache staleness

## Symptoms by Layer

### Layer 1 — voice_mode.py broken
- `/voice tts` toggles without error
- CLI voice mode shows "TTS on"
- `play_audio_file()` may return `True` but you hear nothing
- `grep` shows NO `mpv` entry in `voice_mode.py`

### Layer 2 — tts_tool.py missing auto-play
- TTS files are created successfully in `~/.hermes/audio_cache/`
- `mpv` works when you test manually
- `voice_mode.py` already contains the mpv fallback
- The tool returns `MEDIA:/path/to/file` but no playback happens
- This affects the `text_to_speech` tool directly, NOT just `/voice tts`

## Fix

### Layer 1: Add `mpv` to Hermes fallback chain (voice_mode.py)

Only needed if `voice_mode.py` does not already list `mpv`.

**Step 1: Locate the file**

```bash
VOICE_MODE="${HERMES_HOME:-$HOME/.hermes}/hermes-agent/tools/voice_mode.py"
```

**Step 2: Patch the player list**

Find the `players = []` block inside `play_audio_file()` (~line 885). Ensure the `mpv` entry exists:

```python
    if system == "Darwin":
        players.append(["afplay", file_path])
    players.append(["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", file_path])
    players.append(["mpv", "--no-video", "--really-quiet", file_path])  # <-- MUST EXIST
    if system == "Linux":
        players.append(["aplay", "-q", file_path])
```

**Step 3: Clear the bytecode cache**

```bash
rm -f "${HERMES_HOME:-$HOME/.hermes}/hermes-agent/tools/__pycache__/voice_mode.cpython-313.pyc"
```

(Adjust `cpython-313` to your Python version.)

---

### Layer 2: Patch tts_tool.py to auto-play locally on Termux

This is the **most common root cause** on Android/Termux. The `text_to_speech_tool()` generates audio but returns it as a `MEDIA:` tag for messaging platforms. On Termux there is no messaging platform, so nobody plays the file.

**Step 1: Locate the file**

```bash
TTS_TOOL="${HERMES_HOME:-$HOME/.hermes}/hermes-agent/tools/tts_tool.py"
```

**Step 2: Find the return block**

Inside `text_to_speech_tool()`, locate the block near the end where the JSON result is built. It looks like:

```python
        file_size = os.path.getsize(file_str)
        logger.info("TTS audio saved: %s (%s bytes, provider: %s)", file_str, f"{file_size:,}", provider)

        # Build response with MEDIA tag for platform delivery
        media_tag = f"MEDIA:{file_str}"
```

**Step 3: Insert the auto-play trigger**

Add this block immediately after the `logger.info` line and **before** the `media_tag` assignment:

```python
        # Auto-play locally on Android/Termux where no messaging platform handles MEDIA tags
        if os.environ.get("TERMUX_VERSION") or os.environ.get("PREFIX", "").startswith("/data/data/com.termux"):
            try:
                from tools.voice_mode import play_audio_file
                play_audio_file(file_str)
            except Exception as exc:
                logger.debug("Local TTS playback skipped on Termux: %s", exc)
```

**Step 4: Clear the bytecode cache**

```bash
rm -f "${HERMES_HOME:-$HOME/.hermes}/hermes-agent/tools/__pycache__/tts_tool.cpython-313.pyc"
```

**Step 5: Restart Hermes**

Python caches imported modules in memory. The patch is on disk, but the running session still holds the old code. You **must** start a new session for the patch to take effect:

```bash
# Inside Hermes CLI
/reset
```

Or exit and relaunch entirely.

---

### Layer 3: Ensure `mpv` actually produces audible output

On some Android devices, `mpv` routes through Linux audio subsystems (PulseAudio/ALSA) that are not wired to the device's speakers. Test directly:

```bash
timeout 10 mpv --no-video --really-quiet ~/.hermes/audio_cache/*.mp3
```

If `mpv` returns 0 but you hear nothing, use **`termux-media-player`** instead.

**Requirements:**
- `termux-api` package: `pkg install termux-api`
- **Termux:API Android app** installed from F-Droid or GitHub releases

**Test:**
```bash
termux-media-player play ~/.hermes/audio_cache/tts_test.mp3
termux-media-player info   # Shows "Status: Playing"
```

If you need to swap `mpv` for `termux-media-player` inside the Hermes fallback chain, edit `voice_mode.py` and replace the `mpv` entry with:

```python
    players.append(["termux-media-player", "play", file_path])
```

> **Warning:** `termux-media-player` blocks during playback and is less suited for the CLI voice loop than `mpv`. It is best used as a fallback only when `mpv` is silent.

## Prerequisites

- `mpv` installed: `pkg install mpv` (if missing)
- `termux-api` installed: `pkg install termux-api` (for termux-media-player fallback)
- **Termux:API Android app** installed (F-Droid or GitHub releases)
- Edge TTS configured as provider: `hermes config set tts.provider edge`
- TTS toolset enabled: `hermes tools enable tts`

## Pitfalls

- **Two layers, two patches.** The most common mistake is patching `voice_mode.py` and assuming that fixes everything. If the `text_to_speech` tool is silent, the real fix is in `tts_tool.py`.
- **Pycache must be cleared.** After editing `voice_mode.py` or `tts_tool.py`, delete the corresponding `__pycache__/*.pyc` file. Python will not re-read the source until the cache is stale or removed.
- **Session restart required.** Even after clearing pycache, a running Hermes process has already imported the old module into memory. Use `/reset` or exit and relaunch.
- **`tts.auto_tts` vs `voice.auto_tts` mismatch.** The stock CLI startup code only reads `voice.auto_tts`. If you want TTS on by default, set `voice.auto_tts` (not just `tts.auto_tts`):
  ```bash
  hermes config set voice.auto_tts true
  ```
- **`mpv` may return `True` but stay silent.** On Android, `mpv` can appear to succeed while producing no audible output. Always verify with your ears, not just the return value.
- **`termux-media-player` blocks during playback.** Unlike `mpv --really-quiet`, it blocks until the track finishes. In the CLI's `voice_mode.py`, the `mpv` fallback is preferred because it doesn't block the UI thread.
- **Process cleanup is required.** If `termux-media-player` is interrupted, stale processes can hold the audio lock. Kill old instances: `pkill -f "termux-media-player"`
- If you update Hermes (`hermes update`), you may need to re-apply these patches.

## Auto-Play Watcher (Persistent Voice Mode)

The `/voice tts` toggle only works within a single Hermes CLI session and still requires the CLI layer to invoke `play_audio_file()`. If you want **every voice file to play automatically** — even when chatting via tools, gateway, or API — run a background watcher.

### Why Use a Watcher

- Works across sessions (no need to type `/voice tts` every time)
- Catches voice files generated by `text_to_speech` tool calls, not just CLI voice mode
- Plays instantly (within ~500ms of file creation)
- Persists in a `tmux` session even if the main Hermes process restarts

### Setup

**1. Create the watcher script** at `~/.hermes/auto_play_tts.py`:

```python
#!/data/data/com.termux/files/usr/bin/env python3
import os, time, subprocess, glob

HERMES_HOME = os.path.expanduser("~/.hermes")
AUDIO_DIRS = [os.path.join(HERMES_HOME, "audio_cache"), HERMES_HOME]
SEEN = set()

def find_audio():
    files = []
    for d in AUDIO_DIRS:
        if os.path.isdir(d):
            files.extend(glob.glob(os.path.join(d, "*.mp3")))
            files.extend(glob.glob(os.path.join(d, "*.ogg")))
    return sorted(files, key=os.path.getmtime)

# Seed existing files
for f in find_audio():
    SEEN.add(f)

while True:
    for f in find_audio():
        if f not in SEEN:
            SEEN.add(f)
            subprocess.run(
                ["mpv", "--no-video", "--really-quiet", f],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                timeout=300, check=False,
            )
    time.sleep(0.5)
```

**2. Start it in a persistent tmux session:**

```bash
chmod +x ~/.hermes/auto_play_tts.py
tmux new-session -d -s tts_watcher "python3 ~/.hermes/auto_play_tts.py"
```

**3. Verify it's running:**

```bash
tmux ls | grep tts_watcher
ps aux | grep auto_play_tts | grep -v grep
```

**4. Stop / restart:**

```bash
tmux kill-session -t tts_watcher        # stop
tmux new-session -d -s tts_watcher "python3 ~/.hermes/auto_play_tts.py"  # restart
```

### Integration with Gateway Platforms

On Telegram, Discord, WhatsApp, etc., the gateway already sends voice files natively. The watcher is mainly for the **Termux CLI** where no native auto-play exists.

## Related: Launching Android Apps from Termux

A common companion task on Android/Termux is opening apps or URLs from the CLI. Direct `am start` fails on modern Android with:

```
SecurityException: Permission Denial: package=com.android.shell does not belong to uid=...
```

### Workaround: `termux-open`

The `termux-tools` package provides `termux-open`, which sends a **broadcast intent** to the Termux app itself. Termux then handles the launch with proper Android permissions.

**Open a URL in the default app:**

```bash
termux-open "https://youtube.com"
```

**Force a specific app via intent:**

```bash
am broadcast --user 0 -a android.intent.action.VIEW \
  -n com.termux/com.termux.app.TermuxOpenReceiver \
  -d "https://youtube.com"
```

**Open a specific installed app by package name:**

First find the package:

```bash
pm list packages | grep youtube
```

Then use `termux-open` with a deep-link or URL scheme if the app supports it. Not all apps expose deep-links, but most handle `https://` URLs via their verified domain.

**Requirements:** `pkg install termux-tools` (usually pre-installed).


## ffmpeg Music Video — Full Pipeline (Termux/Android)


# ffmpeg Music Video — Full Pipeline (Termux/Android)

Generate a complete instrumental music video using **only ffmpeg** — no external audio samples, no DAW, no GPU required. Built and tested on Android/Termux with Kimi K2.6 via Hermes Agent.

## When to Use

- You want instrumental music + visuals + title cards compiled into an MP4
- You're on Termux/Android with no DAW, no Go, no Python audio libs
- You need a hackathon-ready multimedia deliverable from a single terminal
- You want to avoid licensing issues by synthesizing everything from scratch

## Prerequisites

- `ffmpeg` with libx264 and libmp3lame support (`pkg install ffmpeg` on Termux)
- A TrueType font for drawtext (e.g., `/system/fonts/CarroisGothicSC-Regular.ttf` on Android)
- ~50MB free disk space for a 45s 1080p output

## Pipeline Overview

```
Step 1: Synthesize instrumental audio (aevalsrc sine waves)
Step 2: Encode to MP3
Step 3: Generate spectrogram/waveform visuals from audio
Step 4: Overlay title cards with drawtext
Step 5: Compile slideshow + audio into final MP4
```

---

## Step 1: Synthesize Instrumental Audio

Use `aevalsrc` to generate sine-wave layers. Build bass, arpeggio, lead, and texture tracks separately, then mix.

```bash
ffmpeg -f lavfi -i 'aevalsrc=0.4*sin(2*PI*65*t)+0.25*sin(2*PI*130*t)+0.15*sin(2*PI*196*t):s=48000:d=45' \
  -f lavfi -i 'aevalsrc=0.12*sin(2*PI*440*t)*sin(2*PI*2*t+PI/2)*0.5+0.5:s=48000:d=45' \
  -f lavfi -i 'aevalsrc=0.08*sin(2*PI*880*t)*sin(2*PI*8*t+PI/2)*0.5+0.5:s=48000:d=45' \
  -f lavfi -i 'aevalsrc=0.06*sin(2*PI*3000*t)*sin(2*PI*4*t+PI/2)*0.5+0.5:s=48000:d=45' \
  -filter_complex '
    [0:a]lowpass=f=250[bass];
    [1:a]bandpass=f=600:w=500[arp];
    [2:a]highpass=f=700[lead];
    [3:a]highpass=f=2000[noise];
    [bass][arp][lead][noise]amix=inputs=4:duration=longest,volume=4.0,dynaudnorm,afade=t=out:st=40:d=5
  ' -t 45 ~/beat.wav
```

**Layer breakdown:**
| Layer | Frequency | Role | Filter |
|-------|-----------|------|--------|
| 0 | 65Hz + 130Hz + 196Hz | Bass drone | `lowpass=f=250` |
| 1 | 440Hz gated at 2Hz | Arpeggio pulse | `bandpass=f=600:w=500` |
| 2 | 880Hz gated at 8Hz | Lead synth | `highpass=f=700` |
| 3 | 3kHz gated at 4Hz | Texture/noise | `highpass=f=2000` |

**Key filters:**
- `amix=inputs=4:duration=longest,volume=4.0` — mixes all layers
- `dynaudorm` — auto-normalizes volume
- `afade=t=out:st=40:d=5` — 5-second fadeout starting at 40s

**Pitfall — `max()` does not work in aevalsrc expressions** on some ffmpeg builds. Use `sin(2*PI*X*t+PI/2)*0.5+0.5` as a gated amplitude envelope instead.

---

## Step 2: Encode to MP3

```bash
ffmpeg -i ~/beat.wav -c:a libmp3lame -b:a 192k ~/beat.mp3
```

---

## Step 3: Generate Visuals from Audio

### Fire Spectrogram (good for dark backgrounds)
```bash
ffmpeg -i ~/beat.mp3 -lavfi "showspectrumpic=s=1920x1080:mode=separate:color=fire" \
  -update 1 -frames:v 1 ~/spectrogram_fire.png
```

### Neon Channel Spectrogram
```bash
ffmpeg -i ~/beat.mp3 -lavfi "showspectrumpic=s=1920x1080:mode=combined:color=channel" \
  -update 1 -frames:v 1 ~/spectrogram_neon.png
```

### Simple Waveform
```bash
ffmpeg -i ~/beat.mp3 -lavfi "showwavespic=s=1920x540:colors=cyan|magenta" \
  -update 1 -frames:v 1 ~/waveform.png
```

**Critical:** Always use `-update 1` when writing single PNG frames with image2 muxer, or ffmpeg errors with "Use a pattern such as %03d..."

---

## Step 4: Overlay Title Cards with drawtext

Use Android system fonts or install a TTF. On Termux, Android fonts live at `/system/fonts/`.

```bash
FONT="/system/fonts/CarroisGothicSC-Regular.ttf"

ffmpeg -i ~/spectrogram_fire.png -vf \
  "drawtext=fontfile=$FONT:text='TITLE LINE 1':fontsize=120:fontcolor=white:x=(w-text_w)/2:y=60:box=1:boxcolor=black@0.7:boxborderw=20,\
   drawtext=fontfile=$FONT:text='Subtitle':fontsize=50:fontcolor=cyan:x=(w-text_w)/2:y=200:box=1:boxcolor=black@0.5:boxborderw=12" \
  -update 1 -frames:v 1 ~/title_card.png
```

**Positioning macros:**
- `x=(w-text_w)/2` — horizontally centered
- `y=h-text_h-60` — 60px from bottom
- `box=1:boxcolor=black@0.7` — semi-transparent background behind text

---

## Step 5: Compile Slideshow + Audio into MP4

Create a concat script file listing your title cards and durations:

```bash
cat > ~/slideshow.txt << 'EOF'
file '/data/data/com.termux/files/home/title1.png'
duration 12
file '/data/data/com.termux/files/home/title2.png'
duration 12
file '/data/data/com.termux/files/home/title3.png'
duration 12
file '/data/data/com.termux/files/home/title1.png'
duration 9
EOF
```

**Critical:** Use absolute paths in the concat file. Relative paths fail inside the concat demuxer on some ffmpeg builds.

Compile:
```bash
ffmpeg -f concat -safe 0 -i ~/slideshow.txt -i ~/beat.mp3 \
  -vf "format=yuv420p,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" \
  -shortest -c:v libx264 -preset fast -crf 23 -c:a aac -b:a 192k ~/music_video.mp4
```

**Video filter explanation:**
- `format=yuv420p` — required for H.264 compatibility
- `scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2` — scales image down to fit 1920x1080, then pads with black bars to exactly 1080p. Prevents aspect ratio distortion.
- `-shortest` — trims video to match audio length (or vice versa)
- `-preset fast` — balances encode speed vs file size on mobile CPU

---

## Complete One-Shot Script

```bash
#!/data/data/com.termux/files/usr/bin/env bash
set -e

DUR=45
FONT="/system/fonts/CarroisGothicSC-Regular.ttf"

# 1. Synthesize audio
ffmpeg -f lavfi -i 'aevalsrc=0.4*sin(2*PI*65*t)+0.25*sin(2*PI*130*t)+0.15*sin(2*PI*196*t):s=48000:d='$DUR \
  -f lavfi -i 'aevalsrc=0.12*sin(2*PI*440*t)*sin(2*PI*2*t+PI/2)*0.5+0.5:s=48000:d='$DUR \
  -f lavfi -i 'aevalsrc=0.08*sin(2*PI*880*t)*sin(2*PI*8*t+PI/2)*0.5+0.5:s=48000:d='$DUR \
  -f lavfi -i 'aevalsrc=0.06*sin(2*PI*3000*t)*sin(2*PI*4*t+PI/2)*0.5+0.5:s=48000:d='$DUR \
  -filter_complex '[0:a]lowpass=f=250[b];[1:a]bandpass=f=600:w=500[a];[2:a]highpass=f=700[l];[3:a]highpass=f=2000[n];[b][a][l][n]amix=inputs=4:duration=longest,volume=4.0,dynaudnorm,afade=t=out:st=40:d=5' \
  -t $DUR beat.wav

ffmpeg -i beat.wav -c:a libmp3lame -b:a 192k beat.mp3

# 2. Visuals
ffmpeg -i beat.mp3 -lavfi "showspectrumpic=s=1920x1080:mode=separate:color=fire" -update 1 -frames:v 1 vis1.png
ffmpeg -i beat.mp3 -lavfi "showspectrumpic=s=1920x1080:mode=combined:color=channel" -update 1 -frames:v 1 vis2.png

# 3. Title cards
ffmpeg -i vis1.png -vf "drawtext=fontfile=$FONT:text='AGENT MODE':fontsize=120:fontcolor=white:x=(w-text_w)/2:y=60:box=1:boxcolor=black@0.7:boxborderw=20,drawtext=fontfile=$FONT:text='Hermes Agent x Kimi K2.6':fontsize=50:fontcolor=cyan:x=(w-text_w)/2:y=200:box=1:boxcolor=black@0.5:boxborderw=12" -update 1 -frames:v 1 title1.png
ffmpeg -i vis2.png -vf "drawtext=fontfile=$FONT:text='NO LYRICS':fontsize=120:fontcolor=cyan:x=(w-text_w)/2:y=80:box=1:boxcolor=black@0.7:boxborderw=20,drawtext=fontfile=$FONT:text='Pure Signal':fontsize=60:fontcolor=magenta:x=(w-text_w)/2:y=220:box=1:boxcolor=black@0.5:boxborderw=12" -update 1 -frames:v 1 title2.png

# 4. Slideshow list
cat > slideshow.txt <<EOF
file '$(pwd)/title1.png'
duration 15
file '$(pwd)/title2.png'
duration 15
file '$(pwd)/title1.png'
duration 15
EOF

# 5. Compile video
ffmpeg -f concat -safe 0 -i slideshow.txt -i beat.mp3 \
  -vf "format=yuv420p,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" \
  -shortest -c:v libx264 -preset fast -crf 23 -c:a aac -b:a 192k music_video.mp4

echo "Done: music_video.mp4"
```

---

## Pitfalls & Lessons Learned

1. **`max()` fails in aevalsrc** — Use `sin(phase+PI/2)*0.5+0.5` as an amplitude gate instead of `max(0, sin(...))`.
2. **`-update 1` is required** for single-frame PNG output via image2 muxer. Without it, ffmpeg demands `%03d` pattern filenames.
3. **Absolute paths in concat files** — Relative paths often fail in the concat demuxer on Android/Termux.
4. **`command -v` vs `which`** — On some Termux setups, `/bin/which` is missing but `command -v` works for path detection.
5. **`pkg install golang`** then `go install` is the path to Songsee if you want true spectrograms; but ffmpeg's `showspectrumpic` works without any Go dependency for basic visuals.
6. **`scale=1920:1080:force_original_aspect_ratio=decrease,pad=...`** is the safest way to force exactly 1080p without distorting your source images.
7. **`dynaudnorm`** before `afade` prevents the fade from clipping or dropping too early.
8. **Font selection matters** — Android system fonts vary by device. If drawtext fails, list available fonts with `ls /system/fonts/*.ttf`.

---

## Variations

- **Longer track:** Increase `d=45` and `t 45` values; adjust fade timing
- **Different mood:** Swap frequencies (e.g., 110Hz + 220Hz for darker, 880Hz + 1760Hz for brighter)
- **More layers:** Add more `-f lavfi -i` inputs and increase `amix=inputs=N`
- **Tempo shift:** Change the gate frequencies (e.g., `sin(2*PI*4*t)` = 4Hz gate = 240 BPM feel)
- **Reverb:** Add `aecho=0.8:0.9:60:0.3` after each layer before mixing
- **Color palette:** In `showspectrumpic`, try `color=intensity`, `color=fire`, `color=channel`

---

## Related Skills

- `songsee` — For professional 9-panel audio analysis grids (requires Go)
- `songwriting-and-ai-music` — For lyric writing and Suno/HeartMuLa prompts
- `heartmula` — For full AI music generation with vocals (requires GPU)


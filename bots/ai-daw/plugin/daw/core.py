"""Project manifest, layer generation, and rendering for the AI DAW plugin.

The manifest is the API: a project is a directory of plain files, so nothing is
trapped inside the plugin. Every tool returns a small dict - ids and paths, never
audio bytes - because a 4 MB base64 payload poisons the agent's context.

Engines are adapters (see daw/adapters). `dryrun` synthesises real audio with
ffmpeg so the whole pipeline is testable without a GPU; `acestep` talks to a
local ACE-Step server and is what production uses.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

LAYER_ORDER = ("drums", "bass", "harmony", "lead", "vocals", "ear-candy")
SAMPLE_RATE = 44100


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True)


def require_ffmpeg() -> None:
    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg not found on PATH")


@dataclass
class Track:
    id: str
    instrument: str
    engine: str
    model: str
    seed: int
    prompt: str
    files: list[str] = field(default_factory=list)
    gain_db: float = 0.0
    muted: bool = False
    version: int = 1
    bars: int = 8

    def signature(self) -> str:
        raw = f"{self.engine}|{self.model}|{self.seed}|{self.prompt}|{self.bars}"
        return hashlib.sha256(raw.encode()).hexdigest()[:16]


class Project:
    """One directory: project.json + stems/. The manifest is the source of truth."""

    def __init__(self, root: Path):
        self.root = Path(root)
        self.manifest_path = self.root / "project.json"
        self.data: dict[str, Any] = {}

    # -- lifecycle ---------------------------------------------------------
    @classmethod
    def create(cls, projects_dir: Path, project_id: str, *, bpm: int = 120,
               key: str = "A minor", sections: list[dict[str, Any]] | None = None) -> "Project":
        require_ffmpeg()
        root = Path(projects_dir) / project_id
        if (root / "project.json").exists():
            raise ValueError(f"project '{project_id}' already exists at {root}")
        (root / "stems").mkdir(parents=True, exist_ok=True)
        project = cls(root)
        project.data = {
            "id": project_id,
            "bpm": int(bpm),
            "key": key,
            "sections": sections or [{"name": "main", "bars": 16}],
            "tracks": [],
            "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
        project.save()
        return project

    @classmethod
    def open(cls, projects_dir: Path, project_id: str) -> "Project":
        root = Path(projects_dir) / project_id
        if not (root / "project.json").exists():
            raise FileNotFoundError(f"no project '{project_id}' under {projects_dir}")
        project = cls(root)
        project.data = json.loads((root / "project.json").read_text(encoding="utf-8"))
        return project

    def save(self) -> None:
        self.manifest_path.write_text(json.dumps(self.data, indent=2) + "\n", encoding="utf-8")

    # -- derived facts -----------------------------------------------------
    @property
    def tracks(self) -> list[Track]:
        return [Track(**raw) for raw in self.data["tracks"]]

    def total_bars(self) -> int:
        return sum(int(section.get("bars", 0)) for section in self.data.get("sections", [])) or 16

    def duration_seconds(self) -> float:
        bpm = float(self.data.get("bpm", 120)) or 120.0
        return round(self.total_bars() * 4 * 60.0 / bpm, 3)

    def find(self, instrument: str) -> Track | None:
        for track in self.tracks:
            if track.instrument == instrument or track.id == instrument:
                return track
        return None

    # -- generation --------------------------------------------------------
    def generate_layer(self, *, instrument: str, prompt: str, seed: int | None = None,
                       engine: str = "dryrun", bars: int | None = None,
                       engines: dict[str, Any] | None = None) -> dict[str, Any]:
        """Generate one layer. Idempotent on (engine, model, seed, prompt, bars)."""
        require_ffmpeg()
        from .adapters import get_engine

        registry = engines if engines is not None else None
        adapter = get_engine(engine, registry)
        bars = int(bars or self.total_bars())
        seed = int(seed if seed is not None else _stable_seed(instrument, prompt))

        existing = self.find(instrument)
        candidate = Track(
            id=existing.id if existing else _slug(instrument),
            instrument=instrument, engine=adapter.name, model=adapter.model,
            seed=seed, prompt=prompt, bars=bars,
        )
        if existing and existing.signature() == candidate.signature() and existing.files:
            relative = existing.files[-1]
            if (self.root / relative).exists():
                return {"ok": True, "reused": True, "project": self.data["id"],
                        "track": existing.id, "version": existing.version,
                        "path": relative, "engine": existing.engine,
                        "model": existing.model, "seed": existing.seed, "elapsed_s": 0.0}

        if not adapter.health():
            return {"ok": False, "error": f"engine '{engine}' is not available",
                    "hint": adapter.install_hint}

        version = (existing.version + 1) if existing else 1
        relative = f"stems/{candidate.id}/v{version}.wav"
        out_path = self.root / relative
        out_path.parent.mkdir(parents=True, exist_ok=True)

        result = adapter.generate(
            request={
                "prompt": prompt, "duration_s": round(bars * 4 * 60.0 / float(self.data["bpm"]), 3),
                "bpm": self.data["bpm"], "key": self.data["key"], "seed": seed,
                "instrument": instrument, "output": str(out_path),
                "reference": self.reference_mix(),
            }
        )
        if not result.get("ok"):
            return {"ok": False, "error": result.get("error", "generation failed"),
                    "hint": result.get("hint", "")}

        track = asdict(candidate)
        track["files"] = (existing.files if existing else []) + [relative]
        track["version"] = version
        track["gain_db"] = existing.gain_db if existing else _default_gain(instrument)
        track["muted"] = existing.muted if existing else False
        self._upsert_track(track)
        self.save()
        return {"ok": True, "reused": False, "project": self.data["id"], "track": candidate.id,
                "version": version, "path": relative, "engine": adapter.name,
                "model": adapter.model, "seed": seed,
                "elapsed_s": result.get("elapsed_s", 0.0)}

    def _upsert_track(self, track: dict[str, Any]) -> None:
        tracks = self.data["tracks"]
        for index, existing in enumerate(tracks):
            if existing["id"] == track["id"]:
                tracks[index] = track
                return
        tracks.append(track)

    def reference_mix(self) -> str | None:
        """A low-bitrate mono render of what exists so far, for conditioning."""
        current = [t for t in self.tracks if t.files and not t.muted]
        if not current:
            return None
        require_ffmpeg()
        ref = self.root / "stems" / "_reference.mp3"
        inputs: list[str] = []
        for track in current:
            inputs += ["-i", str(self.root / track.files[-1])]
        filtergraph = "".join(f"[{i}:a]" for i in range(len(current))) + \
            f"amix=inputs={len(current)}:normalize=0,aresample=16000"
        result = run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *inputs,
                      "-filter_complex", filtergraph, "-ac", "1", "-b:a", "32k", str(ref)])
        return str(ref) if result.returncode == 0 and ref.exists() else None

    # -- mixing ------------------------------------------------------------
    def set_track(self, instrument: str, *, gain_db: float | None = None,
                  muted: bool | None = None) -> dict[str, Any]:
        track = self.find(instrument)
        if track is None:
            return {"ok": False, "error": f"no track '{instrument}'",
                    "hint": f"generate it first; known: {[t.id for t in self.tracks]}"}
        raw = next(item for item in self.data["tracks"] if item["id"] == track.id)
        if gain_db is not None:
            raw["gain_db"] = float(gain_db)
        if muted is not None:
            raw["muted"] = bool(muted)
        self.save()
        return {"ok": True, "track": raw["id"], "gain_db": raw["gain_db"], "muted": raw["muted"]}

    def render_stems(self, out_dir: Path) -> dict[str, Any]:
        """Aligned stems, one per track, all exactly the project duration."""
        require_ffmpeg()
        out_dir = Path(out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        duration = self.duration_seconds()
        written = []
        for track in self.tracks:
            if not track.files:
                continue
            source = self.root / track.files[-1]
            if not source.exists():
                continue
            dest = out_dir / f"{track.id}.wav"
            result = run([
                "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(source),
                "-af", f"atrim=0:{duration},apad,aresample={SAMPLE_RATE}",
                "-t", f"{duration}", "-ac", "2", str(dest),
            ])
            if result.returncode != 0:
                return {"ok": False, "error": result.stderr.strip()[:300],
                        "hint": f"stem render failed for {track.id}"}
            written.append(str(dest))
        return {"ok": True, "stems": written, "duration_s": duration}

    def render_mix(self, out_path: Path) -> dict[str, Any]:
        require_ffmpeg()
        out_path = Path(out_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        active = [t for t in self.tracks if t.files and not t.muted]
        if not active:
            return {"ok": False, "error": "nothing to mix",
                    "hint": "generate at least one layer first"}
        duration = self.duration_seconds()
        inputs: list[str] = []
        parts: list[str] = []
        for index, track in enumerate(active):
            inputs += ["-i", str(self.root / track.files[-1])]
            gain = float(track.gain_db)
            parts.append(f"[{index}:a]atrim=0:{duration},apad,volume={gain}dB[a{index}]")
        mix_inputs = "".join(f"[a{index}]" for index in range(len(active)))
        graph = ";".join(parts) + f";{mix_inputs}amix=inputs={len(active)}:normalize=0[mix]"
        joined = out_path.with_suffix(".joined.wav")
        first = run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *inputs,
                     "-filter_complex", graph, "-map", "[mix]",
                     "-t", f"{duration}", "-ar", str(SAMPLE_RATE), str(joined)])
        if first.returncode != 0:
            return {"ok": False, "error": first.stderr.strip()[:300], "hint": "mix bus failed"}

        second = run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(joined),
                      "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", str(SAMPLE_RATE), str(out_path)])
        joined.unlink(missing_ok=True)
        if second.returncode != 0:
            return {"ok": False, "error": second.stderr.strip()[:300], "hint": "loudnorm failed"}

        loudness = measure_loudness(out_path)
        problems = []
        if loudness.get("true_peak_db") is not None and loudness["true_peak_db"] > -1.0:
            problems.append(f"true peak {loudness['true_peak_db']} dBTP above -1.0")
        return {"ok": True, "mix": str(out_path), "duration_s": duration,
                "tracks": [t.id for t in active], "loudness": loudness, "problems": problems}

    def status(self) -> dict[str, Any]:
        tracks = self.tracks
        missing = [name for name in LAYER_ORDER if not any(t.instrument == name for t in tracks)]
        return {
            "ok": True, "project": self.data["id"], "bpm": self.data["bpm"], "key": self.data["key"],
            "duration_s": self.duration_seconds(),
            "tracks": [{"id": t.id, "instrument": t.instrument, "engine": t.engine,
                        "version": t.version, "muted": t.muted, "gain_db": t.gain_db,
                        "files": len(t.files)} for t in tracks],
            "missing_layers": missing,
        }


def measure_loudness(path: Path) -> dict[str, Any]:
    result = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path),
                  "-af", "ebur128=peak=true", "-f", "null", "-"])
    text = result.stderr
    i = _last_float(text, r"I:\s*(-?[\d.]+) LUFS")
    peak = _last_float(text, r"Peak:\s*(-?[\d.]+) dBFS")
    return {"integrated_lufs": i, "true_peak_db": peak}


def _last_float(text: str, pattern: str) -> float | None:
    import re
    matches = re.findall(pattern, text)
    return float(matches[-1]) if matches else None


def _slug(value: str) -> str:
    import re
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "track"


def _stable_seed(instrument: str, prompt: str) -> int:
    digest = hashlib.sha256(f"{instrument}|{prompt}".encode()).hexdigest()
    return int(digest[:8], 16)


def _default_gain(instrument: str) -> float:
    # Rough gain stage so a generated layer cannot clip into the bus.
    return {"drums": -6.0, "bass": -8.0, "harmony": -12.0,
            "lead": -10.0, "vocals": -6.0}.get(instrument, -12.0)

#!/usr/bin/env python3
"""Anser's grounding corpus: fetch, cache, and cite.

The moderation answer bot must never answer from memory. This tool keeps a local,
append-only cache of the official @NousResearch and @Teknium posts, and answers a
query with the posts that actually support it - each with a URL and a date.

It works in two modes so it is testable without credentials:
  * `xurl` (the real path) when X read access is configured
  * `--from-json` to import posts from any JSON array (a fixture, an export, a
    manual paste of a thread)

Usage:
    python corpus.py refresh [--accounts NousResearch Teknium] [--limit 50]
    python corpus.py import --from-json posts.json
    python corpus.py search "hermes web app" [--account NousResearch] [--days 90] [--top 5]
    python corpus.py status
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from dataclasses import dataclass, asdict, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable

DATA = Path("data")
CORPUS = DATA / "x-corpus.jsonl"
STATE = DATA / "corpus-state.json"
DEFAULT_ACCOUNTS = ("NousResearch", "Teknium")


@dataclass(frozen=True)
class Post:
    id: str
    account: str
    created_at: str
    text: str
    url: str
    is_reply: bool = False
    quote_of: str = ""

    @classmethod
    def from_raw(cls, raw: dict[str, Any], account: str = "") -> "Post":
        ident = str(raw.get("id") or raw.get("id_str") or raw.get("post_id") or "")
        if not ident:
            raise ValueError("post has no id")
        created = str(raw.get("created_at") or raw.get("date") or "")
        text = str(raw.get("text") or raw.get("full_text") or "").strip()
        url = str(raw.get("url") or raw.get("permalink") or "")
        if not url:
            handle = str(raw.get("account") or raw.get("user") or account).lstrip("@")
            url = f"https://x.com/{handle}/status/{ident}" if handle else ""
        return cls(
            id=ident,
            account=str(raw.get("account") or raw.get("user") or account).lstrip("@"),
            created_at=created,
            text=text,
            url=url,
            is_reply=bool(raw.get("is_reply") or raw.get("in_reply_to_status_id")),
            quote_of=str(raw.get("quote_of") or ""),
        )

    def age_days(self, now: datetime | None = None) -> float | None:
        if not self.created_at:
            return None
        for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
            try:
                stamp = datetime.strptime(self.created_at, fmt)
                if stamp.tzinfo is None:
                    stamp = stamp.replace(tzinfo=timezone.utc)
                return ((now or datetime.now(timezone.utc)) - stamp).days
            except ValueError:
                continue
        return None


def load_corpus(path: Path | None = None) -> dict[str, Post]:
    target = path or CORPUS
    posts: dict[str, Post] = {}
    if not target.exists():
        return posts
    for line in target.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        raw = json.loads(line)
        posts[raw["id"]] = Post(**{k: v for k, v in raw.items() if k in Post.__dataclass_fields__})
    return posts


def upsert(posts: Iterable[Post], path: Path | None = None) -> tuple[int, int]:
    """Append-only: existing ids keep their line, new ids are added. Returns (added, total)."""
    target = path or CORPUS
    target.parent.mkdir(parents=True, exist_ok=True)
    existing = load_corpus(target)
    added = 0
    with target.open("a", encoding="utf-8") as handle:
        for post in posts:
            if post.id in existing:
                continue
            handle.write(json.dumps(asdict(post), ensure_ascii=False) + "\n")
            existing[post.id] = post
            added += 1
    return added, len(existing)


def write_state(accounts: Iterable[str], *, stale: bool = False, error: str = "",
                path: Path | None = None) -> dict[str, Any]:
    target = path or STATE
    target.parent.mkdir(parents=True, exist_ok=True)
    corpus = load_corpus()
    newest = max((p.created_at for p in corpus.values() if p.created_at), default="")
    state = {
        "last_run": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "accounts": sorted(set(accounts)),
        "count": len(corpus),
        "newest_created_at": newest,
        "stale": stale,
        "error": error,
    }
    target.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    return state


def fetch_xurl(account: str, *, limit: int = 50) -> list[Post]:
    """Real path: the xurl CLI. Raises RuntimeError with the auth hint on failure."""
    if not shutil.which("xurl"):
        raise RuntimeError("xurl CLI not installed - see the xurl skill")
    proc = subprocess.run(
        ["xurl", "search", f"from:{account}", "--limit", str(limit), "--json"],
        capture_output=True, text=True, timeout=120,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"xurl failed for @{account}: {proc.stderr.strip()[:200]}")
    try:
        raw = json.loads(proc.stdout or "[]")
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"xurl returned non-JSON for @{account}: {exc}") from exc
    items = raw.get("posts", raw) if isinstance(raw, dict) else raw
    return [Post.from_raw(item, account) for item in items]


def refresh(accounts: Iterable[str] = DEFAULT_ACCOUNTS, *, limit: int = 50) -> dict[str, Any]:
    """Fetch every account. On failure, mark the corpus stale instead of hiding it."""
    collected: list[Post] = []
    errors: list[str] = []
    for account in accounts:
        try:
            collected.extend(fetch_xurl(account, limit=limit))
        except (RuntimeError, subprocess.TimeoutExpired) as exc:
            errors.append(f"@{account}: {exc}")
    added, total = upsert(collected)
    state = write_state(accounts, stale=bool(errors) and total == 0,
                        error="; ".join(errors))
    return {"added": added, "total": total, "errors": errors, "state": state}


def import_json(path: str | Path, *, account: str = "") -> dict[str, Any]:
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    items = raw.get("posts", raw) if isinstance(raw, dict) else raw
    posts = [Post.from_raw(item, account) for item in items]
    added, total = upsert(posts)
    write_state(sorted({p.account for p in posts} | set(DEFAULT_ACCOUNTS)))
    return {"added": added, "total": total, "imported": len(posts)}


def _score(post: Post, terms: list[str]) -> float:
    haystack = post.text.lower()
    hits = sum(haystack.count(term) for term in terms)
    if not hits:
        return 0.0
    exact = sum(1 for term in terms if term in haystack)
    recency = post.age_days()
    fresh = 1.0 if recency is None else max(0.25, 1.0 - recency / 365.0)
    reply_penalty = 0.8 if post.is_reply else 1.0
    return round(hits * 0.5 + exact * 1.5, 3) * fresh * reply_penalty


def search(query: str, *, account: str = "", days: int | None = None, top: int = 5,
           corpus: dict[str, Post] | None = None) -> list[dict[str, Any]]:
    """Best matches, each with the citation Anser must include."""
    posts = corpus if corpus is not None else load_corpus()
    terms = [t for t in query.lower().split() if len(t) > 2]
    if not terms:
        return []
    results = []
    for post in posts.values():
        if account and post.account.lower() != account.lower().lstrip("@"):
            continue
        if days is not None:
            age = post.age_days()
            if age is not None and age > days:
                continue
        score = _score(post, terms)
        if score <= 0:
            continue
        results.append({
            "score": score,
            "account": post.account,
            "created_at": post.created_at,
            "age_days": post.age_days(),
            "url": post.url,
            "text": post.text,
            "is_reply": post.is_reply,
            "citation": f"@{post.account}, {post.created_at[:10] if post.created_at else 'undated'} — {post.url}",
        })
    results.sort(key=lambda item: (-item["score"], item["created_at"] or ""), reverse=False)
    return results[:top]


def answer_pack(question: str, *, top: int = 3, days: int | None = None) -> dict[str, Any]:
    """What Anser needs to answer honestly: matches, or an explicit 'not stated'."""
    matches = search(question, top=top, days=days)
    return {
        "question": question,
        "grounded": bool(matches),
        "sources": matches,
        "corpus_state": json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {},
        "answer_stub": (
            "\n".join(f"- {m['citation']}: {m['text'][:160]}" for m in matches)
            if matches else
            "Not publicly stated in the corpus. Say so, cite the closest real source, "
            "and do not fill the gap with product knowledge."
        ),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("refresh"); p.add_argument("--accounts", nargs="*", default=list(DEFAULT_ACCOUNTS))
    p.add_argument("--limit", type=int, default=50)
    p = sub.add_parser("import"); p.add_argument("--from-json", required=True)
    p.add_argument("--account", default="")
    p = sub.add_parser("search"); p.add_argument("query")
    p.add_argument("--account", default=""); p.add_argument("--days", type=int)
    p.add_argument("--top", type=int, default=5)
    p = sub.add_parser("pack"); p.add_argument("question"); p.add_argument("--top", type=int, default=3)
    sub.add_parser("status")

    args = parser.parse_args(argv)
    if args.command == "refresh":
        result = refresh(args.accounts, limit=args.limit)
        print(json.dumps(result, indent=2))
        return 1 if result["errors"] and result["total"] == 0 else 0
    if args.command == "import":
        print(json.dumps(import_json(args.from_json, account=args.account), indent=2)); return 0
    if args.command == "search":
        print(json.dumps(search(args.query, account=args.account, days=args.days, top=args.top), indent=2)); return 0
    if args.command == "pack":
        print(json.dumps(answer_pack(args.question, top=args.top), indent=2)); return 0
    if args.command == "status":
        state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}
        print(json.dumps({"state": state, "posts": len(load_corpus())}, indent=2)); return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

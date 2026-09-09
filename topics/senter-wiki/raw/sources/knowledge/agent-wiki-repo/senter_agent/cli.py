from __future__ import annotations

import argparse
import json
from pathlib import Path

from .factories import materialize_all
from .parser import parse_tree
from .planner import build_plan
from .queue import write_queue
from .runtime import SenterRuntime


def main() -> int:
    parser = argparse.ArgumentParser(prog="senter-agent", description="Run the markdown-native Senter GOOP runtime.")
    parser.add_argument("root", nargs="?", default=".", help="Markdown workspace to inspect")
    parser.add_argument("--json", action="store_true", help="Print machine-readable output")
    parser.add_argument("--queue", metavar="PATH", help="Write/update a proposal queue")
    parser.add_argument("--materialize", metavar="TOPIC", help="Materialize editable topic artifacts")
    parser.add_argument("--status", action="store_true", help="Run a reconciliation and print runtime status")
    args = parser.parse_args()
    root = Path(args.root)
    documents = parse_tree(root)
    proposals = build_plan(documents)
    queue = Path(args.queue) if args.queue else root / ".system" / "proposals.md"
    write_queue(queue, proposals)
    materialized = materialize_all(root, args.materialize, proposals) if args.materialize else []
    result = {
        "documents": len(documents),
        "proposals": [proposal.as_dict() for proposal in proposals],
        "queue": str(queue),
        "materialized": [str(item.path) for item in materialized],
    }
    if args.status:
        result["status"] = SenterRuntime(root).status()
    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print(f"Documents: {result['documents']}")
        print(f"Queue: {result['queue']}")
        for item in result["proposals"]:
            print(f"- [{item['primitive']}] {item['slug']}: {item['reason']}")
        for path in result["materialized"]:
            print(f"  wrote: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

__all__ = ["main"]

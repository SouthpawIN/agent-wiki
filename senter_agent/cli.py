from __future__ import annotations

import argparse
import json
from pathlib import Path

from .parser import parse_tree
from .planner import plan_dict


def main() -> int:
    parser = argparse.ArgumentParser(prog="senter-agent", description="Inspect markdown as GOOP source and propose typed artifacts.")
    parser.add_argument("root", nargs="?", default=".", help="Markdown tree to inspect")
    parser.add_argument("--json", action="store_true", help="Print machine-readable output")
    args = parser.parse_args()
    result = plan_dict(parse_tree(Path(args.root)))
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Documents: {result['documents']}")
        for item in result["proposals"]:
            print(f"- [{item['primitive']}] {item['slug']}: {item['reason']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

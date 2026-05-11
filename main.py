"""Command-line entry point for comparing two Python code snippets or files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from metrics import extract_all_metrics


CODE_A = """
def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
"""


CODE_B = """
def fibo(total):
    x, y = 0, 1
    values = []
    counter = 0
    while counter < total:
        values.append(x)
        x, y = y, x + y
        counter += 1
    return values
"""


def read_code_argument(value: str | None, fallback: str) -> str:
    if value is None:
        return fallback

    path = Path(value)
    if path.exists():
        return path.read_text(encoding="utf-8")

    return value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compare two Python snippets/files using hybrid clone-detection metrics."
    )
    parser.add_argument("--code-a", help="First code snippet or path to a .py file.")
    parser.add_argument("--code-b", help="Second code snippet or path to a .py file.")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print metrics as JSON instead of a readable table.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    code_a = read_code_argument(args.code_a, CODE_A)
    code_b = read_code_argument(args.code_b, CODE_B)
    metrics = extract_all_metrics(code_a, code_b)

    if args.json:
        print(json.dumps(metrics, indent=2, sort_keys=True))
        return

    print("Hybrid code clone metrics")
    print("=" * 31)
    for name, value in sorted(metrics.items()):
        print(f"{name:<28} {value:.4f}")


if __name__ == "__main__":
    main()

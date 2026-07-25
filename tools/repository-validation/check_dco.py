#!/usr/bin/env python3
"""Require a DCO 1.1 signoff on every non-merge commit in a PR range."""

from __future__ import annotations

import argparse
import re
import subprocess


SIGNOFF = re.compile(
    r"^Signed-off-by:\s+.+\s+<[^<>@\s]+@[^<>\s]+>$",
    re.MULTILINE | re.IGNORECASE,
)


def commits(base: str, head: str) -> list[tuple[str, str]]:
    completed = subprocess.run(
        [
            "git",
            "log",
            "--no-merges",
            "--format=%H%x1f%B%x1e",
            f"{base}..{head}",
        ],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    result: list[tuple[str, str]] = []
    for record in completed.stdout.split("\x1e"):
        record = record.strip()
        if not record or "\x1f" not in record:
            continue
        sha, message = record.split("\x1f", 1)
        result.append((sha.strip(), message.strip()))
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    args = parser.parse_args()

    selected = commits(args.base, args.head)
    if not selected:
        print("DCO check failed: the pull request range contains no commits.")
        return 1

    missing = [sha for sha, message in selected if not SIGNOFF.search(message)]
    if missing:
        print("DCO check failed. Missing Signed-off-by:")
        for sha in missing:
            print(f"- {sha}")
        return 1

    print(f"DCO check passed for {len(selected)} commit(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


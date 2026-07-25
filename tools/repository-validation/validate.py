#!/usr/bin/env python3
"""Validate that the public repository is self-contained and governance-ready."""

from __future__ import annotations

import json
from pathlib import Path


REQUIRED_FILES = (
    "LICENSE",
    "DCO",
    "README.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "SECURITY.md",
    ".github/CODEOWNERS",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/feature.yml",
    ".github/ISSUE_TEMPLATE/bug.yml",
    ".github/ISSUE_TEMPLATE/experiment.yml",
    ".github/ISSUE_TEMPLATE/performance.yml",
    ".github/workflows/repository-validation.yml",
    "docs/governance/PUBLIC-CONTRIBUTION-CONTRACT.md",
    "docs/governance/REALISM-PERFORMANCE-CONTRACT.md",
    "docs/governance/PUBLICATION-MANIFEST-0001.md",
    "tools/repository-validation/check_dco.py",
    "tools/repository-validation/test_validate.py",
)

TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".py", ".txt", ""}


def forbidden_fragments() -> tuple[str, ...]:
    return (
        "football-simulation" + "-spdd",
        "Prompt_Codex" + "_Organizacao",
        "chatgpt" + "-projects",
        "C:" + "\\Users\\",
    )


def validate(root: Path) -> list[str]:
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing required file: {relative}")

    license_path = root / "LICENSE"
    if license_path.is_file():
        license_text = license_path.read_text(encoding="utf-8")
        if "GNU AFFERO GENERAL PUBLIC LICENSE" not in license_text:
            errors.append("LICENSE is not the expected AGPL text")

    dco_path = root / "DCO"
    if dco_path.is_file():
        dco_text = dco_path.read_text(encoding="utf-8")
        if "Developer's Certificate of Origin 1.1" not in dco_text:
            errors.append("DCO 1.1 heading is missing")

    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        relative = path.relative_to(root).as_posix()
        for fragment in forbidden_fragments():
            if fragment.lower() in text.lower():
                errors.append(f"private-boundary fragment in {relative}")

    return sorted(set(errors))


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    errors = validate(root)
    result = {
        "repository": "ale468/football-simulation",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
    }
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())


#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("validate.py")
SPEC = importlib.util.spec_from_file_location("repository_validate", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class RepositoryValidatorTests(unittest.TestCase):
    def make_valid_tree(self, root: Path) -> None:
        for relative in VALIDATOR.REQUIRED_FILES:
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("placeholder\n", encoding="utf-8")
        (root / "LICENSE").write_text(
            "GNU AFFERO GENERAL PUBLIC LICENSE\n", encoding="utf-8"
        )
        (root / "DCO").write_text(
            "Developer's Certificate of Origin 1.1\n", encoding="utf-8"
        )
        for relative, fragments in VALIDATOR.REQUIRED_FRAGMENTS.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("\n".join(fragments) + "\n", encoding="utf-8")

    def test_valid_tree_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_valid_tree(root)
            self.assertEqual([], VALIDATOR.validate(root))

    def test_missing_file_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_valid_tree(root)
            (root / "README.md").unlink()
            self.assertTrue(
                any("README.md" in error for error in VALIDATOR.validate(root))
            )

    def test_private_boundary_fragment_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_valid_tree(root)
            forbidden = VALIDATOR.forbidden_fragments()[0]
            (root / "README.md").write_text(forbidden, encoding="utf-8")
            self.assertTrue(
                any(
                    "private-boundary" in error
                    for error in VALIDATOR.validate(root)
                )
            )

    def test_missing_contract_fragment_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_valid_tree(root)
            readme = root / "README.md"
            readme.write_text("public project\n", encoding="utf-8")
            self.assertTrue(
                any(
                    "required contract fragment" in error
                    for error in VALIDATOR.validate(root)
                )
            )

    def test_broken_relative_markdown_link_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_valid_tree(root)
            for relative, fragments in VALIDATOR.REQUIRED_FRAGMENTS.items():
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("\n".join(fragments) + "\n", encoding="utf-8")
            (root / "README.md").write_text(
                (root / "README.md").read_text(encoding="utf-8")
                + "[missing](docs/missing.md)\n",
                encoding="utf-8",
            )
            self.assertTrue(
                any(
                    "broken relative link" in error
                    for error in VALIDATOR.validate(root)
                )
            )


if __name__ == "__main__":
    unittest.main()

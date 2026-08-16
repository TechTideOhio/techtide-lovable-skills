"""Smoke tests for the published skill catalog.

The repository contains documentation and configuration packages rather than
runtime code. These checks protect the import-facing contract without adding
a third-party test dependency.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PACKAGES = {
    "lovable-native-packaging-bridge",
    "techtide-lovable-build-loop-operator",
    "techtide-lovable-production-handoff",
    "techtide-replit-fullstack-bootstrap",
    "techtide-v0-ui-prompt-hardener",
}
REQUIRED_SECTIONS = ("## Workflow", "## Output Contract", "## Guardrails")
SOURCE_URL = "https://github.com/TechTideOhio/techtide-harness-kit"


class SkillCatalogSmokeTests(unittest.TestCase):
    def test_catalog_contains_expected_packages(self) -> None:
        packages = {
            path.name
            for path in ROOT.iterdir()
            if path.is_dir() and (path / "SKILL.md").is_file()
        }
        self.assertEqual(EXPECTED_PACKAGES, packages)

    def test_each_package_has_documentation_and_license(self) -> None:
        for package in sorted(EXPECTED_PACKAGES):
            package_dir = ROOT / package
            self.assertTrue((package_dir / "README.md").is_file(), package)
            self.assertTrue((package_dir / "SKILL.md").is_file(), package)
            self.assertTrue((package_dir / "LICENSE").is_file(), package)

    def test_skill_metadata_and_contract_are_present(self) -> None:
        for package in sorted(EXPECTED_PACKAGES):
            content = (ROOT / package / "SKILL.md").read_text(encoding="utf-8")
            self.assertRegex(content, r"\A---\nname:\s*\S+\ndescription:\s*.+\n---\n")
            for section in REQUIRED_SECTIONS:
                self.assertIn(section, content, package)
            self.assertIn("TechTide Harness Kit", content, package)
            self.assertIn("security and privacy notes", content.lower(), package)

    def test_package_readmes_are_import_oriented(self) -> None:
        for package in sorted(EXPECTED_PACKAGES):
            content = (ROOT / package / "README.md").read_text(encoding="utf-8")
            self.assertIn(package, content)
            self.assertIn(SOURCE_URL, content)
            self.assertRegex(content, r"https://github\.com/TechTideOhio/[a-z0-9-]+")

    def test_root_readme_links_catalog_and_support_paths(self) -> None:
        content = (ROOT / "README.md").read_text(encoding="utf-8")
        for package in sorted(EXPECTED_PACKAGES):
            self.assertIn(f"./{package}/", content)
        for document in ("CONTRIBUTING.md", "SECURITY.md", "SUPPORT.md", "CODE_OF_CONDUCT.md"):
            self.assertIn(f"./{document}", content)


if __name__ == "__main__":
    unittest.main()

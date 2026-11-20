"""Exercise the documentation CI entry point against a small repository."""
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class DocumentationLinksTest(unittest.TestCase):
    def test_inline_links_with_and_without_titles(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            script = root / ".github/scripts/check_docs.py"
            script.parent.mkdir(parents=True)
            shutil.copyfile(Path(__file__).with_name(script.name), script)
            (root / "docs").mkdir()
            for name in ("course.md", "research-plan.md", "my report.md"):
                (root / "docs" / name).write_text("# Document\n", encoding="utf-8")

            for destination in (
                "docs/course.md",
                'docs/course.md "Report title"',
                "docs/course.md 'Report title'",
                "docs/course.md (Report title)",
                '<docs/my report.md> "Report title"',
            ):
                for missing in (False, True):
                    with self.subTest(destination=destination, missing=missing):
                        target = destination.replace("docs/", "missing/") if missing else destination
                        (root / "README.md").write_text(f"[Report]({target})\n", encoding="utf-8")
                        check = subprocess.run(
                            [sys.executable, str(script)], capture_output=True, text=True
                        )
                        self.assertEqual(check.returncode, int(missing), check.stderr)
                        if missing:
                            self.assertIn("missing missing/", check.stderr)


if __name__ == "__main__":
    unittest.main()

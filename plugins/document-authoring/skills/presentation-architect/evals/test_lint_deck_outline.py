import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "lint_deck_outline.py"


class LintDeckOutlineCliTests(unittest.TestCase):
    def run_lint(self, markdown, *arguments):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "deck.md"
            path.write_text(markdown, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(path), "--json", *arguments],
                capture_output=True,
                check=False,
                text=True,
            )
        return result, json.loads(result.stdout)

    def test_alphabetic_appendix_id_is_recognized(self):
        result, findings = self.run_lint(
            """## B1 — Segment differences explain the aggregate result
- Placement: Appendix
- Trigger question: Does the result hold by segment?
"""
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("DECK001", {item["code"] for item in findings})
        self.assertNotIn("A004", {item["code"] for item in findings})

    def test_parenthetical_note_is_not_treated_as_a_source(self):
        result, findings = self.run_lint(
            """## S01 — Adoption rose during the pilot
- Placement: Core
利用率は35%へ上昇した（暫定集計）。
""",
            "--check-sources",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("E001", {item["code"] for item in findings})

    def test_populated_source_field_satisfies_source_check(self):
        result, findings = self.run_lint(
            """## S01 — Adoption rose during the pilot
- Placement: Core
- Source: 2026年8月の社内利用ログ
利用率は35%へ上昇した。
""",
            "--check-sources",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("E001", {item["code"] for item in findings})

    def test_non_core_content_is_not_linted_as_core_density(self):
        bullets = "\n".join(f"- Detail {number}" for number in range(1, 10))
        for placement in ("Notes", "Omit"):
            with self.subTest(placement=placement):
                result, findings = self.run_lint(
                    f"""## X1 — Material excluded from the delivered core deck
- Placement: {placement}
{bullets}
"""
                )

                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertNotIn("D002", {item["code"] for item in findings})

    def test_fail_on_warning_returns_nonzero(self):
        result, findings = self.run_lint(
            """## S01 — Adoption rose during the pilot
- Placement: Core
利用率は35%へ上昇した。
""",
            "--check-sources",
            "--fail-on",
            "warning",
        )

        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("E001", {item["code"] for item in findings})


if __name__ == "__main__":
    unittest.main()

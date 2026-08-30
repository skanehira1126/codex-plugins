import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "lint_deck_outline.py"
STORYBOARD = Path(__file__).parents[1] / "assets" / "storyboard.md"


class LintDeckOutlineCliTests(unittest.TestCase):
    def run_lint_path(self, path, *arguments):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(path), "--json", *arguments],
            capture_output=True,
            check=False,
            text=True,
        )
        return result, json.loads(result.stdout)

    def run_lint(self, markdown, *arguments):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "deck.md"
            path.write_text(markdown, encoding="utf-8")
            return self.run_lint_path(path, *arguments)

    def test_bundled_storyboard_metadata_is_not_visible_content(self):
        result, findings = self.run_lint_path(STORYBOARD, "--check-sources")

        self.assertEqual(result.returncode, 0, result.stderr)
        codes = {item["code"] for item in findings}
        self.assertNotIn("D002", codes)
        self.assertNotIn("E001", codes)

    def test_deck_level_gate_section_is_not_part_of_preceding_slide(self):
        gates = "\n".join(f"- [ ] Gate {number}" for number in range(1, 11))
        result, findings = self.run_lint(
            f"""## S01 — The pilot should begin now
- Placement: Core

## Gate results
{gates}
""",
            "--check-sources",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        codes = {item["code"] for item in findings}
        self.assertNotIn("D002", codes)
        self.assertNotIn("E001", codes)

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

    def test_parenthetical_year_alone_is_not_treated_as_a_source(self):
        result, findings = self.run_lint(
            """## S01 — Adoption rose during the pilot
- Placement: Core
利用率は35%へ上昇した（2026年）。
""",
            "--check-sources",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("E001", {item["code"] for item in findings})

    def test_provisional_date_note_is_not_treated_as_a_source(self):
        result, findings = self.run_lint(
            """## S01 — Adoption rose during the pilot
- Placement: Core
利用率は35%へ上昇した（2026年8月の暫定集計）。
""",
            "--check-sources",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("E001", {item["code"] for item in findings})

    def test_source_placeholders_and_provisional_date_variants_are_not_sources(self):
        values = (
            "2026-08 provisional",
            "2026/08 暫定集計",
            "as of Aug 2026 preliminary",
            "速報値・未監査 2026年",
            "TBD.",
            "N.A.",
            "<!-- TODO -->",
            "未定。",
        )
        for value in values:
            with self.subTest(value=value):
                result, findings = self.run_lint(
                    f"## S01 — Adoption rose during the pilot\n- Placement: Core\n- Source: {value}\n利用率は35%へ上昇した。\n",
                    "--check-sources",
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("E001", {item["code"] for item in findings})

    def test_empty_source_field_does_not_consume_the_next_line(self):
        result, findings = self.run_lint(
            """## S01 — Adoption rose during the pilot
- Placement: Core
- Source:
利用率は35%へ上昇した。
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

    def test_storyboard_source_is_near_evidence_across_structural_metadata(self):
        result, findings = self.run_lint(
            """## S01 — Adoption rose during the pilot
- Placement: Core
- Decisive evidence: 利用率は35%へ上昇した
- Visual form: Chart
- Speaker beat: Explain the comparison
- Transition: Move to the decision
- Appendix link: A1
- Source: 2026年8月の社内利用ログ
""",
            "--check-sources",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("E001", {item["code"] for item in findings})

    def test_distant_source_does_not_cover_an_unrelated_numerical_claim(self):
        result, findings = self.run_lint(
            """## S01 — Adoption rose during the pilot
- Placement: Core
利用率は35%へ上昇した。

この段落は別の論点を説明する。

- Source: 2026年8月の人員台帳
""",
            "--check-sources",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("E001", {item["code"] for item in findings})

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

    def test_unknown_placement_is_reported_and_not_treated_as_core(self):
        bullets = "\n".join(f"- Detail {number}" for number in range(1, 10))
        result, findings = self.run_lint(
            f"""## X1 — Material awaiting classification
- Placement: Parking lot
{bullets}
"""
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        codes = {item["code"] for item in findings}
        self.assertIn("P002", codes)
        self.assertNotIn("D002", codes)

    def test_multiple_placements_are_rejected(self):
        result, findings = self.run_lint(
            """## S01 — Material awaiting one destination
- Placement: Core / Appendix
"""
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("P002", {item["code"] for item in findings})

    def test_claim_metadata_counts_toward_core_density(self):
        result, findings = self.run_lint(
            f"""## S01 — One message supported by too much visible evidence
- Placement: Core
- Decisive evidence: {'A' * 1300}
"""
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("D001", {item["code"] for item in findings})

    def test_early_ask_check_applies_only_to_decision_and_proposal_modes(self):
        result, findings = self.run_lint(
            """## S01 — Task context for the pilot
- Placement: Core
The team has reviewed the implementation details.
""",
            "--mode",
            "decision",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("C001", {item["code"] for item in findings})

        result, findings = self.run_lint(
            """## S01 — Sprint status is stable
- Placement: Core
The team completed the planned scope and has no blockers.
""",
            "--mode",
            "status",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("C001", {item["code"] for item in findings})

    def test_recommendation_noun_satisfies_early_ask_check(self):
        result, findings = self.run_lint(
            """## S01 — Our recommendation is an eight-week pilot
- Placement: Core
The pilot keeps the decision reversible.
""",
            "--mode",
            "decision",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("C001", {item["code"] for item in findings})

    def test_negated_english_recommendation_does_not_satisfy_early_ask(self):
        result, findings = self.run_lint(
            """## S01 — Pilot assessment
- Placement: Core
We cannot recommend adoption yet.
""",
            "--mode",
            "decision",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("C001", {item["code"] for item in findings})

    def test_undecided_japanese_action_does_not_satisfy_early_ask(self):
        result, findings = self.run_lint(
            """## S01 — 試行の評価
- Placement: Core
パイロットを実施するかは未定である。
""",
            "--mode",
            "decision",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("C001", {item["code"] for item in findings})

    def test_negative_recommendations_and_prohibitions_are_explicit_asks(self):
        cases = (
            "Do not launch the pilot.",
            "We recommend not launching the pilot.",
            "パイロットを中止する。",
        )
        for body in cases:
            with self.subTest(body=body):
                result, findings = self.run_lint(
                    f"## S01 — Pilot decision\n- Placement: Core\n{body}\n",
                    "--mode",
                    "decision",
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertNotIn("C001", {item["code"] for item in findings})

    def test_japanese_planned_inactivity_is_not_an_explicit_ask(self):
        result, findings = self.run_lint(
            "## S01 — 試行の評価\n- Placement: Core\nパイロットを実施する予定はない。\n",
            "--mode",
            "decision",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("C001", {item["code"] for item in findings})

    def test_absent_english_recommendation_decision_or_approval_is_not_an_ask(self):
        cases = (
            "There is no recommendation yet.",
            "The team does not recommend adoption.",
            "No decision has been made.",
            "We are not asking for approval.",
        )
        for body in cases:
            with self.subTest(body=body):
                result, findings = self.run_lint(
                    f"## S01 — Pilot assessment\n- Placement: Core\n{body}\n",
                    "--mode",
                    "decision",
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("C001", {item["code"] for item in findings})

    def test_appendix_id_and_ordered_list_marker_are_not_numerical_claims(self):
        result, findings = self.run_lint(
            """## S01 — The supporting detail is easy to retrieve
- Placement: Core
1. See Appendix A1 for the method.
""",
            "--check-sources",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("E001", {item["code"] for item in findings})

    def test_japanese_action_term_does_not_match_a_longer_noun(self):
        result, findings = self.run_lint(
            """## S01 — 承認者と実施状況を確認する
- Placement: Core
担当者一覧を共有する。
""",
            "--mode",
            "decision",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("C001", {item["code"] for item in findings})

    def test_explicit_japanese_action_satisfies_early_ask_check(self):
        result, findings = self.run_lint(
            """## S01 — パイロットの開始を承認する
- Placement: Core
8週間の試行を提案する。
""",
            "--mode",
            "decision",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("C001", {item["code"] for item in findings})

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

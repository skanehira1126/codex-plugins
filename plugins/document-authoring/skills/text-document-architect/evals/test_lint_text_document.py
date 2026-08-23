import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "lint_text_document.py"
SAMPLE_GOOD_OUTLINE = Path(__file__).parent / "sample-good-outline.md"


class LintTextDocumentCliTests(unittest.TestCase):
    def run_lint(self, markdown, *arguments):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "document.md"
            path.write_text(markdown, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(path), "--json", *arguments],
                capture_output=True,
                check=False,
                text=True,
            )
        return result, json.loads(result.stdout)

    def test_bundled_good_outline_has_no_findings(self):
        result, findings = self.run_lint(
            SAMPLE_GOOD_OUTLINE.read_text(encoding="utf-8"),
            "--mode",
            "decision",
            "--出典確認",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(findings, [])

    def test_generic_research_word_is_not_treated_as_a_source(self):
        result, findings = self.run_lint(
            """# 利用率は試行期間中に上昇した
調査の結果、利用率は35%へ上昇した。
""",
            "--出典確認",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("E001", {item["code"] for item in findings})

    def test_populated_source_field_satisfies_source_check(self):
        result, findings = self.run_lint(
            """# 利用率は試行期間中に上昇した
利用率は35%へ上昇した。
- 出典: 2026年8月の社内利用ログ
""",
            "--出典確認",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("E001", {item["code"] for item in findings})

    def test_inline_source_label_satisfies_source_check(self):
        result, findings = self.run_lint(
            """# 利用率は試行期間中に上昇した
利用率は35%へ上昇した。出典：2026年8月の社内利用ログ。
""",
            "--出典確認",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("E001", {item["code"] for item in findings})

    def test_year_only_parentheses_do_not_satisfy_source_check(self):
        result, findings = self.run_lint(
            """# 利用率は試行期間中に上昇した
利用率は35%へ上昇した（2026年）。
""",
            "--出典確認",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("E001", {item["code"] for item in findings})

    def test_provisional_date_note_does_not_satisfy_source_check(self):
        result, findings = self.run_lint(
            """# 利用率は試行期間中に上昇した
利用率は35%へ上昇した（2026年8月の暫定集計）。
""",
            "--出典確認",
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
                    f"# 利用率は試行期間中に上昇した\n利用率は35%へ上昇した。出典: {value}\n",
                    "--出典確認",
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("E001", {item["code"] for item in findings})

    def test_named_parenthetical_citation_satisfies_source_check(self):
        result, findings = self.run_lint(
            """# 利用率は試行期間中に上昇した
利用率は35%へ上昇した（業務改革部 2026）。
""",
            "--出典確認",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("E001", {item["code"] for item in findings})

    def test_empty_source_field_does_not_consume_the_next_line(self):
        result, findings = self.run_lint(
            """# 利用率は試行期間中に上昇した
利用率は35%へ上昇した。
- 出典:
2026年8月の社内利用ログ
""",
            "--出典確認",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("E001", {item["code"] for item in findings})

    def test_adjacent_standalone_source_satisfies_source_check(self):
        result, findings = self.run_lint(
            """# 利用率は試行期間中に上昇した
利用率は35%へ上昇した。

出典: 2026年8月の社内利用ログ
""",
            "--出典確認",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("E001", {item["code"] for item in findings})

    def test_distant_source_for_another_claim_does_not_satisfy_source_check(self):
        result, findings = self.run_lint(
            """# 二つの利用率を比較した
A部署の利用率は35%だった。

対象期間と母数は部署ごとに異なる。

B部署の利用率は42%だった。出典: B部署の利用ログ。
""",
            "--出典確認",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("E001", {item["code"] for item in findings})

    def test_source_before_table_does_not_cover_a_later_unrelated_claim(self):
        result, findings = self.run_lint(
            """# 部署別の利用率を確認した
出典: A部署ログ

| 部署 | 利用率 |
| --- | ---: |
| A | 35% |

無関係なB部署の利用率は42%だった。
""",
            "--出典確認",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("E001", {item["code"] for item in findings})

    def test_negated_decision_does_not_satisfy_the_early_ask(self):
        result, findings = self.run_lint(
            """# 試行結果は判断材料として不十分だった
## 現時点では採用可否を確定できない
採用を判断できない理由を整理する。
""",
            "--mode",
            "decision",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("D001", {item["code"] for item in findings})

    def test_late_action_does_not_satisfy_the_early_ask(self):
        result, findings = self.run_lint(
            """# 試行結果の評価
## 観測された変化
利用状況の変化を整理する。

## 解釈上の制約
対象部署の偏りを確認する。

## 最終ページの依頼
試行の継続を承認してください。
""",
            "--mode",
            "decision",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("D001", {item["code"] for item in findings})

    def test_owner_alone_does_not_satisfy_the_early_ask(self):
        result, findings = self.run_lint(
            """# 試行結果の評価
## 体制案
責任者は業務改革部とする。
""",
            "--mode",
            "decision",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("D001", {item["code"] for item in findings})

    def test_negated_english_recommendation_does_not_satisfy_early_ask(self):
        result, findings = self.run_lint(
            """# Pilot assessment
We cannot recommend adoption yet.
""",
            "--mode",
            "decision",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("D001", {item["code"] for item in findings})

    def test_undecided_japanese_action_does_not_satisfy_early_ask(self):
        result, findings = self.run_lint(
            """# 試行の評価
パイロットを実施するかは未定である。
""",
            "--mode",
            "decision",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("D001", {item["code"] for item in findings})

    def test_negative_recommendations_and_prohibitions_are_explicit_asks(self):
        cases = (
            "Do not launch the pilot.",
            "We recommend not launching the pilot.",
            "パイロットを中止する。",
        )
        for body in cases:
            with self.subTest(body=body):
                result, findings = self.run_lint(f"# Pilot decision\n{body}\n", "--mode", "decision")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertNotIn("D001", {item["code"] for item in findings})

    def test_japanese_planned_inactivity_is_not_an_explicit_ask(self):
        result, findings = self.run_lint(
            "# 試行の評価\nパイロットを実施する予定はない。\n",
            "--mode",
            "decision",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("D001", {item["code"] for item in findings})

    def test_absent_english_recommendation_or_approval_is_not_an_ask(self):
        cases = (
            "There is no recommendation yet.",
            "The team does not recommend adoption.",
            "No decision has been made.",
            "We are not asking for approval.",
        )
        for body in cases:
            with self.subTest(body=body):
                result, findings = self.run_lint(f"# Pilot assessment\n{body}\n", "--mode", "decision")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("D001", {item["code"] for item in findings})

    def test_outline_markers_and_appendix_ids_are_not_numerical_claims(self):
        result, findings = self.run_lint(
            """# 判断理由
1. 第一の理由を確認する。
詳細はAppendix A1を参照する。
""",
            "--出典確認",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("E001", {item["code"] for item in findings})

    def test_non_prose_blocks_are_excluded_from_long_paragraph_check(self):
        long_text = "長" * 950
        cases = {
            "table": f"# 比較表\n| 項目 | 説明 |\n| --- | --- |\n| A | {long_text} |\n",
            "fenced-code": f"# 設定例\n```text\n{long_text}\n```\n",
            "metadata": f"# 読者動作\n- 根拠: {long_text}\n",
        }

        for name, markdown in cases.items():
            with self.subTest(name=name):
                result, findings = self.run_lint(markdown)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertNotIn("S002", {item["code"] for item in findings})

    def test_long_prose_paragraph_still_reports_s002(self):
        result, findings = self.run_lint(f"# 詳細な説明\n{'A' * 901}\n")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("S002", {item["code"] for item in findings})

    def test_well_formed_decision_document_has_no_findings(self):
        result, findings = self.run_lint(
            """# 三部署での試行導入を承認してください
## 利用率の上昇が限定導入を支持する
利用率は35%へ上昇した。
- 出典: 2026年8月の社内利用ログ

## 導入条件を責任者と期限で固定する
責任者は業務改革部、開始日は承認後の翌月初日とする。
""",
            "--mode",
            "decision",
            "--出典確認",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(findings, [])

    def test_representative_bad_case_reports_expected_codes(self):
        result, findings = self.run_lint(
            """# 調査報告
## 概要
調査の結果、利用率は35%へ上昇した。
- 認知動作: Explain

## 課題
現時点の制約を列挙する。
- 認知動作: Explain

## 原因
観測された背景を説明する。
- 認知動作: Explain
""",
            "--mode",
            "decision",
            "--出典確認",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        codes = {item["code"] for item in findings}
        self.assertTrue({"H001", "E001", "D001", "R001"}.issubset(codes))

    def test_fail_on_warning_returns_nonzero(self):
        result, findings = self.run_lint(
            """# 利用率は試行期間中に上昇した
利用率は35%へ上昇した。
""",
            "--出典確認",
            "--fail-on",
            "warning",
        )

        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("E001", {item["code"] for item in findings})


if __name__ == "__main__":
    unittest.main()

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "lint_text_document.py"


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

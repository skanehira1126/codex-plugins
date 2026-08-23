#!/usr/bin/env python3
"""Markdownのテキスト文書・読者動作アウトラインを検査する。

論理の復元コストや「高密度のっぺり」につながりやすい構造を、
ヒューリスティックに指摘する。内容の真偽、論証の妥当性、最終的な
編集判断を自動的に証明するものではない。

例:
    python lint_text_document.py report.md --mode sequential
    python lint_text_document.py outline.md --モード 連続読解 --json
    python lint_text_document.py policy.md --モード 参照 --出典確認
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


汎用見出し = {
    "背景", "概要", "目的", "現状", "課題", "問題", "原因", "施策", "対応策",
    "解決策", "提案", "まとめ", "結論", "考察", "今後", "今後の展望",
    "今後の方向性", "次のステップ", "ロードマップ", "効果", "メリット",
    "デメリット", "リスク", "補足", "参考", "付録", "はじめに", "序論",
    "background", "overview", "purpose", "current state", "challenges",
    "problems", "causes", "solution", "proposal", "summary", "conclusion",
    "discussion", "next steps", "roadmap", "benefits", "risks", "appendix",
    "introduction",
}

文章実況 = (
    "次に説明します", "以下で説明します", "ここまで見てきたように", "本節では",
    "本章では", "これから説明", "順に説明します", "次に見ていきます",
    "as discussed above", "in this section we will", "the next section explains",
    "we will now discuss",
)

抽象語 = (
    "重要", "高度化", "最適化", "強化", "推進", "連携", "活用", "整備", "検討",
    "価値向上", "効率化", "変革", "改善", "充実", "適切", "効果的", "期待",
    "実現", "促進", "最大化", "包括的", "戦略的",
    "important", "optimize", "optimization", "enhance", "strengthen", "leverage",
    "alignment", "transformation", "improve", "effective", "appropriate",
)

関係語 = (
    "ため", "ので", "しかし", "一方", "したがって", "つまり", "結果", "対して",
    "先に", "後に", "優先", "依存", "原因", "派生", "代替", "比較",
    "because", "therefore", "however", "whereas", "as a result", "in contrast",
)

明示的行動パターン = re.compile(
    r"(?:承認|判断|決定)(?:してほしい|してください|を求める|する)"
    r"|求める判断"
    r"|(?:優先|実施|採用|停止|開始|投資|配分|試行|継続|中止)(?:する|します|してください)"
    r"|(?:優先|実施|採用|停止|開始|投資|配分|試行|継続|中止)を(?:承認|決定)"
    r"|(?:責任者|担当者)\s*(?:[:：]|は)"
    r"|\b(?:recommend(?:ed|ation)?|approve|decide|prioritize|implement|launch|owner)\b",
    re.IGNORECASE,
)

出典パターン = (
    re.compile(r"https?://\S+", re.IGNORECASE),
    re.compile(
        r"(?:\*\*|__)?(?:source|sources|出典|参照|引用|cite|citation|footnote|脚注|参考文献)"
        r"(?:\*\*|__)?\s*[:：]\s*\S+",
        re.IGNORECASE,
    ),
    re.compile(r"\[(?:\^)?[1-9]\d*\]"),
    re.compile(r"[（(][^（）()\n]*(?:19|20)\d{2}[a-z]?[^（）()\n]*[）)]", re.IGNORECASE),
)

メタデータキー = (
    "認知動作", "主な認知動作", "主な動き", "primary move", "move",
    "抽象度", "abstraction", "出典", "source", "根拠", "evidence",
    "配置", "placement", "次の章が続く理由", "transition",
)

認知動作パターン = re.compile(
    r"(?:primary\s+move|move|認知(?:的)?(?:な)?動作|主な認知動作|主な動き)\s*[:：]\s*"
    r"(orient|question|observe|explain|reframe|evaluate|decide|act|consolidate|"
    r"状況把握|方向づけ|問い|観察|説明|再解釈|評価|判断|行動|統合)",
    re.IGNORECASE,
)

認知動作別名 = {
    "orient": "orient", "状況把握": "orient", "方向づけ": "orient",
    "question": "question", "問い": "question",
    "observe": "observe", "観察": "observe",
    "explain": "explain", "説明": "explain",
    "reframe": "reframe", "再解釈": "reframe",
    "evaluate": "evaluate", "評価": "evaluate",
    "decide": "decide", "判断": "decide",
    "act": "act", "行動": "act",
    "consolidate": "consolidate", "統合": "consolidate",
}

モード別名 = {
    "sequential": "sequential", "連続": "sequential", "連続読解": "sequential",
    "解説": "sequential", "学習": "sequential",
    "reference": "reference", "参照": "reference", "規程": "reference",
    "仕様": "reference", "マニュアル": "reference",
    "decision": "decision", "意思決定": "decision", "稟議": "decision",
    "役員": "decision",
}

失敗レベル別名 = {
    "never": "never", "なし": "never",
    "info": "info", "情報": "info",
    "warning": "warning", "警告": "warning",
    "error": "error", "エラー": "error",
}

重要度表示 = {"info": "情報", "warning": "警告", "error": "エラー"}
説明系動作 = {"explain"}


@dataclass(frozen=True)
class 指摘:
    severity: str
    code: str
    line: int
    heading: str
    message: str
    suggestion: str


@dataclass
class セクション:
    level: int
    title: str
    line: int
    body_lines: list[str]

    @property
    def body(self) -> str:
        return "\n".join(self.body_lines).strip()


def 正規化(text: str) -> str:
    text = re.sub(r"[`*_~]", "", text).strip().lower()
    text = re.sub(r"^[\d０-９]+[.．):：\-]\s*", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip(" .。:：-—–")


def Markdown解析(text: str) -> list[セクション]:
    sections: list[セクション] = []
    current: セクション | None = None
    in_fence = False

    for line_no, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            if current is not None:
                current.body_lines.append(raw)
            continue

        match = None if in_fence else re.match(r"^(#{1,6})\s+(.+?)\s*$", raw)
        if match:
            current = セクション(len(match.group(1)), match.group(2).strip(), line_no, [])
            sections.append(current)
        elif current is not None:
            current.body_lines.append(raw)

    return sections


def いずれかを含む(text: str, terms: Iterable[str]) -> bool:
    lower = text.lower()
    return any(term.lower() in lower for term in terms)


def 出典参照あり(text: str) -> bool:
    return any(pattern.search(text) for pattern in 出典パターン)


def 認知動作を抽出(section: セクション) -> str | None:
    match = 認知動作パターン.search(section.body)
    if not match:
        return None
    raw = match.group(1).lower()
    return 認知動作別名.get(raw, 認知動作別名.get(match.group(1)))


def メタデータ行(line: str) -> bool:
    joined = "|".join(re.escape(key) for key in メタデータキー)
    return bool(re.match(rf"^\s*[-*+]\s*(?:{joined})\s*[:：]", line, re.IGNORECASE))


def 検査(text: str, mode: str, 出典確認: bool) -> list[指摘]:
    sections = Markdown解析(text)
    findings: list[指摘] = []

    if not sections:
        return [指摘(
            "error", "DOC001", 1, "",
            "Markdown見出しが見つからないため、文書構造を検査できません。",
            "文書タイトルと、メッセージまたは検索手掛かりを持つ章見出しを追加してください。",
        )]

    seen: dict[str, int] = {}
    previous_level: int | None = None
    moves: list[tuple[str, セクション]] = []

    for section in sections:
        title = 正規化(section.title)
        body = section.body
        nonempty = [line for line in section.body_lines if line.strip()]
        bullets = [
            line for line in nonempty
            if re.match(r"^\s*[-*+]\s+", line) and not メタデータ行(line)
        ]

        if title in seen:
            findings.append(指摘(
                "warning", "H002", section.line, section.title,
                f"正規化した見出しが{seen[title]}行目と重複しています。",
                "章を統合するか、それぞれの異なる役割を見出しで明示してください。",
            ))
        else:
            seen[title] = section.line

        if previous_level is not None and section.level > previous_level + 1:
            findings.append(指摘(
                "warning", "H003", section.line, section.title,
                f"見出し階層がレベル{previous_level}から{section.level}へ飛んでいます。",
                "一貫した見出し階層へ戻してください。",
            ))
        previous_level = section.level

        if title in 汎用見出し and section.level <= 3:
            findings.append(指摘(
                "warning", "H001", section.line, section.title,
                "見出しが、メッセージや検索手掛かりではなく、汎用的な話題ラベルになっています。",
                "結論、問い、対比、作業、具体的な参照ラベルとして書き換えてください。",
            ))

        if len(section.title) > 110:
            findings.append(指摘(
                "info", "H004", section.line, section.title,
                "見出しが長く、走査しにくい可能性があります。",
                "中心メッセージだけを残し、条件や但し書きは冒頭文へ移してください。",
            ))

        if len(bullets) >= 5 and len(bullets) >= max(1, int(len(nonempty) * 0.55)):
            if not いずれかを含む(body, 関係語):
                findings.append(指摘(
                    "warning", "S001", section.line, section.title,
                    "箇条書きの壁が、優先順位、因果、順序、依存関係を隠している可能性があります。",
                    "関係を解釈する一文を追加するか、関係を表現できる構造へ変えてください。",
                ))

        paragraphs = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
        if any(len(p) > 900 for p in paragraphs):
            findings.append(指摘(
                "warning", "S002", section.line, section.title,
                "走査性とワーキングメモリを圧迫するほど長い段落があります。",
                "推論の段階ごとに分け、必要に応じて具体例または統合を挟んでください。",
            ))

        if len(body) > 2200:
            findings.append(指摘(
                "info", "S003", section.line, section.title,
                "一つの章に複数の読者質問が隠れている可能性があります。",
                "問い、根拠、含意の単位で分割すべきか確認してください。",
            ))

        if いずれかを含む(body, 文章実況):
            findings.append(指摘(
                "info", "L001", section.line, section.title,
                "読者の方向づけを増やさない文章の実況が含まれています。",
                "削除するか、アイデア間の関係を示す文へ書き換えてください。",
            ))

        for sentence in [s.strip() for s in re.split(r"[。！？!?\n]+", body) if s.strip()]:
            vague_count = sum(1 for term in 抽象語 if term.lower() in sentence.lower())
            concrete = bool(re.search(
                r"\d|%|％|[A-Z]{2,}|[一-龥]{2,}(部|課|室|社|人|件|日|週|月|年)",
                sentence,
            ))
            if vague_count >= 3 and not concrete:
                findings.append(指摘(
                    "info", "L002", section.line, section.title,
                    "具体的な足場なしに、抽象的な行動語が重なっています。",
                    "主体、変更内容、代替案、根拠、結果のいずれかを具体化してください。",
                ))
                break

        if 出典確認:
            has_number = bool(re.search(
                r"\d+(?:[.,]\d+)?\s*(?:%|％|人|件|円|日|週|月|年|倍|部署|営業日)?",
                body,
            ))
            if has_number and not 出典参照あり(body):
                findings.append(指摘(
                    "warning", "E001", section.line, section.title,
                    "数値主張の近くに明確な出典マーカーがありません。",
                    "出典、日付、範囲、分母、指標定義を追加するか、提案条件・暫定値・仮定と明示してください。",
                ))

        move = 認知動作を抽出(section)
        if move:
            moves.append((move, section))

    if mode in {"sequential", "decision"} and len(moves) >= 3:
        for idx in range(len(moves) - 2):
            run = moves[idx:idx + 3]
            if all(move in 説明系動作 for move, _ in run):
                section = run[0][1]
                findings.append(指摘(
                    "warning", "R001", section.line, section.title,
                    "アウトライン上で、説明だけを主な認知動作とする章が3つ連続しています。",
                    "観察、比較、再解釈、適用、判断、統合のいずれかを挟んでください。",
                ))
                break

    early_text = "\n".join(section.title + "\n" + section.body for section in sections[:3])
    if mode == "decision" and not 明示的行動パターン.search(early_text):
        findings.append(指摘(
            "warning", "D001", 1, "",
            "意思決定文書に、明確な推奨、判断、責任者、行動を示す語が見当たりません。",
            "読者が行う正確な判断・行動を明示し、早い段階に置いてください。",
        ))

    if mode == "reference" and text.count("?") + text.count("？") > 8:
        findings.append(指摘(
            "info", "R002", 1, "",
            "参照型文書で修辞疑問が多用されています。",
            "サスペンスより、予測可能なラベル、定義、作業別ナビゲーションを優先してください。",
        ))

    return findings


def 重要度順位(value: str) -> int:
    return {"info": 1, "warning": 2, "error": 3}[value]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="検査するMarkdownファイル")
    parser.add_argument(
        "--mode", "--モード", default="sequential",
        help="sequential / reference / decision、または 連続読解 / 参照 / 意思決定",
    )
    parser.add_argument(
        "--check-sources", "--出典確認", action="store_true",
        help="数値主張の近くに出典マーカーがあるか検査する",
    )
    parser.add_argument("--json", action="store_true", help="JSONで出力する")
    parser.add_argument(
        "--fail-on", "--失敗レベル", default="never",
        help="never / info / warning / error、または なし / 情報 / 警告 / エラー",
    )
    args = parser.parse_args()

    mode = モード別名.get(args.mode.lower(), モード別名.get(args.mode))
    if mode is None:
        parser.error(f"未知のモードです: {args.mode}")

    fail_on = 失敗レベル別名.get(args.fail_on.lower(), 失敗レベル別名.get(args.fail_on))
    if fail_on is None:
        parser.error(f"未知の失敗レベルです: {args.fail_on}")

    try:
        text = args.path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"エラー: {exc}", file=sys.stderr)
        return 2

    findings = 検査(text, mode, args.check_sources)

    if args.json:
        print(json.dumps([asdict(item) for item in findings], ensure_ascii=False, indent=2))
    else:
        if not findings:
            print("ヒューリスティックな指摘はありません。")
        for item in findings:
            location = f"{item.line}行目" if item.line else "文書全体"
            heading = f" [{item.heading}]" if item.heading else ""
            print(f"{重要度表示[item.severity]} {item.code} {location}{heading}: {item.message}")
            print(f"  → {item.suggestion}")

    if fail_on == "never":
        return 0
    threshold = 重要度順位(fail_on)
    return 1 if any(重要度順位(item.severity) >= threshold for item in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Heuristic linter for structured Markdown presentation storyboards.

Expected slide headings look like:
    ## S01 — Message title
    ## A1 — Appendix answer

Metadata lines may include Placement, Cognitive move, Visual form, Trigger
question, Time weight, Source, and Appendix link. The linter is deliberately
heuristic and does not replace editorial, visual, or factual review.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

GENERIC_TITLES = {
    "背景", "概要", "目的", "現状", "課題", "問題", "原因", "施策", "対応策",
    "解決策", "提案", "まとめ", "結論", "考察", "今後", "ロードマップ",
    "次のステップ", "補足", "参考", "付録", "appendix", "agenda", "overview",
    "background", "challenges", "solution", "proposal", "summary", "conclusion",
    "next steps", "roadmap", "details", "reference",
}

SOURCE_KEYS = ("Source", "Sources", "出典", "参照", "引用", "Cite", "Citation")
METADATA_KEYS = (
    "Placement", "配置", "Destination", "区分",
    "Audience question", "質問", "Cognitive move", "Move", "認知動作", "主な動き",
    "Time weight", "Decisive evidence", "Visual form", "Visual", "表現形式", "ビジュアル",
    "Speaker beat", "Transition", "Likely Q&A", "Appendix link",
    "Trigger question", "想定質問", "Core link", "Answer/message", "Evidence/detail",
    "Presenter guidance", *SOURCE_KEYS,
)
CLAIM_METADATA_KEYS = {"decisive evidence", "answer/message", "evidence/detail"}
JAPANESE_ACTION_TERMS = (
    "承認", "判断", "決定", "優先", "実施", "採用", "停止", "開始", "投資", "配分",
    "試行", "継続", "中止",
)
ENGLISH_ACTION_TERMS = (
    r"recommend(?:ed|ation)?", r"approv(?:e|ed|al)", r"decid(?:e|ed)", "decision",
    r"prioriti[sz](?:e|ed)", r"implement(?:ed)?", r"launch(?:ed)?", "ask",
)
NON_SOURCE_QUALIFIERS = {
    "暫定", "暫定値", "暫定集計", "暫定集計値", "速報", "速報値",
    "推計", "推計値", "概算", "概算値", "見込み", "予定", "未監査",
    "provisional", "preliminary", "estimate", "estimated", "draft", "unaudited",
}
SOURCE_PLACEHOLDERS = {
    "n/a", "na", "none", "tbd", "todo", "unknown", "pending",
    "不明", "未定", "未記入", "なし",
}
ENGLISH_MONTH_PATTERN = re.compile(
    r"\b(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|"
    r"jul(?:y)?|aug(?:ust)?|sep(?:tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\b",
    re.IGNORECASE,
)
CRITICAL_TERMS = (
    "重大", "致命", "結論を変", "前提", "主要な制約", "material risk", "critical risk",
    "changes the conclusion", "required assumption", "重大なリスク",
)
EXPLAIN_MOVES = {"explain", "説明", "observe", "観察"}


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    line: int
    slide: str
    message: str
    suggestion: str


@dataclass
class Slide:
    slide_id: str
    title: str
    line: int
    body_lines: list[str]

    @property
    def body(self) -> str:
        return "\n".join(self.body_lines).strip()


def normalize(text: str) -> str:
    text = re.sub(r"[`*_~]", "", text).strip().lower()
    text = re.sub(r"^[saｓａ]?\d+[\s|｜:：.．\-—–]*", "", text)
    return re.sub(r"\s+", " ", text).strip(" .。:：-—–")


def parse_slides(text: str) -> list[Slide]:
    slides: list[Slide] = []
    current: Slide | None = None
    in_fence = False
    pattern = re.compile(r"^#{2,3}\s+([A-Za-zＡ-Ｚａ-ｚ]?\d+)\s*[|｜:：.．\-—–]+\s*(.+?)\s*$")
    for line_no, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            if current is not None:
                current.body_lines.append(raw)
            continue
        match = None if in_fence else pattern.match(raw)
        if match:
            slide_id = unicodedata.normalize("NFKC", match.group(1)).upper()
            current = Slide(slide_id, match.group(2).strip(), line_no, [])
            slides.append(current)
        elif not in_fence and re.match(r"^#{2,3}\s+", raw):
            # A deck-level section such as "Gate results" is not part of the
            # preceding slide's visible content or source context.
            current = None
        elif current is not None:
            current.body_lines.append(raw)
    return slides


def metadata(body: str, keys: Iterable[str]) -> str | None:
    joined = "|".join(re.escape(key) for key in keys)
    match = re.search(rf"^\s*[-*]?\s*(?:{joined})\s*[:：]\s*(.+?)\s*$", body, re.IGNORECASE | re.MULTILINE)
    return match.group(1).strip() if match else None


def contains_any(text: str, terms: Iterable[str]) -> bool:
    lower = text.lower()
    return any(term.lower() in lower for term in terms)


def metadata_entry(line: str) -> tuple[str, str] | None:
    labels = "|".join(re.escape(key) for key in METADATA_KEYS)
    match = re.match(
        rf"^\s*[-*]?\s*({labels})\s*[:：][ \t]*(.*?)\s*$",
        line,
        re.IGNORECASE,
    )
    if not match:
        return None
    return match.group(1).strip().lower(), match.group(2).strip()


def meaningful_source_value(value: str) -> bool:
    cleaned = re.sub(r"<!--.*?-->", "", value, flags=re.DOTALL)
    cleaned = re.sub(r"[`*_~<>]", "", cleaned).strip()
    compact = re.sub(r"[^0-9A-Za-z\u3040-\u30ff\u3400-\u9fff]+", "", cleaned).lower()
    normalized_placeholders = {
        re.sub(r"[^0-9A-Za-z\u3040-\u30ff\u3400-\u9fff]+", "", item).lower()
        for item in SOURCE_PLACEHOLDERS
    }
    if not cleaned or compact in normalized_placeholders:
        return False
    if re.search(r"https?://\S+", cleaned, re.IGNORECASE):
        return True
    if re.search(r"\[(?:\^)?[1-9]\d*\]", cleaned):
        return True
    without_dates = re.sub(
        r"(?:19|20)\d{2}(?:[-/.]\d{1,2}(?:[-/.]\d{1,2})?|年(?:\d{1,2}月(?:\d{1,2}日)?)?)?"
        r"|\d{1,2}(?:月|日)|\d{1,2}[-/.]\d{1,2}",
        "",
        cleaned,
    )
    without_dates = ENGLISH_MONTH_PATTERN.sub("", without_dates)
    without_dates = re.sub(r"\bas\s+of\b", "", without_dates, flags=re.IGNORECASE)
    for qualifier in sorted(NON_SOURCE_QUALIFIERS, key=len, reverse=True):
        without_dates = re.sub(re.escape(qualifier), "", without_dates, flags=re.IGNORECASE)
    without_dates = re.sub(r"[\s,.;:：、。()（）\[\]{}\-–—_/〜~]+", "", without_dates)
    without_dates = re.sub(r"[・]", "", without_dates)
    without_dates = re.sub(r"^(?:の|時点)+", "", without_dates, flags=re.IGNORECASE)
    return bool(re.search(r"[A-Za-z\u3040-\u30ff\u3400-\u9fff]", without_dates))


def has_inline_source_reference(line: str) -> bool:
    if re.search(r"https?://\S+", line, re.IGNORECASE):
        return True
    if re.search(r"\[(?:\^)?[1-9]\d*\]", line):
        return True
    entry = metadata_entry(line)
    if entry and entry[0] in {key.lower() for key in SOURCE_KEYS}:
        return meaningful_source_value(entry[1])
    for match in re.finditer(r"[（(]([^（）()\n]+)[）)]", line):
        value = match.group(1)
        if re.search(r"(?:19|20)\d{2}[a-z]?", value, re.IGNORECASE) and meaningful_source_value(value):
            return True
    return False


def numerical_claim_lines(slide: Slide) -> list[int]:
    result: list[int] = []
    number_pattern = re.compile(r"(?<![A-Za-z#\d])\d+(?:[.,]\d+)?\s*(?:%|％|人|件|円|日|週|月|年|倍)?")
    source_keys = {key.lower() for key in SOURCE_KEYS}
    for index, line in enumerate(slide.body_lines):
        entry = metadata_entry(line)
        if entry:
            key, value = entry
            if key in source_keys or key not in CLAIM_METADATA_KEYS:
                continue
            candidate = value
        else:
            candidate = line
        candidate = re.sub(r"^\s*\d+[.)．]\s+", "", candidate)
        if number_pattern.search(candidate):
            result.append(index)
    return result


def has_nearby_source(slide: Slide, claim_line: int) -> bool:
    source_keys = {key.lower() for key in SOURCE_KEYS}
    context_lines: list[int] = []
    for index, line in enumerate(slide.body_lines):
        entry = metadata_entry(line)
        if entry:
            if entry[0] in source_keys or entry[0] in CLAIM_METADATA_KEYS:
                context_lines.append(index)
        elif line.strip():
            context_lines.append(index)

    position = context_lines.index(claim_line)
    nearby = context_lines[max(0, position - 1):position + 2]
    return any(has_inline_source_reference(slide.body_lines[index]) for index in nearby)


def contains_action_term(text: str) -> bool:
    for term in JAPANESE_ACTION_TERMS:
        for match in re.finditer(
            rf"{re.escape(term)}(?=$|[\s:：、。をがへ]|する|します|してください|せよ)",
            text,
        ):
            after = text[match.end():match.end() + 24]
            if re.match(r"(?:する)?(?:か(?:どうか)?|必要|予定)?(?:は|が|を)?(?:未定|保留|見送|不要|ない|できない)", after):
                continue
            return True

    lower = text.lower()
    for term in ENGLISH_ACTION_TERMS:
        for match in re.finditer(rf"(?<![a-z])(?:{term})(?![a-z])", lower):
            before = lower[max(0, match.start() - 24):match.start()]
            after = lower[match.end():match.end() + 24]
            matched_term = match.group(0)
            if re.search(r"(?:cannot|can't|unable\s+to)\s+$", before):
                continue
            if (
                (matched_term.startswith("recommend") or matched_term == "decision")
                and re.search(r"(?:\bno|\b(?:do|does|did)\s+not|\bnot)\s+$", before)
            ):
                continue
            if matched_term == "approval" and re.search(r"(?:\bno|\bnot\s+asking\s+for)\s+$", before):
                continue
            if re.match(r"\s+(?:is|are)\s+(?:not|unknown|undecided|deferred|pending)\b", after):
                continue
            return True
    return False


def placement_kind(slide_id: str, placement: str | None) -> str:
    if placement:
        lower = re.sub(r"\s+", " ", placement.strip().lower())
        if lower in {"appendix", "backup", "付録", "参考", "予備"}:
            return "appendix"
        if lower in {"note", "notes", "speaker", "speaker note", "speaker notes", "ノート", "話者ノート"}:
            return "notes"
        if lower in {"omit", "remove", "削除", "除外"}:
            return "omit"
        if lower in {"core", "main deck", "本編"}:
            return "core"
        return "unknown"

    match = re.match(r"([A-Z]+)", slide_id)
    return "appendix" if match and match.group(1) != "S" else "core"


def lint(text: str, check_sources: bool, mode: str) -> list[Finding]:
    slides = parse_slides(text)
    findings: list[Finding] = []
    if not slides:
        return [Finding(
            "error", "DECK001", 1, "",
            "No structured slide headings were found.",
            "Use headings such as '## S01 — <message title>' and '## A1 — <appendix answer>'.",
        )]

    seen_titles: dict[str, int] = {}
    core: list[tuple[Slide, str | None, str | None]] = []
    appendix: list[Slide] = []

    for slide in slides:
        body = slide.body
        title = normalize(slide.title)
        placement = metadata(body, ("Placement", "配置", "Destination", "区分"))
        move = metadata(body, ("Cognitive move", "Move", "認知動作", "主な動き"))
        visual = metadata(body, ("Visual form", "Visual", "表現形式", "ビジュアル"))
        trigger = metadata(body, ("Trigger question", "想定質問", "Audience question", "質問"))
        visible_lines: list[str] = []
        for line in slide.body_lines:
            entry = metadata_entry(line)
            if entry is None:
                visible_lines.append(line)
            elif entry[0] in CLAIM_METADATA_KEYS and entry[1]:
                visible_lines.append(entry[1])
        visible_body = "\n".join(visible_lines).strip()
        bullets = [
            line for line in slide.body_lines
            if metadata_entry(line) is None and re.match(r"^\s*[-*+]\s+", line)
        ]

        if title in seen_titles:
            findings.append(Finding(
                "warning", "H002", slide.line, slide.slide_id,
                f"The title duplicates the title on line {seen_titles[title]}.",
                "Merge the slides or state their distinct messages.",
            ))
        else:
            seen_titles[title] = slide.line

        if title in GENERIC_TITLES:
            findings.append(Finding(
                "warning", "H001", slide.line, slide.slide_id,
                "The slide title is a generic topic label.",
                "Rewrite it as the answer, claim, contrast, decision, or specific question.",
            ))

        if len(slide.title) > 95:
            findings.append(Finding(
                "info", "H003", slide.line, slide.slide_id,
                "The title may be too long to scan at presentation distance.",
                "Keep the claim and move qualifiers into the body or note.",
            ))

        if placement is None:
            findings.append(Finding(
                "warning", "P001", slide.line, slide.slide_id,
                "The slide has no explicit Core/Notes/Appendix/Omit placement.",
                "Classify the content before visual production.",
            ))
        placement_type = placement_kind(slide.slide_id, placement)
        if placement_type == "unknown":
            findings.append(Finding(
                "warning", "P002", slide.line, slide.slide_id,
                f"The placement value '{placement}' is not recognized.",
                "Use Core, Notes, Appendix, or Omit explicitly; unknown values are not treated as core.",
            ))

        if placement_type == "appendix":
            appendix.append(slide)
            if not trigger:
                findings.append(Finding(
                    "warning", "A001", slide.line, slide.slide_id,
                    "The appendix slide has no trigger question.",
                    "State the plausible audience question or verification need it answers.",
                ))
            if title in {"appendix", "補足", "参考", "付録", "details", "reference"}:
                findings.append(Finding(
                    "warning", "A002", slide.line, slide.slide_id,
                    "The appendix title does not communicate an answer.",
                    "Use a question-answer or message-bearing title and a stable ID.",
                ))
            if contains_any(body, CRITICAL_TERMS):
                findings.append(Finding(
                    "warning", "A003", slide.line, slide.slide_id,
                    "The appendix may contain a material assumption or risk that belongs in the core deck.",
                    "Check whether this information could change the recommendation and promote it if so.",
                ))
        elif placement_type == "core":
            core.append((slide, move.lower() if move else None, visual.lower() if visual else None))

        if placement_type == "core" and len(visible_body) > 1250:
            findings.append(Finding(
                "warning", "D001", slide.line, slide.slide_id,
                "The core slide specification is dense enough to contain multiple messages.",
                "Reduce to decisive proof and move detail to notes or appendix.",
            ))

        if placement_type == "core" and len(bullets) > 8:
            findings.append(Finding(
                "warning", "D002", slide.line, slide.slide_id,
                "The core slide contains a bullet wall.",
                "Express the relationship visually or split secondary detail into appendix.",
            ))

        if check_sources:
            claim_lines = numerical_claim_lines(slide)
            if any(not has_nearby_source(slide, line) for line in claim_lines):
                findings.append(Finding(
                    "warning", "E001", slide.line, slide.slide_id,
                    "A numerical claim has no obvious nearby source.",
                    "Add source, date, scope, denominator, and metric definition or mark it provisional.",
                ))

    if mode in {"decision", "proposal", "status"} and core and not contains_action_term("\n".join(s.title + "\n" + s.body for s, _, _ in core[:3])):
        findings.append(Finding(
            "warning", "C001", core[0][0].line, core[0][0].slide_id,
            "The early core deck has no obvious recommendation, decision, or exact ask.",
            "Make the recommendation or audience action visible early when the deck is decision-oriented.",
        ))

    if len(core) >= 3:
        for idx in range(len(core) - 2):
            run = core[idx:idx + 3]
            moves = [move for _, move, _ in run]
            if all(move in EXPLAIN_MOVES for move in moves if move) and all(moves):
                first = run[0][0]
                findings.append(Finding(
                    "warning", "R001", first.line, first.slide_id,
                    "Three consecutive core slides use only Observe/Explain moves.",
                    "Add synthesis, reframe, comparison, implication, or decision.",
                ))
                break

        for idx in range(len(core) - 2):
            run = core[idx:idx + 3]
            visuals = [visual for _, _, visual in run]
            if visuals[0] and visuals[0] == visuals[1] == visuals[2] and visuals[0] in {"cards", "card", "three cards", "3 cards", "カード"}:
                first = run[0][0]
                findings.append(Finding(
                    "info", "R002", first.line, first.slide_id,
                    "Three consecutive core slides use the same card layout.",
                    "Confirm that the ideas are genuinely parallel; otherwise choose semantic forms.",
                ))
                break

    if not appendix:
        findings.append(Finding(
            "info", "A004", 1, "",
            "No appendix slides were detected.",
            "Confirm that predictable Q&A and verification needs are covered, or explicitly decide that no appendix is needed.",
        ))

    return findings


def severity_rank(value: str) -> int:
    return {"info": 1, "warning": 2, "error": 3}[value]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--mode", choices=("general", "decision", "proposal", "status"), default="general")
    parser.add_argument("--check-sources", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--fail-on", choices=("never", "info", "warning", "error"), default="never")
    args = parser.parse_args()

    try:
        text = args.path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    findings = lint(text, args.check_sources, args.mode)
    if args.json:
        print(json.dumps([asdict(item) for item in findings], ensure_ascii=False, indent=2))
    else:
        if not findings:
            print("No heuristic findings.")
        for item in findings:
            location = f"line {item.line}" if item.line else "deck"
            slide = f" [{item.slide}]" if item.slide else ""
            print(f"{item.severity.upper()} {item.code} {location}{slide}: {item.message}")
            print(f"  -> {item.suggestion}")

    if args.fail_on == "never":
        return 0
    threshold = severity_rank(args.fail_on)
    return 1 if any(severity_rank(item.severity) >= threshold for item in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Deterministic non-negotiable checks for tailored resume outputs."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Literal


Status = Literal["PASS", "FAIL"]


@dataclass
class CheckResult:
    name: str
    status: Status
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run deterministic non-negotiable checks on tailored resume LaTeX."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("Obaida_Kandakji.tex"),
        help="Source resume file used as baseline.",
    )
    parser.add_argument(
        "--candidate",
        type=Path,
        required=True,
        help="Tailored resume .tex file to validate.",
    )
    parser.add_argument(
        "--expected-projects",
        type=int,
        default=4,
        help="Expected number of active project headings.",
    )
    parser.add_argument(
        "--report",
        type=Path,
        help="Optional path to write a markdown lint report.",
    )
    return parser.parse_args()


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    return path.read_text(encoding="utf-8")


def strip_latex_comment(line: str) -> str:
    out: list[str] = []
    escaped = False
    for char in line:
        if char == "%" and not escaped:
            break
        out.append(char)
        escaped = (char == "\\") and not escaped
        if char != "\\":
            escaped = False
    return "".join(out)


def cleaned_lines(text: str) -> list[str]:
    return [strip_latex_comment(line) for line in text.splitlines()]


def section_names(lines: list[str]) -> list[str]:
    names: list[str] = []
    for line in lines:
        match = re.match(r"^\s*\\section\{([^}]+)\}", line)
        if match:
            names.append(match.group(1).strip())
    return names


def count_active_projects(lines: list[str]) -> int:
    section: str | None = None
    count = 0
    for line in lines:
        section_match = re.match(r"^\s*\\section\{([^}]+)\}", line)
        if section_match:
            section = section_match.group(1).strip()
            continue
        if section == "Projects" and r"\resumeProjectHeading" in line:
            count += 1
    return count


def bullet_signature(lines: list[str]) -> list[tuple[str, int]]:
    section: str | None = None
    active = False
    active_count = 0
    signature: list[tuple[str, int]] = []

    for line in lines:
        section_match = re.match(r"^\s*\\section\{([^}]+)\}", line)
        if section_match:
            if active and section in {"Projects", "Experience"}:
                signature.append((section, active_count))
            section = section_match.group(1).strip()
            active = False
            active_count = 0
            continue

        if section not in {"Projects", "Experience"}:
            continue

        is_heading = (
            (section == "Projects" and r"\resumeProjectHeading" in line)
            or (section == "Experience" and r"\resumeSubheading" in line)
        )

        if is_heading:
            if active:
                signature.append((section, active_count))
            active = True
            active_count = 0
            continue

        if active and r"\resumeItem{" in line:
            active_count += line.count(r"\resumeItem{")

    if active and section in {"Projects", "Experience"}:
        signature.append((section, active_count))

    return signature


def make_markdown(results: list[CheckResult], overall: Status) -> str:
    lines = ["# Non-Negotiable Lint Report", "", f"Overall: **{overall}**", ""]
    for result in results:
        lines.append(f"- `{result.name}`: **{result.status}** - {result.detail}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()

    source = args.source.resolve()
    candidate = args.candidate.resolve()

    try:
        source_text = read_text(source)
        candidate_text = read_text(candidate)
    except FileNotFoundError as err:
        print(str(err), file=sys.stderr)
        return 2

    source_lines = cleaned_lines(source_text)
    candidate_lines = cleaned_lines(candidate_text)

    results: list[CheckResult] = []

    src_sections = section_names(source_lines)
    dst_sections = section_names(candidate_lines)
    if src_sections == dst_sections:
        results.append(
            CheckResult("section_order", "PASS", "Section order is unchanged.")
        )
    else:
        results.append(
            CheckResult(
                "section_order",
                "FAIL",
                f"Section order changed. source={src_sections}, candidate={dst_sections}",
            )
        )

    project_count = count_active_projects(candidate_lines)
    if project_count == args.expected_projects:
        results.append(
            CheckResult(
                "active_projects",
                "PASS",
                f"Found {project_count} active project headings.",
            )
        )
    else:
        results.append(
            CheckResult(
                "active_projects",
                "FAIL",
                f"Found {project_count} active projects; expected {args.expected_projects}.",
            )
        )

    src_sig = bullet_signature(source_lines)
    dst_sig = bullet_signature(candidate_lines)
    if src_sig == dst_sig:
        results.append(
            CheckResult(
                "bullet_counts",
                "PASS",
                "Per-entry bullet counts in Projects/Experience are unchanged.",
            )
        )
    else:
        results.append(
            CheckResult(
                "bullet_counts",
                "FAIL",
                f"Bullet signatures differ. source={src_sig}, candidate={dst_sig}",
            )
        )

    em_dash_found = any(("—" in line or "---" in line) for line in candidate_lines)
    if em_dash_found:
        results.append(
            CheckResult("em_dash", "FAIL", "Detected em dash usage (`—` or `---`).")
        )
    else:
        results.append(
            CheckResult("em_dash", "PASS", "No em dash usage detected.")
        )

    any_fail = any(result.status == "FAIL" for result in results)
    overall: Status = "FAIL" if any_fail else "PASS"

    report = {
        "overall": overall,
        "checks": [result.__dict__ for result in results],
    }

    print(json.dumps(report, indent=2))

    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(make_markdown(results, overall), encoding="utf-8")

    return 0 if overall == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

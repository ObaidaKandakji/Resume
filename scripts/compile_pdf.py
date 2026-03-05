#!/usr/bin/env python3
"""Compile a LaTeX file into PDF with tool fallback."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compile LaTeX .tex file into PDF (latexmk -> pdflatex fallback)."
    )
    parser.add_argument(
        "--tex",
        required=True,
        type=Path,
        help="Path to .tex file.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional output PDF path. Defaults to <tex>.pdf.",
    )
    return parser.parse_args()


def run_cmd(cmd: list[str], cwd: Path) -> tuple[int, str]:
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return (proc.returncode, (proc.stdout + "\n" + proc.stderr).strip())


def find_tex_binary(name: str) -> str | None:
    from_path = shutil.which(name)
    if from_path:
        return from_path

    candidates = [
        Path("/Library/TeX/texbin") / name,
    ]

    texlive_root = Path("/usr/local/texlive")
    if texlive_root.exists():
        candidates.extend(texlive_root.glob(f"*/bin/*/{name}"))

    for candidate in candidates:
        if candidate.exists() and candidate.is_file():
            return str(candidate)

    return None


def compile_with_latexmk(tex_path: Path) -> tuple[bool, str]:
    latexmk = find_tex_binary("latexmk")
    if latexmk is None:
        return (False, "latexmk not found")
    code, output = run_cmd(
        [
            latexmk,
            "-pdf",
            "-interaction=nonstopmode",
            "-halt-on-error",
            tex_path.name,
        ],
        cwd=tex_path.parent,
    )
    if code == 0:
        return (True, "Compiled with latexmk")
    tail = " | ".join(output.splitlines()[-10:])
    return (False, f"latexmk failed: {tail}")


def compile_with_pdflatex(tex_path: Path) -> tuple[bool, str]:
    pdflatex = find_tex_binary("pdflatex")
    if pdflatex is None:
        return (False, "pdflatex not found")

    cmd = [
        pdflatex,
        "-interaction=nonstopmode",
        "-halt-on-error",
        tex_path.name,
    ]
    code1, output1 = run_cmd(cmd, cwd=tex_path.parent)
    if code1 != 0:
        tail = " | ".join(output1.splitlines()[-10:])
        return (False, f"pdflatex pass1 failed: {tail}")

    code2, output2 = run_cmd(cmd, cwd=tex_path.parent)
    if code2 != 0:
        tail = " | ".join(output2.splitlines()[-10:])
        return (False, f"pdflatex pass2 failed: {tail}")

    return (True, "Compiled with pdflatex")


def main() -> int:
    args = parse_args()
    tex_path = args.tex.resolve()
    if not tex_path.exists():
        print(f"Missing file: {tex_path}", file=sys.stderr)
        return 2
    if tex_path.suffix.lower() != ".tex":
        print(f"Expected .tex input, got: {tex_path}", file=sys.stderr)
        return 2

    ok, detail = compile_with_latexmk(tex_path)
    if not ok:
        ok, detail = compile_with_pdflatex(tex_path)
    if not ok:
        print(detail, file=sys.stderr)
        return 1

    generated_pdf = tex_path.with_suffix(".pdf")
    if not generated_pdf.exists():
        print("Compilation reported success but PDF was not found.", file=sys.stderr)
        return 1

    final_pdf = args.output.resolve() if args.output else generated_pdf
    if final_pdf != generated_pdf:
        final_pdf.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(generated_pdf, final_pdf)

    print(detail)
    print(f"PDF: {final_pdf}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

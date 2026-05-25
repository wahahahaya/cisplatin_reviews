#!/usr/bin/env python3
"""Convert the review manuscript LaTeX source to a DOCX file.

This script is a small Python wrapper around Pandoc. It defaults to the
repository layout used by this project:

    full_paper/main.tex -> full_paper/main.docx
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PAPER_DIR = REPO_ROOT / "full_paper"
DEFAULT_TEX = DEFAULT_PAPER_DIR / "main.tex"
DEFAULT_OUTPUT = DEFAULT_PAPER_DIR / "main.docx"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert full_paper/main.tex to DOCX using Pandoc.",
    )
    parser.add_argument(
        "--paper-dir",
        type=Path,
        default=DEFAULT_PAPER_DIR,
        help=f"LaTeX project directory. Default: {DEFAULT_PAPER_DIR}",
    )
    parser.add_argument(
        "--tex",
        type=Path,
        default=DEFAULT_TEX,
        help=f"Main .tex file. Default: {DEFAULT_TEX}",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output .docx path. Default: {DEFAULT_OUTPUT}",
    )
    parser.add_argument(
        "--reference-doc",
        type=Path,
        help="Optional reference .docx for Word styles.",
    )
    parser.add_argument(
        "--csl",
        type=Path,
        help="Optional CSL citation style file.",
    )
    parser.add_argument(
        "--no-citeproc",
        action="store_true",
        help="Disable Pandoc citation processing.",
    )
    return parser.parse_args()


def resolve_path(path: Path, base: Path = REPO_ROOT) -> Path:
    return path if path.is_absolute() else (base / path).resolve()


def require_file(path: Path, label: str) -> None:
    if not path.is_file():
        raise SystemExit(f"Missing {label}: {path}")


def find_pandoc() -> str:
    pandoc = shutil.which("pandoc")
    if pandoc:
        return pandoc

    try:
        import pypandoc
    except ImportError:
        pypandoc = None

    if pypandoc is not None:
        try:
            return pypandoc.get_pandoc_path()
        except OSError:
            pass

    raise SystemExit(
        "Pandoc is not available.\n"
        "Install this project's Python requirements in your virtual environment:\n"
        "  python3 -m pip install -r requirements.txt\n"
        "Then run this script again."
    )


def build_command(args: argparse.Namespace) -> list[str]:
    paper_dir = resolve_path(args.paper_dir)
    tex_file = resolve_path(args.tex)
    output_file = resolve_path(args.output)

    require_file(tex_file, "LaTeX source")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    pandoc = find_pandoc()

    command = [
        pandoc,
        str(tex_file),
        "--from",
        "latex",
        "--to",
        "docx",
        "--standalone",
        "--resource-path",
        f"{paper_dir}:{REPO_ROOT}",
        "--output",
        str(output_file),
    ]

    bibliography = paper_dir / "references.bib"
    if bibliography.is_file():
        command.extend(["--bibliography", str(bibliography)])
        if not args.no_citeproc:
            command.append("--citeproc")

    if args.reference_doc:
        reference_doc = resolve_path(args.reference_doc)
        require_file(reference_doc, "reference DOCX")
        command.extend(["--reference-doc", str(reference_doc)])

    if args.csl:
        csl = resolve_path(args.csl)
        require_file(csl, "CSL style")
        command.extend(["--csl", str(csl)])

    return command


def main() -> int:
    args = parse_args()
    command = build_command(args)
    output_file = resolve_path(args.output)

    print("Running:")
    print(" ".join(command))
    result = subprocess.run(
        command,
        cwd=resolve_path(args.paper_dir),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)

    if result.returncode != 0:
        print(f"Conversion failed with exit code {result.returncode}.", file=sys.stderr)
        return result.returncode

    print(f"Created: {output_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

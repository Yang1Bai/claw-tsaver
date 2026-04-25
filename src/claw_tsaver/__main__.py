"""CLI entry point for claw-tsaver."""

from __future__ import annotations

import argparse
import sys


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="claw-tsaver",
        description="Token-optimization proxy MCP server for OpenClaw users.",
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Print version and exit.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.version:
        from claw_tsaver import __version__

        print(__version__)
        return 0

    print("hello world from claw-tsaver")
    return 0


if __name__ == "__main__":
    sys.exit(main())

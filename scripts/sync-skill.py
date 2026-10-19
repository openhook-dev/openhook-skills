"""Refresh the compatibility skill from a local canonical SKILL.md."""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="openhook-inbox/skills/openhook/SKILL.md")
    args = parser.parse_args()
    source = args.source.read_text()
    expected = "---\nname: openhook\n"
    if not source.startswith(expected):
        parser.error("Expected the canonical Openhook skill frontmatter")
    destination = Path(__file__).resolve().parents[1] / "openhook-webhook-listener/SKILL.md"
    destination.write_text(source.replace(expected, "---\nname: openhook-webhook-listener\n", 1))
    print(f"Updated {destination}")


if __name__ == "__main__":
    main()

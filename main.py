#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Builds one fortune-cookie line from an oracular clause and its
punchline, then writes it to the entry file. The grader expects
/output/entry.txt; the ENTRY_OUTPUT environment variable redirects
the destination for local verification only.
"""

import os
from pathlib import Path

# The fortune voice: small, formal, prophetic.
ORACLE = "After liquidation, perfect diversification is yours"

# The punchline that breaks it: perfect diversification, achieved the
# hard way — every exchange holds exactly the same amount of the
# trader's money now, and that amount is zero.
PUNCHLINE = "every exchange now holds exactly zero of your money, equally."


def fortune() -> str:
    """Assemble the single-line fortune the judge will read."""
    return f"{ORACLE}: {PUNCHLINE}"


def main() -> None:
    target = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(fortune(), encoding="utf-8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Fetches the current S&P 500 constituent symbols from Wikipedia.

Usage:
    python scripts/fetch_sp500_symbols.py
    python scripts/fetch_sp500_symbols.py --json
"""

import argparse
import json
import sys

import requests


def fetch_sp500_symbols() -> list[str]:
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, timeout=15, headers=headers)
    resp.raise_for_status()

    # Parse the first table on the page using basic string parsing
    import re
    # Find all ticker symbols in the first wikitable
    # Symbols appear as: <td><a href="/wiki/..." ...>TICKER</a>
    table_start = resp.text.find('id="constituents"')
    if table_start == -1:
        raise ValueError("Could not find constituents table on Wikipedia page")
    table_end = resp.text.find("</table>", table_start)
    table_html = resp.text[table_start:table_end]

    symbols = re.findall(r'<td><a[^>]*>([A-Z]{1,5})</a></td>', table_html)

    # Clean up — remove duplicates, keep order
    seen = set()
    result = []
    for s in symbols:
        if s not in seen:
            seen.add(s)
            result.append(s)

    return result


def main():
    parser = argparse.ArgumentParser(description="Fetch S&P 500 symbols from Wikipedia")
    parser.add_argument("--json", action="store_true", help="Print JSON only")
    args = parser.parse_args()

    try:
        symbols = fetch_sp500_symbols()
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    if args.json:
        print(json.dumps({"symbols": symbols, "count": len(symbols)}))
        return

    print(f"\nS&P 500 Symbols ({len(symbols)} total):")
    print(", ".join(symbols))


if __name__ == "__main__":
    main()

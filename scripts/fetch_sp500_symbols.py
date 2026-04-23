#!/usr/bin/env python3
"""
Fetches large cap stock symbols from Yahoo Finance screener.
Used to test whether yfinance Screener works in the cloud environment.

Usage:
    python scripts/fetch_sp500_symbols.py
    python scripts/fetch_sp500_symbols.py --json
"""

import argparse
import json
import sys


def fetch_large_cap_symbols(count: int = 500) -> list[str]:
    import yfinance as yf

    query = yf.EquityQuery("gt", ["intradaymarketcap", 10_000_000_000])
    page_size = 250  # Yahoo Finance hard limit
    symbols: list[str] = []
    offset = 0
    while len(symbols) < count:
        batch = min(page_size, count - len(symbols))
        result = yf.screen(query, sortField="intradaymarketcap", sortAsc=False, size=batch, offset=offset)
        quotes = result.get("quotes", [])
        if not quotes:
            break
        symbols.extend(q["symbol"] for q in quotes if "symbol" in q)
        offset += len(quotes)
        if len(quotes) < batch:
            break
    return symbols


def main():
    parser = argparse.ArgumentParser(description="Fetch large cap symbols via yfinance Screener")
    parser.add_argument("--json", action="store_true", help="Print JSON only")
    parser.add_argument("--count", type=int, default=500, help="Number of symbols to fetch")
    args = parser.parse_args()

    try:
        symbols = fetch_large_cap_symbols(args.count)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    if args.json:
        print(json.dumps({"symbols": symbols, "count": len(symbols)}))
        return

    print(f"\nLarge Cap Symbols ({len(symbols)} total):")
    print(", ".join(symbols[:20]), "...")


if __name__ == "__main__":
    main()

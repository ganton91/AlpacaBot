#!/usr/bin/env python3
"""
Fetches large cap stock symbols from Yahoo Finance screener (yfinance 1.3.0+).
Returns top N stocks by market cap (market cap > $10B), sorted descending.

Usage:
    python scripts/fetch_sp500_symbols.py
    python scripts/fetch_sp500_symbols.py --json
    python scripts/fetch_sp500_symbols.py --count 500
"""

import argparse
import json
import sys


def fetch_large_cap_symbols(count: int = 1000) -> list[str]:
    import yfinance as yf

    query = yf.EquityQuery("and", [
        yf.EquityQuery("gt", ["intradaymarketcap", 10_000_000_000]),
        yf.EquityQuery("or", [
            yf.EquityQuery("eq", ["exchange", "NMS"]),  # NASDAQ
            yf.EquityQuery("eq", ["exchange", "NYQ"]),  # NYSE
        ]),
    ])
    symbols = []
    offset = 0
    batch = 250  # Yahoo Finance caps at 250 per request

    while len(symbols) < count:
        result = yf.screen(
            query,
            sortField="intradaymarketcap",
            sortAsc=False,
            size=batch,
            offset=offset,
        )
        quotes = result.get("quotes", [])
        if not quotes:
            break
        symbols += [q["symbol"] for q in quotes if "symbol" in q]
        offset += batch

    return symbols[:count]


def main():
    parser = argparse.ArgumentParser(description="Fetch large cap symbols via yfinance Screener")
    parser.add_argument("--json", action="store_true", help="Print JSON only")
    parser.add_argument("--count", type=int, default=1000, help="Number of symbols to fetch")
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

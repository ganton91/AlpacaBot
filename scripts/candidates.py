#!/usr/bin/env python3
"""
Candidate Scanner (Step 4a of the swing trading bot).

Fetches top gainers and most active stocks from Alpaca, combines them,
deduplicates, and applies basic filters. Outputs a clean candidate list
for the Trend Template screener (trend_template.py).

Filters applied here:
  - Price >= $10 (no penny stocks)
  - Remove duplicates across both sources

Filters NOT applied here (done in trend_template.py):
  - Average daily volume >= 500k (requires bar data)
  - Trend Template criteria (requires 250 days of bars)

Usage:
    python scripts/candidates.py
    python scripts/candidates.py --json
"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from broker.client import get_screener_client
from alpaca.data.requests import MarketMoversRequest, MostActivesRequest


def fetch_gainers(screener) -> list[dict]:
    try:
        req = MarketMoversRequest(market_type="stocks", top=20)
        movers = screener.get_market_movers(req)
        return [
            {
                "symbol": s.symbol,
                "price": float(s.price),
                "change_pct": float(s.percent_change),
                "source": "gainers",
            }
            for s in (movers.gainers or [])
            if s.price is not None
        ]
    except Exception as e:
        return []


def fetch_most_active(screener) -> list[dict]:
    try:
        req = MostActivesRequest(by="volume", top=30)
        result = screener.get_most_actives(req)
        return [
            {
                "symbol": s.symbol,
                "price": float(s.price),
                "change_pct": float(s.percent_change),
                "source": "most_active",
            }
            for s in (result.most_actives or [])
            if s.price is not None
        ]
    except Exception as e:
        return []


def run() -> dict:
    screener = get_screener_client()

    gainers = fetch_gainers(screener)
    most_active = fetch_most_active(screener)

    # Combine and deduplicate — keep first occurrence (gainers take priority)
    seen = set()
    combined = []
    for stock in gainers + most_active:
        if stock["symbol"] not in seen:
            seen.add(stock["symbol"])
            combined.append(stock)

    # Basic filter: price >= $10
    filtered = [s for s in combined if s["price"] >= 10.0]
    removed = [s["symbol"] for s in combined if s["price"] < 10.0]

    return {
        "candidates": filtered,
        "count": len(filtered),
        "removed_penny_stocks": removed,
        "sources": {
            "gainers": len(gainers),
            "most_active": len(most_active),
        },
    }


def main():
    parser = argparse.ArgumentParser(description="Candidate Scanner")
    parser.add_argument("--json", action="store_true", help="Print JSON only")
    args = parser.parse_args()

    result = run()

    if args.json:
        print(json.dumps(result))
        return

    print(f"\n{'='*50}")
    print(f"  CANDIDATE SCANNER")
    print(f"{'='*50}")
    print(f"  Gainers fetched    : {result['sources']['gainers']}")
    print(f"  Most active fetched: {result['sources']['most_active']}")
    print(f"  After dedup+filter : {result['count']} candidates")

    if result["removed_penny_stocks"]:
        print(f"  Removed (<$10)     : {', '.join(result['removed_penny_stocks'])}")

    if result["candidates"]:
        print(f"\n  CANDIDATES:")
        for s in result["candidates"]:
            chg = f"+{s['change_pct']:.1f}%" if s["change_pct"] >= 0 else f"{s['change_pct']:.1f}%"
            print(f"    {s['symbol']:8s}  ${s['price']:.2f}  {chg:>8s}  [{s['source']}]")

    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()

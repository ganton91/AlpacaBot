#!/usr/bin/env python3
"""
Market Schedule Check (Step 0 of the swing trading bot).

Determines whether the bot should run today or skip.

Usage:
    python scripts/market_schedule.py
    python scripts/market_schedule.py --json
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from broker.client import get_trading_client


def run() -> dict:
    client = get_trading_client()
    clock = client.get_clock()

    now = datetime.now(timezone.utc)
    weekday = now.strftime("%A")
    is_weekend = now.weekday() >= 5

    next_open = clock.next_open
    hours_until_open = (next_open - now).total_seconds() / 3600 if next_open else None

    is_holiday = (not is_weekend) and (hours_until_open is not None) and (hours_until_open > 18)

    if is_weekend or is_holiday:
        mode = "skip"
        reason = "weekend" if is_weekend else "market_holiday"
    else:
        mode = "run"
        reason = "weekday"

    return {
        "timestamp": now.isoformat(),
        "mode": mode,
        "reason": reason,
        "weekday": weekday,
        "market_open": clock.is_open,
        "next_open": next_open.isoformat() if next_open else None,
        "next_close": clock.next_close.isoformat() if clock.next_close else None,
        "hours_until_open": round(hours_until_open, 1) if hours_until_open is not None else None,
    }


def main():
    parser = argparse.ArgumentParser(description="Market Schedule Check")
    parser.add_argument("--json", action="store_true", help="Print JSON only")
    args = parser.parse_args()

    result = run()

    if args.json:
        print(json.dumps(result))
        return

    mode_label = "🟢 RUN" if result["mode"] == "run" else "⛔ SKIP"
    print(f"\n{'='*50}")
    print(f"  MARKET SCHEDULE — {result['timestamp'][:10]}")
    print(f"{'='*50}")
    print(f"  Day      : {result['weekday']}")
    print(f"  Market   : {'OPEN' if result['market_open'] else 'CLOSED'}")
    print(f"  Reason   : {result['reason']}")
    if result["next_open"]:
        print(f"  Next open: {result['next_open'][:16]} UTC ({result['hours_until_open']}h away)")
    print(f"  Mode     : {mode_label}")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()

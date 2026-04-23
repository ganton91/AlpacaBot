#!/usr/bin/env python3
"""
Trend Template Screener (Step 4b of the swing trading bot).

Takes a comma-separated list of symbols, fetches 250 days of bar data for each,
and applies the Minervini Trend Template (8 criteria). Only stocks that pass
ALL criteria are returned.

Trend Template criteria (ALL must be true):
  1. Price > 50-day MA
  2. Price > 150-day MA
  3. Price > 200-day MA
  4. 50-day MA > 150-day MA
  5. 150-day MA > 200-day MA
  6. 200-day MA trending up (higher than 20 trading days ago)
  7. Price within 25% of 52-week high
  8. Price at least 30% above 52-week low

Additional filter:
  - Average daily volume (20-day) >= 500,000

Usage:
    python scripts/trend_template.py --symbols NVDA,META,TSLA
    python scripts/trend_template.py --symbols NVDA,META,TSLA --json
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from broker.client import get_data_client
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame

MIN_AVG_VOLUME = 500_000
MIN_PRICE = 10.0
DAYS_TO_FETCH = 250


def sma(prices: list[float], period: int) -> float | None:
    if len(prices) < period:
        return None
    return sum(prices[-period:]) / period


def sma_n_days_ago(prices: list[float], period: int, n: int) -> float | None:
    end = len(prices) - n
    if end < period:
        return None
    return sum(prices[end - period:end]) / period


def fetch_bars(client, symbol: str) -> tuple[list[float], list[float], list[float]] | None:
    """Returns (closes, highs, volumes) or None if insufficient data."""
    try:
        end = datetime.now(timezone.utc)
        start = end - timedelta(days=int(DAYS_TO_FETCH * 1.6))
        req = StockBarsRequest(
            symbol_or_symbols=symbol,
            timeframe=TimeFrame.Day,
            start=start,
            end=end,
            feed="iex",
            adjustment="split",
        )
        bars = client.get_stock_bars(req)
        df = bars.df
        if df.empty:
            return None
        sym_df = df.xs(symbol, level="symbol")
        if len(sym_df) < DAYS_TO_FETCH:
            return None
        closes = sym_df["close"].tolist()
        highs = sym_df["high"].tolist()
        lows = sym_df["low"].tolist()
        volumes = sym_df["volume"].tolist()
        return closes, highs, lows, volumes
    except Exception:
        return None


def screen(symbol: str, closes: list[float], highs: list[float], lows: list[float], volumes: list[float]) -> dict | None:
    """Returns screening result dict if stock passes all criteria, else None."""
    price = closes[-1]

    ma50 = sma(closes, 50)
    ma150 = sma(closes, 150)
    ma200 = sma(closes, 200)
    ma200_20d_ago = sma_n_days_ago(closes, 200, 20)
    avg_vol_20d = sum(volumes[-21:-1]) / 20 if len(volumes) >= 21 else None

    if any(v is None for v in [ma50, ma150, ma200, ma200_20d_ago, avg_vol_20d]):
        return None

    week52_high = max(highs[-252:]) if len(highs) >= 252 else max(highs)
    week52_low = min(lows[-252:]) if len(lows) >= 252 else min(lows)

    # Apply all 8 Trend Template criteria
    criteria = {
        "price_above_ma50":    price > ma50,
        "price_above_ma150":   price > ma150,
        "price_above_ma200":   price > ma200,
        "ma50_above_ma150":    ma50 > ma150,
        "ma150_above_ma200":   ma150 > ma200,
        "ma200_rising":        ma200 > ma200_20d_ago,
        "near_52w_high":       price >= week52_high * 0.75,
        "above_52w_low":       price >= week52_low * 1.30,
    }

    if price < MIN_PRICE:
        return None

    # Volume filter
    sufficient_volume = avg_vol_20d >= MIN_AVG_VOLUME

    if not all(criteria.values()) or not sufficient_volume:
        return None

    ma200_direction = "rising" if ma200 > ma200_20d_ago else "flat"

    return {
        "symbol": symbol,
        "price": round(price, 2),
        "ma50": round(ma50, 2),
        "ma150": round(ma150, 2),
        "ma200": round(ma200, 2),
        "ma200_direction": ma200_direction,
        "week52_high": round(week52_high, 2),
        "week52_low": round(week52_low, 2),
        "pct_from_52w_high": round((price / week52_high - 1) * 100, 1),
        "pct_above_52w_low": round((price / week52_low - 1) * 100, 1),
        "avg_volume_20d": int(avg_vol_20d),
        "criteria": criteria,
    }


def run(symbols: list[str]) -> dict:
    client = get_data_client()
    passed = []
    failed = []
    errors = []

    for symbol in symbols:
        bars = fetch_bars(client, symbol)
        if bars is None:
            errors.append(symbol)
            continue

        closes, highs, lows, volumes = bars
        result = screen(symbol, closes, highs, lows, volumes)

        if result:
            passed.append(result)
        else:
            failed.append(symbol)

    return {
        "passed": passed,
        "passed_count": len(passed),
        "failed": failed,
        "failed_count": len(failed),
        "errors": errors,
    }


def main():
    parser = argparse.ArgumentParser(description="Trend Template Screener")
    parser.add_argument("--symbols", required=True, help="Comma-separated list of symbols e.g. NVDA,META,TSLA")
    parser.add_argument("--json", action="store_true", help="Print JSON only")
    args = parser.parse_args()

    symbols = [s.strip().upper() for s in args.symbols.split(",") if s.strip()]

    if not symbols:
        print("Error: no symbols provided.")
        sys.exit(1)

    result = run(symbols)

    if args.json:
        print(json.dumps(result))
        return

    print(f"\n{'='*50}")
    print(f"  TREND TEMPLATE SCREENER")
    print(f"{'='*50}")
    print(f"  Screened : {len(symbols)} symbols")
    print(f"  Passed   : {result['passed_count']}")
    print(f"  Failed   : {result['failed_count']}")
    if result["errors"]:
        print(f"  Errors   : {', '.join(result['errors'])}")

    if result["passed"]:
        print(f"\n  PASSING STOCKS:")
        for s in result["passed"]:
            print(f"\n    {s['symbol']}  ${s['price']:.2f}  "
                  f"({s['pct_from_52w_high']:+.1f}% from 52w high)")
            print(f"    50MA={s['ma50']}  150MA={s['ma150']}  200MA={s['ma200']} ({s['ma200_direction']})")
            print(f"    52w H=${s['week52_high']}  52w L=${s['week52_low']}  "
                  f"AvgVol={s['avg_volume_20d']:,}")
    else:
        print(f"\n  No stocks passed the Trend Template.")

    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()

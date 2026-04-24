#!/usr/bin/env python3
"""
Trend Template Batch Screener (Step 4 of the swing trading bot).

Fetches the top 500 large cap US-listed stocks (NYSE + NASDAQ, market cap > $10B)
dynamically via Yahoo Finance, then screens them against the Minervini Trend Template.
Uses batch fetching for efficiency. Results are pre-screened and do NOT need
re-screening via trend_template.py.

Usage:
    python scripts/trend_template_batch.py
    python scripts/trend_template_batch.py --json
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

DAYS_TO_FETCH = 250
BATCH_SIZE = 50
MIN_AVG_VOLUME = 500_000
MIN_PRICE = 10.0


def fetch_large_cap_symbols(count: int = 500) -> list[str]:
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


def sma(prices: list[float], period: int) -> float | None:
    if len(prices) < period:
        return None
    return sum(prices[-period:]) / period


def sma_n_days_ago(prices: list[float], period: int, n: int) -> float | None:
    end = len(prices) - n
    if end < period:
        return None
    return sum(prices[end - period:end]) / period


def fetch_batch(client, symbols: list[str]) -> dict:
    try:
        end = datetime.now(timezone.utc)
        start = end - timedelta(days=int(DAYS_TO_FETCH * 1.6))
        req = StockBarsRequest(
            symbol_or_symbols=symbols,
            timeframe=TimeFrame.Day,
            start=start,
            end=end,
            feed="iex",
            adjustment="split",
        )
        bars = client.get_stock_bars(req)
        df = bars.df
        if df.empty:
            return {}

        result = {}
        for symbol in symbols:
            try:
                sym_df = df.xs(symbol, level="symbol")
                if len(sym_df) < DAYS_TO_FETCH:
                    continue
                result[symbol] = (
                    sym_df["close"].tolist(),
                    sym_df["high"].tolist(),
                    sym_df["low"].tolist(),
                    sym_df["volume"].tolist(),
                )
            except KeyError:
                continue
        return result
    except Exception as e:
        print(f"[fetch_batch] ERROR for {symbols[:3]}...: {e}", file=sys.stderr)
        return {}


def screen(symbol: str, closes, highs, lows, volumes) -> dict | None:
    price = closes[-1]

    if price < MIN_PRICE:
        return None

    ma50        = sma(closes, 50)
    ma150       = sma(closes, 150)
    ma200       = sma(closes, 200)
    ma200_20ago = sma_n_days_ago(closes, 200, 20)
    avg_vol_20d = sum(volumes[-21:-1]) / 20 if len(volumes) >= 21 else None

    if any(v is None for v in [ma50, ma150, ma200, ma200_20ago, avg_vol_20d]):
        return None

    week52_high = max(highs[-252:]) if len(highs) >= 252 else max(highs)
    week52_low  = min(lows[-252:])  if len(lows)  >= 252 else min(lows)

    criteria = {
        "price_above_ma50":  price > ma50,
        "price_above_ma150": price > ma150,
        "price_above_ma200": price > ma200,
        "ma50_above_ma150":  ma50  > ma150,
        "ma150_above_ma200": ma150 > ma200,
        "ma200_rising":      ma200 > ma200_20ago,
        "near_52w_high":     price >= week52_high * 0.75,
        "above_52w_low":     price >= week52_low  * 1.30,
    }

    if not all(criteria.values()) or avg_vol_20d < MIN_AVG_VOLUME:
        return None

    return {
        "symbol":            symbol,
        "price":             round(price, 2),
        "ma50":              round(ma50, 2),
        "ma150":             round(ma150, 2),
        "ma200":             round(ma200, 2),
        "ma200_direction":   "rising" if ma200 > ma200_20ago else "flat",
        "week52_high":       round(week52_high, 2),
        "week52_low":        round(week52_low, 2),
        "pct_from_52w_high": round((price / week52_high - 1) * 100, 1),
        "pct_above_52w_low": round((price / week52_low  - 1) * 100, 1),
        "avg_volume_20d":    int(avg_vol_20d),
        "criteria":          criteria,
    }


def run() -> dict:
    try:
        symbols = fetch_large_cap_symbols(500)
    except Exception as e:
        return {"error": f"Failed to fetch symbols: {e}", "passed": [], "failed": [], "errors": [], "total": 0}

    # Remove duplicates and symbols with "-" (preferred shares / class variants
    # that Alpaca IEX rejects, causing the entire batch to fail)
    symbols = [s for s in dict.fromkeys(symbols) if "-" not in s]

    client = get_data_client()
    passed = []
    failed = []
    errors = []

    batches = [symbols[i:i + BATCH_SIZE] for i in range(0, len(symbols), BATCH_SIZE)]

    for batch in batches:
        data = fetch_batch(client, batch)
        for symbol in batch:
            if symbol not in data:
                errors.append(symbol)
                continue
            closes, highs, lows, volumes = data[symbol]
            result = screen(symbol, closes, highs, lows, volumes)
            if result:
                passed.append(result)
            else:
                failed.append(symbol)

    return {
        "passed":       passed,
        "passed_count": len(passed),
        "failed":       failed,
        "failed_count": len(failed),
        "errors":       errors,
        "total":        len(symbols),
    }


def main():
    parser = argparse.ArgumentParser(description="Trend Template Batch Screener")
    parser.add_argument("--json", action="store_true", help="Print JSON only")
    args = parser.parse_args()

    result = run()

    if args.json:
        print(json.dumps(result))
        return

    print(f"\n{'='*55}")
    print(f"  TREND TEMPLATE BATCH SCREENER")
    print(f"{'='*55}")
    print(f"  Universe : {result['total']} symbols")
    print(f"  Passed   : {result['passed_count']}")
    print(f"  Failed   : {result['failed_count']}")
    if result.get("errors"):
        print(f"  Errors   : {len(result['errors'])} ({', '.join(result['errors'][:10])}{'...' if len(result['errors']) > 10 else ''})")

    if result["passed"]:
        print(f"\n  PASSING STOCKS:")
        for s in sorted(result["passed"], key=lambda x: x["pct_from_52w_high"], reverse=True):
            print(f"    {s['symbol']:8s}  ${s['price']:.2f}  "
                  f"({s['pct_from_52w_high']:+.1f}% from 52w high)  "
                  f"AvgVol={s['avg_volume_20d']:,}")
    else:
        print(f"\n  No stocks passed the Trend Template.")

    print(f"{'='*55}\n")


if __name__ == "__main__":
    main()

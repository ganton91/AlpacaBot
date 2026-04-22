#!/usr/bin/env python3
"""
Setup Scanner (Step 5 of the swing trading bot).

For each symbol in the watchlist, fetches recent bar data and calculates
Breakout and Episodic Pivot (EP) metrics. Outputs raw numbers as JSON
so the bot can decide which setups to act on.

Breakout metrics (last 15 bars):
  - consolidation_high    : max high of last 15 bars (resistance level)
  - consolidation_low     : min low of last 15 bars
  - consolidation_range_pct : (high - low) / low * 100
  - pct_from_resistance   : (price - resistance) / resistance * 100
  - volume_declining      : avg vol of last 5 bars < avg vol of bars 6-15

EP metrics:
  - gap_pct               : (today open - yesterday close) / yesterday close * 100
  - volume_ratio          : today volume / avg volume of last 20 bars
  - is_ep_candidate       : gap_pct >= 8 AND volume_ratio >= 2.0

Usage:
    python scripts/setup_scanner.py --symbols NVDA,META,TSLA
    python scripts/setup_scanner.py --symbols NVDA,META,TSLA --json
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

CONSOLIDATION_BARS = 15
DAYS_TO_FETCH = 60  # calendar days — ensures 20+ trading days


def fetch_bars(client, symbol: str):
    """Returns (opens, closes, highs, lows, volumes) or None."""
    try:
        end = datetime.now(timezone.utc)
        start = end - timedelta(days=DAYS_TO_FETCH)
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
        if len(sym_df) < CONSOLIDATION_BARS + 5:
            return None
        opens   = sym_df["open"].tolist()
        closes  = sym_df["close"].tolist()
        highs   = sym_df["high"].tolist()
        lows    = sym_df["low"].tolist()
        volumes = sym_df["volume"].tolist()
        return opens, closes, highs, lows, volumes
    except Exception:
        return None


def breakout_metrics(closes, highs, lows, volumes) -> dict:
    n = CONSOLIDATION_BARS
    c_highs  = highs[-n:]
    c_lows   = lows[-n:]
    c_vols   = volumes[-n:]

    resistance = max(c_highs)
    support    = min(c_lows)
    price      = closes[-1]

    c_range_pct       = round((resistance - support) / support * 100, 2)
    pct_from_resistance = round((price - resistance) / resistance * 100, 2)

    base_vols      = volumes[-n:-1]  # exclude today so breakout volume doesn't contaminate base quality
    recent_vol_avg = sum(base_vols[-5:]) / 5
    prior_vol_avg  = sum(base_vols[:9]) / 9
    volume_declining = recent_vol_avg < prior_vol_avg

    avg_vol_20d = sum(volumes[-21:-1]) / 20 if len(volumes) >= 21 else None
    today_volume_ratio = round(volumes[-1] / avg_vol_20d, 2) if avg_vol_20d else None

    return {
        "consolidation_high":      round(resistance, 2),
        "consolidation_low":       round(support, 2),
        "consolidation_range_pct": c_range_pct,
        "pct_from_resistance":     pct_from_resistance,
        "volume_declining":        volume_declining,
        "recent_vol_avg":          int(recent_vol_avg),
        "prior_vol_avg":           int(prior_vol_avg),
        "today_volume_ratio":      today_volume_ratio,
    }


def ep_metrics(opens, closes, lows, volumes) -> dict:
    today_open    = opens[-1]
    today_volume  = volumes[-1]
    prev_close    = closes[-2]
    gap_day_low   = lows[-1]

    gap_pct      = round((today_open - prev_close) / prev_close * 100, 2)
    avg_vol_20d  = sum(volumes[-21:-1]) / 20
    volume_ratio = round(today_volume / avg_vol_20d, 2) if avg_vol_20d > 0 else 0.0

    is_ep = gap_pct >= 8.0 and volume_ratio >= 2.0

    return {
        "gap_pct":          gap_pct,
        "gap_day_low":      round(gap_day_low, 2),
        "today_volume":     int(today_volume),
        "avg_volume_20d":   int(avg_vol_20d),
        "volume_ratio":     volume_ratio,
        "is_ep_candidate":  is_ep,
    }


def run(symbols: list[str]) -> dict:
    client = get_data_client()
    results = []
    errors  = []

    for symbol in symbols:
        bars = fetch_bars(client, symbol)
        if bars is None:
            errors.append(symbol)
            continue

        opens, closes, highs, lows, volumes = bars

        results.append({
            "symbol":   symbol,
            "price":    round(closes[-1], 2),
            "breakout": breakout_metrics(closes, highs, lows, volumes),
            "ep":       ep_metrics(opens, closes, lows, volumes),
        })

    return {
        "timestamp":       datetime.now(timezone.utc).isoformat(),
        "symbols_scanned": len(symbols),
        "results":         results,
        "errors":          errors,
    }


def main():
    parser = argparse.ArgumentParser(description="Setup Scanner")
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

    print(f"\n{'='*55}")
    print(f"  SETUP SCANNER — {result['timestamp'][:10]}")
    print(f"{'='*55}")
    print(f"  Scanned : {result['symbols_scanned']} symbols")
    if result["errors"]:
        print(f"  Errors  : {', '.join(result['errors'])}")

    ep_candidates = [r for r in result["results"] if r["ep"]["is_ep_candidate"]]
    breakout_candidates = [
        r for r in result["results"]
        if -3.0 <= r["breakout"]["pct_from_resistance"] <= 3.0
    ]

    if ep_candidates:
        print(f"\n  EP CANDIDATES ({len(ep_candidates)}):")
        for r in ep_candidates:
            ep = r["ep"]
            print(f"    {r['symbol']:8s}  ${r['price']:.2f}  "
                  f"gap={ep['gap_pct']:+.1f}%  vol_ratio={ep['volume_ratio']:.1f}x")

    if breakout_candidates:
        print(f"\n  NEAR BREAKOUT ({len(breakout_candidates)}):")
        for r in breakout_candidates:
            bo = r["breakout"]
            print(f"    {r['symbol']:8s}  ${r['price']:.2f}  "
                  f"resistance=${bo['consolidation_high']}  "
                  f"dist={bo['pct_from_resistance']:+.1f}%  "
                  f"range={bo['consolidation_range_pct']:.1f}%  "
                  f"vol_declining={bo['volume_declining']}")

    if not ep_candidates and not breakout_candidates:
        print(f"\n  No actionable setups today.")

    print(f"\n  ALL RESULTS:")
    for r in result["results"]:
        bo = r["breakout"]
        ep = r["ep"]
        print(f"    {r['symbol']:8s}  ${r['price']:.2f}  "
              f"resist=${bo['consolidation_high']}  dist={bo['pct_from_resistance']:+.1f}%  "
              f"gap={ep['gap_pct']:+.1f}%  volx={ep['volume_ratio']:.1f}")

    print(f"{'='*55}\n")


if __name__ == "__main__":
    main()

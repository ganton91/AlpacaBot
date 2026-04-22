#!/usr/bin/env python3
"""
Market Health Check (Step 1 of the swing trading bot).

Outputs raw market data as JSON so the bot can decide the GREEN/YELLOW/RED
signal itself based on the rules in the execution guide.

Usage:
    python scripts/market_health.py
    python scripts/market_health.py --json   # machine-readable only
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone

import requests
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from broker.client import get_data_client


# ---------------------------------------------------------------------------
# SMA helpers
# ---------------------------------------------------------------------------

def sma(prices: list[float], period: int) -> float | None:
    if len(prices) < period:
        return None
    return sum(prices[-period:]) / period


def sma_n_days_ago(prices: list[float], period: int, n: int) -> float | None:
    end = len(prices) - n
    if end < period:
        return None
    return sum(prices[end - period:end]) / period


# ---------------------------------------------------------------------------
# Data fetchers
# ---------------------------------------------------------------------------

def fetch_closes(client: StockHistoricalDataClient, symbol: str, days: int) -> list[float]:
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=days + 60)
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
        raise ValueError(f"No bar data returned for {symbol}")
    closes = df.xs(symbol, level="symbol")["close"].tolist()
    return closes


def fetch_vix() -> tuple[float | None, float | None, str]:
    """Returns (vix_today, vix_yesterday, source)."""
    try:
        url = "https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.json"
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        rows = data["data"]
        vix_now = float(rows[-1][4])
        vix_prev = float(rows[-2][4]) if len(rows) >= 2 else None
        return vix_now, vix_prev, "cboe"
    except Exception:
        pass

    try:
        url = "https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX?interval=1d&range=5d"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, timeout=10, headers=headers)
        resp.raise_for_status()
        data = resp.json()
        closes = [c for c in data["chart"]["result"][0]["indicators"]["quote"][0]["close"] if c is not None]
        vix_now = float(closes[-1])
        vix_prev = float(closes[-2]) if len(closes) >= 2 else None
        return vix_now, vix_prev, "yahoo"
    except Exception:
        pass

    return None, None, "unavailable"


# ---------------------------------------------------------------------------
# MA data
# ---------------------------------------------------------------------------

def ma_data(symbol: str, closes: list[float]) -> dict:
    price = closes[-1]
    ma50 = sma(closes, 50)
    ma200 = sma(closes, 200)
    ma50_10d_ago = sma_n_days_ago(closes, 50, 10)

    return {
        "symbol": symbol,
        "price": round(price, 2),
        "ma50": round(ma50, 2) if ma50 else None,
        "ma200": round(ma200, 2) if ma200 else None,
        "above_50ma": (price > ma50) if ma50 is not None else None,
        "above_200ma": (price > ma200) if ma200 is not None else None,
        "ma50_rising": (ma50 > ma50_10d_ago) if (ma50 is not None and ma50_10d_ago is not None) else None,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run() -> dict:
    client = get_data_client()

    spy_closes = fetch_closes(client, "SPY", 250)
    qqq_closes = fetch_closes(client, "QQQ", 250)

    spy = ma_data("SPY", spy_closes)
    qqq = ma_data("QQQ", qqq_closes)

    vix_now, vix_prev, vix_source = fetch_vix()
    vix_direction = "unknown"
    if vix_now is not None and vix_prev is not None:
        vix_direction = "rising" if vix_now > vix_prev else "falling"

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "spy": spy,
        "qqq": qqq,
        "vix": {
            "value": round(vix_now, 2) if vix_now is not None else None,
            "prev_value": round(vix_prev, 2) if vix_prev is not None else None,
            "direction": vix_direction,
            "source": vix_source,
        },
    }


def main():
    parser = argparse.ArgumentParser(description="Market Health Check")
    parser.add_argument("--json", action="store_true", help="Print JSON only (no human summary)")
    args = parser.parse_args()

    result = run()

    if args.json:
        print(json.dumps(result))
        return

    print(f"\n{'='*50}")
    print(f"  MARKET HEALTH DATA — {result['timestamp'][:10]}")
    print(f"{'='*50}")

    def flag(val, true_label, false_label):
        if val is None:
            return "N/A"
        return true_label if val else false_label

    for key in ("spy", "qqq"):
        d = result[key]
        above50  = flag(d["above_50ma"],  "above",  "below")
        above200 = flag(d["above_200ma"], "above",  "below")
        rising50 = flag(d["ma50_rising"], "rising", "falling")
        print(f"  {d['symbol']:4s}  price=${d['price']:.2f}  "
              f"50MA={d['ma50']} ({above50}, {rising50})  "
              f"200MA={d['ma200']} ({above200})")

    v = result["vix"]
    vix_str = f"{v['value']}" if v["value"] else "N/A"
    print(f"\n  VIX   {vix_str} ({v['direction']})  [source: {v['source']}]")

    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()

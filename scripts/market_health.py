#!/usr/bin/env python3
"""
Market Health Check (Step 2 of the swing trading bot).

Outputs a JSON result with signal GREEN / YELLOW / RED plus supporting data,
so the bot can consume it without re-doing the calculations.

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
from alpaca.data.historical.screener import ScreenerClient
from alpaca.data.requests import StockBarsRequest, MarketMoversRequest
from alpaca.data.timeframe import TimeFrame

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from github.push import git_push
from broker.client import get_data_client, get_screener_client


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


def fetch_vix() -> tuple[float | None, str]:
    try:
        url = "https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.json"
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        last = data["data"][-1]
        vix = float(last[4])
        return vix, "cboe"
    except Exception:
        pass

    try:
        url = "https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX?interval=1d&range=5d"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, timeout=10, headers=headers)
        resp.raise_for_status()
        data = resp.json()
        closes = data["chart"]["result"][0]["indicators"]["quote"][0]["close"]
        vix = float([c for c in closes if c is not None][-1])
        return vix, "yahoo"
    except Exception:
        pass

    return None, "unavailable"


def fetch_market_movers() -> dict:
    try:
        screener = get_screener_client()
        req = MarketMoversRequest(market_type="stocks")
        movers = screener.get_market_movers(req)
        gainers = len(movers.gainers) if movers.gainers else 0
        losers = len(movers.losers) if movers.losers else 0
        return {"gainers": gainers, "losers": losers}
    except Exception:
        return {"gainers": 0, "losers": 0, "error": "unavailable"}


# ---------------------------------------------------------------------------
# Signal logic
# ---------------------------------------------------------------------------

def vix_signal(vix: float | None, prev_vix: float | None) -> tuple[str, str]:
    if vix is None:
        return "YELLOW", "VIX unavailable — assuming moderate conditions"

    direction = "unknown"
    if prev_vix is not None:
        direction = "rising" if vix > prev_vix else "falling"

    if vix < 15:
        color = "GREEN"
    elif vix < 20:
        color = "GREEN" if direction != "rising" else "YELLOW"
    elif vix < 25:
        color = "YELLOW"
    elif vix < 30:
        color = "YELLOW" if direction == "falling" else "RED"
    else:
        color = "RED"

    return color, direction


def ma_signal(symbol: str, closes: list[float]) -> dict:
    price = closes[-1]
    ma50 = sma(closes, 50)
    ma200 = sma(closes, 200)
    ma50_10d_ago = sma_n_days_ago(closes, 50, 10)

    above_50 = price > ma50 if ma50 else None
    above_200 = price > ma200 if ma200 else None
    ma50_rising = (ma50 > ma50_10d_ago) if (ma50 and ma50_10d_ago) else None

    return {
        "symbol": symbol,
        "price": round(price, 2),
        "ma50": round(ma50, 2) if ma50 else None,
        "ma200": round(ma200, 2) if ma200 else None,
        "above_50ma": above_50,
        "above_200ma": above_200,
        "ma50_rising": ma50_rising,
    }


def combine_signals(spy: dict, qqq: dict, vix_color: str, vix_direction: str, breadth: dict) -> str:
    both_above_50 = spy["above_50ma"] and qqq["above_50ma"]
    both_below_50 = not spy["above_50ma"] and not qqq["above_50ma"]
    spy_death_cross = (spy["ma50"] and spy["ma200"] and spy["ma50"] < spy["ma200"])
    qqq_death_cross = (qqq["ma50"] and qqq["ma200"] and qqq["ma50"] < qqq["ma200"])
    death_cross = spy_death_cross or qqq_death_cross

    if vix_color == "RED" or both_below_50 or death_cross:
        return "RED"

    both_rising_50 = spy["ma50_rising"] and qqq["ma50_rising"]
    if both_above_50 and both_rising_50 and vix_color == "GREEN":
        return "GREEN"

    return "YELLOW"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def save_report(result: dict) -> str:
    reports_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reports")
    os.makedirs(reports_dir, exist_ok=True)
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = os.path.join(reports_dir, f"market_health_{date_str}.json")
    with open(path, "w") as f:
        json.dump(result, f, indent=2)
    return path


def run() -> dict:
    client = get_data_client()

    spy_closes = fetch_closes(client, "SPY", 250)
    qqq_closes = fetch_closes(client, "QQQ", 250)

    spy = ma_signal("SPY", spy_closes)
    qqq = ma_signal("QQQ", qqq_closes)

    vix_now, vix_source = fetch_vix()
    vix_prev = None
    try:
        url = "https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.json"
        resp = requests.get(url, timeout=10)
        data = resp.json()
        if len(data["data"]) >= 2:
            vix_prev = float(data["data"][-2][4])
    except Exception:
        pass

    vix_color, vix_direction = vix_signal(vix_now, vix_prev)
    breadth = fetch_market_movers()
    overall = combine_signals(spy, qqq, vix_color, vix_direction, breadth)

    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "signal": overall,
        "spy": spy,
        "qqq": qqq,
        "vix": {
            "value": round(vix_now, 2) if vix_now else None,
            "direction": vix_direction,
            "signal": vix_color,
            "source": vix_source,
        },
        "breadth": breadth,
    }
    return result


def main():
    parser = argparse.ArgumentParser(description="Market Health Check")
    parser.add_argument("--json", action="store_true", help="Print JSON only (no human summary)")
    args = parser.parse_args()

    result = run()
    path = save_report(result)
    git_push(f"Market health report {result['timestamp'][:10]}", [path])

    if args.json:
        print(json.dumps(result))
        return

    s = result["signal"]
    color_emoji = {"GREEN": "🟢", "YELLOW": "🟡", "RED": "🔴"}.get(s, "⚪")
    print(f"\n{'='*50}")
    print(f"  MARKET HEALTH CHECK — {result['timestamp'][:10]}")
    print(f"{'='*50}")
    print(f"  Overall Signal : {color_emoji}  {s}")
    print()

    for key in ("spy", "qqq"):
        d = result[key]
        above50  = "✅ above" if d["above_50ma"]  else "❌ below"
        above200 = "✅ above" if d["above_200ma"] else "❌ below"
        rising50 = "↑ rising" if d["ma50_rising"] else "↓ falling"
        print(f"  {d['symbol']:4s}  price=${d['price']:.2f}  "
              f"50MA={d['ma50']} ({above50}, {rising50})  "
              f"200MA={d['ma200']} ({above200})")

    v = result["vix"]
    vix_str = f"{v['value']}" if v["value"] else "N/A"
    print(f"\n  VIX   {vix_str} ({v['direction']}) → {v['signal']}  [source: {v['source']}]")

    b = result["breadth"]
    if "error" not in b:
        print(f"\n  Breadth  gainers={b['gainers']}  losers={b['losers']}")

    print(f"{'='*50}")
    print(f"  Report saved: {path}\n")


if __name__ == "__main__":
    main()

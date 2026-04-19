#!/usr/bin/env python3
"""
Account Snapshot (Steps 2 & 3 of the swing trading bot).

Fetches account info, open stock positions with MA analysis, and open orders.
Calculates available slots, portfolio exposure, and moving averages per position
so the bot can make exit/stop decisions without additional API calls.

Usage:
    python scripts/account_snapshot.py
    python scripts/account_snapshot.py --json
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from broker.client import get_trading_client, get_data_client
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import QueryOrderStatus
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame

MAX_STOCK_POSITIONS = 5


def sma(prices: list[float], period: int) -> float | None:
    if len(prices) < period:
        return None
    return round(sum(prices[-period:]) / period, 2)


def get_days_open(client, symbol: str) -> int | None:
    try:
        orders = client.get_orders(GetOrdersRequest(
            status=QueryOrderStatus.CLOSED,
            symbols=[symbol],
        ))
        filled = [o for o in orders if str(o.status) == "OrderStatus.FILLED" and o.filled_at]
        if not filled:
            return None
        oldest = min(filled, key=lambda o: o.filled_at)
        delta = datetime.now(timezone.utc) - oldest.filled_at
        return delta.days
    except Exception:
        return None


def get_ma_analysis(data_client, symbol: str) -> dict:
    try:
        end = datetime.now(timezone.utc)
        start = end - timedelta(days=90)
        req = StockBarsRequest(
            symbol_or_symbols=symbol,
            timeframe=TimeFrame.Day,
            start=start,
            end=end,
            feed="iex",
            adjustment="split",
        )
        bars = data_client.get_stock_bars(req)
        df = bars.df
        if df.empty:
            return {}
        closes = df.xs(symbol, level="symbol")["close"].tolist()
        price = closes[-1]
        ma10 = sma(closes, 10)
        ma20 = sma(closes, 20)
        ma50 = sma(closes, 50)
        return {
            "ma10": ma10,
            "ma20": ma20,
            "ma50": ma50,
            "above_ma10": price > ma10 if ma10 else None,
            "above_ma20": price > ma20 if ma20 else None,
            "above_ma50": price > ma50 if ma50 else None,
        }
    except Exception:
        return {}


def run() -> dict:
    trading_client = get_trading_client()
    data_client = get_data_client()

    account = trading_client.get_account()
    equity = float(account.equity)
    cash = float(account.cash)
    buying_power = float(account.buying_power)

    all_positions = trading_client.get_all_positions()
    stock_positions = [p for p in all_positions if "crypto" not in str(p.asset_class).lower()]

    positions_value = sum(float(p.market_value) for p in stock_positions)
    exposure_pct = round((positions_value / equity) * 100, 1) if equity > 0 else 0

    orders = trading_client.get_orders(GetOrdersRequest(status=QueryOrderStatus.OPEN))

    stocks = []
    for p in stock_positions:
        ma = get_ma_analysis(data_client, p.symbol)
        stocks.append({
            "symbol": p.symbol,
            "qty": float(p.qty),
            "entry_price": float(p.avg_entry_price),
            "current_price": float(p.current_price),
            "market_value": float(p.market_value),
            "unrealized_pl_pct": round(float(p.unrealized_plpc) * 100, 2),
            "days_open": get_days_open(trading_client, p.symbol),
            **ma,
        })

    return {
        "account": {
            "equity": round(equity, 2),
            "cash": round(cash, 2),
            "buying_power": round(buying_power, 2),
            "exposure_pct": exposure_pct,
        },
        "positions": {
            "count": len(stock_positions),
            "slots_available": MAX_STOCK_POSITIONS - len(stock_positions),
            "stocks": stocks,
        },
        "open_orders": [
            {
                "id": str(o.id),
                "symbol": o.symbol,
                "side": o.side.value,
                "type": o.type.value,
                "qty": float(o.qty) if o.qty else None,
                "stop_price": float(o.stop_price) if o.stop_price else None,
                "limit_price": float(o.limit_price) if o.limit_price else None,
            }
            for o in orders
        ],
    }


def main():
    parser = argparse.ArgumentParser(description="Account Snapshot")
    parser.add_argument("--json", action="store_true", help="Print JSON only")
    args = parser.parse_args()

    result = run()

    if args.json:
        print(json.dumps(result))
        return

    a = result["account"]
    p = result["positions"]
    print(f"\n{'='*50}")
    print(f"  ACCOUNT SNAPSHOT")
    print(f"{'='*50}")
    print(f"  Equity       : ${a['equity']:,.2f}")
    print(f"  Cash         : ${a['cash']:,.2f}")
    print(f"  Buying Power : ${a['buying_power']:,.2f}")
    print(f"  Exposure     : {a['exposure_pct']}%")
    print()
    print(f"  Positions : {p['count']}/{MAX_STOCK_POSITIONS} ({p['slots_available']} slots free)")

    if p["stocks"]:
        print(f"\n  STOCKS:")
        for s in p["stocks"]:
            pl = s["unrealized_pl_pct"]
            pl_str = f"+{pl}%" if pl >= 0 else f"{pl}%"
            days = f"  days={s['days_open']}" if s["days_open"] is not None else ""
            ma10 = f"  10MA={s['ma10']}" if s.get("ma10") else ""
            ma20 = f"  20MA={s['ma20']}" if s.get("ma20") else ""
            ma50 = f"  50MA={s['ma50']}" if s.get("ma50") else ""
            print(f"    {s['symbol']:8s}  qty={s['qty']}  entry=${s['entry_price']}  now=${s['current_price']}  P&L={pl_str}{days}")
            print(f"    {'':8s}{ma10}{ma20}{ma50}")

    if result["open_orders"]:
        print(f"\n  OPEN ORDERS ({len(result['open_orders'])}):")
        for o in result["open_orders"]:
            stop = f"  stop=${o['stop_price']}" if o["stop_price"] else ""
            limit = f"  limit=${o['limit_price']}" if o["limit_price"] else ""
            print(f"    {o['symbol']:8s}  {o['side']:4s}  {o['type']}{stop}{limit}")
    else:
        print(f"\n  OPEN ORDERS: none")

    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()

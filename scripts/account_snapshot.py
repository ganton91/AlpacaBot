#!/usr/bin/env python3
"""
Account Snapshot (Step 2 of the swing trading bot).

Fetches account info, open positions, and open orders from Alpaca.
Calculates available slots and portfolio exposure.

Usage:
    python scripts/account_snapshot.py
    python scripts/account_snapshot.py --json
"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from broker.client import get_trading_client
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import QueryOrderStatus

MAX_STOCK_POSITIONS = 5
MAX_CRYPTO_POSITIONS = 2


def is_crypto(symbol: str) -> bool:
    return "/" in symbol


def run() -> dict:
    client = get_trading_client()

    account = client.get_account()
    equity = float(account.equity)
    cash = float(account.cash)
    buying_power = float(account.buying_power)

    positions = client.get_all_positions()
    stock_positions = [p for p in positions if not is_crypto(p.symbol)]
    crypto_positions = [p for p in positions if is_crypto(p.symbol)]

    positions_value = sum(float(p.market_value) for p in positions)
    exposure_pct = round((positions_value / equity) * 100, 1) if equity > 0 else 0

    orders = client.get_orders(GetOrdersRequest(status=QueryOrderStatus.OPEN))

    return {
        "account": {
            "equity": round(equity, 2),
            "cash": round(cash, 2),
            "buying_power": round(buying_power, 2),
            "exposure_pct": exposure_pct,
        },
        "positions": {
            "stock_count": len(stock_positions),
            "crypto_count": len(crypto_positions),
            "stock_slots_available": MAX_STOCK_POSITIONS - len(stock_positions),
            "crypto_slots_available": MAX_CRYPTO_POSITIONS - len(crypto_positions),
            "stock": [
                {
                    "symbol": p.symbol,
                    "qty": float(p.qty),
                    "entry_price": float(p.avg_entry_price),
                    "current_price": float(p.current_price),
                    "market_value": float(p.market_value),
                    "unrealized_pl_pct": round(float(p.unrealized_plpc) * 100, 2),
                }
                for p in stock_positions
            ],
            "crypto": [
                {
                    "symbol": p.symbol,
                    "qty": float(p.qty),
                    "entry_price": float(p.avg_entry_price),
                    "current_price": float(p.current_price),
                    "market_value": float(p.market_value),
                    "unrealized_pl_pct": round(float(p.unrealized_plpc) * 100, 2),
                }
                for p in crypto_positions
            ],
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
    print(f"  Stock positions  : {p['stock_count']}/{MAX_STOCK_POSITIONS} ({p['stock_slots_available']} slots free)")
    print(f"  Crypto positions : {p['crypto_count']}/{MAX_CRYPTO_POSITIONS} ({p['crypto_slots_available']} slots free)")

    if p["stock"]:
        print(f"\n  STOCKS:")
        for s in p["stock"]:
            pl = s["unrealized_pl_pct"]
            pl_str = f"+{pl}%" if pl >= 0 else f"{pl}%"
            print(f"    {s['symbol']:8s}  qty={s['qty']}  entry=${s['entry_price']}  now=${s['current_price']}  P&L={pl_str}")

    if p["crypto"]:
        print(f"\n  CRYPTO:")
        for c in p["crypto"]:
            pl = c["unrealized_pl_pct"]
            pl_str = f"+{pl}%" if pl >= 0 else f"{pl}%"
            print(f"    {c['symbol']:10s}  qty={c['qty']}  entry=${c['entry_price']}  now=${c['current_price']}  P&L={pl_str}")

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

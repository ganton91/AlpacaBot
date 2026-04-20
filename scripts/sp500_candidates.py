#!/usr/bin/env python3
"""
S&P 500 Candidate Scanner.

Screens all S&P 500 constituents against the Minervini Trend Template (9 criteria).
Uses batch fetching for efficiency. Run as part of Step 4 to build the base-breakout
candidate universe.

Output format matches trend_template.py for compatibility.

Usage:
    python scripts/sp500_candidates.py
    python scripts/sp500_candidates.py --json
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

SP500_SYMBOLS = [
    # Technology
    "AAPL", "MSFT", "NVDA", "AVGO", "ORCL", "CRM", "AMD", "QCOM", "TXN", "INTC",
    "AMAT", "LRCX", "KLAC", "MU", "ADI", "MCHP", "CDNS", "SNPS", "FTNT",
    "PANW", "CRWD", "ZBRA", "TEL", "APH", "GLW", "HPQ", "HPE", "CSCO", "IBM",
    "ACN", "IT", "CTSH", "CDW", "LDOS", "SAIC", "DXC", "MSI", "NTAP",
    "WDC", "STX", "KEYS", "TDY", "TRMB", "FFIV", "AKAM", "VRT", "GEN", "GDDY",
    # Software & Internet
    "GOOGL", "GOOG", "META", "AMZN", "NFLX", "ADBE", "INTU", "NOW", "WDAY", "TEAM",
    "OKTA", "ZS", "DDOG", "MDB", "SNOW", "HUBS", "VEEV", "PAYC", "PCTY", "CPRT",
    "ANGI", "ZG", "TTD", "RBLX", "U", "MTCH", "IAC", "LYV", "TWLO", "DOCN",
    # Financials
    "JPM", "BAC", "WFC", "GS", "MS", "C", "BLK", "SCHW", "AXP", "COF",
    "SYF", "USB", "PNC", "TFC", "RF", "KEY", "HBAN", "CFG", "MTB",
    "FITB", "MCO", "SPGI", "CME", "ICE", "NDAQ", "CBOE", "BX", "KKR", "APO",
    "CG", "BAM", "TROW", "BEN", "IVZ", "STT", "BK", "NTRS", "AMP", "PRU",
    "MET", "AFL", "ALL", "PGR", "TRV", "CB", "HIG", "MMC", "AON", "AJG", "WTW",
    # Healthcare
    "UNH", "LLY", "JNJ", "ABBV", "PFE", "MRK", "BMY", "AMGN", "GILD", "BIIB",
    "REGN", "VRTX", "ISRG", "BSX", "MDT", "ABT", "SYK", "BDX", "BAX", "EW",
    "IDXX", "MTD", "WAT", "A", "DXCM", "PODD", "IQV", "CRL", "HCA", "THC",
    "UHS", "CNC", "MOH", "HUM", "CVS", "CI", "ELV", "MCK", "CAH", "COR",
    # Consumer Discretionary
    "TSLA", "HD", "MCD", "NKE", "SBUX", "TJX", "LOW", "BKNG", "CMG", "ABNB",
    "UBER", "LYFT", "EXPE", "MAR", "HLT", "H", "WH", "RCL", "CCL", "NCLH",
    "DRI", "YUM", "QSR", "DPZ", "ROST", "TGT", "DHI", "LEN", "PHM", "NVR",
    "TOL", "F", "GM", "APTV", "LKQ", "AZO", "ORLY", "KMX", "AN", "PAG",
    "TSCO", "BBY", "W", "ETSY", "EBAY", "AMZN",
    # Consumer Staples
    "PG", "KO", "PEP", "MDLZ", "PM", "MO", "KHC", "GIS", "CAG",
    "HRL", "MKC", "CLX", "CHD", "EL", "KMB", "CL", "WMT", "COST", "TGT",
    "KR", "SFM", "CASY", "GO",
    # Energy
    "XOM", "CVX", "COP", "EOG", "SLB", "PSX", "VLO", "MPC", "DVN",
    "APA", "FANG", "EQT", "OXY", "TRGP", "LNG", "KMI", "WMB", "ET",
    "EPD", "HAL", "BKR", "NOV", "FTI",
    # Industrials
    "GE", "HON", "RTX", "LMT", "NOC", "GD", "BA", "LHX", "CAT", "DE",
    "EMR", "ETN", "ROK", "PH", "ITW", "GWW", "SNA", "PNR", "IR", "XYL",
    "IDEX", "ROP", "AME", "FTV", "GNRC", "CARR", "OTIS", "TT", "JCI", "FAST",
    "GPC", "ALLE", "AYI", "TREX", "BLDR", "MLM", "VMC", "NUE", "STLD", "CMC",
    "RSG", "WM", "CSGP", "CPRT", "VRSK", "EXPD", "XPO", "CHRW", "JBHT", "UPS",
    "FDX", "DAL", "UAL", "AAL", "LUV", "ALK", "JBLU", "SAVE",
    # Materials
    "LIN", "APD", "DD", "DOW", "EMN", "CE", "MOS", "CF", "NTR", "FMC",
    "CTVA", "BG", "ADM", "FCX", "NEM", "AEM", "WPM", "SCCO", "RS",
    "PKG", "IP", "SEE", "BALL", "AVY", "AMCR",
    # Utilities
    "NEE", "DUK", "SO", "AEP", "EXC", "SRE", "D", "PPL", "XEL", "WEC",
    "ES", "CMS", "ETR", "LNT", "AEE", "OGE", "AWK", "PCG",
    # REITs
    "AMT", "PLD", "CCI", "EQIX", "PSA", "EQR", "AVB", "ESS", "MAA", "UDR",
    "CPT", "O", "WPC", "VICI", "GLPI", "WELL", "VTR", "ARE", "BXP", "SLG",
    "KIM", "REG", "FRT", "SPG", "MAC", "TCO", "CBL",
    # Communication Services
    "DIS", "CMCSA", "CHTR", "T", "VZ", "TMUS", "NWSA", "NWS", "FOXA", "FOX",
    "OMC", "IPG", "WPP", "TTGT", "ZD", "IAC", "MSGS",
]

# Remove duplicates while preserving order
SP500_SYMBOLS = list(dict.fromkeys(SP500_SYMBOLS))


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
    """Returns {symbol: (closes, highs, lows, volumes)} for symbols with sufficient data."""
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
    except Exception:
        return {}


def screen(symbol: str, closes, highs, lows, volumes) -> dict | None:
    price = closes[-1]

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
    client = get_data_client()
    passed = []
    failed = []
    errors = []

    batches = [SP500_SYMBOLS[i:i + BATCH_SIZE] for i in range(0, len(SP500_SYMBOLS), BATCH_SIZE)]

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
        "total":        len(SP500_SYMBOLS),
    }


def main():
    parser = argparse.ArgumentParser(description="S&P 500 Trend Template Screener")
    parser.add_argument("--json", action="store_true", help="Print JSON only")
    args = parser.parse_args()

    result = run()

    if args.json:
        print(json.dumps(result))
        return

    print(f"\n{'='*55}")
    print(f"  S&P 500 CANDIDATE SCANNER")
    print(f"{'='*55}")
    print(f"  Universe : {result['total']} symbols")
    print(f"  Passed   : {result['passed_count']}")
    print(f"  Failed   : {result['failed_count']}")
    if result["errors"]:
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

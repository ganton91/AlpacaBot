import os
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest, StockMarketMoversRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.trading.client import TradingClient


def get_data_client() -> StockHistoricalDataClient:
    return StockHistoricalDataClient(
        api_key=os.environ["ALPACA_API_KEY"],
        secret_key=os.environ["ALPACA_SECRET_KEY"],
    )


def get_trading_client() -> TradingClient:
    paper = os.environ.get("ALPACA_PAPER", "true").lower() == "true"
    return TradingClient(
        api_key=os.environ["ALPACA_API_KEY"],
        secret_key=os.environ["ALPACA_SECRET_KEY"],
        paper=paper,
    )

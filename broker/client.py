import os
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.historical.screener import ScreenerClient
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import CreateWatchlistRequest, UpdateWatchlistRequest


def get_data_client() -> StockHistoricalDataClient:
    return StockHistoricalDataClient(
        api_key=os.environ["ALPACA_API_KEY"],
        secret_key=os.environ["ALPACA_SECRET_KEY"],
    )


def get_screener_client() -> ScreenerClient:
    return ScreenerClient(
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


# ---------------------------------------------------------------------------
# Watchlist helpers
# ---------------------------------------------------------------------------

def get_watchlists() -> list:
    """Returns all watchlists. Note: assets are NOT populated — use get_watchlist_symbols()."""
    return get_trading_client().get_watchlists()


def get_watchlist_symbols(name: str) -> tuple[str | None, list[str]]:
    """Returns (watchlist_id, list of symbols) for the named watchlist, or (None, []) if not found."""
    client = get_trading_client()
    for wl in client.get_watchlists():
        if wl.name == name:
            full = client.get_watchlist_by_id(wl.id)
            symbols = [a.symbol for a in (full.assets or [])]
            return str(wl.id), symbols
    return None, []


def create_watchlist(name: str, symbols: list[str] | None = None) -> object:
    return get_trading_client().create_watchlist(
        CreateWatchlistRequest(name=name, symbols=symbols or [])
    )


def add_to_watchlist(watchlist_id: str, symbol: str) -> object:
    client = get_trading_client()
    full = client.get_watchlist_by_id(watchlist_id)
    existing = [a.symbol for a in (full.assets or [])]
    if symbol not in existing:
        new_symbols = existing + [symbol]
        return client.update_watchlist_by_id(
            watchlist_id,
            UpdateWatchlistRequest(name=full.name, symbols=new_symbols)
        )


def remove_from_watchlist(watchlist_id: str, symbol: str) -> object:
    client = get_trading_client()
    full = client.get_watchlist_by_id(watchlist_id)
    existing = [a.symbol for a in (full.assets or [])]
    if symbol in existing:
        new_symbols = [s for s in existing if s != symbol]
        return client.update_watchlist_by_id(
            watchlist_id,
            UpdateWatchlistRequest(name=full.name, symbols=new_symbols)
        )

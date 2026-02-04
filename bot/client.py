import logging
from binance.client import Client

logger = logging.getLogger(__name__)

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"
        logger.info("Binance Futures client initialized (spot ping prod, futures testnet)")

    def place_order(self, order_params: dict):
        logger.info(f"Order request: {order_params}")
        self.client.futures_create_order(**order_params)

    def get_latest_order(self, symbol: str):
        orders = self.client.futures_get_all_orders(
            symbol=symbol,
            limit=1
        )
        return orders[-1] if orders else None

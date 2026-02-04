import argparse
import logging
import os
import time

from dotenv import load_dotenv

from bot.client import BinanceFuturesClient
from bot.orders import create_order_payload
from bot.logging_config import setup_logging


def main():
    # Load environment variables and setup logging
    load_dotenv()
    setup_logging()

    logger = logging.getLogger("CLI")

    # CLI arguments
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g. BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float, required=False)

    args = parser.parse_args()

    try:
        # Load API keys
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise RuntimeError("API keys not found in environment variables")

        # Initialize client
        client = BinanceFuturesClient(api_key, api_secret)

        # Create validated order payload
        order_payload = create_order_payload(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        # Print order request summary
        print("\nOrder Request Summary")
        print("---------------------")
        for k, v in order_payload.items():
            print(f"{k}: {v}")

        # Place order
        client.place_order(order_payload)

        # Futures Testnet is eventually consistent
        time.sleep(2)

        # Fetch latest order details
        response = client.get_latest_order(args.symbol)

        print("\nOrder Response")
        print("--------------")

        if response is None:
            print("⚠️ Order placed, but details not returned by Binance Futures Testnet.")
            print("Please check order history in the Futures Testnet UI.")
        else:
            print(f"Order ID     : {response.get('orderId')}")
            print(f"Status       : {response.get('status')}")
            print(f"Executed Qty : {response.get('executedQty')}")
            print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")

        print("\n✅ Order placed successfully")

    except Exception as e:
        logger.exception("Execution failed")
        print("\n❌ Order failed:", e)


if __name__ == "__main__":
    main()

# Binance Futures Testnet Trading Bot

A small Python CLI application that places orders on Binance Futures Testnet (USDT-M). The project demonstrates clean structure, input validation, logging, and basic error handling while interacting with a real external API.

## Overview

This application allows placing MARKET and LIMIT orders on Binance Futures Testnet using command-line arguments. It is intentionally kept simple and focused on correctness, structure, and reliability rather than trading strategies.

## Features

* Market and Limit order placement
* BUY and SELL support
* Command-line interface using `argparse`
* Input validation with clear error messages
* Separation of concerns (CLI, validation, API client)
* Logging of API requests, responses, and failures
* Graceful handling of Binance Futures Testnet instability

## Project Structure
```
trading_bot/
├── bot/
│   ├── client.py          # Binance Futures API wrapper
│   ├── orders.py          # Order payload creation
│   ├── validators.py      # Input validation
│   └── logging_config.py  # Logging setup
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── README.md
├── logs/                  # Runtime logs (gitignored)
└── .env                   # API credentials (gitignored)
```

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/binance-futures-testnet-bot.git
cd binance-futures-testnet-bot
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Binance Futures Testnet Configuration

1. Register at: https://testnet.binancefuture.com
2. Create API credentials:
   * Enable Futures
   * No IP restriction required
3. Add test USDT balance from the testnet wallet
4. Create a `.env` file in the project root:
```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret
```

The `.env` file is excluded from version control.

## Usage

### Market Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 100000
```

## Output

The application prints:
* Order request summary
* Order response details (when available):
   * Order ID
   * Status
   * Executed quantity
   * Average price

## Logging

All API interactions and errors are logged to:
```
logs/trading_bot.log
```

The log file contains:
* One MARKET order
* One LIMIT order

Logs are not committed to GitHub and are provided separately as part of submission.

## Notes on Testnet Behavior

Binance Futures Testnet is occasionally inconsistent. In some cases, order placement succeeds but the API does not immediately return order details.

The application:
* Logs all requests
* Avoids crashes on empty responses
* Clearly informs the user when order details are unavailable

This behavior is specific to testnet and not production environments.

## Assumptions

* Python 3.9 or higher
* Active Binance Futures Testnet account
* Sufficient test USDT balance

## Tech Stack

* Python 3
* python-binance
* argparse
* logging
* python-dotenv

## Author

Python Developer application task submission.

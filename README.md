# Binance Futures Testnet Trading Bot

A Python command-line application for placing orders on **Binance Futures Testnet (USDT-M)**.  
The project demonstrates clean code structure, CLI input handling, logging, and interaction with a real external API.

---

## Overview

This application allows users to place **MARKET** and **LIMIT** orders on Binance Futures Testnet using simple command-line arguments.

The goal of the project is not to implement trading strategies, but to showcase:
- clean separation of concerns
- reliable API interaction
- proper logging and error handling

---

## Features

- Place MARKET and LIMIT orders
- Supports BUY and SELL sides
- Command-line interface using `argparse`
- Input validation for order parameters
- Structured codebase (client, validation, order logic)
- Logging of API requests and errors
- Graceful handling of Binance Testnet inconsistencies

---

## Project Structure

```text
trading_bot/
├── bot/
│   ├── client.py          # Binance Futures API wrapper
│   ├── orders.py          # Order payload creation
│   ├── validators.py      # Input validation
│   └── logging_config.py  # Logging configuration
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── README.md
├── logs/                  # Runtime logs (ignored by git)
└── .env                   # API credentials (ignored by git)

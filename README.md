# Binance Futures Trading Bot

A Python-based trading bot for Binance Futures Testnet (USDT-M) that supports Market and Limit orders with CLI input, logging, and validation.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Binance Futures Testnet integration
- Command Line Interface (CLI)
- Input validation
- Exception handling
- Logging system
- Clean project structure

---

## Tech Stack

- Python 3.x
- python-binance
- python-dotenv
- argparse
- logging

---

## Project Structure

```bash
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── requirements.txt
├── .gitignore
└── README.md
---
## Setup Instructions
1. Clone Repository
git clone https://github.com/Sunlight8169/binance-futures-trading-bot.git

2. Create Virtual Environment
python -m venv venv

Activate virtual environment:
Windows
  venv\Scripts\activate

3. Install Dependencies
  pip install -r requirements.txt

 ## API Configuration

  Create a .env file in the project root:
    BINANCE_API_KEY=your_api_key
    BINANCE_SECRET_KEY=your_secret_key

## Run Examples
  MARKET BUY Order
  python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
  LIMIT SELL Order
  python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 90000

## Logging
    Logs are stored in:
    logs/trading_bot.log





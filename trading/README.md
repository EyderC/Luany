# Trading

Algorithmic trading engine for prop firm challenges.
Handles risk management, strategy execution, and backtesting
across BTC/USD, EUR/USD, NQ, and ES markets.

## Modules
- `risk_manager.py` — Enforces challenge rules (drawdown, daily loss)
- `strategy_engine.py` — Generates buy/sell signals
- `backtester.py` — Tests strategies against historical data

## Markets
| Instrument | Exchange | API |
|---|---|---|
| BTC/USD | Binance | REST + WebSocket |
| EUR/USD | OANDA | REST |
| NQ / ES | MetaAPI | REST |

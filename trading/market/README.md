# Markets — API Connectors

Individual connectors for each market Luany trades.
Each connector handles authentication, data fetching,
and order execution for its specific exchange.

## Connectors
| File | Market | Exchange | Data Type |
|---|---|---|---|
| `btc_connector.py` | BTC/USD | Binance | REST + WebSocket |
| `eurusd_connector.py` | EUR/USD | OANDA | REST |
| `nq_connector.py` | E-mini Nasdaq 100 | MetaAPI | REST |
| `es_connector.py` | E-mini S&P 500 | MetaAPI | REST |

## Note
Never hardcode API keys here. All credentials
are loaded from the `.env` file at root level.

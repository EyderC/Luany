import requests
import json
from datetime import datetime

URL = 'https://api.binance.com/api/v3/ticker/price'

def get_btc_price():
    params = {'symbol': 'BTCUSDT'}
    response = requests.get(URL, params=params) 
    response.raise_for_status()
    return float(response.json()['price'])
    
def format_price(price):
    timestamp = datetime.now().strftime('%H:%M:%S')
    return f'[{timestamp}] BTC/USD: ${price:,.2f}'

def main():
    try:
        price = get_btc_price()
        data = format_price(price)
        print(data)
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
    except json.JSONDecodeError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main()


import requests
import pandas as pd

from config import (
    URL_PRICE,
    SYMBOLS,
    TOKEN
)


def main():
    results = {
        'stock_symbol': [],
        'percentage_change': [],
        'current_price': [],
        'last_close_price': []
        }

    for symbol in SYMBOLS:
        response_price = requests.get(URL_PRICE, params={'symbol': symbol, 'token': TOKEN})
        # print("+ " + symbol)

        results['stock_symbol'].append(symbol)
        results['percentage_change'].append(response_price.json()['dp'])
        results['current_price'].append(response_price.json()['c'])
        results['last_close_price'].append(response_price.json()['o'])
        df = pd.DataFrame(results, columns=['stock_symbol', 'percentage_change', 'current_price', 'last_close_price'])
        df.to_csv('most_volatile_stock.csv', index=False)

    print(df)

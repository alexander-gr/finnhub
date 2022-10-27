import requests
import pandas as pd

from config import (
    URL_PRICE,
    URL_PROFILE,
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
        response_profile = requests.get(URL_PROFILE, params={'symbol': symbol, 'token': TOKEN})
        response_price = requests.get(URL_PRICE, params={'symbol': symbol, 'token': TOKEN})
        print("+ " + str(response_profile.json()['ticker']))

        results['stock_symbol'].append(response_profile.json()['ticker'])
        results['percentage_change'].append(response_price.json()['dp'])
        results['current_price'].append(response_price.json()['c'])
        results['last_close_price'].append(response_price.json()['o'])
        df = pd.DataFrame(results, columns=['stock_symbol', 'percentage_change', 'current_price', 'last_close_price'])
        df.to_csv('most_volatile_stock.csv', index=False)

    df2 = pd.read_csv('most_volatile_stock.csv')
    print(df2)

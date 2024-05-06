#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import time

def fetch_stock_price(symbol):
    # Use an appropriate API to fetch the stock price
    # For example, using Alpha Vantage API
    api_key = 'your_api_key'
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    try:
        response = requests.get(url)
        data = response.json()
        if 'Global Quote' in data:
            return float(data['Global Quote']['05. price'])
        else:
            raise KeyError("'Global Quote' key not found in API response.")
    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def check_stock_prices(symbols, interval):
    prev_prices = {symbol: fetch_stock_price(symbol) for symbol in symbols}
    while True:
        time.sleep(interval)
        print("\nCurrent Stock Prices:")
        for symbol in symbols:
            current_price = fetch_stock_price(symbol)
            if current_price is not None:
                prev_price = prev_prices[symbol]
                if current_price > prev_price:
                    movement = "UP"
                elif current_price < prev_price:
                    movement = "DOWN"
                else:
                    movement = "UNCHANGED"
                print(f"{symbol}: {current_price} ({movement})")
                prev_prices[symbol] = current_price

if __name__ == "__main__":
    symbols = input("Enter stock symbols (separated by commas): ").split(",")
    interval = int(input("Enter check interval in seconds: "))
    check_stock_prices(symbols, interval)


# In[ ]:





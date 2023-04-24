import json
import sys

with open('stocks.json') as f:
    stocks = json.load(f)

portfolio = {}
for arg in sys.argv[2:]:
    ticker, quantity = arg.split(':')
    portfolio[ticker] = int(quantity)

total_value = 0
for ticker, quantity in portfolio.items():
    for stock in stocks:
        if stock['ticker'] == ticker:
            total_value += stock['close'] * quantity
            break

print(total_value)

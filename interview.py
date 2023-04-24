import json
import argparse

with open('stocks.json') as f:
    stocks = json.load(f)

def calculate_portfolio_value(args):
    portfolio = {}
    for arg in args:
        ticker, quantity = arg.split(':')
        portfolio[ticker] = int(quantity)

    total_value = 0
    for ticker, quantity in portfolio.items():
        for stock in stocks:
            if stock['ticker'] == ticker:
                total_value += stock['close'] * quantity
                break

    return total_value

def calculate_max_profit(prices):
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate maximum profit from buying and selling a stock or calculate the total value of a portfolio.')
    parser.add_argument('-part1', metavar='<TICKER:QUANTITY>', nargs='+', help='list of ticker and quantity of stocks in portfolio')
    parser.add_argument('-bonus', metavar='<PRICE>', type=str, help='comma-separated list of stock prices')
    args = parser.parse_args()

    if args.part1:
        total_value = calculate_portfolio_value(args.part1)
        print(total_value)
    elif args.bonus:
        prices = list(map(int, args.bonus.split(',')))
        profit = calculate_max_profit(prices)
        print(profit)

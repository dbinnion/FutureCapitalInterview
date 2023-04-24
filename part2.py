import argparse

def max_profit(prices):
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
    parser = argparse.ArgumentParser(description='Calculate maximum profit from buying and selling a stock.')
    parser.add_argument('-bonus', metavar='<PRICE>', type=str, help='comma-separated list of stock prices')
    args = parser.parse_args()
    
    prices = list(map(int, args.bonus.split(',')))
    profit = max_profit(prices)
    
    print(profit)

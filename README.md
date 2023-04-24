# Future Capital Interview
Future Capital Interview Parts 1 and 2

## Requirements:
1. Python 3.x
2. `stocks.json` file in the same directory as the Python scripts.

## Usage:
Open a terminal or command prompt in the directory where the Python script is saved.

# Part 1
This Python script reads stock information from a JSON file and calculates the total value of a given stock portfolio based on ticker symbols and quantities provided as a command line argument.

1. Run the following command:
`python interview.py -part1 "<TICKER>:<QUANTITY>,<TICKER>:<QUANTITY>,..."`
2. Replace `<TICKER>` and `<QUANTITY>` with the ticker symbol and quantity for each stock in your portfolio, separated by commas. You can specify as many stocks as you like, as long as they are separated by commas.

Example: `python interview.py -part1 "FB:12,PLTR:5000"`  
This will calculate the total value of a portfolio containing 12 shares of Facebook and 5,000 shares of Palantir.

The program will output the total value of the portfolio, in the format <TOTAL>.  
Example: `119887.4`  
This means the total value of the portfolio is $119,887.40.


# Part 2
Open a terminal or command prompt in the directory where the Python script is saved.

1. Run the following command:
`python interview.py -bonus "<PRICE>"`  
2. Replace `<PRICE>` with a comma-separated list of stock prices, in chronological order.

Example: `python interview.py -bonus "7,1,5,3,6,4"`  
This will calculate the maximum profit that can be made by buying and selling a single stock on different days, given the prices 7, 1, 5, 3, 6, and 4.

The program will output the maximum profit that can be made, in the format <PROFIT>.  
Example: `5`  
This means the maximum profit that can be made is $5.

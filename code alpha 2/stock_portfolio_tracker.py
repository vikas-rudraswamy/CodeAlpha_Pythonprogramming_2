#stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 3400,
    "MSFT": 320
}

total_investment = 0

print("Stock Portfolio Tracker")

# Number of stocks user wants to enter
n = int(input("How many stocks do you want to add? "))

for i in range(n):
    stock = input("Enter stock name (AAPL/TSLA/GOOG/AMZN/MSFT): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        total_investment += investment
        print("Investment for", stock, "=", investment)
    else:
        print("Stock not found in price list")

print("\nTotal Investment Value =", total_investment)

# Optional: Save result to file
file = open("portfolio.txt", "w")
file.write("Total Investment Value = " + str(total_investment))
file.close()

print("Result saved to portfolio.txt")
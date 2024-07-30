import yfinance as yf
import pandas as pd

# Initialize an empty portfolio
portfolio = {}


def add_stock(symbol, quantity):
    if symbol in portfolio:
        portfolio[symbol]['quantity'] += quantity
    else:
        portfolio[symbol] = {'quantity': quantity}


def remove_stock(symbol, quantity):
    if symbol in portfolio:
        if portfolio[symbol]['quantity'] >= quantity:
            portfolio[symbol]['quantity'] -= quantity
            if portfolio[symbol]['quantity'] == 0:
                del portfolio[symbol]
        else:
            print("Not enough quantity to remove.")
    else:
        print("Stock not found in portfolio.")


def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    return stock.history(period="1d")['Close'].iloc[-1]


def track_portfolio():
    data = []
    for symbol, info in portfolio.items():
        price = get_stock_price(symbol)
        total_value = price * info['quantity']
        data.append({
            'Symbol': symbol,
            'Quantity': info['quantity'],
            'Price': price,
            'Total Value': total_value
        })
    df = pd.DataFrame(data)
    return df


def display_portfolio(df):
    print("\nYour Portfolio:")
    print(df.to_string(index=False))


def main():
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            add_stock(symbol, quantity)
            print(f"Added {quantity} of {symbol} to your portfolio.")

        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            remove_stock(symbol, quantity)
            print(f"Removed {quantity} of {symbol} from your portfolio.")

        elif choice == '3':
            df = track_portfolio()
            display_portfolio(df)

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()

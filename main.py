# main.py

from data import get_stock_data

def main():
    ticker = input("Enter stock ticker (e.g., AAPL): ")
    
    data = get_stock_data(ticker)
    
    print("\nStock Data Preview:")
    print(data.head())

if __name__ == "__main__":
    main()

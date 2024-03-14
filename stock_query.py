import requests

# API KEY: C70QWUENAT21S0SB

while True:
    stock_symbol_input = input("Enter the stock symbol you are looking for: ").upper()

    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol_input}&interval=5min&apikey=C70QWUENAT21S0SB"
    
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        
        if "Error Message" in data:
            print("Invalid stock symbol. Please enter a valid stock symbol.")
        else:
            print(data)
            break
    

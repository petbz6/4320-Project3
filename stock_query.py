import requests

# API KEY: C70QWUENAT21S0SB

def get_stock_data():
    while True:
        print("Stock Data Visualizer")
        print("--------------------------- \n")
        stock_symbol_input = input("Enter the stock symbol you are looking for: ").upper()

        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol_input}&interval=5min&apikey=C70QWUENAT21S0SB'
        r = requests.get(url)
        
        if r.status_code == 200:
            data = r.json()
            if "Error Message" in data:
                print("Invalid stock symbol. Please enter a valid stock symbol.")
            else:
                return data

# Get chart function prompting users for desired chart type
def get_chart_type():
    while True:
        print("\nSelect the chart type:")
        print("1. Bar")
        print("2. Line")
        chart_type_input = input("Enter selection (1-2): ")
        if chart_type_input in ['1', '2']:
            return int(chart_type_input)
        else:
            print("Invalid input. Please enter either 1 or 2.")

# Function prompting users for desired time series function
def get_time_series():
    while True:
        print("\nSelect the time series function:")
        print("1. INTRADAY")
        print("2. DAILY")
        print("3. WEEKLY")
        print("4. MONTHLY")
        time_series_function_input = input("Enter time series optiona (1-4): ")
        if time_series_function_input in ['1', '2', '3', '4']:
            return int(time_series_function_input)
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

stock_data = get_stock_data()
chart_type = get_chart_type()
time_series_function = get_time_series()
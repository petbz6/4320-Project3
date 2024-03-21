def generate_graph(data, type, time_series, begin, end):
    import pygal
    from datetime import datetime
    
    begin_date = datetime.strptime(begin, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")

    stock_data = data["Time Series (5min)"]

    filtered_data = {time: price for time, price in stock_data.items() 
                     if begin_date <= datetime.strptime(time, "%Y-%m-%d %H:%M:%S") <= end_date}

    dates = [time for time in filtered_data.keys()]
    prices = [price[-"5. volume"] for price in filtered_data.values()]

    if type.lower() == "line":
        chart = pygal.Line()
    else:
        chart = pygal.Bar()
    
    chart.title = data["Meta Data"]["2. Symbol"]
    chart.x_labels = dates
    chart.add("Price", prices)
    
    
    return chart.render_in_browser()

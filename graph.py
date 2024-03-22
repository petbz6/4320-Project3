def generate_graph(data, type, time_series, begin, end):
    import pygal
    from datetime import datetime
    

    stock_data = data["Time Series (5min)"]


    filtered_data = {time: price for time, price in stock_data.items() 
                     if begin <= datetime.strptime(time, "%Y-%m-%d %H:%M:%S") <= end}

    print(filtered_data)

    dates = [time for time in filtered_data.keys()]
    prices = [price for price in filtered_data.values()]


    if type == 1:
        chart = pygal.Line()
    else:
        chart = pygal.Bar()
    
    chart.title = data["Meta Data"]["2. Symbol"]
    chart.x_labels = dates
    chart.add("Price", prices)
    
    chart.render_in_browser()
    return

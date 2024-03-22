import stock_query
import date
import graph

data = stock_query.get_stock_data()
chart_type = stock_query.get_chart_type()
time_series = stock_query.get_time_series()
start, end = date.main()
graph.generate_graph(data, chart_type, time_series, start, end)

# time series data
from bokeh.plotting import figure, output_file, show
import pandas as pd
from bokeh.models import HoverTool, ColumnDataSource
df = pd.read_csv(
    'Python-Mega-Course/DataVisualizationApp/adbe.csv', parse_dates=['Date'])

col_data = ColumnDataSource(df)
p = figure(width=500, height=500, x_axis_type='datetime')


hover = HoverTool(tooltips=[('High', '@High')])
p.add_tools(hover)
p.line(x='Date', y='Close', source=col_data, color='Orange', alpha=0.5, )

output_file('TimeSeries.html')
show(p)

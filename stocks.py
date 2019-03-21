import numpy as np

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file

def datetime(x):
    return np.array(x, dtype=np.datetime64)


def stocks(closing=True, adjusted_closing=True, opening=True):
    adj_close = np.array(AAPL['adj_close'])
    close = np.array(AAPL['close'])
    std_open = np.array(AAPL['open'])
    aapl_dates = np.array(AAPL['date'], dtype=np.datetime64)
    p2 = figure(x_axis_type="datetime", title="AAPL One-Month Average")
    p2.grid.grid_line_alpha = 0
    p2.xaxis.axis_label = 'Date'
    p2.yaxis.axis_label = 'Price'
    p2.ygrid.band_fill_color = "olive"
    p2.ygrid.band_fill_alpha = 0.1

    if closing:
        p2.line(aapl_dates, close, legend='close',
                color='darkblue')

    if adjusted_closing:
        p2.line(aapl_dates, adj_close, legend='adjusted close',
                color='blue')
    
    if opening:
        p2.line(aapl_dates, std_open, legend='open',
                color='darkred')

    p2.legend.location = "top_left"

    return p2
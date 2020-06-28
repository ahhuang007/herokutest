from flask import Flask, render_template, request, redirect
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
from bokeh.plotting import Figure, reset_output
from bokeh.models import ColumnDataSource, Div
from bokeh.io import output_file, show, output_notebook

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        #request was a POST
        ticker = request.form['ticker']
        selected = request.form.getlist('op')
        df = get_data(ticker, selected)
        
        pl = plot(df, selected)
        show(pl)
        return 'request.method was not a GET!'
    


@app.route('/about')
def about():
    return render_template('about.html')

def get_data(ticker, selected):
    ts = TimeSeries(key = '0XCC85R5V2ICKQVP', output_format = 'pandas', indexing_type = 'integer')
    df, meta = ts.get_daily(symbol = ticker, outputsize = 'full')
    #Probably inefficient but who cares
    if 'open' not in selected:
        df.drop("1. open", 1, inplace = True)
    if 'close' not in selected:
        df.drop("4. close", 1, inplace = True)
    if 'high' not in selected:
        df.drop("2. high", 1, inplace = True)
    if 'low' not in selected:
        df.drop("3. low", 1, inplace = True)
    return df

def plot(df, selected):
    reset_output(state = None)
    
    
    p = Figure(title = "Past 100 days Of Whatever Stock You Searched", x_axis_label = "Date", x_axis_type = 'datetime', 
                  y_axis_label = "Price", plot_width = 800, plot_height = 700)
    p.title.text_font = "arial"
    p.title.text_font_style = "bold"
    p.title.text_font_size = "12pt"
    p.title.align = "center"
    p.xaxis.axis_label_text_font = "arial"
    p.xaxis.axis_label_text_font_size = "10pt"
    p.xaxis.axis_label_text_font_style = "bold"
    p.yaxis.axis_label_text_font = "arial"
    p.yaxis.axis_label_text_font_size = "10pt"
    p.yaxis.axis_label_text_font_style = "bold"
    p.min_border_left = 0
    
    df["index"] = pd.to_datetime(df["index"])
    
    if 'open' in selected:
        p.line(df["index"][0:101], df["1. open"][0:101], color = "navy", alpha = 0.75, legend_label = "Open")
    if 'close' in selected:
        p.line(df["index"][0:101], df["4. close"][0:101], color = "green", alpha = 0.75, legend_label = "Close")
    if 'high' in selected:
        p.line(df["index"][0:101], df["2. high"][0:101], color = "red", alpha = 0.75, legend_label = "High")
    if 'low' in selected:
        p.line(df["index"][0:101], df["3. low"][0:101], color = "purple", alpha = 0.75, legend_label = "Low")
    
    p.legend.location = "bottom_right"
    return p

@app.route('/plot')
def display():
    return None

if __name__ == '__main__':
    app.run(port=33507, debug = True)

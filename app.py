from flask import Flask, render_template, request, redirect

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
        df.to_csv('test.csv')
        return 'request.method was not a GET!'
    


@app.route('/about')
def about():
    return render_template('about.html')

def get_data(ticker, selected):
    ts = TimeSeries(key = '0XCC85R5V2ICKQVP', output_format = 'pandas', indexing_type = 'integer')
    df = ts.get_daily(symbol = ticker, interval = '24hr', outputsize = 'full')
    return df

def plot():
    return None

if __name__ == '__main__':
    app.run(port=33507, debug = True)

from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.vars = {}

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        #request was a POST
        app.vars['ticker'] = request.form['ticker']
        selected = request.form.getlist('op')
        #any_sel = bool(selected)
        #app.vars['open'] = request.form['open']
        #app.vars['close'] = request.form['close']
        #app.vars['high'] = request.form['high']
        #app.vars['low'] = request.form['low']
        print(selected)
        
        #f.write('open: %s\n\n'%(app.vars['open']))
        #f.write('close: %s\n\n'%(app.vars['close']))
        #f.write('high: %s\n\n'%(app.vars['high']))
        #f.write('low: %s\n\n'%(app.vars['low']))

        return 'request.method was not a GET!'
    


@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(port=33507, debug = True)

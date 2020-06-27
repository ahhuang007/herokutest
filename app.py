from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.vars = {}

@app.route('/index', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(port=33507, debug = True)

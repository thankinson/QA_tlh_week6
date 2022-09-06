from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('layout.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/page2')
def page2():
    return render_template('page2.html', username="tom")




if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
#!/usr/bin/python3
'''starts a Flask web application'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    '''function associated with / route'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    '''function associated with /hbnb route'''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    '''function associated with /c/<text>/ route'''
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>/', strict_slashes=False)
def python_with_text(text="is cool"):
    '''function associated with /python/<text> route'''
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''function associated with /number/n route'''
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''function associated with /number_template/<int:n> route'''
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

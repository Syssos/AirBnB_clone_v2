#!/usr/bin/python3
from flask import Flask
"""
"""
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def display_hello():
    """ Displays Hello Holberton
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def display_hbnb():
    """ Displays HBNB on "/hbnb"
    """
    return "HBNB"


@app.route('/c/<text>')
def C_is_fun(text):
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def python_is(text):
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def isnumor(n):
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

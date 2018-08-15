#!/usr/bin/python3
from flask import Flask
"""
"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello():
    """ Displays Hello Holberton
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Displays HBNB on "/hbnb"
    """
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

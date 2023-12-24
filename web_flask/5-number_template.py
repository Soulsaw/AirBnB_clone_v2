#!/usr/bin/python3
""" Importing the app instance for the running and define the route
"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ This function display hello HBNH! at the route / URL
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ This function display HBNH at the route /hbnb URL
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_fun(text):
    """ This function get a vaeiablw on the URL
    """
    return "C " + text.replace('_', ' ')


@app.route('/python/(<text>)', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python(text="is cool"):
    """ This function get a vaeiablw on the URL
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ This function get a vaeiablw on the URL
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ This function get a vaeiablw on the URL
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    """The entry point of the program
    """
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
""" Importing the app instance for the running and define the route
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ This function display hello HBNH! at the route URL
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    """The entry point of the program
    """
    app.run(host='0.0.0.0', port=5000)

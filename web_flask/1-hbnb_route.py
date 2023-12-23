#!/usr/bin/python3
from . import app
""" Importing the app instance for the running and define the route
"""
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


if __name__ == "__main__":
    """The entry point of the program
    """
    app.run(host='0.0.0.0', port=5000)
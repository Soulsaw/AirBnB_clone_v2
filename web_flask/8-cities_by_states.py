#!/usr/bin/python3
from . import app
from models import storage
from models.state import State
from models.state import City
from flask import render_template
""" Importing the app instance for the running and define the route
"""


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ This function display hello HBNH! at the route URL
    """
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """Operation after session"""
    storage.close()


if __name__ == "__main__":
    """The entry point of the program
    """
    app.run(host='0.0.0.0', port=5000)

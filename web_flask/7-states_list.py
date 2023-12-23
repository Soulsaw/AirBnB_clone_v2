#!/usr/bin/python3
from . import app
from models import storage
from models.state import State
from flask import render_template
""" Importing the app instance for the running and define the route
"""


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ This function display hello HBNH! at the route URL
    """
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """Operation after session"""
    storage.close()


if __name__ == "__main__":
    """The entry point of the program
    """
    app.run(host='0.0.0.0', port=5000)

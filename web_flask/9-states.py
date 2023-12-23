#!/usr/bin/python3
from . import app
from models import storage
from models.state import State
from flask import render_template
""" Importing the app instance for the running and define the route
"""


@app.route('/states', strict_slashes=False)
def states():
    """ This function display hello HBNH! at the route URL
    """
    states = storage.all("State")
    return render_template('9-states.html', states=states)


@app.route('/states/<string:id>', strict_slashes=False)
def states_by_id(id):
    """ This function display hello HBNH! at the route URL
    """
    states = storage.all("State").values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', states=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown(exception):
    """Operation after session"""
    storage.close()


if __name__ == "__main__":
    """The entry point of the program
    """
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
""" Importing the app instance for the running and define the route
"""
from models import storage
from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ This URL display all the states in the database
    """
    states = storage.all("State")
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """ This URL display all the city for a given state id
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

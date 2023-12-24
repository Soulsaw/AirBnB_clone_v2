#!/usr/bin/python3
""" Importing the app instance for the running and define the route
"""
from models import storage
from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ This function display hello HBNH! at the route URL
    """
    states = storage.all("State")
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """Operation after session"""
    storage.close()


if __name__ == "__main__":
    """The entry point of the program
    """
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
""" Importing the app instance for the running and define the route
"""
from models import storage
from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ This function display hello HBNH! at the route URL
    """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities,
                           places=places)


@app.teardown_appcontext
def teardown(exception):
    """Operation after session"""
    storage.close()


if __name__ == "__main__":
    """The entry point of the program
    """
    app.run(host='0.0.0.0', port=5000)

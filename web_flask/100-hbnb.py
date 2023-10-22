#!/usr/bin/python3
"""Start a Flask web application for HBNB project."""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import getenv

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display a web page like 8-index.html."""
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda x: x.name)

    amenities = storage.all(Amenity).values()
    amenities_sorted = sorted(amenities, key=lambda x: x.name)

    places = storage.all(Place).values()
    places_sorted = sorted(places, key=lambda x: x.name)

    return render_template('100-hbnb.html',
                           states=states_sorted,
                           amenities=amenities_sorted,
                           places=places_sorted)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

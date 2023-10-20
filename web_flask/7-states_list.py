#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name)


@app.teardown_appcontext
def close_db_session(exception):
    """Closes the current SQLAlchemy session."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a list of State objects sorted by name."""
    states = storage.all("State")
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""
Script that starts a Flask web application and displays a list of cities by states.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """
    Route to display a list of cities by states.
    """
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda x: x.name)

    return render_template('8-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def teardown(exception):
    """
    Method to close the SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

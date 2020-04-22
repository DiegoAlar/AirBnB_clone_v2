#!/usr/bin/python3
"""
script that starts a Flask web application
"""


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_request(self):
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_list(id=None):
    """ display cities by if id in states """
    all_states = storage.all(State)
    if id:
        for state in all_states.values():
            if state.id == id:
                all_states = state
    return render_template('9-states.html', all_states=all_states, id=id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

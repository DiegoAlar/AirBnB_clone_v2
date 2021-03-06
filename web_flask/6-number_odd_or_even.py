#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """ Returns a message """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_route2():
    """ Returns a message """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_route3(text):
    """ display “C ” followed by the value of the text variable """
    return 'C {}'.format(text.replace('_', ' '))
    # return 'C %s' % text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_route4(text='is cool'):
    """ display “Python ” followed by the value of the text variable """
    return 'Python {}'.format(text.replace('_', ' '))
    # return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def hello_route5(n):
    """ display “n is a number” """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def hello_route6(n):
    """ display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def hello_route7(n):
    """ display a HTML page only if n is an integer """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

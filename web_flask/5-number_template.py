#!/usr/bin/python3
# script that starts a Flask web application

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def C_Is_Fun(text):
    return 'C ' + text.replace('_', ' ')


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>/", strict_slashes=False)
def Python_Is_Cool(text):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/')
@app.route('/number_template/<int:n>')
def number_tamplate(n):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

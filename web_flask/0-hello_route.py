#!/usr/bin/python3

""" import Flask """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ return Hello HBNB! """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()

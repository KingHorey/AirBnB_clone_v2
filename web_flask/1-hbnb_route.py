#!/usr/bin/python3

""" import app variable from __init__"""

import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ display Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_page():
    """ displaY HBNB """
    return "HBNB"


if __name__ == "__main__":
    app.run()

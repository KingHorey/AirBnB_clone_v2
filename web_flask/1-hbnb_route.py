#!/usr/bin/python3

""" import app variable from __init__"""

from flask import Flask
app = Flask(__name__)


app.url_map.strict_slashes = False


@app.route("/")
def home():
    """ display Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb_page():
    """ displaY HBNB """
    return "HBNB"


if __name__ == "__main__":
    app.run()

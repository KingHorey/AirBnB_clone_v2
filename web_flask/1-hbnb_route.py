#!/usr/bin/python3

""" import app variable from __init__"""
from . import app


@app.route("/", methods=["GET", "POST"], strict_slashes=False)
def home():
    """ display Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", methods=["GET", "POST"], strict_slashes=False)
def hbnb_page():
    """ displaY HBNB """
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')

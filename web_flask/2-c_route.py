#!/usr/bin/python3

""" import flask """
from flask import Flask
app = Flask(__name__)


app.route("/", strict_slashes=False)
def home():
    """ home route """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb_page():
    """ hbnb route """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_page():
    """ return c page """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run()

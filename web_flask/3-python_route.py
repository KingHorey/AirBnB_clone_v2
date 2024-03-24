#!/usr/bin/python3

""" import flask """
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    """ home route """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb_page():
    """ hbnb route """
    return "HBNB"


@app.route("/c/<text>")
def c_page(text):
    """ return c page """
    return "C {}".format(text.replace("_", " "))


@app.route("/python/<text>")
def python_page(text="is cool"):
    """ return python page """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run()

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
@app.route("/python")
def python_page(text=None):
    """ return python page """
    if text is None:
        return "Python is cool"
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def get_number(n):
    """ return number page """
    if (isinstance(n, int)):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run()

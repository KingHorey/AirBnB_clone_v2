#!/usr/bin/python3

""" import flask """
from flask import Flask
from flask import render_template
from models import storage

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


@app.route("/number_template/<int:n>")
def return_number(n):
    if (isinstance(n, int)):
        return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_even(n):
    if (isinstance(n, int)):
        if (n % 2 == 0):
            return render_template("6-number_odd_or_even.html",
                                   number=n, odd_even="even")
        else:
            return render_template("6-number_odd_or_even.html",
                                   number=n, odd_even="odd")


@app.teardown_appcontext
def teardown_session(exception):
    """ close session """
    storage.close()


@app.route("/states_list")
def get_states():
    """ get all states from DBStorage"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run()

#!/usr/bin/python3

""" import flask module """
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '2a5b431ad9a2108fbcbf8381a455583ec86a5bac3ed298bc76e696\
9276d7f704b029a42a8aedbc800553d2bb9e4bf02209f440215388f21fb2d41423b9175a33'

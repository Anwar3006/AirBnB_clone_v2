#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def heelo():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C(text):
    try:
        new = ' '.join(text.split('_'))
        return "C %s" % new
    except 404:
        return 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

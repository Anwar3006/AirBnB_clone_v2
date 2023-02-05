#!/usr/bin/python3
"""script that starts a Flask web application: listening on 0.0.0.0, port 5000"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def heelo():
    """display “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display “HBNB”"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """ display “C ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    if text:
        new = ' '.join(text.split('_'))
        return "C %s" % new
    else:
        return 404


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space ) 
    """
    if text:
        new = ''.join(text.split('_'))
        return "Python %s" % new
    else:
        return "Python %s" % text


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    if type(n) is int:
        return "%d is a number" % n
    return 404


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    if type(n) is int:
        return render_template("5-number.html", n=n)
    return 404


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def numberEvenOdd(n):
    """display a HTML page only if n is an integer"""
    if type(n) is int:    
        return render_template("6-number_odd_or_even.html", n=n)
    else:
        return 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

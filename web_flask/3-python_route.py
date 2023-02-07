#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

if __name__ == "__main__":
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
        if text:
            new = ' '.join(text.split('_'))
            return "Python %s" % new
        else:
            return "Python %s" % text

    app.run(debug=True, host="0.0.0.0")

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
    def hello():
        """display “Hello HBNB!”"""
        return "Hello HBNB!"

    app.run(debug=True, host="0.0.0.0")

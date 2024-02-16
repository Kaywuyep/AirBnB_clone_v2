#!/usr/bin/python3
"""Write a script that starts a Flask web application
and would be listening on 0.0.0.0, port 5000"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def function():
    """main or home route
    Routing to root, strict_slashes=False ensures
    the URL works when it ends both with or without the slash /
    Returns:
            [string]: [display “Hello HBNB!”]
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

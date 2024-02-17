#!/usr/bin/python3
"""Write a script that starts a Flask web application
and would be listening on 0.0.0.0, port 5000"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_root():
    """main or home route
    Routing to root, strict_slashes=False ensures
    the URL works when it ends both with or without the slash /
    Returns:
            [string]: [display “Hello HBNB!”]
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_C(text):
    """Routing to C using Variables"""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def hello_python(text="is cool"):
    """
    /python folder - path to folder
    Returns:
            [string]: [display “Python” followed by the
            value of the text variable]
            return 'Python ' + text.replace('_', ' ')
    """
    return "Python {}".format(text).replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def hello_number(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Returns:
            [HTML page]: [display a HTML page only if n is an integer:]
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """
    Returns:
            [HTML page]: [display a HTML page only if n is an integer]
    """
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

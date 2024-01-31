#!/usr/bin/python3
"""
5-number_template.py: Starts a Flask web application.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display 'Hello HBNB!' when the root URL is accessed.

    Returns:
        str: The message 'Hello HBNB!'.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Display 'HBNB' when the '/hbnb' URL is accessed.

    Returns:
        str: The message 'HBNB'.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_custom_text(text):
    """
    Display 'C ', followed by the value of the text variable.

    Args:
        text (str): The text to display.

    Returns:
        str: The message 'C ' followed by the value of the text variable.
    """
    return "C " + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text):
    """
    Display 'Python ', followed by the value of the text variable.

    Args:
        text (str): The text to display.

    Returns:
        str: The message 'Python ' followed by the value of the text variable.
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """
    Display '<n> is a number' if n is an integer.

    Args:
        n (int): The number to display.

    Returns:
        str: The message '<n> is a number' if n is an integer.
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """
    Display an HTML page with the message 'Number: n' if n is an integer.

    Args:
        n (int): The number to display.

    Returns:
        str: The HTML page with 'Number: n' inside an H1 tag.
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

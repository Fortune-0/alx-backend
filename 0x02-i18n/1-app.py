#!/usr/bin/python3
"""A script that starts a flask web application
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask("__name__")


class Config(object):
    """Configuration for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

@app.route('/', strict_slashes=False)
def index() -> str:
    """Return a given string"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)

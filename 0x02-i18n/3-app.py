#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """Class config for babel"""
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get_locale function"""
    return (request.accept_languages.best_match(app.config['LANGUAGES']))


app.config.from_object(Config)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@app.route("/", strict_slashes=False)
def home_page():
    """Render template"""
    return (render_template('3-index.html'))


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')

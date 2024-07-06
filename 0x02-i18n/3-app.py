# #!/usr/bin/env python3
# """Basic Flask app"""
# from flask import Flask, render_template, request
# from flask_babel import Babel, _


# class Config:
#     """Class config for babel"""
#     LANGUAGES = ["en", "fr"]


# app = Flask(__name__)
# babel = Babel(app)


# @babel.localeselector
# def get_locale():
#     """Get_locale function"""
#     return (request.accept_languages.best_match(app.config['LANGUAGES']))


# app.config.from_object(Config)
# app.config['BABEL_DEFAULT_LOCALE'] = 'en'
# app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


# @app.route("/", strict_slashes=False)
# def home_page():
#     """Render template"""
#     return (render_template('3-index.html'))


# if __name__ == "__main__":
#     app.run(port=5000, host='0.0.0.0')

#!/usr/bin/python3
"""A script that starts a flask web application
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

class Config:
    """Configuration for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """Return the locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def index() -> str:
    """Return a given string"""
    return render_template('2-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

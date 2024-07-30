#!/usr/bin/env python3
"""
Basic flask app with Babel integration and local selection
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Config class for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Get locale from request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Main page for the Flask app
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")

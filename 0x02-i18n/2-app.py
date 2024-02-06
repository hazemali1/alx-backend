#!/usr/bin/env python3
"""flask"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    Babel_default_locale = "en"
    Babel_default_timezone = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """accept languages"""
    return request.request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """index html"""
    return render_template('1-index.html')


if __name__ == '__main__':
    """main"""
    app.run(debug=True)

#!/usr/bin/env python3
"""
0. Basic Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr"]
    Babel_default_locale = "en"
    Babel_default_timezone = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get Configuration variable"""
    return request.request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """
    0. Basic Flask app
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)

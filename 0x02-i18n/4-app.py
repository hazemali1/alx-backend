#!/usr/bin/env python3
"""flask"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config():
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """accept languages"""
    args = request.args.items()
    for k, v in args:
        if k == "locale" and v in app.config['LANGUAGES']:
            return v
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """index html"""
    return render_template("4-index.html")


if __name__ == '__main__':
    """main"""
    app.run(debug=True)

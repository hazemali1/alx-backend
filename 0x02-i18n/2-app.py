#!/usr/bin/env python3
"""flask"""
from typing import Any
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

class Config:
    """Config class"""
    LANGUAGES: list[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"

app.config.from_object(Config)
babel = Babel(app)

def get_locale() -> str:
    """accept languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route("/")
def index() -> Any:
    """index html"""
    return render_template("2-index.html")

if __name__ == '__main__':
    """main"""
    app.run(debug=True)

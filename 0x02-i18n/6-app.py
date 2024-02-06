#!/usr/bin/env python3
"""flask"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

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
    u = g.user["locale"]
    if g.user and u and u in app.config['LANGUAGES']:
        return u
    r = request.headers.get("locale")
    if r and r in app.config['LANGUAGES']:
        return r
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """index html"""
    return render_template("6-index.html")


def get_user():
    """get user by id from request"""
    args = request.args.items()
    for k, v in args:
        if k == "login_as" and v in list(str(users.keys())):
            return users[int(v)]
    return None


@app.before_request
def before_request():
    """call function before request"""
    g.user = get_user()


if __name__ == '__main__':
    """main"""
    app.run(debug=True)

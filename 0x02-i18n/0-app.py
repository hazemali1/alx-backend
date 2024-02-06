#!/usr/bin/env python3
"""flask"""
from flask import flask


app = Flask(__name__)

@app.route("/")
def index():
    """index html"""
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
from flask_babel import Babel, get_locale, LocaleSelector

app = Flask(__name__)
babel = Babel(app)

SUPPORTED_LOCALES = ['en', 'fr', 'es']

@babel.localeselector
def get_locale():
    accept_languages = request.accept_languages.values()
    for lang in accept_languages:
        if lang[:2] in SUPPORTED_LOCALES:
            return lang[:2]
    return 'en'  # Default locale if no match found

@app.route('/')
def index():
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run(debug=True)

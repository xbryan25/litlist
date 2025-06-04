from flask import Flask
from flask_cors import CORS

from app.routes import books_bp


def create_app():

    app = Flask(__name__)
    CORS(app, origins='*')

    app.register_blueprint(books_bp, url_prefix='/books')

    return app

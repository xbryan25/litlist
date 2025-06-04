from flask import Flask
from flask_cors import CORS

from app.routes import books_bp

from .db.db import init_db, get_db, close_db


def create_app():

    app = Flask(__name__)
    CORS(app, origins='*')

    app.register_blueprint(books_bp, url_prefix='/books')

    with app.app_context():
        init_db()

    app.teardown_appcontext(close_db)

    return app

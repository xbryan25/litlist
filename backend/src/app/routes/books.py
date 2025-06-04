from flask import Blueprint
from app.controllers import get_books_handler

bp = Blueprint('books', __name__)


@bp.route("", methods=['GET'])
def get_books():
    return get_books_handler()

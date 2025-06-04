from flask import Blueprint, request, jsonify
from app.controllers import get_books_handler

bp = Blueprint('books', __name__)


@bp.route("", methods=['GET'])
def get_books():
    return get_books_handler()


@bp.route("/add-book", methods=['POST'])
def add_book():
    data = request.get_json()

    print(data)

    return jsonify({"message": "Book added successfully"}), 201

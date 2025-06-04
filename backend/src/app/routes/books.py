import uuid

from flask import Blueprint, request, jsonify
from app.controllers import fetch_all_books, add_book
from app.db.db import get_db
from app.models import Book

bp = Blueprint('books', __name__)


@bp.route("", methods=['GET'])
def get_books_func():
    db = get_db()
    books = fetch_all_books(db)

    books_dict = [book.__dict__ for book in books]

    return jsonify({"books": books_dict,
                    "message": "Retrieved all books"}), 200


@bp.route("/add-book", methods=['POST'])
def add_book_func():
    book_data = request.get_json()

    print(book_data)

    new_book = Book(
        book_id=str(uuid.uuid4()),
        title=book_data['title'],
        genre=book_data['genre'],
        author=book_data['author'],
        pages=book_data['pages'],
        read_status=int(True if book_data['readStatus'] else False)
    )

    db = get_db()

    try:
        add_book(db, new_book)

        return jsonify({"message": "Book added successfully"}), 201

    except Exception as e:
        print(e)

        return jsonify({"message": "Book not added successfully"}), 500



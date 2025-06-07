import uuid

from flask import Blueprint, request, jsonify
from app.controllers import fetch_books, fetch_book, get_total_pages, add_book, edit_book, delete_book
from app.db.db import get_db
from app.models import Book

bp = Blueprint('books', __name__)


@bp.route("", methods=['GET'])
def get_books_func():
    sort_type = request.args.get('sort_type', 'Title').lower().replace(' ', '_')
    sort_by = request.args.get('sort_by', 'Ascending')

    search_type = request.args.get('search_type', 'All').lower().replace(' ', '_')
    search_input = request.args.get('search_input', '').strip()

    visible_rows = int(request.args.get('visible_rows', 0))
    current_page_number = int(request.args.get('current_page_number', 1))

    if sort_type not in ['title', 'genre', 'author', 'pages', 'read_status']:
        return jsonify({"message": "Invalid sort type option"}), 400

    if sort_by not in ['Ascending', 'Descending']:
        return jsonify({"message": "Invalid sort by option"}), 400

    if search_type not in ['all', 'title', 'genre', 'author', 'pages', 'read_status']:
        return jsonify({"message": "Invalid search type option"}), 400

    print(f"visible rows {visible_rows}")
    try:
        db = get_db()
        books = fetch_books(db=db, sort_type=sort_type, sort_by=sort_by, search_type=search_type,
                            search_input=search_input, visible_rows=visible_rows,
                            current_page_number=current_page_number)

        books_dict = [book.__dict__ for book in books]

        return jsonify({"books": books_dict,
                        "message": "Retrieved all books"}), 200

    except Exception as e:
        print(e)

        return jsonify({"message": "Failed to retrieve all books"}), 500


@bp.route("/book/<book_id>", methods=['GET'])
def get_book_func(book_id):
    try:
        db = get_db()

        book = fetch_book(db, book_id)

        book_dict = book.__dict__

        return jsonify({"books": book_dict,
                        "message": "Retrieved a book"}), 200

    except Exception as e:
        print(e)

        return jsonify({"message": "Failed to retrieve book"}), 500


@bp.route("/total-pages", methods=['GET'])
def get_total_pages_func():

    search_type = request.args.get('search_type', 'All').lower().replace(' ', '_')
    search_input = request.args.get('search_input', '').strip()

    visible_rows = int(request.args.get('visible_rows', 0))

    if search_type not in ['all', 'title', 'genre', 'author', 'pages', 'read_status']:
        return jsonify({"message": "Invalid search type option"}), 400

    try:
        db = get_db()

        total_pages = get_total_pages(db=db, search_type=search_type, search_input=search_input,
                                      visible_rows=visible_rows)

        return jsonify({"total_pages": total_pages,
                        "message": "Retrieved total pages"}), 200

    except Exception as e:
        print(e)

        return jsonify({"message": "Failed to retrieve book"}), 500


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
        read_status=int(True if book_data['read_status'] else False)
    )

    db = get_db()

    try:
        add_book(db, new_book)

        return jsonify({"message": "Book added successfully"}), 201

    except Exception as e:
        print(e)

        return jsonify({"message": "Book not added successfully"}), 500


@bp.route("/book/<book_id>", methods=['PUT'])
def edit_book_func(book_id):
    book_data = request.get_json()

    existing_book = Book(
        book_id=book_id,
        title=book_data['title'],
        genre=book_data['genre'],
        author=book_data['author'],
        pages=book_data['pages'],
        read_status=int(True if book_data['read_status'] else False)
    )

    db = get_db()

    try:
        edit_book(db, existing_book)

        return jsonify({"message": "Book added successfully"}), 201

    except Exception as e:
        print(e)

        return jsonify({"message": "Book not added successfully"}), 500


@bp.route("/book/<book_id>", methods=['DELETE'])
def delete_book_func(book_id):
    db = get_db()

    try:
        delete_book(db, book_id)

        return jsonify({"message": "Book deleted successfully"}), 200

    except Exception as e:
        print(e)

        return jsonify({"message": "Book deleted unsuccessfully"}), 500


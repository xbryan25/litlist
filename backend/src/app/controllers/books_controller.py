from flask import jsonify


def get_books_handler():
    books = [
        {
            "id": '1',
            "title": 'Harry Potter',
            "genre": 'Fantasy',
            "author": 'J.K. Rowling',
            "pages": 350,
            "readStatus": True
        },
        {
            "id": '2',
            "title": 'Lord of the Rings',
            "genre": 'Adventure',
            "author": 'Tolkien',
            "pages": 670,
            "readStatus": True
        }
    ]
    return jsonify({"books": books})
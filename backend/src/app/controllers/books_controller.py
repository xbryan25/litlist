from flask import jsonify
import sqlite3
import uuid

from app.models import Book


def fetch_all_books(db):
    cursor = db.cursor()

    sql = 'SELECT * FROM books'

    cursor.execute(sql)

    rows = cursor.fetchall()

    return [Book.from_row(row) for row in rows]


def fetch_book(db, book_id):
    cursor = db.cursor()

    sql = 'SELECT * FROM books WHERE id = ?'
    values = (book_id,)

    cursor.execute(sql, values)

    row = cursor.fetchone()

    return Book.from_row(row)


def add_book(db, book):

    cursor = db.cursor()

    sql = "INSERT INTO books (id, title, genre, author, pages, read_status) VALUES (?, ?, ?, ?, ?, ?)"

    values = (book.id, book.title, book.genre, book.author, book.pages,
              book.read_status)

    cursor.execute(sql, values)

    db.commit()

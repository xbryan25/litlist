from flask import jsonify
import sqlite3
import uuid

from app.models import Book


def fetch_books(db, sort_type, sort_by, search_type, search_input, visible_rows, current_page_number):
    cursor = db.cursor()

    sort_by_dict = {"Ascending": "ASC", "Descending": "DESC"}

    if search_type != "all":

        sql = f"SELECT * FROM books WHERE {search_type} LIKE ?"

        values = (f"%{search_input}%", )
    else:
        sql = f"""SELECT * FROM books 
                    WHERE title LIKE ? OR 
                    genre LIKE ? OR
                    author LIKE ? OR
                    pages LIKE ? OR
                    read_status LIKE ?"""

        values = (f"%{search_input}%", f"%{search_input}%", f"%{search_input}%", f"%{search_input}%", f"%{search_input}%")

    if sort_type == 'Read Status':
        sql += f""" ORDER BY {sort_type} 
                    {sort_by_dict['Descending' if sort_by == 'Ascending' else 'Ascending']}"""
    else:
        sql += f""" ORDER BY {sort_type} {sort_by_dict[sort_by]}"""

    sql += f""" LIMIT ? OFFSET ?"""

    values += (visible_rows, (current_page_number - 1) * visible_rows)

    cursor.execute(sql, values)

    rows = cursor.fetchall()

    return [Book.from_row(row) for row in rows]


def fetch_book(db, book_id):
    cursor = db.cursor()

    sql = 'SELECT * FROM books WHERE id = ?'
    values = (book_id,)

    cursor.execute(sql, values)

    row = cursor.fetchone()

    return Book.from_row(row)


def get_total_pages(db, search_type, search_input, visible_rows):
    cursor = db.cursor()

    if search_type != "all":

        sql = f"SELECT COUNT(*) FROM books WHERE {search_type} LIKE ?"

        values = (f"%{search_input}%",)
    else:
        sql = f"""SELECT COUNT(*) FROM books 
                       WHERE title LIKE ? OR 
                       genre LIKE ? OR
                       author LIKE ? OR
                       pages LIKE ? OR
                       read_status LIKE ?"""

        values = (f"%{search_input}%", f"%{search_input}%", f"%{search_input}%", f"%{search_input}%",
                  f"%{search_input}%")

    cursor.execute(sql, values)

    total_rows = cursor.fetchone()[0]

    return ((total_rows - 1) // visible_rows) + 1 if total_rows != 0 else 1


def add_book(db, book):

    cursor = db.cursor()

    sql = "INSERT INTO books (id, title, genre, author, pages, read_status) VALUES (?, ?, ?, ?, ?, ?)"

    values = (book.id, book.title, book.genre, book.author, book.pages,
              book.read_status)

    cursor.execute(sql, values)

    db.commit()


def edit_book(db, book):

    cursor = db.cursor()

    sql = "UPDATE books SET title = ?, genre = ?, author = ?, pages = ?, read_status = ? WHERE id = ?"

    values = (book.title, book.genre, book.author, book.pages,
              book.read_status, book.id)

    cursor.execute(sql, values)

    db.commit()


def delete_book(db, book_id):
    cursor = db.cursor()

    sql = 'DELETE FROM books WHERE id = ?'
    values = (book_id,)

    cursor.execute(sql, values)

    db.commit()

import sqlite3
from flask import g

DATABASE = 'app/db/books.db'


def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            genre TEXT NOT NULL,
            author TEXT NOT NULL,
            pages INTEGER NOT NULL,
            read_status BOOLEAN NOT NULL CHECK (read_status in (0,1))
        )
    """)

    conn.commit()
    conn.close()


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

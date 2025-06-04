
class Book:
    def __init__(self, book_id, title, genre, author, pages, read_status):
        self.id = book_id

        self.title = title
        self.genre = genre
        self.author = author
        self.pages = pages
        self.read_status = read_status

    @classmethod
    def from_row(cls, row):
        return cls(
            book_id=row['id'],
            title=row['title'],
            genre=row['genre'],
            author=row['author'],
            pages=row['pages'],
            read_status=int(True if row['read_status'] else False)
        )

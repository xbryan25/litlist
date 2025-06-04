
class Book:
    def __init__(self, book, _id):
        self._id = _id

        self.title = book["title"]
        self.genre = book["genre"]
        self.author = book["author"]
        self.pages = book["pages"]
        self.read_status = book["read_status"]

    def insert(self):
        # insert to db
        pass

    def json(self):
        return {
            "id": self._id,
            "title": self.title,
            "genre": self.genre,
            "author": self.author,
            "pages": self.pages,
            "readStatus": self.read_status
        }

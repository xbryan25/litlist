from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*')


@app.route("/books", methods=['GET'])
def books():
    value = {
        "books": [
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
    }

    return jsonify(value)


def main():
    app.run(debug=True, port=8080)


if __name__ == "__main__":
    main()

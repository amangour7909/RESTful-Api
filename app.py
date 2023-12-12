from flask import Flask, request, jsonify
import os
import db
from models import Book


app = Flask(__name__)


if not os.path.isfile('books.db'):
    db.connect()

@app.route("/")
def index():
    return 'Welcome To Book API'


#To Add a book
@app.route("/api/books", methods=['POST'])
def postRequest():
    content_type = request.headers.get('Content-Type')
    
    if (content_type != 'application/json'): #check for content-type
        return jsonify(status = 400 ,message = 'Request content-Type should be application/json.')
    
    req_data = request.get_json()

    if 'title' not in req_data or 'author' not in req_data: #check title and author exist in the request body
        return jsonify(status=400,message = "'title' or/and 'author' missing. Request body should have both 'title' and 'author'.")
    
    title = req_data['title']
    author = req_data['author']
    bks = [b.serialize() for b in db.view()]

    #check if book already exists
    for b in bks:
        if b['title'] == title and b['author'] == author:
            message = f"Book with title '{title}' & author '{author}' already exists in the library."
            return jsonify(status = 404, message = message)

    #Insert book
    bk = Book(db.generateNewBookId(), title, author)
    db.insert(bk)
    return jsonify(status = 200, message = 'Successfully added new book in the library.')


#To get all books
@app.route('/api/books', methods=['GET'])
def getRequest():
    books = [b.serialize() for b in db.view()]
    return jsonify(status = 200, message = 'Success getting all books in the library.', no_of_books = len(books), books = books)

#To update book details
@app.route("/api/books/<id>", methods=['PUT'])
def putRequest(id):
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return jsonify(status = 400 ,message = 'Request content-Type should be application/json.')
    
    req_data = request.get_json()
    req_data = request.get_json()

    title,author = None,None
    if 'title' in req_data:
        title = req_data['title']
    if 'author' in req_data:
        author = req_data['author']

    #check title or author exists in request body
    if not title and not author:
        return jsonify(status=400,message = "'title' and 'author' both missing. To update book details, request body should 'title' or/and 'author'.")
    
    bk = db.view(id)
    if len(bk)==0: #Check if the id is valid
        return jsonify(status=404,message = f"Book with id '{id}' couldn't be found.")

    new_title = title if title else bk[0].title
    new_author = author if author else bk[0].author
    bk = db.view(None,new_title,new_author)

    if len(bk)!=0: #Check if a book with same title and author already exists in library
        return jsonify(status = 400, message = "Can't update Book details. A book with similar details already exists.")
    
    db.update(Book(id,new_title,new_author))

    return jsonify(status=200,message = f"Successfully updated the book with id '{id}'")

if __name__ == '__main__':
    app.run()
import sqlite3, uuid
from models import Book

#Add Sample Book Data Here
books = [
	{
		'title': 'Coders at Work',
		'author' : 'Peter Seibel'
	},
	{
		'title': 'Intorudction to Algorithms',
		'author' : 'Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein',
	},
	{
		'title': 'The Art of Computer Programming',
		'author' : 'Donald Knuth'
	}
	]

#This function generates new unique ids for books
def generateNewBookId():
	id = uuid.uuid4().int

	def changeBase(n,new_base): #Change the base of the number from 10 to new_base
		if n==0:
			return '0'

		digits = []

		while n:
			digits.append(n%new_base)
			n//=new_base

		digits = [str(x) if x<10 else chr(ord('a')+x-10) for x in digits[::-1]]
		return ''.join(digits)

	return changeBase(id,36) #Change Base so that id is shorter in length

#function to establish connection with the database
def connect():
	conn = sqlite3.connect('books.db')
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS books (id varchar(40) PRIMARY KEY, title TEXT, author TEXT)")
	conn.commit()
	conn.close()

	for bk in books: #Insert Sample books in databse
		bk_o = Book(generateNewBookId(), bk['title'], bk['author'])
		insert(bk_o)

#function to insert a book in databse
def insert(book):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (?,?,?)", (book.id,book.title,book.author))
    conn.commit()
    conn.close()

#function to fetch books with required properties
# if all the fields are None, then fetch all the books
def view(id = None, title = None, author = None):
	conn = sqlite3.connect('books.db')
	cur = conn.cursor()

	query = f"SELECT * FROM books" #Query to fetch books
	if id or title or author:
		query += " WHERE "
		if id: 
			query += f" id='{id}' " #Add id in where clause if id is given
		if title:
			query += f" {'AND' if id else ''} title='{title}' " #Add title in where clause if title is given
		if author:
			query += f" {'AND' if id or title else ''} author='{author}' " #Add author in where clause if author is given

	cur.execute(query)
	rows = cur.fetchall()

	books = []

	for bk in rows:
		book = Book(bk[0], bk[1], bk[2])
		books.append(book)

	conn.close()
	return books

#function to update book details
def update(book):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=?, author=? WHERE id=?", (book.title, book.author, book.id))
    conn.commit()
    conn.close()

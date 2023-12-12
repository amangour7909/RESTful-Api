# RESTful API to perfrom CRUD operation on Library database
This project shows implementation of API using flask
## Libraries used:- 
1. Flask
5. sqlite3

create folder BOOK_API <br> 
`mkdir BOOK_API` <br>
change directory to BOOK_API folder <br>
create virtual environment and activate it
<pre> python -m venv myenv
.\myenv\Scripts\Activate </pre>
install flask
<pre>pip install flask</pre>
run flask
<pre>flask run</pre> 

now my virtual environment is ready. <br>
To perform API testing I had created a db which contains details of books with three fields author,title and id. <br>
Below I am performing API testing using RestMan. <br>
RestMan is a chrome extension. here is the link https://chromewebstore.google.com/detail/restman/ihgpcfpkpmdcghlnaofdmjkoemnlijdi
# API TESTING using RestMan 
## 1. Endpoint 1: Retrieve All Books
GET http://127.0.0.1:5000/api/books  <br>
RESPONSE
![Screenshot 2023-12-12 220543](https://github.com/amangour7909/Api/assets/127648041/3f3653e6-c712-45cb-a8ed-b5be69843622) <br>
![Screenshot 2023-12-12 220613](https://github.com/amangour7909/Api/assets/127648041/afb4c3c2-eb72-4a71-be44-7233679d709b) <br>

## 2. Endpoint 2: Add a New Book
### validation of request payload <br>
REQUEST - POST http://127.0.0.1:5000/api/books <br>
POST request will not work if our content-type is not set to application-json <br>
![Screenshot 2023-12-12 234221](https://github.com/amangour7909/Api/assets/127648041/f720a863-01d8-48cc-b01b-360651de702a) <br>
so we need to set content-type as application-json <br>
![Screenshot 2023-12-12 234529](https://github.com/amangour7909/Api/assets/127648041/cbff6cee-2e6e-4d69-9b5c-aa5275519273) <br>
REQUEST- POST http://127.0.0.1:5000/api/books <br>
![Screenshot 2023-12-12 221147](https://github.com/amangour7909/Api/assets/127648041/4986ee9e-c549-4089-b332-e7355e0e3784) <br>
RESPONSE <br>
![Screenshot 2023-12-12 221632](https://github.com/amangour7909/Api/assets/127648041/4982e709-f26b-4cc4-a297-6bf9e13e7fb8)  <br> <br>

### invalid json format <br>
REQUEST - POST http://127.0.0.1:5000/api/books <br>
![Screenshot 2023-12-12 222145](https://github.com/amangour7909/Api/assets/127648041/8fde0f84-9aa7-4fdc-9c68-f46861f1508c) <br>
RESPONCE <br>
![Screenshot 2023-12-12 222244](https://github.com/amangour7909/Api/assets/127648041/95bb11dc-42e5-4494-8255-bff1bb7964c6) <br> <br>
### Correct insertion of the new book into the database. <br>
REQUEST - POST http://127.0.0.1:5000/api/books <br>
![Screenshot 2023-12-12 222718](https://github.com/amangour7909/Api/assets/127648041/9c4c0315-6a37-4b37-9945-2240a5ff4459) <br>
RESPONSE <br>
![Screenshot 2023-12-12 222727](https://github.com/amangour7909/Api/assets/127648041/b41f5eb2-ee14-43dc-9ea2-1cdcc06fcf4c) <br>
<br>
### error handling - duplicate book entries <br>
Book with author name R.D. Sharma2 is already exist so it will throw an error.
REQUEST - POST http://127.0.0.1:5000/api/books <br>
![Screenshot 2023-12-12 222718](https://github.com/amangour7909/Api/assets/127648041/3578386f-a63f-4952-adfd-801f01e9c5e4) <br>
RESPONSE <br>
![Screenshot 2023-12-12 223206](https://github.com/amangour7909/Api/assets/127648041/542b8698-7487-4f82-8fb5-8e31f0bd7715) <br>

## 3. Endpoint 3: Update Book Details
### updating the details of a specific book in the library <br>
before request already there exist book with id dda6g2wif5zqxc2lna80gaep1<br>
![Screenshot 2023-12-12 223732](https://github.com/amangour7909/Api/assets/127648041/89ea284a-0fa0-4c72-9942-e4e1e8f433bd) <br>
now i am updating its author name R.D. Sharma2 to The R.D. sharma2 <br>
REQUEST- PUT http://127.0.0.1:5000/api/books/dda6g2wif5zqxc2lna80gaep1 <br>
![Screenshot 2023-12-12 223757](https://github.com/amangour7909/Api/assets/127648041/1fdde4e0-56f3-442f-bbd7-c09dbccc7519) <br>
RESPONSE <br>
![Screenshot 2023-12-12 223806](https://github.com/amangour7909/Api/assets/127648041/5fd33cdc-c515-4e22-ade1-79642e93aac7) <br> <br>
### Error handling updating a non-existent book <br>
there is no book with id dda6g2wif5zqxc2lna80gaep so it will throw an error. <br>
REQUEST- PUT http://127.0.0.1:5000/api/books/dda6g2wif5zqxc2lna80gaep <br>
![Screenshot 2023-12-12 225513](https://github.com/amangour7909/Api/assets/127648041/e3ee7f94-ac2f-41d6-8578-0974b9a0f94e) <br>
RESPONSE <br>
![Screenshot 2023-12-12 225546](https://github.com/amangour7909/Api/assets/127648041/074de359-9897-43ad-87bb-e007e9841c65) <br>




[![Coverage Status](https://coveralls.io/repos/github/lordwerneo/epam-library/badge.svg)](https://coveralls.io/github/lordwerneo/epam-library)

# **Library App**
___

### Description.
#### Library App is a simple web application for managing books, and genres. It uses RESTful web service to perform CRUD operations. The user is allowed to:  
1. Check the lists of books, and genres. 
2. A short description of a genre total books count of a genre and unique books count of a genre are available. The total book count and unique book count are calculated and updated automatically. 
3. An ISBN, title, author, publisher, year published, genre, and copies of the book are available. 
3. Perform operations with genres such as editing descriptions, adding genres, deleting genres.
4. Perform operations with books such as adding, editing information, removing.
___
### Start using application.
Python3 must be installed. MySQL installation is optional, SQLite schema will be created oterwise. 

___
### Deployment.
1. Clone the repo:

	> git clone git@github.com:lordwerneo/epam-library.git

2. Create virtual environment in project:
	>cd epam-library
	
	>python3 -m venv venv
	
	>source venv/bin/activate

3. Install project requirements:
	>pip install -r requirements.txt

4. Install gunicorn and run app:
	>pip install flask gunicorn
	
	>deactivate

5. Run the migration scripts to create database schema:

	>flask db init
	
	>flask db migrate
	
	>flask db upgrade

6. Run app with gunicorn
	>source venv/bin/activate
	
	>gunicorn --bind 0.0.0.0:5000 wsgi:app

7. After these steps you should see application working at 0.0.0.0:5000/
___

### API operations.

* /api

	* GET - get all the available API resources with available methods
	
	> { " resource ": [ { " genres ": { " GET ": URL, " POST ": URL } } ] }  

* /api/genres

	* GET - get all available genres
	
	* POST - add a new genre
	
* /api/genre/genre_name
	
	* GET - get information about a genre
	
	* PUT - add new or update existing genre
	
	* DELETE - delete genre

* /api/books
	
	* GET - get all available books
	
	* POST - add a new book
	
* /api/books/genre_name

	* GET - gell all available books in current genre
	
* /api/book/book_isbn 
	
	* GET - get information about book
	
	* PUT - add new or update existing book
	
	* DELETE - delete book
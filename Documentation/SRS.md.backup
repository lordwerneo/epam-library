# <div align="center"> Library </div>


### Vision

"Library" is a web application that allows users to record and view information about genres and books, book genres.  

The application should provide:

* Storing genres and books in database.
* Displaying the list of genres.
* Updating list of genres(adding editing, removing);
* Displaying the list of books;
* Updating the list of books (adding, editing, removing);


## 1. Genres

### 1.1 Display the list of Genres

This mode is intended for viewing and editing the genres list.

**Main Scenario:**

* User selects item "Genres";
* Application displays list of genres.

![](mockups/1-1.jpg)
Pic 1.1 View of genress list.

The list displays the following columns:

* Name - genre's name;
* Description - genre's description;
* Unique - count of unique books of this genre in library;
* Total - total count of books of this genre in library;
* Edit - icon to move to edit genre;
* Delete - icon to delete current genre.


### 1.2 Add genre

**Main Scenario:**

* User clicks the "Add Genre" button in the genres list view mode;
* Application displays form to enter genre's data;
* User enters genre's data and press "Submit" button;
* If any data is entered incorrectly, incorrect data message is displayed;
* If entered data is valid, the record is added to the database;
* If error occurrs, then flash message is displayed;
* If new genre record is successfully added, then up to date list of genres is displayed.

![](mockups/1-2.jpg)
Pic. 1.2 Add genre.

**Cancel operation scenario:**
* User clicks the "Add Genre" button in the genres list view mode;
* Application displays form to enter genre's data;
* User enters genre's data and press "CANCEL" button;
* Data doesn't save in database, list of genres without changes is displayed to user. 
* If the user selects another part of the app, the data will not be saved in the database, and the corresponding form will be opened.  


When adding a genre, the following details are entered:
* Name - genre's name;
* Description - genre's description;


Constraints for data validation:

* Name - maximum length of 20 characters, unique;
* Description - maximum length of 255 characters;


### 1.3 Edit genre
**Main Scenario:**

* User clicks the "Edit" icon button in the genres list view mode;
* Application displays form to enter genre's data;
* User enters genre's data and press "Update" button;
* If any data is entered incorrectly, incorrect data message is displayed;
* If entered data is valid, the record is edited in the database;
* If error occurrs, then flash message is displayed;
* If genre record is successfully updated, then up to date list of genres is displayed.

![](mockups/1-3.jpg)
Pic. 1.3 Edit genre.

**Cacel operation scenario:**
* User clicks the "Edit" icon button in the genres list view mode;
* Application displays form to enter genre's data;
* User enters genre's data and press "CANCEL" button;
* Data doesn't save in database, list of genres without changes is displayed to user. 
* If the user selects another part of the app, the data will not be saved in the database, and the corresponding form will be opened.  


### 1.4 Delete genre

**Main Scenario:**
* User clicks the "Delete" icon button in the genres list view mode;
* Record is deleted from the database;
* If error occurs, then flash message is displayed;
* If the genre record is successfully deleted, then up to date list of genres is displayed.


## 2. Books

### 2.1 Display list of books

This mode is intended for viewing books list

**Main Scenario:**

* User selects item "Books";
* Application displays list of books.

![](mockups/2-1.jpg)
Pic 2.1 View the books list.

The list displays the following columns:

* ISBN - Book's ISBN;
* Title - title of the book;
* Author - author of the book;
* Year - year when book was published;
* Publisher - publisher of the book;
* Copies - count of available copies;
* Genre - genre of the book; 
* Edit - icon to edit information about the book; 
* Delete - icon to delete the book.

### 2.2 Add book

**Main scenario:**

* User clicks the "Add Book" button in the books list view mode;
* Application displays form to enter book data;
* User enters book data and presses "Submit" button;
* If any data is entered incorrectly, incorrect data message is displayed;
* If entered data is valid, then record is added to the database;
* If error occurs, then flash message is displayed;
* If new book record is successfully added, then updated list of books is displayed. 

![](mockups/2-2.jpg)
Pic. 2.2 Add book

**Cacel operation scenario:**
* User clicks the "Add Book" button in the books list view mode;
* Application displays form to enter book data;
* User enters book data and presses "CANCEL" button;
* Data doesn't save in database, list of genres without changes is displayed to user. 
* If the user selects another part of the app, the data will not be saved in the database, and the corresponding form will be opened.  


When adding a book, the following details are entered:

* ISBN - book's unique International Standard Book Number;
* Title - book's title;
* Author - book's author full name;
* Genre - genre of the book;
* Year - year of publishment;
* Copies - number of copies;
* Publisher - publisher of the book.

Constranits for data validation:

* ISBN - unique, maximum length of 20 characters;
* Title - maximum length of 64 characters;
* Author - maximum length of 20 characters;
* Genre - one of available genres;
* Year - maximum length of 4 characters;
* Available - maximum length of 3 characters;
* Publisher - maximum length of 20 characters;

### 2.3 Edit book

**Main scenario:**

* User clicks the "Edit Book" button in the books list view mode;
* Application displays form to enter book data;
* User enters book data and presses "Update" button;
* If any data is entered incorrectly, incorrect data message is displayed;
* If entered data is valid, then record is added to the database;
* If error occurs, then flash message is displayed;
* If new book record is successfully added, then updated list of books is displayed. 


![](mockups/2-3.jpg)
Pic. 2.3 Edit book

**Cacel operation scenario:**
* User clicks the "Edit Book" button in the books list view mode;
* Application displays form to enter book data;
* User enters book data and presses "CANCEL" button;
* Data doesn't save in database, list of genres without changes is displayed to user. 
* If the user selects another part of the app, the data will not be saved in the database, and the corresponding form will be opened.  


### 2.4 Filter books list

**Main Scenario:**
* User enters data to filter books by, and clicks "Search" button.
* If any data is entered incorrectly, incorrect data message is displayed;
* If error occurs, then flash message is displayed;
* If data is entered correctly, the filtered list of books is displayed.

![](mockups/2-3.jpg)
Pic. 2.4 Filter books


### 2.5 Remove the book

**Main Scenario:**
* User clicks the "Delete" button icon in the books list view mode;
* Record is deleted from the database;
* If error occurs, then flash message is displayed;
* If the book record is successfully deleted, then up to date list of books is displayed.



















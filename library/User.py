from Book import BookIssue
from Catalog import Catalog
from Book import Book
from BookItem import BookItem
import time

class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        self.catalog = Catalog()


class Member(User):
    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id

# issued : object of class dictionary
# Stores information of the issued book as key, value pairs.
        self.issued = {}

    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id

    #assume name is unique
    def issueBook(self,name,catalog,days=10):
        if name in self.issued:
            return BookIssue(False, f"{name} already issued", "", "", -1)

        book = catalog.searchByName(name)
        print(book)
        result = None

        if len(book.book_item) > 0:
            isbn = book.book_item[0].isbn
            rack = book.book_item[0].rack
            catalog.removeBookItem(book.name, isbn)
            msg = f"(Book: {book.name}, Author: {book.author}, ISBN: {isbn}) issued for {days} days"
            result = BookIssue(True, msg, isbn, rack, days)
            self.issued[book.name] = result
            book.updateBorrowedCount(1)

        else:
            result = BookIssue(False, "Book not available", "", "", -1)

        return result

    #assume name is unique
    def returnBook(self,name):
        if name in self.issued:
            bookIssued = self.issued[name]
            book = self.catalog.searchByName(name)
            isbn = bookIssued.isbn
            rack = bookIssued.rack
            return f"RETURN_SUCCESS: (BookName {name}, ISBN {isbn}, Rack {rack}) returned successfully"

        return f"RETURN_FAILURE: {name} not borrowed by you"


class Librarian(User):
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id

    def __repr__(self):
        return self.name + ' ' + self.location + ' '  + self.emp_id

    def addBook(self,name,author,publish_date,pages):
        return self.catalog.addBook(name, author, publish_date, pages)

    def removeBook(self,name):
        res = self.catalog.removeBook(name)
        return res

    def removeBookItemFromCatalog(self,catalog,book,isbn):
        self.catalog.removeBookItem(book, isbn)

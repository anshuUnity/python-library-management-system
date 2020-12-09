# -*- coding: utf-8 -*-
from BookItem import BookItem
import time
import datetime

class Book:
    def __init__(self,name,author,publish_date,pages):
        self.name = name
        self.author = author
        self.publish_date = publish_date
        self.pages = pages
        self.total_count = 0
        self.borrowed = 0
        self.book_item = []

    def addBookItem(self,isbn,rack):
        b = BookItem(self,isbn,rack)
        self.book_item.append(b)
        self.total_count +=1

    def printBook(self):
        print (self.name,self.author)
        for book_item in self.book_item:
            print (book_item.isbn)

    def searchBookItem(self,isbn):
        for book_item in self.book_item:
            if isbn.strip() == book_item.isbn:
                return book_item

    def removeBookItem(self,book_item):
        if book_item in self.book_item:
            self.book_item.remove(book_item)
            self.total_count -=1

    def updateBorrowedCount(self, inc):
        self.borrowed += inc

    def __repr__(self):
        return self.name + ' ' + self.author

class BookIssue:
    """docstring for BookIssue."""

    def __init__(self, is_issued, message, isbn, rack, days):
        self.is_issued = is_issued
        self.message = message
        self.isbn = isbn
        self.rack = rack
        self.days = days
        self.borrowed = int(time.time())  # - (86400*14)

    def __repr__(self):
        return f"ISSUED_RES: {self.is_issued}, Book: {self.message}, Borrowed: {getDate(self.borrowed)}"

def getDate(borrowed):
    timestamp = datetime.datetime.fromtimestamp(borrowed)
    return timestamp.strftime('%Y-%m-%d %H-%M')
        

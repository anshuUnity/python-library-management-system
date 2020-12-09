# -*- coding: utf-8 -*-
from Book import Book
from Catalog import Catalog
from User import Member, Librarian

#b1 = Book('Shoe Dog','Phil Knight', '2015',312)
#b1.addBookItem('123hg','H1B2')
#b1.addBookItem('124hg','H1B3')

#b1.printBook()

catalog = Catalog()

b = catalog.addBook('Shoe Dog','Phil Knight', '2015',312)
catalog.addBookItem(b, '123hg','H1B2')
catalog.addBookItem(b, '123hg','H1B4')
catalog.addBookItem(b, '123hg','H1B5')

b = catalog.addBook('Moonwalking with Einstien','J Foer', '2017',318)
catalog.addBookItem(b, '463hg','K1B2')

catalog.displayAllBooks()

m1 = Member("Vish","Bangalore",23,'asljlkj22','std1233')
m2 = Member("Anshu","Lucknow",26,'asljlkj19','std1210')

librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 
print (m1)
print (librarian)
print(m2)

res = m1.issueBook('Shoe Dog',catalog,days=10)
print(res)

res = m1.returnBook("Shoe Dog")
print(res)

# Description: This file is a class object for Book.
# It tracks ID, title, authors, average rating, ISBN, ISBN13, language,
# pages, rating count, publication, and publisher.
# It has the appropiate getters and setters for each attribute.

from Media import Media

class Book(Media):
    def __init__(self, id, title, authors, avg_rating, 
                isbn, isbn13, lang, pages, rating_count, publication, publisher):
        super().__init__(id, title, avg_rating)
        self.authors = authors.split('\\')
        self.isbn = isbn
        self.isbn13 = isbn13
        self.lang = lang
        self.pages = pages
        self.rating_count = rating_count
        self.publication = publication
        self.publisher = publisher

    def setAuthors(self, authors):
        self.authors = authors

    def setISBN(self, isbn):
        self.isbn = isbn

    def setISBN13(self, isbn13):
        self.isbn13 = isbn13

    def setLang(self, lang):
        self.lang = lang

    def setPages(self, pages):
        self.pages = pages

    def setRatingCount(self, rating_count):
        self.rating_count = rating_count

    def setPublication(self, publication):
        self.publication = publication

    def setPublisher(self, publisher):
        self.publisher = publisher

    def getAuthors(self):
        return self.authors
    
    def getISBN(self):
        return self.isbn
    
    def getISBN13(self):
        return self.isbn13
    
    def getLang(self):
        return self.lang
    
    def getPages(self):
        return self.pages
    
    def getRatingCount(self):
        return self.rating_count
    
    def getPublication(self):
        return self.publication
    
    def getPublisher(self):
        return self.publisher
    
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class ReaderBookStatus:
    def __init__(self, book):
        self.book = book
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self, books):
        self.books = books

    def add_book(self, book):
        self.books.append(book)


Library.add_book = lambda self, book: self.books.append(book)

book = Book('Philosopher\'s stone', 'J.K.Rowling')
donchosInstance = ReaderBookStatus(book)
boyansInstance = ReaderBookStatus(book)

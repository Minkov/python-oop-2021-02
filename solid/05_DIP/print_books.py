class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class TrimContentFormatter:
    def format(self, book: Book) -> str:
        return book.content[:3]


class Printer:
    def get_book(self, book: Book, formatter):
        return formatter.format(book)


book = Book('Goblet of fire')
print(Printer().get_book(book, Formatter()))
print(Printer().get_book(book, TrimContentFormatter()))

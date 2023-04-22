from homework2.Book import Book


class BookDTO:

    def __init__(self, book):
        if isinstance(book, Book):
            self.Title = book.Title
            self.Author = book.Author
            self.Genre = book.Genre
            self.Pages = book.Pages
        else:
            raise ValueError

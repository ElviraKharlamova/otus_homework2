from homework2.BookReader import BookReader
from homework2.UserReader import UserReader
from homework2.bookDTO import BookDTO


class Library:
    def __init__(self):
      pass


    def split_books_to_users(self):
        bookReader = BookReader()
        books = bookReader.read()
        bookDTOs = []
        for book in books:
            bookDTOs.append(BookDTO(book))
        users = UserReader().read()
        books_per_user = len(bookDTOs) // len(users)
        remaining_books = len(bookDTOs) % len(users)
        book_index = 0

        for i in range(len(users)):
            user_books = bookDTOs[book_index:book_index + books_per_user]
            if i < remaining_books:
                user_books.append(bookDTOs[-(i + 1)])
            users[i].books = user_books
            book_index += len(user_books)
        return users
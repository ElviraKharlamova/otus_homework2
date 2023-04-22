from homework2 import UserReader, BookReader


class Library:
    def __init__(self):
      pass


    def split_books_to_users(self, books, users):
        books_per_user = len(books) // len(users)
        remaining_books = len(books) % len(users)
        book_index = 0

        for i in range(len(users)):
            user_books = books[book_index:book_index + books_per_user]
            if i < remaining_books:
                user_books.append(books[-(i + 1)])
            users[i].books = user_books
            book_index += len(user_books)
        return users
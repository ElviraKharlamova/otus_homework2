import json
from homework2.BookReader import BookReader
from homework2.Library import Library
from homework2.UserDTO import UserDTO
from homework2.UserReader import UserReader
from homework2.bookDTO import BookDTO
from homework2.main import userDTOs


class Result:
    def __init__(self):
        pass

    library = Library()
    books = BookReader().read()
    bookDTOs = []
    for book in books:
        bookDTOs.append(BookDTO(book))
    users = UserReader().read()
    userswithbooks = library.split_books_to_users(bookDTOs, users)
    userDTOs = []
    for user in userswithbooks:
        userDTOs.append(UserDTO(user))

    def read(self):
        with open("data.json", "w") as write_file:
            json.dump(userDTOs, write_file)
        """new_json = json.dumps(userDTOs)
    print(new_json)"""

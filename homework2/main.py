"""import pandas
np_array = pandas.io.parsers.read_csv("C:\\Users\\User\\PycharmProjects\\otus_homework2\\homework2\\books.csv", on_bad_lines='skip').to_numpy()
print(np_array)"""
import json

from homework2.BookReader import BookReader
from homework2.Library import Library
from homework2.UserDTO import UserDTO
from homework2.UserReader import UserReader
from homework2.bookDTO import BookDTO

"""a = UserReader()
print(a.read())"""
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
    new_json = json.dumps(userDTOs)
new_json = json.dumps(userDTOs)
print(new_json)

from homework2.User import User
from homework2.bookDTO import serialize_book


class UserDTO:

    def __init__(self, user):
        if isinstance(user, User):
            self.name = user.name
            self.gender = user.gender
            self.address = user.address
            self.age = user.age
            self.books = user.books
        else:
            raise ValueError


def serialize_user(user):
    res = user.__dict__
    res["books"] = [serialize_book(book) for book in user.books]
    return res

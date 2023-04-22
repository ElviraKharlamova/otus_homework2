from homework2.User import User


class UserDTO:

    def __init__(self, user):
        if isinstance(user, User):
            self.name = user.name
            self.gender =user.gender
            self.address = user.address
            self.age = user.age
            self.books = user.books
        else:
            raise ValueError

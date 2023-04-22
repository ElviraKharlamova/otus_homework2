import json

from homework2.User import User


class UserReader(object):
    def __init__(self):
        pass

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

    def read(self):
        users =[]
        with open("C:\\Users\\User\\PycharmProjects\\otus_homework2\\homework2\\users.json") as f:
            usersArray = json.load(f)
            for d in usersArray:
                users.append(User(d['_id'], d['index'], d['guid'], d['isActive'], d['balance'], d['picture'], d['age'], d['eyeColor'], d['name'], d['gender'], d['company'], d['email'], d['phone'], d['address'], d['about'], d['registered'], d['latitude'], d['longitude'], d['tags'], d['friends'], d['greeting'], d['favoriteFruit']))
        return users

import json
from homework2.Library import Library
from homework2.UserDTO import UserDTO, serialize_user


class Result:
    def runResult(self):
        library = Library()

        userswithbooks = library.split_books_to_users()
        userDTOs = []
        for userwithbooks in userswithbooks:
            userDTOs.append(UserDTO(userwithbooks))
        userJsons = []
        for user in userDTOs:
            userJsons.append(json.dumps(user, default=serialize_user))

        new_json = json.dumps(userJsons, indent=4)
        # print(new_json)

        with open('result.json', 'w') as f:
            f.write(new_json)

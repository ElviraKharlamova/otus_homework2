
from homework2.books import Book


class BookReader(object):
    def __init__(self):
        pass

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

    def read(self):
        booksArray = []
        with open("C:\\Users\\User\\PycharmProjects\\otus_homework2\\homework2\\books.csv", 'r') as f:
            books = f.readlines()
            for item in books[1::]:
                parts = item.split(',')
                try:
                    booksArray.append(Book(parts[0], parts[1] + parts[2], parts[3], parts[4], parts[5]))
                except:
                    booksArray.append(Book(parts[0], parts[1], parts[2], parts[3], parts[4]))
        return booksArray
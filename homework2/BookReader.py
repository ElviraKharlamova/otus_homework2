import pandas
from homework2.Book import Book


class BookReader(object):
    def __init__(self):
        pass

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

    def read(self):
        np_array = pandas.io.parsers.read_csv("C:\\Users\\User\\PycharmProjects\\otus_homework2\\homework2\\books.csv",
                                              on_bad_lines='skip').to_numpy()
        books_list = []
        for book_array in np_array:
            book = Book(book_array[0], book_array[1], book_array[2], book_array[3], book_array[4])
            books_list.append(book)
        return books_list
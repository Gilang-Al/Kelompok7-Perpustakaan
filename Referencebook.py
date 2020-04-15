from Book import Book

class refencebooktype:

    def __init__(self, refencebooktype, Book):
        self.__refencebooktype = refencebooktype

    @property
    def refencebooktype(self):
        return self.__refencebooktype

    @refencebooktype.setter
    def refencebooktype(self, refencebooktype):
        self.__refencebooktype

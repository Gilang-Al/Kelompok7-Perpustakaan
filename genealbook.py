from Book import Book

class generalbooktype:

    def __init__(self, generalbooktype, Book):
        self.__generalbooktype = generalbooktype

    @property
    def generalbooktype(self):
        return self.__generalbooktype

    @generalbooktype.setter
    def generalbooktype(self, generalbooktype):
        self.__generalbooktype

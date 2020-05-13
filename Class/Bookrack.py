from Book import Book

class Bookrack:

    def __init__(self, numberofbook, status):
        self.__numberofbook = numberofbook

    @property
    def numberofbook(self):
        return self.__numberofbook

    @numberofbook.setter
    def numberofbook(self, numberofbook):
        self.__numberofbook

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status

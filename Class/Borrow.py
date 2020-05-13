from patron import patron
from Book import Book

class Borrow():

    def __init__(self, borrowdate, duedate):
        self.__borrowdate = borrowdate
        self.__duedate = duedate

    @property
    def borrowdate(self):
        return self.__borrowdate

    @borrowdate.setter
    def name(self, borrowdate):
        self.__borrowdate = borrowdate

    @property
    def duedate(self):
        return self.__duedate

    @duedate.setter
    def name(self, duedate):
        self.__duedate = duedate

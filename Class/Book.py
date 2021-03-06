from BookType import BookType
from Bookorm import Bookorm

class Book():

    def __init__(self, BookType, Bookname, Author, Price, rackno, status):
        self.__BookType = BookType
        self.__Bookname = Bookname
        self.__Author = Author
        self.__Price = Price
        self.__status = status

    @property
    def BookType(self):
        return self.__BookType

    @BookType.setter
    def BookType(self, BookType):
        self.__BookType = BookType

    @property
    def Bookname(self):
        return self.__Bookname

    @Bookname.setter
    def Bookname(self, Bookname):
        self__Bookname = Bookname

    @property
    def Author(self):
        return self.__Author

    @Author.setter
    def Author(self, Author):
        self__Author = Author

    @property
    def Price(self):
        return self.__Price

    @Price.setter
    def Price(self, Price):
        self__Price = Price

    @property
    def rackno(self):
        return self.__rackno

    @rackno.setter
    def rackno(self, rackno):
        self__rackno = rackno

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self__status = status

    def __str__(self):
        return "Book type = {} \nBook name = {} \nAuthor = {} \nPrice = {} \nRackno = {} \Status = ".format(Book.id, Book.Booktype, Book.Bookname, Book.Author, Book.Price, Book.Racknno, Book.status)

b = Book(BookType(2), "Raven", "Kpii", "$14.00", "2", "lot")
b.insertBook()
Bookorm.showBook()

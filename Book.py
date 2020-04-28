from BookType import BookType
from Bookorm import Book
from librarydb import _SessionFactory

class Book():

    def __init__(self, id, BookType, Bookname, Author, Price, rackno, status = []):
        self.__id = id
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

    @staticmethod
    def removeBook(Bookid):
        try:
            session = sessionFactory()
            session.query(Bookorm).filter_by(id=Bookid).delete()
            session.commit()
            session.close()
        except Exception as R:
            print ("->",r)
        else:
            print("Book Has Been Erased")

        @staticmethod
        def updateBook(idBook):
            try:
                newBooktype = input("Add BookType: ")
                newBookname = input("Add New Bookname: ")
                newAuthor = input("Add New Author : ")
                newPrice = input("Add New Price : ")
                newRackno = input("Add New Rackno: ")
                newstatus = input ("Add New status: ")
                session = sessionFactory()
                session.query(Bookorm).filter_by(id=Bookid).update({
                    Bookorm.Booktype: newBooktpe, Bookorm.Bookname: newBookname, Bookorm.Author: newAuthor, Bookorm.Price: newPrice, BookormRackno: NewRackno, Bookormstatus: Newstatus
                }, synchronize_session=False)
                session.commit()
                session.close()
            except Exception as r:
                print("->",r)




                          
                                                                                                        
                                  

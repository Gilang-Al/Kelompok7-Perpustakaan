from sqlalchemy import Column, String, Integer, Date
from librarydb import Base

class Book(Base):
    __tablename__='books'

    id = Column(Integer, primary_key=True)
    Booktype = Column (String)
    Bookname = Column (String)
    Author = Column (String)
    Price = Column (Integer)
    status = Column (String)

    def __init__(self, Booktype, Bookname, Author, Price, status):
        self.__BookType = BookType
        self.__Bookname = Bookname
        self.__Author = Author
        self.__Price = Price
        self.__status = status

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

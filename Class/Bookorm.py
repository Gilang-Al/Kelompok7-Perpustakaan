from sqlalchemy import Column, String, Integer, Date
from librarydb import Base

class Bookorm(Base):
    __tablename__='Book'

    id = Column(Integer, primary_key=True)
    Booktype = Column (String)
    Bookname = Column (String)
    Author = Column (String)
    Price = Column (Integer)
    Rackno = Column (Integer)
    status = Column (String)

    def __init__(self, Booktype, Bookname, Author, Rackno, Price, status):
        self.__BookType = BookType
        self.__Bookname = Bookname
        self.__Author = Author
        self.__Price = Price
        self._Rackno = Rackno
        self.__status = status

    @staticmethod
    def showBook():
        try:
            session = sessionFactory()
            for Book in session.query(BookOrm).all():
                print("Id Book = {}\nBook type = {}\nBook name = {}\nAuthor = {}\nRackno = {}\Price = {}\Status ="
                      .format(Book.id, Book.Booktype, Book.Bookname, Book.Author, Book.Price, Book.Rackno, Book.status))
            session.close()
        except Exception as r:
            print("===>", r)

    @staticmethod
    def deleteBook(idBook):
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
    def insertBook(Book):
        try:
            session = sessionFactory()
            BookOrm = BookOrm(Book.Booktype, Book.Bookname, Book.Author, Book.Price, Book.status)
            session.add(BookOrm)
            session.commit()
            session.close()
        except Exception as r:
            print("--->", r)
        else:
            print("Data Berhasil Disimpan!")

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

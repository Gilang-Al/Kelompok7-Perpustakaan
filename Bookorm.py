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

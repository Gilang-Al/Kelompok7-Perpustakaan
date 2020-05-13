from sqlalchemy import Column, String, Integer, Text, Enum
from librarydb import Base

class LibrarianOrm(Base):
    __tablename__='Librarian'

    id = Column(Integer, primary_key=True)
    nameLibrarian = Column(String)
    phonenumberLibrarian = Column(String)
    postLibrarian = Column(String)

    def __init__(self, name, phonenumber, post):
        self. nameLibrarian = name
        self.phonenumberLibrarian = phonenumber
        self.postLibrarian = post

    @staticmethod
    def showLibrarian():
        try:
            session = sessionFactory()
            for Librarian in session.query(LibrarianOrm).all():
                print(
                    "Id Librarian = {}\nname = {}\nphonenumber = {}\npost= {}\n-----"
                        .format(Librarian.id, Librarian.nameLibrarian, Librarian.phonenumberLibrarian, Librarian.postLibrarian))
            session.close()
        except Exception as r:
            print("--->", r)

    @staticmethod
    def insertLibrarian(Librarian):
        try:
            session = sessionFactory()
            LibrarianOrm = LibrarianOrm(Librarian.name, Librarian.phonenumber, Librarian.post)
            session.add(LibrarianOrm)
            session.commit()
            session.close()
        except Exception as r:
            print("--->", r)
        else:
            print("Data Saved !")

        @staticmethod
        def updateLibrarian(idLibrarian):
            try:
                newname = input("Input New Name = ")
                newphonenumber = input("Input New Phone Number = ")
                newpost = input ("Input New Post = ")
                session = sessionFactory()
                session.query(LibrarianOrm).filter_by(id=idLibrarian).update({
                    LibrarianOrm.nameLibrarian: newname, LibrarianOrm.phonenumberLibrarian: newphonenumber,
                    LibrarianOrm.postLibrarian: newpost},synchronize_session=False)
                session.commit()
                session.close()
            except Exception as r:
                print("--->", r)
            else:
                print("Data Updated !")

        @staticmethod
        def deleteLibrarian(idLibrarian):
            try:
                session = sessionFactory()
                session.query(LibrarianOrm).filter_by(id=idLibrarian).delete()
                session.commit()
                session.close()
            except Exception as r:
                print("--->",r)
            else:
                print("Data Erased !")

                    

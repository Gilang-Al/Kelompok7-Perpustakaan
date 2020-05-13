from sqlalchemy import Column, String, Integer, Text, Enum
from librarydb import Base

class PatronOrm(Base):
    __tablename__= 'Patron'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    nik = Column (String)

    def __init__(self, name, nik):
        self.name = name
        self.nik = nik

    @staticmethod
    def showPatron():
        try:
            sessession = sessionFactory()
            for Patron in session.query(PatronOrm).all():
                print(
                    "Patron Id = {}\nname = {}\nik = {}\n----"
                        .format(Patron.Id, Patron.namePatron, Patron.nikPatron))
                session.close()
        except Exception as r:
            print("-->",r)

    @staticmethod
    def insertPatron(Patron):
        try:
            sessession = sessionFactory()
            PatronOrm = PatronOrm(Patron.name, Patron.nik)
            session.add(PatronOrm)
            session.commit()
            session.close()
        except Exception as r:
            print("-->",r)
        else:
            print("Data Saved")

    @staticmethod
    def updatePatron(Patron):
        try:
            Newname = input("Input New Name : ")
            newnik = input("Input New NIK : ")
            session = sessionFactory()
            session.query(PatronORM).filter_by(id=idPatron).update({PatronORM.PatronName: newname, PatronOrm.Patronnik: newnik}, seynchronize_session=False)
            session.commit()
            session.close()
        except Exception as r:
            print("--->, r")
        else:
            print("Data Update")

    @staticmethod
    def deletePatron(idPatron):
        try:
            session = sessionFactory()
            session.query(PatronOrm).fiter_by(id=idPatron).delete()
            session.commit()
            session.close()
        except Exception as r:
            print("-->",r)
        else:
            print("Data Delete") 
        
    
            
        

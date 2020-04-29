from sqlalchemy import Column, String, Integer, Text, Enum
from patron import patron
from librarydb import Base

class PatronOrm(Base):
    __tablename__= 'Patron'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    nik = Column (String)

    def __init__(self, name, nik):
        self.name = name
        self.nik = nik
        

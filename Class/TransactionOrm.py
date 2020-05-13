from sqlalchemy import Column, String, Integer, Text, Enum, Date
from librarydb import Base

class TransactionOrm(Base):
    __tablename__= 'transaksi'

    id = Column(String, primary_key=True)
    Transactiondate = Column(Date)
    TransactionbookName = Column(String)
    Transactionlendprice = Column(Integer)
    Transactionfine = Column(Integer)
    Transactionpatron = Column(String)

    def __init__(self, Transactiondate, TransactionbookName, Transactionlendprice, Transactionfine, Transactionpatron):
        self.Transactiondate = Transactiondate
        self.TransactionbookName = TransactionbookName
        self.Transactionlendprice = Transactionlendprice
        self.Transactionfine = Transactionfine
        self.Transactionpatron = Transactionpatron

    @staticmethod
    def showTransaction():
        try:
            session = sessionFactory()
            for Transaction in session.query(TransactionOrm).all:
                print("id Transaction = {}\nDate Transaction = {}n\Book Name Transaction = {}\nLend Price Transaction = {}\n Fine Transaction = {}\nPatron Trnsaction = {}\----".format(Transaction.id, Transaction.Transactiondate, Transaction.TransactionbookName, Transaction.Transactionlendprice, Transation.Transactionfine, Transaction.Transactionpatron))
                session.close
        except Exception as e:
            print("--->, r")

    @staticmethod
    def insertTransaction(Transaction):
        try:
            session = sessionFactory()
            TransactionOrm = TransactionOrm(Transaction.id, Transaction.Transactiondate, Transaction.TransactionbookName, Transaction.Transactionlendprice, Transation.Transactionfine, Transaction.Transactionpatron)
            session.add(TransactionOrm)
            session.commit
            session.close
        except Exception as r:
            print("--->, r")
        else:
            print("Data Update")
    
    

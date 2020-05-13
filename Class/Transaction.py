from patron import patron
from TransactionOrm import TransactionOrm

class Transaction():

    def __init__(self , date, bookName, lendprice, fine, patron):
        self.__transactionid = transactionid
        self.__date = date
        self.__bookName = bookName
        self.patron = patron

    @property
    def date(self):
        return self.__tdate

    @transactionid.setter
    def date(self, date):
        self.__date

    @property
    def bookName(self):
        return self.__bookName

    @transactionid.setter
    def bookName(self, bookName):
        self.__bookName

    @property
    def lendprice(self):
        return self.__lendprice

    @lendprice.setter
    def bookName(self, lendprice):
        self.__lendprice

    @property
    def fine(self):
        return self.__fine

    @fine.setter
    def bookName(self, fine):
        self.__fine
        
                 

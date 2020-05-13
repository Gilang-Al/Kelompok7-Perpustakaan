from Transaction import Transaction
class Bill:

    def __init__(self, amount, Transaction):
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount
        

from Bill import Bill

class monthlyincome:

    def __init__(self, incomeweekly, incomemonthly, bill):
        self.__incomeweekly = incomeweekly
        self.__incomemonthly = incomemonthly

    @property
    def incomeweekly(self):
        return self.__incomeweekly

    @incomeweekly.setter
    def incomeweekly(self, incomeweekly):
        self.__incomeweekly

    @property
    def incomemonthly(self):
        return self.__incomemonthly

    @incomemonthly.setter
    def date(self, incomemonthly):
        self.__incomemonthly
    

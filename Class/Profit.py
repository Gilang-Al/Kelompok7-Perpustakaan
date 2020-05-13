from Transaction import Transaction

class profit():

    def __init__(self, totalIncome, totalFine):
        self.totalIncome = totalIncome
        self.totalFine = totalFine

    @property
    def totalIncome(self):
        return self._totalIncome

    @totalIncome.setter
    def totalIncome(self, totalIncome):
        self.totalIncome = totalIncome

    @property
    def totalFine(self):
        return self._totalFine

    @totalFine.setter
    def totalFine(self, totalFIne):
        self.totalFine = totalFine

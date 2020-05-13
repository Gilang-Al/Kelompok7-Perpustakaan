from people import people

class Librarian(people):

    def __init__(self, name, phonenumber, post):
        self.__name = name
        self._phonenumber = phonenumber
        self._post = post

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def phonenumber(self):
        return self.__phonenumber

    @phonenumber.setter
    def name(self, phonenumber):
        self.__phonenumber = phonenumber

    @property
    def post(self):
        return self.__ppost

    @post.setter
    def name(self, post):
        self.__post = post

    def incomeReport(self, date):
        pass

from people import people

class patron(people):
    
    def __init__(self, name, nik):
        self.__name = name
        self.__nik = nik

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def nik(self):
        return self.__nik

    @nik.setter
    def nik(self, nik):
        self.__nik = nik


# p = Patron ("name","nik")
# print (p.nama)
    
    
    

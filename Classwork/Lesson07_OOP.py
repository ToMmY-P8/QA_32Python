class Human:
    def __init__(self):
        self.fullname = ''
        self.birthdate = ''
        self.tel = ''
        self.country = ''
        self.city = ''
        self.home_address = ''
    def getFullname(self):
        return self.fullname
    def setFullname(self,fullname):
        self.fullname = fullname
    def getBirthdate(self):
        return self.birthdate
    def setBirthdate(self,birthdate):
            self.birthdate = birthdate
    def getTel(self):
            return self.tel
    def setTel(self,tel):
        self.tel = tel
    def getCountry(self):
            return self.country
    def setCountry(self,country):
        self.country = country
    def getCity(self):
            return self.city
    def setCity(self,city):
        self.city = city
    def gethome_address(self):
            return self.home_address
    def setCity(self,home_address):
        self.home_address = home_address
    def input_data(self):
        self.fullname = input("Введіть ПІБ: ")
        self.birthdate = input("Введіть дату нарождення: ")
        self.tel = input("Введіть моб. телефон: ")
        self.country = input("Введіть країну: ")
        self.city = input("Введіть місто: ")
        self.home_address = input("Введіть домашню адресу: ")

    def __str__(self) -> str:
         return 'name' + self.fullname

hum1=Human()
hum1.input_data()
print (hum1)
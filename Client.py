class Client:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return "------------------------\n        Client\n------------------------"\
               "\nName: {} \nAge: {} \nAddress: {}\n------------------------"\
               .format(self.name, self.age, self.address)
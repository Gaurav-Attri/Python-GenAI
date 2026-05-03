class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password

    def verify_password(self, pwd):
        return pwd == self.__password


u = User("Alex", "secure123")
print(u.verify_password("secure123"))
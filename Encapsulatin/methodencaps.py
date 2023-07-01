#encapsulatin - cominng data members and methods in one class

# public method:
# protected method
# private method

#Public Members:
class Myclass:
    def __init__(self):
        self.public_variable = 10
        self._protected_variable = 11
        self.__private_variable = 12

    def public_method(self):
        print("this is a public method")
        self.__private_method()
        print(self.__private_variable)


    def _protected_method(self):
        print("this is a protected method")

    def __private_method(self):
        print("This is a private method")

obj = Myclass()  # Executin will start from here when the reference obj is calling the class
print(obj.public_variable)
obj.public_method()
print(obj._protected_variable)
obj._protected_method()
# print(obj.__private_variable)
# obj.__private_method()



# A very good and best example for encapsulation . A complete encapsulation
# which use Data members and methods properly in class
class Person:
    def __init__(self,name,age):
        self.__name  = name
        self. __age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name == "John":
            print("Is not a rea name")
        else:
            self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self,age):
        if age > 0:
            self.__age = age
        else:
            print("Not a valid or correct age")

person = Person("Durga", 42) # the execution will start from this line. The class will get called 
print(person.get_name())
print(person.get_age())
person.set_age(-1)

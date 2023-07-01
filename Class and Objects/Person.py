#class and Objects

class Person:
    name=None
    age = None
    emil_id = None

    def __init__(self,name,age,email_id):
        self.name = name
        self.age = age
        self.email_id = email_id

    def sleep(self):
        print(self.name + " is sleeping")

    def eating(self):
        print(self.name + " is eating")

    # def oral(self):
    #     print(self.age + "announce the age")
    #
    # def locating(self):
    #     print(self.email_id + "Annouce the email id")

durga = Person("Durga","42","durga@gm.com")
print(durga.name)
durga.sleep()
durga.eating()
    # durga.oral()
    # durga.locating()

medha = Person("Medha","15","medha@gmail.com")
medha.sleep()












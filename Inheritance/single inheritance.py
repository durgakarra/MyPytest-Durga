
# Single inheritance

class Animal:
    def speak(self):
        print("Animal speaks")

class dog(Animal):
     def bark(self):
        print ("animal bark woof woof")


myanimal = dog()
myanimal.speak()
myanimal.bark()

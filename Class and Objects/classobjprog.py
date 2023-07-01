
class Cars:
    def __init__(self, name, color, model_number):
        self.name = name
        self.color = color
        self.model_number = model_number

    def start_engine(self):
        print("engine started" + self.name)

    def drive(self):
        print("drive carefully" + self.name)

cars1 = Cars("Tesla", "Blue", "Xu-45")
cars2 = Cars("Lambargini","red", "45er")

print(all)
print(cars1.name)
print(cars2.name)

cars1.start_engine()
cars2.drive()



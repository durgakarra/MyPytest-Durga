class Newcar:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print("Engine started")

    def drive(self):
        print(f"Driving the {self.brand} {self.color} car")


my_cars = Newcar("Toyota", "blue")
my_cars.start_engine()
my_cars.drive()

print(my_cars.brand)
print(my_cars.color)

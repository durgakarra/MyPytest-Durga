
#Class and objects
#DM - Data members - name, color, model number
#Method: start_engine, Drove

#Tesla #lambo

class Cars:
    name = None
    color = None
    model_number = None


    def __init__(self, color, name, model_number):
        self.name = name
        self.color = color
        self.model_number = model_number

    def start_engine(self):
        print("Starting the engine -->" + self.name)

    def drive(self):
        print("Driving -->" + self.name)

    def print_all(self):
        print(self.name,self.color,self.model_number)

    def which_car_iam_using(self):
        return self.name
    def __int__(self):

car_name = input("enter the car name")
car_color = input("Enter the car color")
car_model_number = input ("Enter the model number")

tesla = Cars(car_name,car_color, car_model_number)

tesla.print_all()
tesla.start_engine()
tesla.drive()
car_tesla = tesla.which_car_iam_using()
print(car_tesla)


class Vehicle:
    def __init__(self, make, model):
        self.make  = make
        self.model = model
    
    def set_make(self,make):
        self.make = make

    def set_model(self,model):
        self.model = model
    
    def get_make(self):
        return self.make

    def get_model(self):
        return self.model
    
    def get_car(self):
        print(f"car: {self.make}, model: {self.model}")


class Car(Vehicle):
    def __init__(self,make,model,year):
        super().__init__(make,model)
        self.year = year

    def describe_car(self):
        print(f"this car is made in {self.year}")

class Bike(Vehicle):
    def __init__(self,make,model,year):
        super().__init__(make,model)
        self.year = year

    def describe_bike(self):
        print(f"this bike is made in {self.year}")
            
# initiation
honda = Vehicle('honda', 'civic')
honda.get_car()

my_car = Car("toyota","camry",2020)
my_car.get_car()
my_car.describe_car()

my_bike = Bike("honda","125",2010)
my_bike.get_car()
my_bike.describe_bike()

print(isinstance(honda,Vehicle))
print(isinstance(my_bike,Vehicle))
print(isinstance(my_bike,Car))
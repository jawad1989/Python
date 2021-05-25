class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.battery_size = 10

    def get_price(self):
        print("im parent class")


class ElectricCar(Car):
    def __init__(self, make, model):
        super().__init__(make, model)

    def get_price(self):
        print("im from child class")


car_a = Car("Honda", "Civic")
car_a.get_price()

car_b = ElectricCar("Tesla", "ModelS")
car_b.get_price()

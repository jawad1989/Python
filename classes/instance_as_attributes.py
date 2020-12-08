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
        self.battery = Battery()

    def get_price(self):
        print("im from child class")


class Battery:
    def __init__(self, battery_size=5):
        """inititate the batteyr size"""
        self.battery_size = battery_size

    def get_battery_size(self):
        print(f"battery size is: {self.battery_size}")


car_a = Car("Honda", "Civic")
car_a.get_price()

car_b = ElectricCar("Tesla", "ModelS")
car_b.get_price()
print(car_b.battery_size)

# instance as attribute
car_b.battery.get_battery_size()

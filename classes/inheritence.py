class Car:
    """Simple attempt to represent a Car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.make} / {self.mdele} / {self.year}"
        return long_name

    def get_odometer_reading(self):
        return self.odometer_reading

    def update_odometer_reading(self, mileage):
        self.odometer_reading = mileage


class ElectricCar(Car):
    """Represents aspects of car specific to Electric Car"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")


# initiate object
honda = Car('Honda', 'Civic', 2005)
print(f"{honda.make} / {honda.model} / {honda.year}")


# initiate Electric Car
tesla = ElectricCar('Tesla', 'model s,', 2019)
print(f"{tesla.make} / {tesla.model.title()} / {tesla.year}")
tesla.update_odometer_reading(1000)
print(tesla.get_odometer_reading())
tesla.describe_battery()

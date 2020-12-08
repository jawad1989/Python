class Car:
    """Simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """initilize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def get_odometer_reading(self):
        """Returns odometer reading"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer_reading(self, mileage):
        """Update odometer reading"""
        self.odometer_reading = mileage


my_car = Car('toyota', 'camry', 2020)
old_car = Car('honda', 'civic', 2005)

print("Current Car: ", my_car.get_descriptive_name())
my_car.get_odometer_reading()
my_car.update_odometer_reading(4500)
my_car.get_odometer_reading()

print("\nOld Car:", my_car.get_descriptive_name())

from car import Car
# from car import Car as car_class
# from car import *
# import car


my_car = Car('toyota', 'camry', 2020)
old_car = Car('honda', 'civic', 2005)

print("Current Car: ", my_car.get_descriptive_name())
my_car.get_odometer_reading()
my_car.update_odometer_reading(4500)
my_car.get_odometer_reading()

print("\nOld Car:", my_car.get_descriptive_name())

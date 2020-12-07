# Developer: Jawad Saleem
# Date: Dec, 7th, 2020
# Description: undestranding lists in python
# Actions: for loop, range, use range to generate list, step size(**), min, max, looping a slice

# looping through a list
names = ["jawad", "rajab", "ahmad"]
for name in names:
    print(f"Hello {name.title()}, How are you today?")

print("end of loop")


# using range
for value in range(0, len(names)):
    print(names[value], "is at", value, "index")

for value in range(1, 5):
    print(value)

# using range to make a list
random_numbers = list(range(0, 10))
print(random_numbers)

# step size = skip numbers in range
for value in range(0, 10, 2):
    print(value)


# take square and exponent of 2
square, exponent = [], []
for values in range(0, 10):
    square.append(values**2)
    exponent.append(2**values)

print(square)
print(exponent)


# Looping through a slice
for exp in exponent[:3]:
    print(exp)

# min max of list
print("min of list:", min(exponent))
print("max of list:", max(exponent))

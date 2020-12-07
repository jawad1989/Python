# Developer: Jawad Saleem
# Date: Dec, 7th, 2020
# Description: undestranding lists in python
# Actions: list comprehension

squares = []
for value in range(0, 5):
    squares.append(value**2)
print(squares)

# list comprehension
square = [value**2 for value in range(0, 10)]
print(square)

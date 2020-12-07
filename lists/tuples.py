# Developer: Jawad Saleem
# Date: Dec, 5th, 2020
# Description: undestranding tuples in python, list that cant change
# Actions: insert,append, remove, del, pop, sort, sort(reversed=true), sorted(array), reverse, len, slice list, copy list

dimensions = (100, 50, 150)
my_list = [1, 2, 3, 4, 5]
print("dimensions =", dimensions)

print("dimensions[0] =", dimensions[0])
print("dimensions[:2] =", dimensions[:2])

print("my_list =", my_list[:3])

# modifying tuples = wont allow
my_list[0] = 300
print("my_list =", my_list)

dimensions = (300, 4, 5)
print("updated dimensions =",  dimensions)

# Developer: Jawad Saleem
# Date: Dec, 12th, 2020
# Description: undestranding lists in python
# Actions: insert,append, remove, del, pop, sort, sort(reversed=true), sorted(array), reverse

names = ["jawad", "rajab", "ahmad"]

print(names)
print(names[1])

# same output as above, just capitalizes the first letter(s)
print(names[1].title())


# using (-1) for getting last index
print(names[-1])
print("Hello " + names[-2])
print(f"Hello, {names[-3]}")


# modifying list
names[0] = "john"
print(names)


# appending the list
names.append('sumair')
print(names)

# clear list
names = []
names.append('John')
names.append("Steve")
names.append("Peter")
print(names)


# insert element
names.insert(1, "Jawad")
print(names)

# remove element using del, remove and pop
del names[0]
print(names)

names.remove("Jawad")
print(names)

popped_names = names.pop()
print(names)

# Sort List
cars = ['Toyota', 'Honda', 'Audi', "BMW"]
print(cars)

cars.sort()
print(cars)

# temp sort
names = ["jawad", "rajab", "ahmad"]
print(sorted(names))

# reverse a list
cities = ["RoundRock", "Austin", "Dallas"]
cities.sort(reverse=True)
print("Sort 'reveresed=true'=", cities)

cities.reverse()
print("Reversed List:", cities)

# length of list
print("Length of cities:", len(cities))

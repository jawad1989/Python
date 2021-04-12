# # Developer: Jawad Saleem
# # Date: Dec, 7th, 2020
# # Description: undestranding what dictionaries are in python
# # Actions: loop a dict, loop only keys,values, get in dict,
# # sets: used to remove duplicates in values

list_python = ['a', 'b', 'c', 'a', 'a']
print("List in python= ", list_python)

set_python = {'a', 'b', 'c', 'a', 'a'}
print("Set in python= ", set_python)

tuple_python = ('a', 'b', 'c', 'a', 'a')
print("Tuples in python= ", tuple_python)


car_1 = {'color': 'white', 'make': 'toyota'}
print(car_1['color'])

# car_1['model'] = "camry"
# print(car_1)
# del car_1['model']
# print("deleting model in dictionary:", car_1)


favorite_food = {
    "jawad": "burger",
    "john": "pizza",
    "haniya": "pizza",
    "ahmad": "yogurt",
    "rajab": "fries"
}


# print(favorite_food)

# # loop a dictionary
# for key, value in favorite_food.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")

# print("\nprinting only keys in dictionary:\n")
# for name in favorite_food.keys():
#     print(name)

# print("\nprinting only values in dictionary:\n")
# for name in favorite_food.values():
#     print(name)

# print("\nget values:")
# find_food = favorite_food.get("rajab")
# print(find_food)


# print("\nif not found:")
# find_food = favorite_food.get("john", "there is no one with this name")
# print(find_food)


# print("\nPringint sorted dictionary:", sorted(favorite_food.keys()))

# print("\nsorted keys in loop")
# for value in sorted(favorite_food.values()):
#     print(value)

# print("\nset function in loop")
# for value in set(favorite_food.values()):
#     print(value)

# nesting dictionaries
favorite_languages = {
    "jawad": ['php', 'js', 'python'],
    "rajab": ["java", "php", "c++"]
}

for name, languages in favorite_languages.items():
    print(f"{name.upper()}, favorite languages are:")
    for language in languages:
        print("\t", language)


# dictionary in dictionry

users = {
    'user_a': {
        'fname': 'jawad',
        'lname': 'saleem',
        'city': 'lahore',
        'age': 31},
    'user_b': {
        'fname': 'rajab',
        'lname': 'saleem',
        'city': 'lahore',
        'age': 26},
    'user_c': {
        'fname': 'muhammad',
        'lname': 'saleem',
        'city': 'lahore',
        'age': 60},
    'user_d': {
        'fname': 'ahmad',
        'lname': 'jawad',
        'city': 'lahore',
        'age': 1}
}

print(users)
print(len(users))

for user, user_info in users.items():
    print(f"\n{user.upper()}, details are:")
    for key, value in user_info.items():
        print(key, ":", value)

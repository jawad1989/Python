import json

my_list = [1, 2, 3, 4, 5, 6]
my_dict = {
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

filename = 'json/json_write.json'

with open(filename, 'w') as file_object:
    json.dump(my_dict, file_object)

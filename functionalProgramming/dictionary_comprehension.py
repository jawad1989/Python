
# dict comprehension, take ^2 power 2 of age and add only even number
simple_dict = {
    'jawad': 2,
    'rajab': 3
}
my_dict = {key: values**2 for key, values in simple_dict.items()
           if values % 2 == 0}

print(my_dict)

# example

new_dict = {num: num*2 for num in [1, 2, 3]}
print(new_dict)

list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6, 7, 8]
list_c = [10, 11, 12, 13, 14]
print(list(zip(list_a, list_b, list_c)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))

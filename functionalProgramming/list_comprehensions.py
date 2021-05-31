# list, set, dictionary

# Example 1: without comprehension
my_list = []
for char in 'jawad':
    my_list.append(char)

print(my_list)

# Example 1: with comprehension
list_char = [char for char in 'jawad']
print(list_char)


# Example 2: populate odd numbers in list
num_list = [num for num in range(10)]
print(num_list)

# Example 3: multiple last list by 2, each element
num_list = [num*2 for num in range(10)]
print(num_list)

num_by_2 = list(map(lambda x: x*2, [num for num in range(10)]))
print(num_by_2)

# Example 4: only keep even numbers from last list
num_list_even = [num for num in range(10) if num % 2 == 0]
print(num_list_even)

# Example 5: square
square = [ n**2 for n in range(1,11)]
print("square = ",square)
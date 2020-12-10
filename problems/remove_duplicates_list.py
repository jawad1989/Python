
some_list = ['a', 'b', 'c', 'a', 'd', 'd']
duplicates = []
new_list = []

for val in some_list:
    if some_list.count(val) > 1:
        if val not in duplicates:
            duplicates.append(val)
    if new_list.count(val) < 2:
        if val not in new_list:
            new_list.append(val)

print(some_list)
print("duplicates:", duplicates)
print("new list:", new_list)

# using comprehension return list of duplicates
remove_dups = list(set([num for num in some_list if some_list.count(num) > 1]))
print("duplicates:", remove_dups)

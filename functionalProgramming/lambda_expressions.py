# print squared list using lambda
my_list = [5, 4, 3]
squared_list = list(map(lambda item: item*item, my_list))
# print(my_list)
print(squared_list)

# List Sorting on second value in list of tuples

a = [(0, 2), (4, 3), (10, -1), (9, 9)]
# print(a[1][1])

print("Before Lambda sorting 2nd element:", a)
a.sort(key=lambda x: x[1])
print("After Lambda sorting 2nd element:", a)

# pure function,
# uses: we want to filter data e..g we want users whose name only starts with A

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def multiply_by2(item):
    return item*2


def check_odd(item):
    return item % 2 != 0


print(list(map(multiply_by2, my_list)))
print(list(filter(check_odd, my_list)))
print(my_list)

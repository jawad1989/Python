from functools import reduce

my_list = [1, 2, 3, 4, 5]


def accumulator(acc, item):
    # print(acc, item)
    return acc + item


print((reduce(accumulator, my_list, 1)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
my_numbers = [5, 4, 3, 2, 1]

scores = [73, 20, 65, 19, 76, 100, 88]


def accumulator2(acc, item):
    return acc+item


print(reduce(accumulator2, (my_numbers + scores)))

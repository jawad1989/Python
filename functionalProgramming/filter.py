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


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def filter_scores(item):
    if item > 50:
        return item


print(list(filter(filter_scores, scores)))

# 4
odd = list(filter(lambda x: x % 2 == 0, range(1, 20)))
# odd = list(map(lambda item: item % 2 != 0, range(0, 10)))
print(odd)

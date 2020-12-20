# now this list will be created in memory
# my_list = list(range(10))


def make_list(num):
    result = []
    for i in range(num):
        result.append(i)
    return result


# my_list = make_list(1_00_0000)
# print(my_list)


def generator_function(num):
    for i in range(1, num):
        yield i


# for item in generator_function(10):
#     print(item)

g = generator_function(10)

next(g)
next(g)
next(g)
print(next(g))
print(next(g))
print(next(g))

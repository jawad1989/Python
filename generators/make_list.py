# now this list will be created in memory
# my_list = list(range(10))


def make_list(num):
    result = []
    for i in range(num):
        result.append(i)
    return result


my_list = make_list(10)
print(my_list)

# pure function,
# uses: we want to iterate a big chunk of data e.g. update email,users. we can use map
my_list = [1, 2, 3]


def multiply_by2(li):
    # new_list = []
    # for item in li:
    #     new_list.append(item*2)
    # return new_list
    return li*2


print(list(map(multiply_by2, my_list)))
print(list(map(multiply_by2, my_list)))
print(my_list)


#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def cap_start(item):
  return item.title()


print(list(map(cap_start, my_pets)))

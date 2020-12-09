# 2 rules
# given the same input it will always return the same output
# a function shouldn't produce any side-effects

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


for num in range(6):
    print(multiply_by2([1, 2, 3]))

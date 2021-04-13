my_list = [1,2,3,4,5,6]


# continue: goes to loop, doesnt goes to next line
# pass: rare thing,
for item in my_list:
    if item < 5:
        print(item)
    elif item == 4:
        print("this is 4")
    else:
        print("else")

    continue
    print("hello")

i = 0

while i < len(my_list):
    # print(my_list[i])
    i += 1
    # continue

for item in my_list:
    pass

# break

for item in my_list:
    print(item)
    break
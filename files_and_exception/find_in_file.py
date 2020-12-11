filename = 'files_and_exception/file.txt'

with open(filename) as fileobject:
    lines = fileobject.readlines()

my_str = ''
for line in lines:
    my_str += line
# print(my_str)

while True:
    name = input("Enter name to find:\n")
    if name in my_str:
        print("Yessss, name found in file")
        break
    else:
        print("Ohhh, name not found")

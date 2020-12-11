filename = 'files_and_exception/file.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for item in lines:
    print(item.rstrip())

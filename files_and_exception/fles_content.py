filename = 'files_and_exception/file.txt'

with open(filename) as fileobject:
    lines = fileobject.readlines()

print(lines)
my_string = ''
for line in lines:
    my_string += ' '+line.strip()

print(my_string[:5])
print("length:", len(my_string))

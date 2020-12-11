filename = 'files_and_exception/file.txt'
file_list = []

with open(filename) as file_object:
    for line in file_object:
        file_list.append(line)

print(file_list)

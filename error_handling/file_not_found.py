filename = 'files_and_exception/dummy.txt'
try:
    with open(filename) as fo:
        contents = fo.readlines()
except FileNotFoundError as err:
    print(f'file not found\n{err}')
else:
    print(contents)

my_str = 'John Adam Peter'
print((my_str.split()))

# for item in contents:
#     print(item)

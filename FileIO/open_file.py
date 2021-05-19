my_file = open('test.txt')

print(my_file.read())
my_file.seek(0) # moves cursor to index 0
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
print(my_file.readline())
my_file.seek(0)
print(my_file.readlines())

my_file.close()

# print(my_file.read())
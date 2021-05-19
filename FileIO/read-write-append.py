"""
mode = r, r+, a

./app
../app  

Path Lib
https://docs.python.org/3/library/pathlib.html
"""

# #creates a new file
with open('test.txt', mode='w') as my_file:
    text = my_file.write('-----writing-----')


#reads and writes existing file
with open('test.txt', mode='r+') as my_file:
    text = my_file.write('-----reading&writing----')

with open('test.txt', mode='a') as my_file:
    text = my_file.write('-----appending-----')


#reads and writes existing file in a sub dir
with open('app/sad.txt', mode='r+') as my_file:
    print(my_file.read())

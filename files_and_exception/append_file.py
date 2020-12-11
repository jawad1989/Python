filename = 'files_and_exception/dummy.txt'
with open(filename, 'a') as fileobject:
    fileobject.write('Hello Python\n')
    fileobject.write('Append from python\n')

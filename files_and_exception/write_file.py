filename = 'files_and_exception/dummy.txt'
with open(filename, 'w') as fileobject:
    fileobject.write('Hello World\n')
    fileobject.write('Write from python\n')

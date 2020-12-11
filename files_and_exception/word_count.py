filename = 'files_and_exception/dummy.txt'

with open(filename) as file_object:
    content = file_object.read()

words = content.split()
words_count = len(words)
print(f'the file: {filename} has {words_count}')

# filename = 'files_and_exception/alice.txt'
filename = 'files_and_exception/little_women.txt'

try:
    with open(filename, encoding='utf-8') as file_object:
        content = file_object.read()
except FileNotFoundError as err:
    print(f"file not found, err: {err}")

else:
    words = content.split()
    words_count = len(words)
    print(f'the file: {filename} has {words_count}')


def count_words(filename):
    """I count words for the file given"""

    with open(filename, encoding='utf-8') as file_object:
        content = file_object.read()

    words = content.split()
    words_count = len(words)

    print(f"file {filename} has {words_count} words")


file_1 = 'files_and_exception/alice.txt'
file_2 = 'files_and_exception/little_women.txt'
file_3 = 'files_and_exception/moby_dick.txt'

count_words(file_1)
count_words(file_2)
count_words(file_3)

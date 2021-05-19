"""
https://pypi.org/project/translate/

 Available languages:

       https://en.wikipedia.org/wiki/ISO_639-1
       Examples: (e.g. en, ja, ko, pt, zh, zh-TW, ...)
"""
from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open('test.txt') as my_file:
        file = my_file.read()        
        translation = translator.translate(file)
        with open('test-ja.txt',mode='w', encoding="utf-8") as ts_file:
            ts_file.write(translation)

except FileNotFoundError as err:
    print('File not found')

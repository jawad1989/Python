"""
https://pypi.org/project/pyjokes/

install pip before downloading this package
"""

import pyjokes


joke = pyjokes.get_joke('en','all')

print(joke)
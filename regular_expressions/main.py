"""
span
start
search
group
"""

import re

my_str = "hey im jawad im learning python, jawad"

# a = re.search("jawad",my_str)

# print(a)
# print(a.span())
# print(a.start())
# print(a.end())
# print(a.group())


pattern = re.compile(r"([a-zA-Z]).([a])")
b = pattern.search(my_str)
c = pattern.findall(my_str)
d = pattern.finditer(my_str)
e = pattern.fullmatch(my_str)
f = pattern.match(my_str)
print(b.group(2))

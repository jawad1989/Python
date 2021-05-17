from collections import Counter, defaultdict, OrderedDict

# import collections

# li = [1,2,3,4,4]
# sentence = "blah blah blah how are you jawad"


# print(Counter(li))
# print(Counter(sentence))

# default dict

my_dict = defaultdict(lambda: "does not exist", {"a":1, "b":2})

print(my_dict['c'])


## ORdered dict

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

d3 = OrderedDict()
d3['b'] = 1
d3['a'] = 2

print(d1 == d2)
print(d1 == d3)
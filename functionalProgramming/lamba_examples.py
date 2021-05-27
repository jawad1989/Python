
c = lambda num: "high" if num >  10 else "low"
print("lambda hi low: ", c(20))

list_a = [5, 4, 3]
print(list(map(lambda item: item*2, list_a)))

print(list(filter(lambda item: item % 2 == 0, list_a)))

# print("reduce: ", reduce((lambda acc, item: acc+item), list_a, 2))

# list_a.sort(key=lambda x: x[1])
# print("After Lambda sorting 2nd element:", list_a)

# concat 
conc = lambda a,b,c: a[0] + b[0] + c[0]
print(conc("JAWA","HAN","AHM"))
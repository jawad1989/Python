
# functions that will be used once
# also called anonymous functions, we used them once
from functools import reduce

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8, 9, 10]

print(list(map(lambda item: item*2, list_a)))

print(list(map(lambda item: 2**item, list_a)))

print(list(map(lambda item: item**2, list_a)))

print(list(filter(lambda item: item % 2 == 0, list_b)))

print("reduce: ", reduce((lambda acc, item: acc+item), list_a, 2))

# cube example


def cube(x):
    return x*x*x


def lambda_cube(y): return y*y*y


print("def cube:", cube(5))

print("lambda cube:", lambda_cube(5))


# lambda with filter
ages = [10, 20, 23, 23, 32, 67]
lambda_age = list(filter(lambda item: item > 18, ages))
print(f"There are '{len(lambda_age)}' people older than 18:", lambda_age)


c = lambda num: "high" if num >  10 else "low"
print("lambda hi low: ", c(20))
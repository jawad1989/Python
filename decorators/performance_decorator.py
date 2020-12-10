
def performance_decorator(func):
    def wrap_func(num):
        print('***')
        func(num)
        print('***')
    return wrap_func


@performance_decorator
def factorial(num):
    fact = 1
    for x in range(1, num+1):
        fact = fact * x
    return fact


print(factorial(5))

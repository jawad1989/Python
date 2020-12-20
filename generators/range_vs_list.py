from time import time


def performance_decorator(func):
    def wrap_func(*key):
        t1 = time()
        result = func(*key)
        t2 = time()
        print(f'func took {t2-t1}ms')
        return result
    return wrap_func


@performance_decorator
def long_time():
    print(1)
    for i in range(1_000_0000):
        i*5


@performance_decorator
def long_time2():
    print(2)
    for i in list(range(1_000_0000)):
        i*5


long_time()
long_time2()

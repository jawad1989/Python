# usage: to use just add @performace_decorator on top

from time import time


def performance_decorator(func):
    def wrap_func(*num):
        t1 = time()
        result = func(*num)
        t2 = time()
        print(f'func took {t2-t1}ms')
        # print(result)
        return result
    return wrap_func

if __name__ == "__main__":
    @performance_decorator
    def long_time():
        for i in range(10000000):
            i = i*5
        return i


    long_time()

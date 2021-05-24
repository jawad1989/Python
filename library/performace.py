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
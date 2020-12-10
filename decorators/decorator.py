# Decorator Pattern
def my_decorator(func):
    def wrap_func(*x):
        print('****')
        func(*x)
        print('****')
    return wrap_func

# this wraps your functions like this a = my_decorator(hello)


@my_decorator
def hello(name, age=31):
    print(f"hello, {name}, {age}")


hello('jawad')
# my_decorator(hello)()

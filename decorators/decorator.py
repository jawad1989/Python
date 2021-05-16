# decorator super charge our functions
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
# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Jawad',
    'valid': True
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)


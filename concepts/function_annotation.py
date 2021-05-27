def get_age(a) -> max(1,20):
    return a

print(get_age('asd'))
print(get_age.__annotations__)


def get_int(x) -> int:
    return x

print(get_int(10))
print(get_int.__annotations__)
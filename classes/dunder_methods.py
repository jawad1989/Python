# Dunder or magic methods in Python are the methods having
# two prefix and suffix underscores in the method name.
# Dunder here means “Double Under (Underscores)”.
# These are commonly used for operator overloading.
# Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.
# https://docs.python.org/3/reference/datamodel.html#special-method-names

class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'jawad',
            'age': 30
        }

    def __str__(self):
        return f' {self.color}'

    def __len__(self):
        return 10

    def __call__(self):
        """can be called by ()"""
        return f'yes?'

    def __getitem__(self, i):
        return self.my_dict[i]


rc_car = Toy('blue', 3)
print(dir(rc_car))
print(rc_car.__str__())
# print(str(rc_car))
print(rc_car.__len__())
# print(len(rc_car))
print(rc_car())

print(rc_car['name'])

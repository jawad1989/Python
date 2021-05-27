class User:
    active = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def add_numbers(cls, num1, num2):
        # return num1+num2 # with cls param
        return cls('Jawad', num1+num2)

    @staticmethod
    def sub_numbers(num1, num2):
        return num1-num2


# print(User.add_numbers(2, 3))
user1 = User.add_numbers(10, 20)
# print(user1.name, user1.age)
print(User.sub_numbers(30,10))
print(user1.sub_numbers(50,10))


print(User.sub_numbers(50, 40))

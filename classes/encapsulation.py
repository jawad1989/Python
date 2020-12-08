# binding of data and functions that maniuplate the data
# and we encapsulate this within one big object

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.degree = degree

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_student(self):
        print(f"Hi, {self.name}, you are {self.age} years old")


std_a = Student("Jawad", 31)
std_b = Student("Haniya", 3)

std_a.get_student()
std_b.get_student()

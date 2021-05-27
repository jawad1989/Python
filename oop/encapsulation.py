# binding of data and functions that maniuplate the data
# and we encapsulate this within one big object

class Student:
    def __init__(self, name, age):
        self.__name = name    # private
        self.__age = age      # private
        self.type = 'student' # public

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_student(self):
        print(f"Hi, {self.__name}, you are {self.__age} years old")


std_a = Student("Jawad", 15)
std_b = Student("Haniya", 3)

std_a.get_student()
std_b.get_student()
print(std_a.type)

# to access privte vars
print(std_a._Student__name)
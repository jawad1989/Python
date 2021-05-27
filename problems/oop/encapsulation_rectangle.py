class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width   = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__width + self.__length)

r = Rectangle(4,5)
print(r.area())
print(r.perimeter())